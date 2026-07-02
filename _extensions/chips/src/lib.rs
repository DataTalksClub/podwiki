//! podwiki entity-chips WASM extension for rustkyll.
//!
//! A post-render HTML transform that rewrites Option-A `[[ ... ]]` entity tokens
//! in wiki prose into typed "chip" anchors matching `assets/pagecss/chips.css`.
//!
//! rustkyll plugin ABI (see rustkyll `src/extensions/wasm.rs`):
//! - Export `transform`: JSON `{ "html", "collection", "baseurl" }` in ->
//!   JSON `{ "html", "warnings" }` out.
//! - Imports host fn `resolve_link(target) -> url` (empty string = miss). The
//!   host slugifies the target, so it accepts a slug or a title.
//! - Per-entry config under the well-known key `config` (JSON string); we read
//!   `scope` (default `wiki`) — the collection this transform applies to.
//!
//! Token grammar (`[[type:target|field|field]]`):
//! - `[[Topic]]` / `[[topic-slug]]`               -> type `wiki`
//! - `[[person:x]]` (also `author:`/`guest:`)      -> type `person`
//! - `[[book:x]]`                                   -> type `book`
//! - `[[podcast:x]]`                                -> type `podcast`
//! - extra `|`-separated fields: for `podcast` a field matching a timestamp
//!   (`M:SS`/`MM:SS`/`H:MM:SS`) is the time; any other field is the label. For
//!   non-podcast the first extra field is the label.
//! - default label = humanized target (dashes -> spaces).
//!
//! Link targets:
//! - `wiki`  -> resolved via the host `resolve_link` to an internal
//!   `/wiki/<slug>/` page (this is the only collection built on podwiki). A miss
//!   renders `<span class="broken-link">LABEL</span>` + a warning.
//! - `person`/`podcast`/`book` collections are `output: false` on podwiki (not
//!   built here), so they are NOT resolved via the host. Instead we emit
//!   absolute MAIN-SITE URLs built directly from the slug, matching graph.json:
//!     person  -> https://datatalks.club/people/<slug>.html
//!     podcast -> https://datatalks.club/podcast/<slug>.html   (singular)
//!     book    -> https://datatalks.club/books/<slug>.html
//!
//! `<code>` / `<pre>` regions and text inside tags/attributes are never touched.
//!
//! The scanner spans HTML tags when hunting for a token's closing `]]`: some
//! tokens are shredded by the markdown renderer (a `|` inside a token is parsed
//! as a table cell separator, splitting `[[a|b]]` into `<td>[[a</td><td>b]]</td>`,
//! sometimes across newlines). Table cell boundaries crossed inside a token are
//! treated as the original `|`; other markup and whitespace runs collapse to a
//! single space. Code/pre regions still abort the scan so code stays literal.

use extism_pdk::*;
use serde::{Deserialize, Serialize};

/// Absolute base for main-site (datatalks.club) entity pages.
const MAIN_SITE: &str = "https://datatalks.club";

#[host_fn]
extern "ExtismHost" {
    fn resolve_link(target: String) -> String;
}

#[derive(Deserialize)]
struct TransformInput {
    html: String,
    #[serde(default)]
    collection: Option<String>,
    #[serde(default)]
    baseurl: String,
}

#[derive(Serialize)]
struct TransformOutput {
    html: String,
    warnings: Vec<String>,
}

#[derive(Deserialize, Default)]
struct PluginConfig {
    #[serde(default)]
    scope: Option<String>,
}

fn load_config() -> PluginConfig {
    match config::get("config") {
        Ok(Some(raw)) if !raw.is_empty() => serde_json::from_str(&raw).unwrap_or_default(),
        _ => PluginConfig::default(),
    }
}

#[plugin_fn]
pub fn transform(input: Json<TransformInput>) -> FnResult<Json<TransformOutput>> {
    let input = input.into_inner();
    let cfg = load_config();
    let scope = cfg.scope.unwrap_or_else(|| "wiki".to_string());

    // Out of scope: return the HTML untouched.
    if input.collection.as_deref() != Some(scope.as_str()) {
        return Ok(Json(TransformOutput {
            html: input.html,
            warnings: Vec::new(),
        }));
    }

    let (html, warnings) = transform_html(&input.html, &input.baseurl, |target| {
        let url = unsafe { resolve_link(target.to_string()) }.unwrap_or_default();
        if url.is_empty() {
            None
        } else {
            Some(url)
        }
    });

    Ok(Json(TransformOutput { html, warnings }))
}

