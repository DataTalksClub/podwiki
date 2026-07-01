(function () {
  const roots = Array.from(document.querySelectorAll("[data-graph-connections]"));
  if (!roots.length) return;

  const labels = {
    topic: "Topic",
    wiki: "Wiki",
    article: "Content",
    podcast: "Podcast Summary",
    person: "Person",
  };
  const groupLabels = {
    wiki: "Wiki",
    article: "Guides and Editorial Pages",
    podcast: "Podcast Summaries",
    person: "People",
    topic: "Topic Tags",
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

  function typeLabel(node) {
    if (node.type !== "article") return labels[node.type] || node.type;
    const collectionLabels = {
      guide: "Guide",
      comparison: "Comparison",
      roadmap: "Roadmap",
      how_to: "How-To",
    };
    return collectionLabels[node.collection] || "Content";
  }

  function nodeUrl(node) {
    return siteUrl(node.url || "/graph.html");
  }

  function graphUrl(node) {
    return siteUrl(`/graph.html#${encodeURIComponent(node.id)}`);
  }

  function currentNode(graph) {
    const current = normalizePath(window.location.pathname);
    return (graph.nodes || [])
      .filter((node) => normalizePath(node.url || "") === current)
      .sort((a, b) => typeRank(a.type) - typeRank(b.type))[0];
  }

  function linkedNodes(graph, node) {
    const nodes = new Map((graph.nodes || []).map((item) => [item.id, item]));
    const linked = new Map();
    for (const link of graph.links || []) {
      let id = "";
      if (link.source === node.id) id = link.target;
      if (link.target === node.id) id = link.source;
      if (!id || !nodes.has(id)) continue;
      const current = linked.get(id);
      const nextWeight = Math.max(current ? current.weight : 0, link.weight || 1);
      linked.set(id, { ...nodes.get(id), weight: nextWeight, kind: link.kind || "" });
    }
    return Array.from(linked.values())
      .sort((a, b) => b.weight - a.weight || typeRank(a.type) - typeRank(b.type) || String(a.label).localeCompare(String(b.label)));
  }

  function groupNodes(nodes) {
    const groups = new Map();
    for (const item of nodes) {
      const group = groups.get(item.type) || [];
      if (group.length < 6) group.push(item);
      groups.set(item.type, group);
    }
    return Array.from(groups.entries()).sort((a, b) => typeRank(a[0]) - typeRank(b[0]));
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
    const groups = groupNodes(linked);
    root.innerHTML = `
      <h2>See Also in the Graph</h2>
      ${groups.map(([type, items]) => `
        <section class="graph-connection-group">
          <h3>${escapeHtml(groupLabels[type] || labels[type] || type)}</h3>
          <div class="graph-connection-list">
            ${items.map((item) => `
              <a class="graph-connection" href="${escapeHtml(nodeUrl(item))}">
                <span>${escapeHtml(typeLabel(item))}</span>
                ${escapeHtml(item.label || item.title)}
              </a>
            `).join("")}
          </div>
        </section>
      `).join("")}
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
