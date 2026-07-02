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
//! - resolve miss -> `<span class="broken-link">LABEL</span>` + a warning.
//!
//! `<code>` / `<pre>` regions and text inside tags/attributes are never touched.

use extism_pdk::*;
use serde::{Deserialize, Serialize};

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
        } else {
            // Text run up to the next tag.
            let next = html[i..].find('<').map(|e| i + e).unwrap_or(len);
            let text = &html[i..next];
            if skip_depth > 0 {
                out.push_str(text);
            } else {
                process_text(text, baseurl, &resolve, &mut out, &mut warnings);
            }
            i = next;
        }
    }

    (out, warnings)
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

/// Find and rewrite every `[[...]]` token in a text run.
fn process_text<F>(
    text: &str,
    baseurl: &str,
    resolve: &F,
    out: &mut String,
    warnings: &mut Vec<String>,
) where
    F: Fn(&str) -> Option<String>,
{
    let mut rest = text;
    while let Some(start) = rest.find("[[") {
        out.push_str(&rest[..start]);
        let after = &rest[start + 2..];
        match after.find("]]") {
            Some(end) => {
                let token = &after[..end];
                out.push_str(&render_chip(token, baseurl, resolve, warnings));
                rest = &after[end + 2..];
            }
            None => {
                // No closing `]]`; emit the opener literally and stop.
                out.push_str("[[");
                rest = after;
            }
        }
    }
    out.push_str(rest);
}

/// Render a single `[[...]]` token (inner text, no brackets) to chip markup.
fn render_chip<F>(token: &str, baseurl: &str, resolve: &F, warnings: &mut Vec<String>) -> String
where
    F: Fn(&str) -> Option<String>,
{
    let mut parts = token.split('|');
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

    let original = format!("[[{token}]]");

    match resolve(target) {
        Some(url) => {
            let href = format!("{baseurl}{url}");
            let mut s = format!(
                "<a class=\"chip chip--{ty}\" data-chip=\"{ty}\" href=\"{href}\" title=\"{title}\">",
                ty = chip_type.as_str(),
                href = escape_attr(&href),
                title = escape_attr(&original),
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

    /// Resolver stub: any target whose slug is in the known set resolves to a
    /// URL; everything else misses.
    fn stub(target: &str) -> Option<String> {
        let slug = target
            .to_ascii_lowercase()
            .chars()
            .map(|c| if c == ' ' { '-' } else { c })
            .collect::<String>();
        match slug.as_str() {
            "event-tracking" => Some("/wiki/event-tracking/".to_string()),
            "a-b-testing" => Some("/wiki/a-b-testing/".to_string()),
            "alexeygrigorev" => Some("/people/alexeygrigorev/".to_string()),
            "designing-data-intensive-applications" => {
                Some("/books/designing-data-intensive-applications/".to_string())
            }
            "ab-testing-and-product-experimentation" => {
                Some("/podcasts/ab-testing-and-product-experimentation/".to_string())
            }
            _ => None,
        }
    }

    fn run(html: &str) -> (String, Vec<String>) {
        transform_html(html, "", stub)
    }

    #[test]
    fn wiki_slug_and_title() {
        let (html, warns) = run("<p>See [[event-tracking]] and [[A B Testing]]... no.</p>");
        assert!(html.contains(
            "<a class=\"chip chip--wiki\" data-chip=\"wiki\" href=\"/wiki/event-tracking/\" title=\"[[event-tracking]]\"><span class=\"chip-label\">event tracking</span></a>"
        ), "got: {html}");
        // Title-based resolution (slugified to a-b-testing) also works.
        assert!(html.contains("href=\"/wiki/a-b-testing/\""), "got: {html}");
        assert!(warns.is_empty(), "warns: {warns:?}");
    }

    #[test]
    fn person_book_prefixes() {
        let (html, _) = run("<p>[[person:alexeygrigorev]] wrote [[book:designing-data-intensive-applications|DDIA]].</p>");
        assert!(
            html.contains("chip chip--person") && html.contains("href=\"/people/alexeygrigorev/\""),
            "got: {html}"
        );
        assert!(
            html.contains("chip chip--book")
                && html.contains("<span class=\"chip-label\">DDIA</span>"),
            "got: {html}"
        );
    }

    #[test]
    fn author_guest_aliases_map_to_person() {
        let (html, _) = run("<p>[[author:alexeygrigorev]] [[guest:alexeygrigorev]]</p>");
        assert_eq!(html.matches("chip--person").count(), 2, "got: {html}");
    }

    #[test]
    fn podcast_with_timestamp_and_label() {
        let (html, _) = run(
            "<p>[[podcast:ab-testing-and-product-experimentation|A/B Testing|27:52]]</p>",
        );
        assert!(html.contains("chip chip--podcast"), "got: {html}");
        assert!(
            html.contains("<span class=\"chip-label\">A/B Testing</span>"),
            "got: {html}"
        );
        assert!(
            html.contains("<span class=\"chip-time\">27:52</span>"),
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
    fn unresolved_becomes_broken_link_and_warns() {
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
    fn baseurl_is_prepended() {
        let (html, _) = transform_html("<p>[[event-tracking]]</p>", "/podwiki", stub);
        assert!(html.contains("href=\"/podwiki/wiki/event-tracking/\""), "got: {html}");
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
        // Original token with a quote should be escaped in the title attribute.
        let (html, _) = run("<p>[[event-tracking|say \"hi\"]]</p>");
        assert!(html.contains("&quot;"), "got: {html}");
        assert!(!html.contains("title=\"[[event-tracking|say \"hi\""), "raw quote leaked: {html}");
    }
}
