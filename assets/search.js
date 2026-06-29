(function () {
  const input = document.getElementById("search-input");
  const button = document.getElementById("search-button");
  const status = document.getElementById("search-status");
  const results = document.getElementById("search-results");
  const apiUrl = (window.PODWIKI_SEARCH_API || "").trim();
  let localDocs = null;

  function escapeHtml(value) {
    return String(value || "")
      .replaceAll("&", "&amp;")
      .replaceAll("<", "&lt;")
      .replaceAll(">", "&gt;")
      .replaceAll('"', "&quot;");
  }

  function render(items) {
    results.innerHTML = "";
    if (!items.length) {
      status.textContent = "No results.";
      return;
    }
    status.textContent = `${items.length} results`;
    for (const item of items) {
      const title = item.level === "segment" && item.segment_title
        ? `${item.segment_title}`
        : item.level === "section" && item.segment_title
          ? `${item.segment_title}`
        : item.title;
      const meta = item.level === "segment"
        ? `${item.title} · ${item.time || ""}`
        : item.level === "section"
          ? `${item.title} · section`
          : `${String(item.level || "page").replaceAll("_", " ")} page`;
      const el = document.createElement("article");
      el.className = "result";
      el.innerHTML = `
        <h2><a href="${escapeHtml(item.url)}">${escapeHtml(title)}</a></h2>
        <div class="result-meta">${escapeHtml(meta)}</div>
        <p>${escapeHtml((item.text || "").slice(0, 320))}</p>
      `;
      results.appendChild(el);
    }
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
      const response = await fetch("/search/search-corpus.json");
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
    return payload.results || [];
  }

  async function runSearch() {
    const query = input.value.trim();
    if (!query) return;
    status.textContent = "Searching...";
    results.innerHTML = "";
    const params = new URLSearchParams(window.location.search);
    params.set("q", query);
    history.replaceState(null, "", `${window.location.pathname}?${params.toString()}`);
    try {
      const items = apiUrl ? await remoteSearch(query) : await localSearch(query);
      render(items);
    } catch (err) {
      status.textContent = `Search failed: ${err.message}`;
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