// ---------------------------------------------------------------------------
// Pure logic (host-independent, unit-tested below with a stub resolver).
// ---------------------------------------------------------------------------

/// Sentinel used while scanning a token to mark a spot where a `|` separator was
/// consumed by the markdown renderer (a table cell boundary). Not a legal HTML
/// text character, so it can never collide with real content.
const BAR: char = '\u{1}';

/// Chip entity type.
#[derive(Debug, Clone, Copy, PartialEq, Eq)]
enum ChipType {
    Wiki,
    Person,
    Book,
    Podcast,
}

impl ChipType {
    fn as_str(&self) -> &'static str {
        match self {
            ChipType::Wiki => "wiki",
            ChipType::Person => "person",
            ChipType::Book => "book",
            ChipType::Podcast => "podcast",
        }
    }

    /// Map a token prefix (before the first `:`) to a chip type, if recognized.
    fn from_prefix(prefix: &str) -> Option<ChipType> {
        match prefix {
            "wiki" => Some(ChipType::Wiki),
            "person" | "author" | "guest" => Some(ChipType::Person),
            "book" => Some(ChipType::Book),
            "podcast" => Some(ChipType::Podcast),
            _ => None,
        }
    }
}

/// Walk `html`, rewriting `[[...]]` tokens in text nodes while skipping the
/// contents of `<code>`/`<pre>` elements and anything inside a tag.
fn transform_html<F>(html: &str, baseurl: &str, resolve: F) -> (String, Vec<String>)
where
    F: Fn(&str) -> Option<String>,
{
    let mut out = String::with_capacity(html.len());
    let mut warnings: Vec<String> = Vec::new();
    let mut skip_depth: i32 = 0;
    let bytes = html.as_bytes();
    let len = bytes.len();
    let mut i = 0;

    while i < len {
        if bytes[i] == b'<' {
            // Consume a whole tag `<...>` verbatim.
            let end = html[i..].find('>').map(|e| i + e + 1).unwrap_or(len);
            let tag = &html[i..end];
            skip_depth = (skip_depth + tag_effect(tag)).max(0);
            out.push_str(tag);
            i = end;
        } else if skip_depth == 0 && starts_with_at(bytes, i, b"[[") {
            // A `[[` opener in live text: try to scan a whole token (possibly
            // spanning tags/newlines). On success emit the chip; otherwise emit
            // the opener literally and continue past it.
            match scan_token(html, i) {
                Some((inner, end)) => {
                    out.push_str(&render_chip(&inner, baseurl, &resolve, &mut warnings));
                    i = end;
                }
                None => {
                    out.push_str("[[");
                    i += 2;
                }
            }
        } else {
            // Copy a run of text up to the next tag, or (in live text) the next
            // `[[` opener.
            let mut j = i + 1;
            while j < len {
                if bytes[j] == b'<' {
                    break;
                }
                if skip_depth == 0 && starts_with_at(bytes, j, b"[[") {
                    break;
                }
                j += 1;
            }
            out.push_str(&html[i..j]);
            i = j;
        }
    }

    (out, warnings)
}

/// Whether `bytes[at..]` starts with `needle` (needle is ASCII).
fn starts_with_at(bytes: &[u8], at: usize, needle: &[u8]) -> bool {
    at + needle.len() <= bytes.len() && &bytes[at..at + needle.len()] == needle
}

