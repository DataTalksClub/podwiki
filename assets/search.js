(function () {
  const input = document.getElementById("search-input");
  const button = document.getElementById("search-button");
  const status = document.getElementById("search-status");
  const results = document.getElementById("search-results");
  const apiUrl = (window.PODWIKI_SEARCH_API || "").trim();
  const baseUrl = (window.PODWIKI_BASE_URL || "").replace(/\/$/, "");
  let localDocs = null;
  let lastTerms = [];

  function siteUrl(path) {
    if (!path || /^https?:\/\//i.test(path)) return path;
    if (path.startsWith("/")) return `${baseUrl}${path}`;
    return path;
  }

  function escapeHtml(value) {
    return String(value || "")
      .replaceAll("&", "&amp;")
      .replaceAll("<", "&lt;")
      .replaceAll(">", "&gt;")
      .replaceAll('"', "&quot;");
  }

  function setStatus(text, state) {
    status.textContent = text;
    if (state) status.setAttribute("data-state", state);
    else status.removeAttribute("data-state");
  }

  function highlight(escaped, terms) {
    if (!terms || !terms.length) return escaped;
    const pattern = terms
      .filter(Boolean)
      .map((t) => t.replace(/[.*+?^${}()|[\]\\]/g, "\\$&"))
      .join("|");
    if (!pattern) return escaped;
    return escaped.replace(new RegExp(`(${pattern})`, "gi"), "<mark>$1</mark>");
  }

  function badgeFor(item) {
    if (item.level === "segment") return "Segment";
    if (item.document_type === "section" || item.level === "section") return "Section";
    return String(item.level || "page").replaceAll("_", " ");
  }

  function metaFor(item) {
    const isSegment = item.level === "segment";
    const isSection = item.document_type === "section" || item.level === "section";
    if (isSegment) {
      return [item.title, item.time].filter(Boolean).join(" · ");
    }
    if (isSection) {
      return item.page_title && item.page_title !== item.segment_title ? item.page_title : "";
    }
    return "";
  }

  function titleFor(item) {
    const isSegment = item.level === "segment";
    const isSection = item.document_type === "section" || item.level === "section";
    if ((isSegment || isSection) && item.segment_title) return item.segment_title;
    return item.title;
  }

  function showEmpty(query) {
    results.innerHTML = `
      <div class="search-empty">
        <strong>No matches for “${escapeHtml(query)}”</strong>
        <span>Try a broader term, or browse the <a href="${escapeHtml(siteUrl("/wiki/"))}">wiki topics</a>.</span>
      </div>`;
  }

  function showSkeletons(n) {
    let html = "";
    for (let i = 0; i < n; i++) {
      html += `
        <article class="result is-skeleton" aria-hidden="true">
          <span class="sk sk-title"></span>
          <span class="sk sk-meta"></span>
          <span class="sk sk-line"></span>
          <span class="sk sk-line short"></span>
        </article>`;
    }
    results.innerHTML = html;
  }

  function render(items, query) {
    results.innerHTML = "";
    if (!items.length) {
      setStatus("No results", "empty");
      showEmpty(query);
      return;
    }
    setStatus(`${items.length} result${items.length === 1 ? "" : "s"}`, "ok");
    const frag = document.createDocumentFragment();
    for (const item of items) {
      const title = highlight(escapeHtml(titleFor(item)), lastTerms);
      const meta = metaFor(item);
      const snippet = (item.text || "").slice(0, 320);
      const snippetHtml = highlight(escapeHtml(snippet), lastTerms) + (item.text && item.text.length > 320 ? "…" : "");
      const el = document.createElement("article");
      el.className = "result";
      el.innerHTML = `
        <h2><a href="${escapeHtml(siteUrl(item.url))}">${title}</a></h2>
        <div class="result-meta">
          <span class="result-badge">${escapeHtml(badgeFor(item))}</span>
          ${meta ? `<span class="result-meta-text">${escapeHtml(meta)}</span>` : ""}
        </div>
        <p>${snippetHtml}</p>
      `;
      frag.appendChild(el);
    }
    results.appendChild(frag);
  }

  function scoreDoc(doc, terms) {
    const haystack = `${doc.title || ""} ${doc.segment_title || ""} ${doc.text || ""}`.toLowerCase();
    let score = 0;
    for (const term of terms) {
      if (!term) continue;
      const matches = haystack.split(term).length - 1;
      score += matches;
      if (String(doc.title || "").toLowerCase().includes(term)) score += 4;
      if (String(doc.segment_title || "").toLowerCase().includes(term)) score += 3;
    }
    return score;
  }

  async function localSearch(query) {
    if (!localDocs) {
      const response = await fetch(siteUrl("/search/search-corpus.json"));
      const payload = await response.json();
      localDocs = payload.docs || payload;
    }
    const terms = query.toLowerCase().split(/[^a-z0-9_.#+-]+/).filter(Boolean);
    return localDocs
      .map((doc) => ({ ...doc, score: scoreDoc(doc, terms) }))
      .filter((doc) => doc.score > 0)
      .sort((a, b) => b.score - a.score)
      .slice(0, 20);
  }

  async function remoteSearch(query) {
    const url = new URL(apiUrl);
    url.searchParams.set("q", query);
    const response = await fetch(url.toString());
    if (!response.ok) throw new Error(`Search API returned ${response.status}`);
    const payload = await response.json();
    if (!payload || !Array.isArray(payload.results)) {
      throw new Error("Search API returned unusable data");
    }
    return payload.results;
  }

  async function runSearch() {
    const query = input.value.trim();
    if (!query) {
      setStatus("");
      results.innerHTML = "";
      return;
    }
    lastTerms = query.toLowerCase().split(/[^a-z0-9_.#+-]+/).filter(Boolean);
    setStatus("Searching…", "loading");
    showSkeletons(4);
    const params = new URLSearchParams(window.location.search);
    params.set("q", query);
    history.replaceState(null, "", `${window.location.pathname}?${params.toString()}`);
    try {
      if (!apiUrl) {
        render(await localSearch(query), query);
        return;
      }

      try {
        render(await remoteSearch(query), query);
      } catch (remoteErr) {
        const items = await localSearch(query);
        render(items, query);
        if (items.length) {
          setStatus(`${items.length} result${items.length === 1 ? "" : "s"} (offline index)`, "ok");
        }
      }
    } catch (err) {
      results.innerHTML = "";
      setStatus(`Search failed: ${err.message}`, "error");
    }
  }

  button.addEventListener("click", runSearch);
  input.addEventListener("keydown", (event) => {
    if (event.key === "Enter") runSearch();
  });

  const initial = new URLSearchParams(window.location.search).get("q");
  if (initial) {
    input.value = initial;
    runSearch();
  }
})();
