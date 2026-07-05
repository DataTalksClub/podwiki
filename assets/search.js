(function () {
  const input = document.getElementById("search-input");
  const button = document.getElementById("search-button");
  const status = document.getElementById("search-status");
  const results = document.getElementById("search-results");
  const filterButtons = Array.from(document.querySelectorAll("[data-search-filter]"));
  const apiUrl = (window.PODWIKI_SEARCH_API || "").trim();
  const baseUrl = (window.PODWIKI_BASE_URL || "").replace(/\/$/, "");
  let localDocs = null;
  let localDocsPromise = null;
  let lastTerms = [];
  let activeFilter = "all";

  const filterLabels = {
    all: "All",
    topic: "Topics",
    guide: "Guides",
    comparison: "Comparisons",
    roadmap: "Roadmaps",
    transition: "Transitions",
    "how-to": "How-tos",
    podcast_summary: "Podcasts",
    person: "People",
    book: "Books",
    section: "Sections",
  };

  const singularLabels = {
    topic: "Topic",
    guide: "Guide",
    comparison: "Comparison",
    roadmap: "Roadmap",
    transition: "Transition",
    "how-to": "How-to",
    podcast_summary: "Podcast",
    person: "Person",
    book: "Book",
  };

  const levelToFilter = {
    wiki: "topic",
    topic: "topic",
    guide: "guide",
    comparison: "comparison",
    roadmap: "roadmap",
    transition: "transition",
    how_to: "how-to",
    "how-to": "how-to",
    podcast_summary: "podcast_summary",
    person: "person",
    book: "book",
    section: "section",
  };

  const filterToLevel = {
    topic: "wiki",
    guide: "guide",
    comparison: "comparison",
    roadmap: "roadmap",
    transition: "transition",
    "how-to": "how_to",
    podcast_summary: "podcast_summary",
    person: "person",
    book: "book",
    section: "section",
  };

  const browseFilters = new Set([
    "topic",
    "guide",
    "comparison",
    "roadmap",
    "transition",
    "how-to",
    "podcast_summary",
    "person",
    "book",
    "section",
  ]);
  const browseLimit = 40;

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

  function pluralize(count, singular, plural) {
    return count === 1 ? singular : plural || `${singular}s`;
  }

  function termsFor(query) {
    return query.toLowerCase().split(/[^a-z0-9_.#+-]+/).filter(Boolean);
  }

  function normalizeFilter(value) {
    return levelToFilter[String(value || "").trim().toLowerCase()] || "all";
  }

  function searchLevelFor(filter) {
    return filterToLevel[filter] || "";
  }

  function categoryFor(item) {
    return normalizeFilter(item.level);
  }

  function setStatus(text, state) {
    status.textContent = text;
    if (state) status.setAttribute("data-state", state);
    else status.removeAttribute("data-state");
  }

  function setActiveFilter(value) {
    activeFilter = normalizeFilter(value);
    for (const btn of filterButtons) {
      const active = normalizeFilter(btn.dataset.searchFilter) === activeFilter;
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
    const category = categoryFor(item);
    const label = singularLabels[category] || String(item.level || "Page").replaceAll("_", " ");
    if (item.document_type === "section" || item.level === "section") return `${label} section`;
    if (item.level === "segment") return "Podcast segment";
    return label;
  }

  function matchesFilter(item) {
    return matchesNamedFilter(item, activeFilter);
  }

  function matchesNamedFilter(item, filter) {
    if (filter === "all") return true;
    if (filter === "section") {
      return item.document_type === "section" || item.level === "section";
    }
    return categoryFor(item) === filter;
  }

  function isBrowseable(item) {
    return isBrowseableForFilter(item, activeFilter);
  }

  function isBrowseableForFilter(item, filter) {
    if (filter === "section") return item.document_type === "section" || item.level === "section";
    return item.document_type !== "section";
  }

  function metaFor(item) {
    const isSection = item.document_type === "section" || item.level === "section";
    if (item.level === "segment") {
      return [item.title, item.time].filter(Boolean).join(" · ");
    }
    if (isSection) {
      return item.page_title && item.page_title !== item.segment_title ? item.page_title : "";
    }
    return "";
  }

  function titleFor(item) {
    const isSection = item.document_type === "section" || item.level === "section";
    if ((item.level === "segment" || isSection) && item.segment_title) return item.segment_title;
    return item.title;
  }

  function showEmpty(query, browsing) {
    if (browsing) {
      const filterText = activeFilter === "all" ? "browse entries" : filterLabels[activeFilter].toLowerCase();
      results.innerHTML = `
        <div class="search-empty">
          <strong>No ${escapeHtml(filterText)} in the local index</strong>
          <span>Enter a search term to query the full search index.</span>
        </div>`;
      return;
    }
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

  function resultStatus(items, options) {
    const count = options.totalCount || items.length;
    const shown = count > items.length ? `${items.length} of ${count}` : String(items.length);
    const noun = options.browsing ? pluralize(count, "item") : pluralize(count, "result");
    const filterText = activeFilter === "all" ? "" : ` · ${filterLabels[activeFilter]}`;
    const suffix = options.statusSuffix || "";
    if (options.browsing) return `${shown} ${noun}${filterText}${suffix}`;
    return `${shown} ${noun}${filterText}${suffix}`;
  }

  function render(items, query, options = {}) {
    results.innerHTML = "";
    if (!items.length) {
      setStatus(options.browsing ? "No browse entries" : "No results", "empty");
      showEmpty(query, options.browsing);
      return;
    }
    setStatus(resultStatus(items, options), "ok");
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

  function sortForBrowse(a, b) {
    const categoryA = categoryFor(a);
    const categoryB = categoryFor(b);
    if (categoryA !== categoryB) {
      const order = ["topic", "guide", "comparison", "roadmap", "transition", "how-to", "podcast_summary", "book", "person"];
      return order.indexOf(categoryA) - order.indexOf(categoryB);
    }
    return String(titleFor(a) || "").localeCompare(String(titleFor(b) || ""));
  }

  async function loadLocalDocs() {
    if (localDocs) return localDocs;
    if (!localDocsPromise) {
      localDocsPromise = fetch(siteUrl("/search/search-corpus.json"))
        .then((response) => {
          if (!response.ok) throw new Error(`Local index returned ${response.status}`);
          return response.json();
        })
        .then((payload) => {
          localDocs = payload.docs || payload;
          return localDocs;
        })
        .finally(() => {
          localDocsPromise = null;
        });
    }
    return localDocsPromise;
  }

  function countForFilter(docs, filter) {
    return docs
      .filter((doc) => matchesNamedFilter(doc, filter))
      .filter((doc) => isBrowseableForFilter(doc, filter)).length;
  }

  function updateFilterCounts(docs) {
    for (const btn of filterButtons) {
      const filter = normalizeFilter(btn.dataset.searchFilter);
      if (!browseFilters.has(filter) && filter !== "all") continue;
      const count = filter === "all"
        ? docs.filter((doc) => doc.document_type !== "section").length
        : countForFilter(docs, filter);
      let countEl = btn.querySelector("[data-filter-count]");
      if (!countEl) {
        countEl = document.createElement("span");
        countEl.className = "search-filter-count";
        countEl.setAttribute("data-filter-count", "");
        btn.appendChild(countEl);
      }
      countEl.textContent = String(count);
    }
  }

  async function refreshFilterCounts() {
    try {
      updateFilterCounts(await loadLocalDocs());
    } catch (err) {
      // Lambda search can still work when the static browser corpus is absent.
    }
  }

  async function localSearch(query) {
    const docs = await loadLocalDocs();
    const terms = termsFor(query);
    return docs
      .map((doc) => ({ ...doc, score: scoreDoc(doc, terms) }))
      .filter((doc) => doc.score > 0)
      .filter(matchesFilter)
      .sort((a, b) => b.score - a.score)
      .slice(0, 20);
  }

  async function localBrowse() {
    const docs = await loadLocalDocs();
    const matching = docs
      .filter(matchesFilter)
      .filter(isBrowseable)
      .sort(sortForBrowse);
    return {
      items: matching.slice(0, browseLimit),
      totalCount: matching.length,
    };
  }

  async function remoteSearch(query) {
    const url = new URL(apiUrl);
    const level = searchLevelFor(activeFilter);
    url.searchParams.set("q", query);
    if (level) url.searchParams.set("level", level);
    const response = await fetch(url.toString());
    if (!response.ok) throw new Error(`Search API returned ${response.status}`);
    const payload = await response.json();
    if (!payload || !Array.isArray(payload.results)) {
      throw new Error("Search API returned unusable data");
    }
    return payload.results;
  }

  function updateUrl(query) {
    const params = new URLSearchParams(window.location.search);
    if (query) params.set("q", query);
    else params.delete("q");
    if (activeFilter === "all") params.delete("level");
    else params.set("level", activeFilter);
    const search = params.toString();
    history.replaceState(null, "", `${window.location.pathname}${search ? `?${search}` : ""}`);
  }

  async function browse() {
    lastTerms = [];
    updateUrl("");
    if (activeFilter === "all") {
      setStatus("");
      results.innerHTML = "";
      return;
    }
    setStatus("Loading local index…", "loading");
    showSkeletons(3);
    try {
      const browseResults = await localBrowse();
      render(browseResults.items, "", {
        browsing: true,
        totalCount: browseResults.totalCount,
        statusSuffix: " · local index",
      });
    } catch (err) {
      results.innerHTML = "";
      setStatus("Enter a search term to use the search index", "");
    }
  }

  async function runSearch() {
    const query = input.value.trim();
    if (!query) {
      await browse();
      return;
    }
    lastTerms = termsFor(query);
    setStatus("Searching…", "loading");
    showSkeletons(4);
    updateUrl(query);
    try {
      if (!apiUrl) {
        render(await localSearch(query), query);
        return;
      }

      try {
        render(await remoteSearch(query), query);
      } catch (remoteErr) {
        const items = await localSearch(query);
        render(items, query, { statusSuffix: " · offline index" });
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
      runSearch();
    });
  }

  const initialParams = new URLSearchParams(window.location.search);
  setActiveFilter(initialParams.get("level") || "all");
  const initial = initialParams.get("q");
  if (initial) {
    input.value = initial;
    runSearch();
  } else if (activeFilter !== "all") {
    browse();
  }
  refreshFilterCounts();
})();
