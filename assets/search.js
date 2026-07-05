(function () {
  const input = document.getElementById("search-input");
  const button = document.getElementById("search-button");
  const status = document.getElementById("search-status");
  const results = document.getElementById("search-results");
  const filterButtons = Array.from(document.querySelectorAll("[data-search-filter]"));
  const apiUrl = (window.PODWIKI_SEARCH_API || "").trim();
  const baseUrl = (window.PODWIKI_BASE_URL || "").replace(/\/$/, "");
  let localDocs = null;
  let lastTerms = [];
  let activeFilter = "all";
  const filterLabels = {
    all: "All",
    wiki: "Wiki",
    guide: "Guides",
    comparison: "Comparisons",
    roadmap: "Roadmaps",
    transition: "Transitions",
    how_to: "How-tos",
    podcast_summary: "Podcasts",
    person: "People",
    book: "Books",
    section: "Sections",
  };

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

  function setActiveFilter(value) {
    activeFilter = filterLabels[value] ? value : "all";
    for (const btn of filterButtons) {
      const active = btn.dataset.searchFilter === activeFilter;
      btn.classList.toggle("active", active);
      btn.setAttribute("aria-pressed", active ? "true" : "false");
    }
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
    const labels = {
      wiki: "Wiki",
      guide: "Guide",
      comparison: "Comparison",
      roadmap: "Roadmap",
      transition: "Transition",
      how_to: "How-To",
      podcast_summary: "Podcast",
      person: "Person",
      book: "Book",
    };
    if (item.level === "segment") return "Segment";
    if (item.document_type === "section" || item.level === "section") return "Section";
    return labels[item.level] || String(item.level || "page").replaceAll("_", " ");
  }

  function matchesFilter(item) {
    if (activeFilter === "all") return true;
    if (activeFilter === "section") {
      return item.document_type === "section" || item.level === "section";
    }
    return item.level === activeFilter;
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
    const filterText = activeFilter === "all" ? "" : ` · ${filterLabels[activeFilter]}`;
    setStatus(`${items.length} result${items.length === 1 ? "" : "s"}${filterText}`, "ok");
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
      .filter(matchesFilter)
      .sort((a, b) => b.score - a.score)
      .slice(0, 20);
  }

  async function remoteSearch(query) {
    const url = new URL(apiUrl);
    url.searchParams.set("q", query);
    if (activeFilter !== "all") url.searchParams.set("level", activeFilter);
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
    if (activeFilter === "all") params.delete("level");
    else params.set("level", activeFilter);
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
          const filterText = activeFilter === "all" ? "" : ` · ${filterLabels[activeFilter]}`;
          setStatus(`${items.length} result${items.length === 1 ? "" : "s"}${filterText} (offline index)`, "ok");
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
  for (const btn of filterButtons) {
    btn.addEventListener("click", () => {
      setActiveFilter(btn.dataset.searchFilter);
      if (input.value.trim()) runSearch();
    });
  }

  const initialParams = new URLSearchParams(window.location.search);
  setActiveFilter(initialParams.get("level") || "all");
  const initial = initialParams.get("q");
  if (initial) {
    input.value = initial;
    runSearch();
  }
})();