/// Scan a `[[...]]` token starting at `start` (where `html[start..]` begins with
/// `[[`). The scan crosses HTML tags to find the closing `]]`, so tokens the
/// markdown renderer split across table cells / newlines are healed. Returns the
/// normalized inner text (brackets stripped, cell boundaries restored to `|`,
/// whitespace collapsed) and the byte index just past the closing `]]`.
///
/// Returns `None` (caller emits the opener literally) if there is no closing
/// `]]`, if another `[[` opener appears first, or if the scan would enter a
/// `<code>`/`<pre>` region.
fn scan_token(html: &str, start: usize) -> Option<(String, usize)> {
    let bytes = html.as_bytes();
    let len = bytes.len();
    let mut content = String::new();
    let mut j = start + 2;
    // Depth of `<code>`/`<pre>` we're inside. Brackets there are literal text
    // (protects a `[[x]]` written inside code), but a label may legitimately
    // contain balanced inline code, so we keep scanning rather than bailing.
    let mut code_depth: i32 = 0;

    while j < len {
        // Text run up to the next tag.
        let next_lt = html[j..].find('<').map(|e| j + e).unwrap_or(len);
        let seg = &html[j..next_lt];

        if code_depth == 0 {
            let close = seg.find("]]");
            let open = seg.find("[[");
            // A nested `[[` opener before any closer means this isn't a token.
            if let Some(o) = open {
                if close.map_or(true, |c| o < c) {
                    return None;
                }
            }
            // A closer in this text run completes the token.
            if let Some(c) = close {
                content.push_str(&seg[..c]);
                return Some((normalize(&content), j + c + 2));
            }
        }

        // No closer in this text run: absorb it and step over the tag.
        content.push_str(seg);
        if next_lt >= len {
            return None; // EOF, unterminated.
        }
        let tag_end = html[next_lt..]
            .find('>')
            .map(|e| next_lt + e + 1)
            .unwrap_or(len);
        let tag = &html[next_lt..tag_end];
        match classify_tag(tag) {
            TagKind::CodePreOpen => {
                code_depth += 1;
                content.push(' ');
            }
            TagKind::CodePreClose => {
                code_depth = (code_depth - 1).max(0);
                content.push(' ');
            }
            // A table cell boundary is where a `|` separator used to be.
            TagKind::Cell if code_depth == 0 => content.push(BAR),
            // Any other markup (or a cell boundary inside code) -> whitespace.
            _ => content.push(' '),
        }
        j = tag_end;
    }

    None
}

/// How a tag encountered inside a token affects the scan.
enum TagKind {
    CodePreOpen,
    CodePreClose,
    Cell,
    Other,
}

fn classify_tag(tag: &str) -> TagKind {
    let inner = tag
        .trim_start_matches('<')
        .trim_end_matches('>')
        .trim_end_matches('/')
        .trim();
    let (is_close, rest) = match inner.strip_prefix('/') {
        Some(r) => (true, r),
        None => (false, inner),
    };
    let name = tag_name(rest);
    match name.as_str() {
        "code" | "pre" if is_close => TagKind::CodePreClose,
        "code" | "pre" => TagKind::CodePreOpen,
        "td" | "th" => TagKind::Cell,
        _ => TagKind::Other,
    }
}

/// Collapse a scanned token's inner text: runs of whitespace become a single
/// space, cell-boundary sentinels (with any surrounding whitespace) become a
/// single `|`, and leading/trailing separators are trimmed.
fn normalize(s: &str) -> String {
    let mut out = String::with_capacity(s.len());
    let mut pending_bar = false;
    let mut pending_ws = false;
    for c in s.chars() {
        if c == BAR {
            pending_bar = true;
        } else if c.is_whitespace() {
            pending_ws = true;
        } else {
            if pending_bar {
                if !out.is_empty() {
                    out.push('|');
                }
            } else if pending_ws && !out.is_empty() {
                out.push(' ');
            }
            pending_bar = false;
            pending_ws = false;
            out.push(c);
        }
    }
    out
}

/// Net effect of a tag on the code/pre skip depth: +1 for an opening
/// `<code>`/`<pre>`, -1 for a closing one, 0 otherwise.
fn tag_effect(tag: &str) -> i32 {
    // Strip the angle brackets.
    let inner = tag
        .trim_start_matches('<')
        .trim_end_matches('>')
        .trim_end_matches('/')
        .trim();
    if let Some(rest) = inner.strip_prefix('/') {
        let name = tag_name(rest);
        if name == "code" || name == "pre" {
            return -1;
        }
    } else {
        let name = tag_name(inner);
        if name == "code" || name == "pre" {
            return 1;
        }
    }
    0
}

/// Lowercased element name: leading run of ASCII letters/digits.
fn tag_name(s: &str) -> String {
    s.trim()
        .chars()
        .take_while(|c| c.is_ascii_alphanumeric())
        .collect::<String>()
        .to_ascii_lowercase()
}

/// Slugify a target for a main-site URL: trim, lowercase, whitespace -> dashes.
/// Targets in the wiki are already slugs, so this is normally the identity.
fn slugify(target: &str) -> String {
    target
        .trim()
        .chars()
        .map(|c| if c.is_whitespace() { '-' } else { c.to_ascii_lowercase() })
        .collect()
}

