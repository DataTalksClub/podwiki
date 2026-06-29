(function () {
  const roots = Array.from(document.querySelectorAll("[data-graph-connections]"));
  if (!roots.length) return;

  const labels = {
    topic: "Topic",
    wiki: "Wiki",
    article: "Article",
    podcast: "Podcast",
    person: "Person",
  };

  function baseUrl() {
    return (window.PODWIKI_BASE_URL || "").replace(/\/$/, "");
  }

  function siteUrl(path) {
    if (!path || /^https?:\/\//i.test(path)) return path;
    if (path.startsWith("/")) return `${baseUrl()}${path}`;
    return path;
  }

  function normalizePath(path) {
    const base = baseUrl();
    let value = path || "/";
    if (base && value.startsWith(base)) value = value.slice(base.length) || "/";
    value = value.split("#", 1)[0].split("?", 1)[0];
    if (!value.startsWith("/")) value = `/${value}`;
    return value.endsWith("/") ? value : `${value}/`;
  }

  function escapeHtml(value) {
    return String(value || "")
      .replaceAll("&", "&amp;")
      .replaceAll("<", "&lt;")
      .replaceAll(">", "&gt;")
      .replaceAll('"', "&quot;");
  }

  function typeRank(type) {
    return { wiki: 0, article: 1, podcast: 2, person: 3, topic: 4 }[type] || 5;
  }

  function nodeUrl(node) {
    return siteUrl(node.url || "/graph.html");
  }

  function graphUrl(node) {
    return siteUrl(`/graph.html#${encodeURIComponent(node.id)}`);
  }

  function currentNode(graph) {
    const current = normalizePath(window.location.pathname);
    return (graph.nodes || []).find((node) => normalizePath(node.url || "") === current);
  }

  function linkedNodes(graph, node) {
    const nodes = new Map((graph.nodes || []).map((item) => [item.id, item]));
    const linked = [];
    for (const link of graph.links || []) {
      let id = "";
      if (link.source === node.id) id = link.target;
      if (link.target === node.id) id = link.source;
      if (!id || !nodes.has(id)) continue;
      linked.push({ ...nodes.get(id), weight: link.weight || 1, kind: link.kind || "" });
    }
    return linked
      .sort((a, b) => b.weight - a.weight || typeRank(a.type) - typeRank(b.type) || String(a.label).localeCompare(String(b.label)))
      .slice(0, 12);
  }

  function render(root, graph, node) {
    if (!node) {
      root.hidden = true;
      return;
    }
    const linked = linkedNodes(graph, node);
    if (!linked.length) {
      root.hidden = true;
      return;
    }
    root.innerHTML = `
      <h2>Graph Connections</h2>
      <div class="graph-connection-list">
        ${linked.map((item) => `
          <a class="graph-connection" href="${escapeHtml(nodeUrl(item))}">
            <span>${escapeHtml(labels[item.type] || item.type)}</span>
            ${escapeHtml(item.label || item.title)}
          </a>
        `).join("")}
      </div>
      <p class="graph-open"><a href="${escapeHtml(graphUrl(node))}">Open this page in the graph</a></p>
    `;
  }

  fetch(siteUrl("/graph/graph.json"))
    .then((response) => response.json())
    .then((graph) => {
      const node = currentNode(graph);
      for (const root of roots) render(root, graph, node);
    })
    .catch(() => {
      for (const root of roots) root.hidden = true;
    });
})();
