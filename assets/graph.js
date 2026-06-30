(function () {
  const canvas = document.getElementById("podcast-graph-canvas");
  const panel = document.getElementById("graph-panel");
  const search = document.getElementById("graph-search");
  const reset = document.getElementById("graph-reset");
  const toggles = Array.from(document.querySelectorAll(".graph-type"));
  if (!canvas || !panel || !search) return;
  const baseUrl = (window.PODWIKI_BASE_URL || "").replace(/\/$/, "");

  const ctx = canvas.getContext("2d");
  const colors = {
    topic: "#0b7285",
    wiki: "#2c573e",
    article: "#2563eb",
    podcast: "#d97706",
    person: "#7c3aed",
  };
  const labels = {
    topic: "Topic",
    wiki: "Wiki",
    article: "Content",
    podcast: "Podcast Summary",
    person: "Person",
  };
  let graph = null;
  let nodes = [];
  let links = [];
  let nodeById = new Map();
  let neighborById = new Map();
  let selected = null;
  let hover = null;
  let scale = 1;
  let offsetX = 0;
  let offsetY = 0;
  let dragging = false;
  let dragStart = null;

  function escapeHtml(value) {
    return String(value || "")
      .replaceAll("&", "&amp;")
      .replaceAll("<", "&lt;")
      .replaceAll(">", "&gt;")
      .replaceAll('"', "&quot;");
  }

  function activeTypes() {
    return new Set(toggles.filter((item) => item.checked).map((item) => item.value));
  }

  function hashId() {
    const raw = decodeURIComponent(window.location.hash.replace(/^#/, ""));
    return raw || "";
  }

  function setHash(id) {
    history.replaceState(null, "", `${window.location.pathname}#${encodeURIComponent(id)}`);
  }

  function siteUrl(path) {
    if (!path || /^https?:\/\//i.test(path)) return path;
    if (path.startsWith("/")) return `${baseUrl}${path}`;
    return path;
  }

  function nodeUrl(node) {
    return siteUrl(node.url || `/graph.html#${encodeURIComponent(node.id)}`);
  }

  function graphUrl(node) {
    return `${window.location.origin}${window.location.pathname}#${encodeURIComponent(node.id)}`;
  }

  function visibleNodes() {
    const types = activeTypes();
    const query = search.value.trim().toLowerCase();
    return nodes.filter((node) => {
      if (!types.has(node.type)) return false;
      if (!query) return true;
      return `${node.label || ""} ${node.title || ""} ${node.search || ""}`.toLowerCase().includes(query);
    });
  }

  function visibleLinks(visibleIds) {
    return links.filter((link) => {
      if (!visibleIds.has(link.source) || !visibleIds.has(link.target)) return false;
      return true;
    });
  }

  function typeRank(type) {
    return { wiki: 0, article: 1, podcast: 2, person: 3, topic: 4 }[type] || 5;
  }

  function layout() {
    const byType = {
      wiki: nodes.filter((node) => node.type === "wiki").sort((a, b) => a.label.localeCompare(b.label)),
      article: nodes.filter((node) => node.type === "article").sort((a, b) => a.label.localeCompare(b.label)),
      podcast: nodes.filter((node) => node.type === "podcast").sort((a, b) => String(a.label).localeCompare(String(b.label))),
      person: nodes.filter((node) => node.type === "person").sort((a, b) => String(a.label).localeCompare(String(b.label))),
      topic: nodes.filter((node) => node.type === "topic").sort((a, b) => b.count - a.count || a.label.localeCompare(b.label)),
    };
    const width = 1800;
    const height = 1200;
    placeRing(byType.wiki, width / 2, height / 2, 110, -Math.PI / 2);
    placeRing(byType.article, width / 2, height / 2, 260, -Math.PI / 2);
    placeRing(byType.podcast, width / 2, height / 2, 420, -Math.PI / 2);
    placeRing(byType.person, width / 2, height / 2, 560, -Math.PI / 2);
    placeRing(byType.topic, width / 2, height / 2, 690, -Math.PI / 2);

    scale = Math.min(canvas.clientWidth / width, canvas.clientHeight / height) * 0.95;
    offsetX = canvas.clientWidth / 2 - (width * scale) / 2;
    offsetY = canvas.clientHeight / 2 - (height * scale) / 2;
  }

  function placeRing(items, cx, cy, radius, startAngle) {
    const total = Math.max(items.length, 1);
    items.forEach((node, index) => {
      const angle = startAngle + (Math.PI * 2 * index) / total;
      node.x = cx + Math.cos(angle) * radius;
      node.y = cy + Math.sin(angle) * radius;
    });
  }

  function radius(node) {
    const base = { wiki: 8, article: 6.5, podcast: 5.5, person: 5, topic: 4 }[node.type] || 4;
    return base + Math.min(Math.sqrt(node.count || 1), 6);
  }

  function resizeCanvas() {
    const rect = canvas.getBoundingClientRect();
    const dpr = window.devicePixelRatio || 1;
    canvas.width = Math.max(1, Math.floor(rect.width * dpr));
    canvas.height = Math.max(1, Math.floor(rect.height * dpr));
    ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
  }

  function worldToScreen(node) {
    return { x: node.x * scale + offsetX, y: node.y * scale + offsetY };
  }

  function screenToWorld(x, y) {
    return { x: (x - offsetX) / scale, y: (y - offsetY) / scale };
  }

  function draw() {
    resizeCanvas();
    const width = canvas.clientWidth;
    const height = canvas.clientHeight;
    ctx.clearRect(0, 0, width, height);
    const visible = visibleNodes();
    const visibleIds = new Set(visible.map((node) => node.id));
    const selectedNeighbors = selected ? neighborById.get(selected.id) || new Set() : new Set();
    const queryActive = Boolean(search.value.trim());

    ctx.lineWidth = 1;
    for (const link of visibleLinks(visibleIds)) {
      const source = nodeById.get(link.source);
      const target = nodeById.get(link.target);
      if (!source || !target) continue;
      const a = worldToScreen(source);
      const b = worldToScreen(target);
      const emphasized = selected && (link.source === selected.id || link.target === selected.id);
      ctx.strokeStyle = emphasized ? "rgba(11, 114, 133, 0.75)" : "rgba(102, 112, 133, 0.18)";
      ctx.lineWidth = emphasized ? 2 : Math.min(1.6, 0.5 + (link.weight || 1) * 0.15);
      ctx.beginPath();
      ctx.moveTo(a.x, a.y);
      ctx.lineTo(b.x, b.y);
      ctx.stroke();
    }

    for (const node of visible.sort((a, b) => typeRank(a.type) - typeRank(b.type))) {
      const p = worldToScreen(node);
      const r = radius(node);
      const isSelected = selected && selected.id === node.id;
      const isNeighbor = selectedNeighbors.has(node.id);
      const dim = selected && !isSelected && !isNeighbor;
      ctx.globalAlpha = dim ? 0.25 : 1;
      ctx.fillStyle = colors[node.type] || "#475467";
      ctx.beginPath();
      ctx.arc(p.x, p.y, isSelected ? r + 4 : r, 0, Math.PI * 2);
      ctx.fill();
      if (isSelected || hover === node || queryActive) {
        ctx.globalAlpha = 1;
        ctx.font = "12px Inter, sans-serif";
        ctx.fillStyle = "#162033";
        ctx.fillText(String(node.label || "").slice(0, 34), p.x + r + 6, p.y + 4);
      }
    }
    ctx.globalAlpha = 1;
  }

  function hitTest(x, y) {
    const point = screenToWorld(x, y);
    const visible = visibleNodes();
    for (let i = visible.length - 1; i >= 0; i -= 1) {
      const node = visible[i];
      const dx = node.x - point.x;
      const dy = node.y - point.y;
      if (Math.sqrt(dx * dx + dy * dy) <= radius(node) / scale + 6) return node;
    }
    return null;
  }

  function selectNode(node, updateHash) {
    selected = node;
    if (node && updateHash) setHash(node.id);
    renderPanel(node);
    draw();
  }

  function relatedNodes(node) {
    if (!node) return [];
    const ids = neighborById.get(node.id) || new Set();
    return Array.from(ids)
      .map((id) => nodeById.get(id))
      .filter(Boolean)
      .sort((a, b) => typeRank(a.type) - typeRank(b.type) || String(a.label).localeCompare(String(b.label)))
      .slice(0, 24);
  }

  function renderPanel(node) {
    if (!node) {
      const counts = graph ? graph.counts : {};
      panel.innerHTML = `
        <p class="muted">Search or click a node to inspect links.</p>
        <dl class="graph-stats">
          <div><dt>Wiki</dt><dd>${counts.wikis || 0}</dd></div>
          <div><dt>Content</dt><dd>${counts.articles || 0}</dd></div>
          <div><dt>Podcasts</dt><dd>${counts.podcasts || 0}</dd></div>
          <div><dt>People</dt><dd>${counts.persons || 0}</dd></div>
          <div><dt>Topics</dt><dd>${counts.topics || 0}</dd></div>
        </dl>
      `;
      return;
    }
    const related = relatedNodes(node);
    const searchQuery = encodeURIComponent(node.label || node.title || "");
    panel.innerHTML = `
      <p class="eyebrow">${labels[node.type] || node.type}</p>
      <h2>${escapeHtml(node.title || node.label)}</h2>
      ${node.time ? `<p class="muted">Starts at ${escapeHtml(node.time)}</p>` : ""}
      <div class="graph-actions">
        <a class="button" href="${escapeHtml(nodeUrl(node))}">Open page</a>
        <a class="button secondary" href="${escapeHtml(siteUrl(`/search.html?q=${searchQuery}`))}">Search this</a>
        <button id="copy-graph-link" type="button">Copy graph link</button>
      </div>
      <h3>Linked Nodes</h3>
      <div class="graph-related">
        ${related.map((item) => `
          <button class="related-node" type="button" data-node-id="${escapeHtml(item.id)}">
            <span>${escapeHtml(labels[item.type] || item.type)}</span>
            ${escapeHtml(item.label)}
          </button>
        `).join("") || '<p class="muted">No linked nodes in the current graph.</p>'}
      </div>
    `;
    const copy = document.getElementById("copy-graph-link");
    if (copy) {
      copy.addEventListener("click", () => {
        copyText(graphUrl(node));
        copy.textContent = "Copied";
        setTimeout(() => { copy.textContent = "Copy graph link"; }, 1200);
      });
    }
    for (const item of Array.from(panel.querySelectorAll(".related-node"))) {
      item.addEventListener("click", () => {
        const next = nodeById.get(item.dataset.nodeId);
        if (next) selectNode(next, true);
      });
    }
  }

  function copyText(value) {
    if (navigator.clipboard && navigator.clipboard.writeText) {
      navigator.clipboard.writeText(value).catch(() => fallbackCopy(value));
      return;
    }
    fallbackCopy(value);
  }

  function fallbackCopy(value) {
    const input = document.createElement("textarea");
    input.value = value;
    input.setAttribute("readonly", "readonly");
    input.style.position = "fixed";
    input.style.left = "-9999px";
    document.body.appendChild(input);
    input.select();
    document.execCommand("copy");
    document.body.removeChild(input);
  }

  function buildNeighborIndex() {
    neighborById = new Map(nodes.map((node) => [node.id, new Set()]));
    for (const link of links) {
      if (!neighborById.has(link.source) || !neighborById.has(link.target)) continue;
      neighborById.get(link.source).add(link.target);
      neighborById.get(link.target).add(link.source);
    }
  }

  canvas.addEventListener("mousemove", (event) => {
    const rect = canvas.getBoundingClientRect();
    if (dragging && dragStart) {
      offsetX = dragStart.offsetX + event.clientX - dragStart.x;
      offsetY = dragStart.offsetY + event.clientY - dragStart.y;
      draw();
      return;
    }
    hover = hitTest(event.clientX - rect.left, event.clientY - rect.top);
    canvas.style.cursor = hover ? "pointer" : "grab";
    draw();
  });

  canvas.addEventListener("mousedown", (event) => {
    dragging = true;
    dragStart = { x: event.clientX, y: event.clientY, offsetX, offsetY };
  });

  window.addEventListener("mouseup", () => {
    dragging = false;
    dragStart = null;
  });

  canvas.addEventListener("click", (event) => {
    const rect = canvas.getBoundingClientRect();
    const node = hitTest(event.clientX - rect.left, event.clientY - rect.top);
    if (node) selectNode(node, true);
  });

  canvas.addEventListener("wheel", (event) => {
    event.preventDefault();
    const rect = canvas.getBoundingClientRect();
    const before = screenToWorld(event.clientX - rect.left, event.clientY - rect.top);
    const factor = event.deltaY < 0 ? 1.12 : 0.9;
    scale = Math.max(0.15, Math.min(4, scale * factor));
    offsetX = event.clientX - rect.left - before.x * scale;
    offsetY = event.clientY - rect.top - before.y * scale;
    draw();
  }, { passive: false });

  search.addEventListener("input", () => draw());
  for (const toggle of toggles) {
    toggle.addEventListener("change", () => draw());
  }
  reset.addEventListener("click", () => {
    search.value = "";
    for (const toggle of toggles) toggle.checked = true;
    selected = null;
    history.replaceState(null, "", window.location.pathname);
    layout();
    renderPanel(null);
    draw();
  });

  fetch(siteUrl("/graph/graph.json"))
    .then((response) => response.json())
    .then((payload) => {
      graph = payload;
      nodes = payload.nodes || [];
      links = payload.links || [];
      nodeById = new Map(nodes.map((node) => [node.id, node]));
      buildNeighborIndex();
      layout();
      const initial = nodeById.get(hashId());
      renderPanel(initial || null);
      if (initial) selected = initial;
      draw();
    })
    .catch((error) => {
      panel.innerHTML = `<p class="muted">Graph failed to load: ${escapeHtml(error.message)}</p>`;
    });

  window.addEventListener("resize", draw);
})();