/// Render a single token's normalized inner text (no brackets) to chip markup.
fn render_chip<F>(inner: &str, baseurl: &str, resolve: &F, warnings: &mut Vec<String>) -> String
where
    F: Fn(&str) -> Option<String>,
{
    let mut parts = inner.split('|');
    let head = parts.next().unwrap_or("").trim();
    let extras: Vec<&str> = parts.map(|p| p.trim()).collect();

    // Determine type + target from the head.
    let (chip_type, target) = match head.split_once(':') {
        Some((prefix, rest)) => match ChipType::from_prefix(prefix.trim()) {
            Some(t) => (t, rest.trim()),
            // Unrecognized prefix -> treat the whole head as a wiki target.
            None => (ChipType::Wiki, head),
        },
        None => (ChipType::Wiki, head),
    };

    // Extract label + time from the extra fields.
    let mut time: Option<&str> = None;
    let mut label: Option<&str> = None;
    if chip_type == ChipType::Podcast {
        for field in &extras {
            if field.is_empty() {
                continue;
            }
            if time.is_none() && is_timestamp(field) {
                time = Some(field);
            } else if label.is_none() {
                label = Some(field);
            }
        }
    } else if let Some(first) = extras.iter().find(|f| !f.is_empty()) {
        label = Some(first);
    }

    // Resolve label text. Podcast bare-time (a time but no explicit label) has
    // no label span at all.
    let humanized = humanize(target);
    let label_text: Option<String> = match label {
        Some(l) => Some(l.to_string()),
        None if chip_type == ChipType::Podcast && time.is_some() => None,
        None => Some(humanized.clone()),
    };

    let original = format!("[[{inner}]]");

    // Build the href. Only `wiki` is resolved via the host (internal page);
    // person/podcast/book always link out to the main site, built from the slug.
    let href_opt: Option<String> = match chip_type {
        ChipType::Wiki => resolve(target).map(|url| format!("{baseurl}{url}")),
        ChipType::Person => Some(format!("{MAIN_SITE}/people/{}.html", slugify(target))),
        ChipType::Podcast => Some(format!("{MAIN_SITE}/podcast/{}.html", slugify(target))),
        ChipType::Book => Some(format!("{MAIN_SITE}/books/{}.html", slugify(target))),
    };

    match href_opt {
        Some(href) => {
            // Tooltip is the human label (falls back to the humanized target for
            // a bare-time podcast chip that has no label span).
            let title = label_text.as_deref().unwrap_or(&humanized);
            let mut s = format!(
                "<a class=\"chip chip--{ty}\" data-chip=\"{ty}\" href=\"{href}\" title=\"{title}\">",
                ty = chip_type.as_str(),
                href = escape_attr(&href),
                title = escape_attr(title),
            );
            if let Some(l) = &label_text {
                s.push_str(&format!(
                    "<span class=\"chip-label\">{}</span>",
                    escape_text(l)
                ));
            }
            if let Some(t) = time {
                s.push_str(&format!(
                    "<span class=\"chip-time\">{}</span>",
                    escape_text(t)
                ));
            }
            s.push_str("</a>");
            s
        }
        None => {
            // Only reachable for a `wiki` resolve miss.
            warnings.push(format!("chips: unresolved {original}"));
            // Always show something visible for a broken link.
            let display = label_text
                .or_else(|| time.map(|t| t.to_string()))
                .unwrap_or(humanized);
            format!(
                "<span class=\"broken-link\">{}</span>",
                escape_text(&display)
            )
        }
    }
}

/// Whether `s` looks like `M:SS`, `MM:SS`, or `H:MM:SS`.
fn is_timestamp(s: &str) -> bool {
    let parts: Vec<&str> = s.split(':').collect();
    if parts.len() < 2 || parts.len() > 3 {
        return false;
    }
    // Every segment must be all digits and non-empty; the seconds/minutes
    // trailing segments must be exactly two digits.
    for (idx, p) in parts.iter().enumerate() {
        if p.is_empty() || !p.bytes().all(|b| b.is_ascii_digit()) {
            return false;
        }
        if idx > 0 && p.len() != 2 {
            return false;
        }
    }
    true
}

/// Humanize a target: dashes -> spaces.
fn humanize(target: &str) -> String {
    target.replace('-', " ")
}

