(function () {
  const canvas = document.getElementById("podcast-graph-canvas");
  const panel = document.getElementById("graph-panel");
  const search = document.getElementById("graph-search");
  const searchResults = document.getElementById("graph-search-results");
  const randomBtn = document.getElementById("graph-random");
  const trailEl = document.getElementById("graph-trail");
  if (!canvas || !panel || !search) return;
  const baseUrl = (window.PODWIKI_BASE_URL || "").replace(/\/$/, "");
  const ctx = canvas.getContext("2d");
  const REDUCED = window.matchMedia && window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  const DURATION = 380;

  const colors = {
    wiki: "#2c573e",
    topic: "#0b7285",
    podcast: "#d97706",
    person: "#7c3aed",
    book: "#2563eb",
    article: "#2563eb",
  };
  const labels = {
    wiki: "Wiki",
    topic: "Topic",
    podcast: "Podcast",
    person: "Person",
    book: "Book",
    article: "Content",
    guide: "Guide",
    comparison: "Comparison",
    roadmap: "Roadmap",
    how_to: "How-To",
  };
  const LEGEND = [
    ["wiki", "Wiki"],
    ["topic", "Topic"],
    ["podcast", "Podcast"],
    ["person", "Person"],
    ["book", "Book"],
  ];
  const CANVAS_MAX = 18; // neighbours drawn on canvas (panel lists all)
  const PANEL_MAX = 40;

  let nodes = [];
  let links = [];
  let nodeById = new Map();
  let neighborById = new Map();
  let focus = null;
  let trail = []; // visited ids, excluding current
  let scene = []; // render items with animation state
  let hover = null;
  let cx = 0;
  let cy = 0;
  let animStart = 0;
  let animating = false;
  let coachDismissed = false;

  function escapeHtml(value) {
    return String(value || "")
      .replaceAll("&", "&amp;")
      .replaceAll("<", "&lt;")
      .replaceAll(">", "&gt;")
      .replaceAll('"', "&quot;");
  }
  function isDark() {
    return document.documentElement.classList.contains("dark");
  }
  function siteUrl(path) {
    if (!path || /^https?:\/\//i.test(path)) return path;
    if (path.startsWith("/")) return `${baseUrl}${path}`;
    return path;
  }
  function nodeUrl(node) {
    return siteUrl(node.url || `/graph.html#${encodeURIComponent(node.id)}`);
  }
  function typeKey(node) {
    if (node.type === "article" && node.collection) return node.collection;
    return node.type;
  }
  function nodeLabel(node) {
    return labels[typeKey(node)] || node.type;
  }
  function nodeColor(node) {
    return colors[typeKey(node)] || "#64748b";
  }
  function degree(node) {
    return (neighborById.get(node.id) || new Set()).size;
  }
  function nodeRadius(node) {
    return 6 + Math.min(Math.sqrt(degree(node)), 7);
  }
  function neighborsOf(node) {
    if (!node) return [];
    const ids = neighborById.get(node.id) || new Set();
    return Array.from(ids)
      .map((id) => nodeById.get(id))
      .filter(Boolean)
      .sort(
        (a, b) => degree(b) - degree(a) || String(a.label).localeCompare(String(b.label))
      );
  }

  const TYPE_ORDER = ["wiki", "podcast", "person", "topic", "book"];
  function orderIndex(key) {
    const i = TYPE_ORDER.indexOf(key);
    return i === -1 ? TYPE_ORDER.length : i;
  }

  // Group a node's neighbours by type (each group degree-sorted).
  function neighborsByType(node) {
    const groups = new Map();
    for (const nb of neighborsOf(node)) {
      const key = typeKey(nb);
      if (!groups.has(key)) groups.set(key, []);
      groups.get(key).push(nb);
    }
    return groups;
  }

  // Pick up to `cap` neighbours with a balanced spread of types (round-robin),
  // so people / podcasts / topics aren't crowded out by high-degree wiki nodes.
  function diverseNeighbors(node, cap) {
    const groups = neighborsByType(node);
    const keys = Array.from(groups.keys()).sort((a, b) => orderIndex(a) - orderIndex(b));
    const cursor = new Map(keys.map((k) => [k, 0]));
    const out = [];
    let advanced = true;
    while (out.length < cap && advanced) {
      advanced = false;
      for (const key of keys) {
        const arr = groups.get(key);
        const i = cursor.get(key);
        if (i < arr.length) {
          out.push(arr[i]);
          cursor.set(key, i + 1);
          advanced = true;
          if (out.length >= cap) break;
        }
      }
    }
    return out;
  }
  function setHash(id) {
    history.replaceState(null, "", `${window.location.pathname}#${encodeURIComponent(id)}`);
  }
  function hashId() {
    return decodeURIComponent(window.location.hash.replace(/^#/, "")) || "";
  }

  function resizeCanvas() {
    const rect = canvas.getBoundingClientRect();
    const dpr = window.devicePixelRatio || 1;
    canvas.width = Math.max(1, Math.floor(rect.width * dpr));
    canvas.height = Math.max(1, Math.floor(rect.height * dpr));
    ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
  }

  // Compute target positions for focus + its (capped) neighbours.
  function computeTargets(focusNode) {
    resizeCanvas();
    const w = canvas.clientWidth;
    const h = canvas.clientHeight;
    cx = w / 2;
    cy = h / 2;
    const targets = [{ node: focusNode, x: cx, y: cy, r: 16, center: true }];
    const shown = diverseNeighbors(focusNode, CANVAS_MAX);
    const rings = shown.length > 12 ? 2 : 1;
    const maxR = Math.max(96, Math.min(w, h) / 2 - 108);
    const inner = rings === 2 ? Math.ceil(shown.length / 2) : shown.length;
    shown.forEach((node, index) => {
      let ringIndex = 0;
      let posInRing = index;
      let ringTotal = shown.length;
      if (rings === 2) {
        if (index < inner) {
          ringTotal = inner;
        } else {
          ringIndex = 1;
          posInRing = index - inner;
          ringTotal = shown.length - inner;
        }
      }
      const radius = rings === 2 ? (ringIndex === 0 ? maxR * 0.6 : maxR) : maxR;
      const offset = ringIndex === 1 ? Math.PI / Math.max(ringTotal, 1) : 0;
      const angle = -Math.PI / 2 + offset + (Math.PI * 2 * posInRing) / Math.max(ringTotal, 1);
      targets.push({
        node,
        x: cx + Math.cos(angle) * radius,
        y: cy + Math.sin(angle) * radius,
        r: nodeRadius(node),
        center: false,
      });
    });
    return targets;
  }

  function mergeScene(targets, animate) {
    const targetById = new Map(targets.map((t) => [t.node.id, t]));
    const spawnX = scene.length ? (scene.find((s) => s.center) || {}).x || cx : cx;
    const spawnY = scene.length ? (scene.find((s) => s.center) || {}).y || cy : cy;

    // update existing items
    for (const item of scene) {
      const t = targetById.get(item.node.id);
      if (t) {
        item.tx = t.x; item.ty = t.y; item.tr = t.r; item.talpha = 1; item.center = t.center;
      } else {
        item.talpha = 0; // leaving — fade in place
      }
    }
    // add new items
    const present = new Set(scene.map((s) => s.node.id));
    for (const t of targets) {
      if (present.has(t.node.id)) continue;
      scene.push({
        node: t.node,
        x: spawnX, y: spawnY, r: t.r * 0.5, alpha: 0,
        tx: t.x, ty: t.y, tr: t.r, talpha: 1, center: t.center,
      });
    }
    // snapshot start values
    for (const item of scene) {
      item.sx = item.x; item.sy = item.y; item.sr = item.r; item.salpha = item.alpha == null ? 1 : item.alpha;
      if (item.alpha == null) item.alpha = 1;
    }
    if (!animate || REDUCED) {
      finalizeScene();
      draw();
    } else {
      animStart = performance.now();
      animating = true;
      requestAnimationFrame(tick);
    }
  }

  function finalizeScene() {
    for (const item of scene) {
      item.x = item.tx; item.y = item.ty; item.r = item.tr; item.alpha = item.talpha;
    }
    scene = scene.filter((item) => item.talpha > 0);
    animating = false;
  }

  function easeInOut(t) {
    return t < 0.5 ? 4 * t * t * t : 1 - Math.pow(-2 * t + 2, 3) / 2;
  }

  function tick(now) {
    const raw = Math.min(1, (now - animStart) / DURATION);
    const k = easeInOut(raw);
    for (const item of scene) {
      item.x = item.sx + (item.tx - item.sx) * k;
      item.y = item.sy + (item.ty - item.sy) * k;
      item.r = item.sr + (item.tr - item.sr) * k;
      item.alpha = item.salpha + (item.talpha - item.salpha) * k;
    }
    draw();
    if (raw < 1) {
      requestAnimationFrame(tick);
    } else {
      finalizeScene();
      draw();
    }
  }

  function centerItem() {
    return scene.find((s) => s.center);
  }

  function draw() {
    const w = canvas.clientWidth;
    const h = canvas.clientHeight;
    ctx.clearRect(0, 0, w, h);
    const c = centerItem();
    if (!c) return;
    const dark = isDark();
    const labelText = dark ? "#f0f7f3" : "#1a1a1a";
    const chipBg = dark ? "rgba(16, 24, 21, 0.82)" : "rgba(255, 255, 255, 0.85)";
    const baseEdge = dark ? "rgba(142, 216, 173, 0.30)" : "rgba(120, 130, 140, 0.35)";
    const hoverActive = Boolean(hover);

    // ---- edges + edge type labels ----
    for (const item of scene) {
      if (item.center || item.alpha <= 0.03) continue;
      const dim = hoverActive && hover !== item.node ? 0.55 : 1;
      const isH = hover === item.node;
      ctx.globalAlpha = item.alpha * dim;
      ctx.strokeStyle = isH ? nodeColor(item.node) : baseEdge;
      ctx.lineWidth = isH ? 1.7 : 1.1;
      ctx.beginPath();
      ctx.moveTo(c.x, c.y);
      ctx.lineTo(item.x, item.y);
      ctx.stroke();
    }

    // edge type labels rotated along each spoke
    ctx.globalAlpha = 1;
    for (const item of scene) {
      if (item.center || item.alpha <= 0.06) continue;
      const dim = hoverActive && hover !== item.node ? 0.55 : 1;
      let angle = Math.atan2(item.y - c.y, item.x - c.x);
      const flip = angle > Math.PI / 2 || angle < -Math.PI / 2;
      if (flip) angle += Math.PI;
      const t = 0.52;
      const lx = c.x + (item.x - c.x) * t;
      const ly = c.y + (item.y - c.y) * t;
      const text = (nodeLabel(item.node) || "").toUpperCase();
      ctx.save();
      ctx.translate(lx, ly);
      ctx.rotate(angle);
      ctx.font = "700 9px 'Alegreya Sans', sans-serif";
      ctx.textAlign = "center";
      ctx.textBaseline = "middle";
      const tw = ctx.measureText(text).width;
      ctx.globalAlpha = item.alpha * dim;
      ctx.fillStyle = chipBg;
      ctx.fillRect(-tw / 2 - 3, -7, tw + 6, 13);
      ctx.fillStyle = nodeColor(item.node);
      ctx.fillText(text, 0, 0);
      ctx.restore();
    }
    ctx.globalAlpha = 1;

    // ---- nodes ----
    for (const item of scene) {
      const isCenter = item.center;
      const isH = hover === item.node;
      const dim = hoverActive && !isCenter && !isH ? 0.6 : 1;
      ctx.globalAlpha = item.alpha * dim;
      ctx.fillStyle = nodeColor(item.node);
      ctx.beginPath();
      ctx.arc(item.x, item.y, isH ? item.r + 1.5 : item.r, 0, Math.PI * 2);
      ctx.fill();
      if (isCenter) {
        ctx.lineWidth = 3;
        ctx.strokeStyle = dark ? "#101815" : "#ffffff";
        ctx.stroke();
      }
    }

    // ---- node title labels ----
    ctx.textBaseline = "alphabetic";
    for (const item of scene) item.labelBox = null;
    function drawTitle(item) {
      const isCenter = item.center;
      const isH = hover === item.node;
      const dim = hoverActive && !isCenter && !isH ? 0.6 : 1;
      const cap = isCenter ? 40 : 22;
      const raw = String(item.node.label || "");
      const text = raw.slice(0, cap) + (raw.length > cap ? "…" : "");
      ctx.font = isH
        ? "700 13px 'Alegreya Sans', sans-serif"
        : isCenter
        ? "600 15px Raleway, sans-serif"
        : "12px 'Alegreya Sans', sans-serif";
      ctx.textAlign = "left";
      const tw = ctx.measureText(text).width;
      let tx;
      let ty;
      if (isCenter) {
        tx = item.x - tw / 2;
        ty = item.y + item.r + 17;
      } else {
        const left = item.x < c.x;
        tx = left ? item.x - item.r - 6 - tw : item.x + item.r + 6;
        ty = item.y + 4;
      }
      ctx.globalAlpha = item.alpha * dim;
      ctx.fillStyle = chipBg;
      ctx.fillRect(tx - 3, ty - 12, tw + 6, 16);
      if (isH && !isCenter) {
        // subtle highlight: colour the hovered node's title + a thin underline
        ctx.fillStyle = nodeColor(item.node);
        ctx.fillText(text, tx, ty);
        ctx.fillRect(tx, ty + 2, tw, 1.5);
      } else {
        ctx.fillStyle = labelText;
        ctx.fillText(text, tx, ty);
      }
      // record the label's box so hovering the title also targets the node
      if (!isCenter) item.labelBox = { x: tx - 5, y: ty - 14, w: tw + 10, h: 19 };
    }
    for (const item of scene) {
      if (item.alpha <= 0.12 || item.node === hover) continue;
      drawTitle(item);
    }
    // draw the hovered node's title last so it sits on top of every other label
    if (hover) {
      const hItem = scene.find((s) => s.node === hover);
      if (hItem && hItem.alpha > 0.12) drawTitle(hItem);
    }
    ctx.globalAlpha = 1;

    drawLegend(dark, labelText, chipBg);
  }

  function drawLegend(dark, labelText, chipBg) {
    const pad = 10;
    const rowH = 16;
    const x = 12;
    let y = 14;
    ctx.textAlign = "left";
    ctx.textBaseline = "middle";
    ctx.font = "12px 'Alegreya Sans', sans-serif";
    const boxW = 108;
    const boxH = pad * 2 + LEGEND.length * rowH;
    ctx.globalAlpha = 0.92;
    ctx.fillStyle = dark ? "rgba(16, 24, 21, 0.72)" : "rgba(255, 255, 255, 0.78)";
    ctx.fillRect(x, y - 4, boxW, boxH);
    ctx.strokeStyle = dark ? "rgba(255,255,255,0.12)" : "rgba(0,0,0,0.1)";
    ctx.lineWidth = 1;
    ctx.strokeRect(x, y - 4, boxW, boxH);
    let ly = y + pad;
    for (const [key, name] of LEGEND) {
      ctx.fillStyle = colors[key];
      ctx.beginPath();
      ctx.arc(x + pad + 4, ly, 5, 0, Math.PI * 2);
      ctx.fill();
      ctx.fillStyle = labelText;
      ctx.fillText(name, x + pad + 16, ly + 1);
      ly += rowH;
    }
    ctx.globalAlpha = 1;
  }

  function pick(px, py) {
    // node circles first (front-to-back)
    for (let i = scene.length - 1; i >= 0; i -= 1) {
      const item = scene[i];
      if (item.talpha <= 0) continue;
      const dx = item.x - px;
      const dy = item.y - py;
      if (Math.sqrt(dx * dx + dy * dy) <= item.r + 6) return item;
    }
    // then title label boxes, so hovering a title targets its node too
    for (let i = scene.length - 1; i >= 0; i -= 1) {
      const item = scene[i];
      if (item.talpha <= 0 || !item.labelBox) continue;
      const b = item.labelBox;
      if (px >= b.x && px <= b.x + b.w && py >= b.y && py <= b.y + b.h) return item;
    }
    return null;
  }

  // ---------- panel + trail ----------
  function renderTrail() {
    if (!trailEl) return;
    const crumbs = [];
    if (trail.length) {
      crumbs.push('<button type="button" class="trail-back" data-back="1">← Back</button>');
    }
    const chain = trail.concat(focus ? [focus.id] : []);
    const parts = chain.map((id, idx) => {
      const node = nodeById.get(id);
      if (!node) return "";
      const current = idx === chain.length - 1;
      const label = escapeHtml(String(node.label || "").slice(0, 24));
      return current
        ? `<span class="trail-current">${label}</span>`
        : `<button type="button" class="trail-crumb" data-index="${idx}">${label}</button>`;
    });
    let html = crumbs.join("") + parts.join('<span class="trail-sep">›</span>');
    if (!trail.length && !coachDismissed) {
      html += '<span class="trail-hint">— click any node to explore its connections</span>';
    }
    trailEl.innerHTML = html;
    const back = trailEl.querySelector("[data-back]");
    if (back) back.addEventListener("click", goBack);
    for (const crumb of Array.from(trailEl.querySelectorAll(".trail-crumb"))) {
      crumb.addEventListener("click", () => {
        const idx = Number(crumb.dataset.index);
        const id = chain[idx];
        const node = nodeById.get(id);
        if (node) {
          trail = trail.slice(0, idx); // truncate history to that point
          setFocus(node, { push: false });
        }
      });
    }
  }

  function renderPanel() {
    if (!focus) {
      panel.innerHTML = '<p class="muted">Pick a starting point or show a random page.</p>';
      return;
    }
    const related = neighborsOf(focus);
    const groups = neighborsByType(focus);
    const keys = Array.from(groups.keys()).sort((a, b) => orderIndex(a) - orderIndex(b));
    const PER_TYPE = 6;
    const groupsHtml = keys
      .map((key) => {
        const arr = groups.get(key);
        const rows = arr
          .map(
            (item, i) => `
          <button class="related-node${i >= PER_TYPE ? " is-extra" : ""}" type="button" data-node-id="${escapeHtml(item.id)}"><span class="rn-label">${escapeHtml(item.label)}</span></button>`
          )
          .join("");
        const more =
          arr.length > PER_TYPE
            ? `<button type="button" class="related-more" data-type="${escapeHtml(key)}">Show ${arr.length - PER_TYPE} more</button>`
            : "";
        return `
        <section class="related-group" data-type="${escapeHtml(key)}">
          <h4 class="related-group-title">
            <span class="type-dot" style="background:${colors[key] || "#64748b"}"></span>
            ${escapeHtml(labels[key] || key)}
            <span class="related-count">${arr.length}</span>
          </h4>
          <div class="related-list">${rows}</div>
          ${more}
        </section>`;
      })
      .join("");
    const searchQuery = encodeURIComponent(focus.label || focus.title || "");
    panel.innerHTML = `
      <div class="panel-head">
        <p class="eyebrow">${escapeHtml(nodeLabel(focus))}</p>
        <h2>${escapeHtml(focus.title || focus.label)}</h2>
        ${focus.summary ? `<p class="panel-summary muted">${escapeHtml(focus.summary)}</p>` : ""}
        <div class="graph-actions">
          <a class="button" href="${escapeHtml(nodeUrl(focus))}">Open page</a>
          <a class="button secondary" href="${escapeHtml(siteUrl(`/search.html?q=${searchQuery}`))}">Search this</a>
        </div>
        <div class="panel-conn-head">
          <h3>Connections</h3>
          ${related.length ? `<span class="conn-total">${related.length}</span>` : ""}
        </div>
      </div>
      <div class="panel-body">
        <div class="graph-related">
          ${groupsHtml || '<p class="muted">No connections recorded yet.</p>'}
        </div>
      </div>
    `;
    for (const btn of Array.from(panel.querySelectorAll(".related-more"))) {
      btn.addEventListener("click", () => {
        const group = btn.closest(".related-group");
        if (group) group.classList.add("expanded");
        btn.remove();
      });
    }
    for (const item of Array.from(panel.querySelectorAll(".related-node"))) {
      item.addEventListener("click", () => {
        const next = nodeById.get(item.dataset.nodeId);
        if (next) setFocus(next, { push: true });
      });
      item.addEventListener("mouseenter", () => {
        hover = nodeById.get(item.dataset.nodeId) || null;
        if (!animating) draw();
      });
      item.addEventListener("mouseleave", () => {
        hover = null;
        if (!animating) draw();
      });
    }
  }

  function setFocus(node, options) {
    const opts = options || {};
    if (!node || node === focus) return;
    if (focus && opts.push !== false && trail[trail.length - 1] !== focus.id) {
      trail.push(focus.id);
    }
    if (opts.push !== false) coachDismissed = true;
    focus = node;
    hover = null;
    setHash(node.id);
    renderPanel();
    renderTrail();
    mergeScene(computeTargets(node), opts.animate !== false);
  }

  function goBack() {
    if (!trail.length) return;
    const id = trail.pop();
    const node = nodeById.get(id);
    if (node) setFocus(node, { push: false });
  }

  function pickRandom() {
    if (!nodes.length) return;
    const pool = nodes.filter((n) => (neighborById.get(n.id) || new Set()).size > 2);
    const source = pool.length ? pool : nodes;
    const node = source[Math.floor(Math.random() * source.length)];
    setFocus(node, { push: true });
  }

  // ---------- search combobox ----------
  function closeResults() {
    searchResults.hidden = true;
    searchResults.innerHTML = "";
    search.setAttribute("aria-expanded", "false");
  }
  function runSearch() {
    const query = search.value.trim().toLowerCase();
    if (!query) return closeResults();
    const matches = nodes
      .filter((node) =>
        `${node.label || ""} ${node.title || ""} ${node.search || ""}`.toLowerCase().includes(query)
      )
      .sort((a, b) => degree(b) - degree(a))
      .slice(0, 8);
    if (!matches.length) {
      searchResults.innerHTML = '<li class="graph-search-empty" aria-disabled="true">No matches</li>';
      searchResults.hidden = false;
      search.setAttribute("aria-expanded", "true");
      return;
    }
    searchResults.innerHTML = matches
      .map(
        (node) => `
      <li role="option">
        <button type="button" data-node-id="${escapeHtml(node.id)}">
          <span>${escapeHtml(nodeLabel(node))}</span> ${escapeHtml(node.label)}
        </button>
      </li>`
      )
      .join("");
    searchResults.hidden = false;
    search.setAttribute("aria-expanded", "true");
    for (const btn of Array.from(searchResults.querySelectorAll("button"))) {
      btn.addEventListener("click", () => {
        const node = nodeById.get(btn.dataset.nodeId);
        if (node) {
          search.value = "";
          closeResults();
          setFocus(node, { push: true });
        }
      });
    }
  }
  search.addEventListener("input", runSearch);
  search.addEventListener("keydown", (event) => {
    if (event.key === "Enter") {
      event.preventDefault();
      const first = searchResults.querySelector("button[data-node-id]");
      if (first) first.click();
    } else if (event.key === "Escape") {
      closeResults();
    }
  });
  document.addEventListener("click", (event) => {
    if (!event.target.closest(".graph-search")) closeResults();
  });
  if (randomBtn) randomBtn.addEventListener("click", pickRandom);

  // ---------- canvas interaction ----------
  canvas.addEventListener("mousemove", (event) => {
    const rect = canvas.getBoundingClientRect();
    const hit = pick(event.clientX - rect.left, event.clientY - rect.top);
    const next = hit && !hit.center ? hit.node : null;
    canvas.style.cursor = hit ? "pointer" : "default";
    if (next !== hover) {
      hover = next;
      if (!animating) draw();
    }
  });
  canvas.addEventListener("mouseleave", () => {
    if (hover) {
      hover = null;
      if (!animating) draw();
    }
  });
  canvas.addEventListener("click", (event) => {
    const rect = canvas.getBoundingClientRect();
    const hit = pick(event.clientX - rect.left, event.clientY - rect.top);
    if (!hit) return;
    if (hit.center) window.location.href = nodeUrl(hit.node);
    else setFocus(hit.node, { push: true });
  });

  // keyboard: Backspace/Esc = back (unless typing in the search box)
  document.addEventListener("keydown", (event) => {
    if (event.target && event.target.closest(".graph-search")) return;
    if (event.key === "Backspace" || event.key === "Escape") {
      if (trail.length) {
        event.preventDefault();
        goBack();
      }
    }
  });

  window.addEventListener("resize", () => {
    if (focus) mergeScene(computeTargets(focus), false);
  });
  window.addEventListener("hashchange", () => {
    const node = nodeById.get(hashId());
    if (node && node !== focus) setFocus(node, { push: true });
  });

  fetch(siteUrl("/graph/graph.json"))
    .then((response) => response.json())
    .then((payload) => {
      nodes = payload.nodes || [];
      links = payload.links || [];
      nodeById = new Map(nodes.map((node) => [node.id, node]));
      neighborById = new Map(nodes.map((node) => [node.id, new Set()]));
      for (const link of links) {
        if (!neighborById.has(link.source) || !neighborById.has(link.target)) continue;
        neighborById.get(link.source).add(link.target);
        neighborById.get(link.target).add(link.source);
      }
      const initial = nodeById.get(hashId());
      if (initial) setFocus(initial, { push: false, animate: false });
      else pickRandom();
    })
    .catch((error) => {
      panel.innerHTML = `<p class="muted">Graph failed to load: ${escapeHtml(error.message)}</p>`;
    });
})();