/// Escape a string for use in an HTML attribute value (double-quoted).
fn escape_attr(s: &str) -> String {
    let mut out = String::with_capacity(s.len());
    for c in s.chars() {
        match c {
            '&' => out.push_str("&amp;"),
            '<' => out.push_str("&lt;"),
            '>' => out.push_str("&gt;"),
            '"' => out.push_str("&quot;"),
            '\'' => out.push_str("&#39;"),
            _ => out.push(c),
        }
    }
    out
}

/// Escape a string for use as HTML text content.
fn escape_text(s: &str) -> String {
    let mut out = String::with_capacity(s.len());
    for c in s.chars() {
        match c {
            '&' => out.push_str("&amp;"),
            '<' => out.push_str("&lt;"),
            '>' => out.push_str("&gt;"),
            _ => out.push(c),
        }
    }
    out
}

// ---------------------------------------------------------------------------
// Tests
// ---------------------------------------------------------------------------

#[cfg(test)]
mod tests {
    use super::*;

    /// Resolver stub for `wiki` targets: any target whose slug is in the known
    /// set resolves to an internal URL; everything else misses. (person/podcast/
    /// book never call the resolver — they build main-site URLs directly.)
    fn stub(target: &str) -> Option<String> {
        let slug = target
            .to_ascii_lowercase()
            .chars()
            .map(|c| if c == ' ' { '-' } else { c })
            .collect::<String>();
        match slug.as_str() {
            "event-tracking" => Some("/wiki/event-tracking/".to_string()),
            "a-a-testing" => Some("/wiki/a-a-testing/".to_string()),
            "a-b-testing" => Some("/wiki/a-b-testing/".to_string()),
            _ => None,
        }
    }

    fn run(html: &str) -> (String, Vec<String>) {
        transform_html(html, "", stub)
    }

    #[test]
    fn wiki_slug_and_title() {
        // Wiki chips resolve to internal pages; the tooltip is the LABEL.
        let (html, warns) = run("<p>See [[event-tracking]].</p>");
        assert!(html.contains(
            "<a class=\"chip chip--wiki\" data-chip=\"wiki\" href=\"/wiki/event-tracking/\" title=\"event tracking\"><span class=\"chip-label\">event tracking</span></a>"
        ), "got: {html}");
        assert!(warns.is_empty(), "warns: {warns:?}");
    }

    #[test]
    fn wiki_title_resolution() {
        // A title (slugified to a-b-testing) also resolves internally.
        let (html, _) = run("<p>[[A B Testing]]</p>");
        assert!(html.contains("href=\"/wiki/a-b-testing/\""), "got: {html}");
    }

    #[test]
    fn person_links_to_main_site() {
        let (html, _) = run("<p>[[person:alexeygrigorev|Alexey Grigorev]]</p>");
        assert!(html.contains("chip chip--person"), "got: {html}");
        assert!(
            html.contains("href=\"https://datatalks.club/people/alexeygrigorev.html\""),
            "got: {html}"
        );
        // Tooltip == label, not the raw token.
        assert!(html.contains("title=\"Alexey Grigorev\""), "got: {html}");
        assert!(!html.contains("title=\"[["), "raw token leaked into title: {html}");
    }

    #[test]
    fn book_links_to_main_site() {
        let (html, _) =
            run("<p>[[book:designing-data-intensive-applications|DDIA]]</p>");
        assert!(
            html.contains("chip chip--book")
                && html.contains(
                    "href=\"https://datatalks.club/books/designing-data-intensive-applications.html\""
                ),
            "got: {html}"
        );
        assert!(html.contains("<span class=\"chip-label\">DDIA</span>"), "got: {html}");
        assert!(html.contains("title=\"DDIA\""), "got: {html}");
    }

    #[test]
    fn podcast_links_to_main_site_singular() {
        let (html, _) = run(
            "<p>[[podcast:ab-testing-and-product-experimentation|A/B Testing|27:52]]</p>",
        );
        assert!(html.contains("chip chip--podcast"), "got: {html}");
        // Note: singular "podcast" in the main-site path.
        assert!(
            html.contains(
                "href=\"https://datatalks.club/podcast/ab-testing-and-product-experimentation.html\""
            ),
            "got: {html}"
        );
        assert!(
            html.contains("<span class=\"chip-label\">A/B Testing</span>"),
            "got: {html}"
        );
        assert!(
            html.contains("<span class=\"chip-time\">27:52</span>"),
            "got: {html}"
        );
        assert!(html.contains("title=\"A/B Testing\""), "got: {html}");
    }

    #[test]
    fn author_guest_aliases_map_to_person() {
        let (html, _) = run("<p>[[author:alexeygrigorev]] [[guest:alexeygrigorev]]</p>");
        assert_eq!(html.matches("chip--person").count(), 2, "got: {html}");
        assert_eq!(
            html.matches("https://datatalks.club/people/alexeygrigorev.html")
                .count(),
            2,
            "got: {html}"
        );
    }

    #[test]
    fn podcast_bare_timestamp_has_no_label() {
        let (html, _) =
            run("<p>[[podcast:ab-testing-and-product-experimentation|27:52]]</p>");
        assert!(html.contains("chip chip--podcast"), "got: {html}");
        assert!(
            html.contains("<span class=\"chip-time\">27:52</span>"),
            "got: {html}"
        );
        assert!(!html.contains("chip-label"), "bare time must have no label: {html}");
        // Tooltip falls back to the humanized target.
        assert!(
            html.contains("title=\"ab testing and product experimentation\""),
            "got: {html}"
        );
    }

    #[test]
    fn podcast_hms_timestamp() {
        let (html, _) =
            run("<p>[[podcast:ab-testing-and-product-experimentation|1:02:03]]</p>");
        assert!(
            html.contains("<span class=\"chip-time\">1:02:03</span>"),
            "got: {html}"
        );
        assert!(!html.contains("chip-label"), "got: {html}");
    }

    #[test]
    fn unresolved_wiki_becomes_broken_link_and_warns() {
        let (html, warns) = run("<p>[[does-not-exist]]</p>");
        assert!(
            html.contains("<span class=\"broken-link\">does not exist</span>"),
            "got: {html}"
        );
        assert_eq!(warns.len(), 1);
        assert!(
            warns[0].contains("chips: unresolved [[does-not-exist]]"),
            "warns: {warns:?}"
        );
    }

    #[test]
    fn newline_spanning_token_renders() {
        // A label wrapped across a newline inside the token must still render,
        // with the newline collapsed to a single space in label and title.
        let (html, warns) = run("<p>[[person:bartoszmikulski|Bartosz\nMikulski]]</p>");
        assert!(
            html.contains("href=\"https://datatalks.club/people/bartoszmikulski.html\""),
            "got: {html}"
        );
        assert!(
            html.contains("<span class=\"chip-label\">Bartosz Mikulski</span>"),
            "got: {html}"
        );
        assert!(html.contains("title=\"Bartosz Mikulski\""), "got: {html}");
        assert!(!html.contains("[["), "no literal token should leak: {html}");
        assert!(warns.is_empty(), "warns: {warns:?}");
    }

    #[test]
    fn token_split_across_table_cells_is_healed() {
        // The markdown renderer turns a `|` inside a token into a table cell
        // boundary, shredding the token. The scanner must reassemble it, using
        // the cell boundary as the original `|`.
        let (html, _) = run(
            "<table><tbody><tr><td>[[a-a-testing</td>\n<td>A/A Testing]]</td></tr></tbody></table>",
        );
        assert!(
            html.contains("href=\"/wiki/a-a-testing/\""),
            "got: {html}"
        );
        assert!(
            html.contains("<span class=\"chip-label\">A/A Testing</span>"),
            "got: {html}"
        );
        assert!(!html.contains("[["), "no literal token should leak: {html}");
        assert!(!html.contains("]]"), "no literal token should leak: {html}");
    }

    #[test]
    fn podcast_split_across_three_cells_is_healed() {
        // target|time|label spread across three cells.
        let (html, _) = run(
            "<table><tbody><tr><td>[[podcast:ab-testing-and-product-experimentation</td><td>27:52</td><td>A/B Testing]]</td></tr></tbody></table>",
        );
        assert!(
            html.contains(
                "href=\"https://datatalks.club/podcast/ab-testing-and-product-experimentation.html\""
            ),
            "got: {html}"
        );
        assert!(
            html.contains("<span class=\"chip-time\">27:52</span>"),
            "got: {html}"
        );
        assert!(
            html.contains("<span class=\"chip-label\">A/B Testing</span>"),
            "got: {html}"
        );
        assert!(!html.contains("[["), "no literal token should leak: {html}");
    }

    #[test]
    fn code_and_pre_are_skipped() {
        let (html, warns) = run(
            "<p>[[event-tracking]]</p><pre><code>[[event-tracking]]</code></pre><p>x <code>[[event-tracking]]</code></p>",
        );
        // Exactly one real chip; the two inside code/pre stay literal.
        assert_eq!(html.matches("class=\"chip ").count(), 1, "got: {html}");
        assert!(html.contains("<code>[[event-tracking]]</code>"), "got: {html}");
        assert!(
            html.contains("<pre><code>[[event-tracking]]</code></pre>"),
            "got: {html}"
        );
        assert!(warns.is_empty(), "warns: {warns:?}");
    }

    #[test]
    fn token_scan_does_not_enter_code() {
        // A `[[` in live text whose only `]]` is inside a code span must NOT be
        // healed across the code boundary; the opener stays literal.
        let (html, _) = run("<p>[[foo <code>bar]]</code></p>");
        assert!(html.contains("[[foo "), "got: {html}");
        assert!(html.contains("<code>bar]]</code>"), "got: {html}");
        assert!(!html.contains("class=\"chip"), "got: {html}");
    }

    #[test]
    fn label_with_balanced_inline_code_is_healed() {
        // A backticked word in a label renders as a balanced inline <code>; the
        // token must still heal (code text folded into the label as plain text).
        let (html, _) = run(
            "<p>[[podcast:ab-testing-and-product-experimentation|<code>dbt</code> modeling discussion]]</p>",
        );
        assert!(
            html.contains(
                "href=\"https://datatalks.club/podcast/ab-testing-and-product-experimentation.html\""
            ),
            "got: {html}"
        );
        assert!(
            html.contains("<span class=\"chip-label\">dbt modeling discussion</span>"),
            "got: {html}"
        );
        assert!(!html.contains("[["), "no literal token should leak: {html}");
    }

    #[test]
    fn tokens_inside_tags_and_attributes_untouched() {
        // A `[[...]]` sequence appearing inside a tag/attribute is not text and
        // must not be rewritten.
        let html_in = "<a href=\"/x?q=[[event-tracking]]\">link</a>";
        let (html, _) = run(html_in);
        assert_eq!(html, html_in, "attribute content must be untouched");
    }

    #[test]
    fn out_of_scope_is_noop() {
        // The full transform: a non-wiki collection returns HTML unchanged.
        let input = TransformInput {
            html: "<p>[[event-tracking]]</p>".to_string(),
            collection: Some("people".to_string()),
            baseurl: String::new(),
        };
        // Mirror the scope gate used in `transform`.
        let scope = "wiki";
        let result = if input.collection.as_deref() != Some(scope) {
            input.html.clone()
        } else {
            transform_html(&input.html, "", stub).0
        };
        assert_eq!(result, "<p>[[event-tracking]]</p>");
    }

    #[test]
    fn baseurl_is_prepended_for_wiki() {
        let (html, _) = transform_html("<p>[[event-tracking]]</p>", "/podwiki", stub);
        assert!(html.contains("href=\"/podwiki/wiki/event-tracking/\""), "got: {html}");
    }

    #[test]
    fn baseurl_does_not_affect_main_site_links() {
        let (html, _) = transform_html("<p>[[person:alexeygrigorev]]</p>", "/podwiki", stub);
        assert!(
            html.contains("href=\"https://datatalks.club/people/alexeygrigorev.html\""),
            "got: {html}"
        );
    }

    #[test]
    fn is_timestamp_grammar() {
        assert!(is_timestamp("1:23"));
        assert!(is_timestamp("12:34"));
        assert!(is_timestamp("1:02:03"));
        assert!(!is_timestamp("123"));
        assert!(!is_timestamp("1:2"));
        assert!(!is_timestamp("1:234"));
        assert!(!is_timestamp("foo"));
        assert!(!is_timestamp("1:23:45:67"));
    }

    #[test]
    fn attribute_values_escaped() {
        // A label containing a quote must be escaped in the title attribute.
        let (html, _) = run("<p>[[event-tracking|say \"hi\"]]</p>");
        assert!(html.contains("title=\"say &quot;hi&quot;\""), "got: {html}");
        assert!(!html.contains("title=\"say \"hi\""), "raw quote leaked: {html}");
    }

    #[test]
    fn unterminated_opener_left_literal() {
        let (html, _) = run("<p>see [[event-tracking and more</p>");
        assert!(html.contains("[[event-tracking and more"), "got: {html}");
        assert!(!html.contains("class=\"chip"), "got: {html}");
    }
}
