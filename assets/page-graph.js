(function () {
  const roots = Array.from(document.querySelectorAll("[data-graph-connections]"));
  if (!roots.length) return;

  // ---- config -------------------------------------------------
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
  const groupLabels = {
    wiki: "Wiki",
    article: "Guides and Editorial Pages",
    podcast: "Podcast Summaries",
    person: "People",
    book: "Books",
    topic: "Topic Tags",
  };
  const LEGEND = [
    ["wiki", "Wiki"],
    ["topic", "Topic"],
    ["podcast", "Podcast"],
    ["person", "Person"],
    ["book", "Book"],
  ];
  const TYPE_ORDER = ["wiki", "podcast", "person", "book", "topic"];
  const CANVAS_MAX = 16; // neighbours drawn on the canvas
  const REDUCED =
    window.matchMedia && window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  const DURATION = 420;

  // ---- data plumbing (shared helpers) -------------------------
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
  function isDark() {
    return document.documentElement.classList.contains("dark");
  }
  function typeRank(type) {
    return { wiki: 0, article: 1, podcast: 2, person: 3, book: 4, topic: 5 }[type] || 6;
  }
  function typeKey(node) {
    if (node.type === "article" && node.collection) return node.collection;
    return node.type;
  }
  function nodeColor(node) {
    return colors[typeKey(node)] || "#64748b";
  }
  function nodeLabel(node) {
    return labels[typeKey(node)] || node.type;
  }
  function nodeUrl(node) {
    return siteUrl(node.url || `/graph.html#${encodeURIComponent(node.id)}`);
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

  // A well-connected wiki node makes for a rich starting ego view.
  function pickRandomCenter(graph, degreeById) {
    const nodes = graph.nodes || [];
    const rich = nodes.filter(
      (node) => typeKey(node) === "wiki" && (degreeById.get(node.id) || 0) >= 4
    );
    const pool = rich.length ? rich : nodes;
    if (!pool.length) return null;
    return pool[Math.floor(Math.random() * pool.length)];
  }

  function linkedNodes(graph, node, degreeById) {
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
    return Array.from(linked.values()).sort(
      (a, b) =>
        (degreeById.get(b.id) || 0) - (degreeById.get(a.id) || 0) ||
        b.weight - a.weight ||
        typeRank(a.type) - typeRank(b.type) ||
        String(a.label).localeCompare(String(b.label))
    );
  }

  // Round-robin across types so people / podcasts / books aren't crowded
  // out by high-degree wiki nodes (mirrors graph.js's diverseNeighbors).
  function diverseNeighbors(linked, cap) {
    const groups = new Map();
    for (const nb of linked) {
      const key = typeKey(nb);
      if (!groups.has(key)) groups.set(key, []);
      groups.get(key).push(nb);
    }
    const keys = Array.from(groups.keys()).sort(
      (a, b) =>
        (TYPE_ORDER.indexOf(a) + 1 || 99) - (TYPE_ORDER.indexOf(b) + 1 || 99)
    );
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

  function groupNodes(nodes) {
    const groups = new Map();
    for (const item of nodes) {
      const group = groups.get(item.type) || [];
      if (group.length < 6) group.push(item);
      groups.set(item.type, group);
    }
    return Array.from(groups.entries()).sort((a, b) => typeRank(a[0]) - typeRank(b[0]));
  }

  // ---- the interactive ego-graph ------------------------------
  function buildEgo(root, center, linked, degreeById, opts) {
    const allShown = diverseNeighbors(linked, CANVAS_MAX);
    const random = !!(opts && opts.random);

    root.hidden = false;
    root.innerHTML = `
      <h2>${random ? "Explore the wiki as a graph" : "Explore the graph"}</h2>
      <p class="graph-embed-intro">${
        random
          ? `Starting from <strong>${escapeHtml(
              center.label || center.title
            )}</strong> — hover a connection, click to open it, or show another topic.`
          : `See how <strong>${escapeHtml(
              center.label || center.title
            )}</strong> connects to other pages. Hover to focus a link, click to open it.`
      }</p>
      <div class="graph-embed" data-embed>
        <canvas class="graph-embed-canvas" role="img" aria-label="Connection graph for ${escapeHtml(
          center.label || center.title
        )}"></canvas>
      </div>
      <p class="graph-open">
        ${
          random
            ? `<button type="button" class="graph-reroll" data-graph-reroll>Show another topic &rarr;</button> `
            : ""
        }<a href="${escapeHtml(graphUrl(center))}">Open in the full graph &rarr;</a>
      </p>
      <details class="graph-embed-fallback">
        <summary>All ${linked.length} connection${linked.length === 1 ? "" : "s"}</summary>
        ${groupNodes(linked)
          .map(
            ([type, items]) => `
          <section class="graph-connection-group">
            <h3>${escapeHtml(groupLabels[type] || labels[type] || type)}</h3>
            <div class="graph-connection-list">
              ${items
                .map(
                  (item) => `
                <a class="graph-connection" href="${escapeHtml(nodeUrl(item))}">${escapeHtml(
                    item.label || item.title
                  )}</a>`
                )
                .join("")}
            </div>
          </section>`
          )
          .join("")}
      </details>
    `;

    if (random && opts.onReroll) {
      const rerollBtn = root.querySelector("[data-graph-reroll]");
      if (rerollBtn) {
        rerollBtn.addEventListener("click", (event) => {
          event.preventDefault();
          opts.onReroll();
        });
      }
    }

    const canvas = root.querySelector(".graph-embed-canvas");
    const ctx = canvas.getContext("2d");

    // ---- layout ----
    let cx = 0;
    let cy = 0;
    let placed = []; // {node, x, y, r, center}
    let hover = null;
    let anim = 0; // 0..1 entrance progress
    let narrow = false;

    function degreeRadius(node) {
      return 5 + Math.min(Math.sqrt(degreeById.get(node.id) || 1), 6);
    }

    function resize() {
      const rect = canvas.getBoundingClientRect();
      const dpr = window.devicePixelRatio || 1;
      canvas.width = Math.max(1, Math.round(rect.width * dpr));
      canvas.height = Math.max(1, Math.round(rect.height * dpr));
      ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
      layout(rect.width, rect.height);
    }

    function layout(w, h) {
      cx = w / 2;
      cy = h / 2;
      narrow = w < 520;
      placed = [{ node: center, x: cx, y: cy, r: 15, center: true }];
      // Fewer neighbours on a narrow canvas so labels have room to breathe.
      const shown = allShown.slice(0, narrow ? 10 : CANVAS_MAX);
      const n = shown.length;
      // Spread neighbours evenly by angle. When crowded, stagger the radius
      // node-by-node (near / far) so adjacent labels sit at different depths
      // and overlap far less than a clustered two-ring split.
      const stagger = n > 9;
      const maxR = Math.max(70, Math.min(w, h) / 2 - 42);
      const nearR = maxR * 0.62;
      shown.forEach((node, index) => {
        const angle = -Math.PI / 2 + (Math.PI * 2 * index) / Math.max(n, 1);
        const radius = stagger && index % 2 === 1 ? nearR : maxR;
        placed.push({
          node,
          x: cx + Math.cos(angle) * radius,
          y: cy + Math.sin(angle) * radius,
          r: degreeRadius(node),
          center: false,
        });
      });
    }

    function draw() {
      const w = canvas.clientWidth;
      const h = canvas.clientHeight;
      ctx.clearRect(0, 0, w, h);
      const center0 = placed[0];
      if (!center0) return;
      const dark = isDark();
      const labelText = dark ? "#f0f7f3" : "#1a1a1a";
      const chipBg = dark ? "rgba(16, 24, 21, 0.82)" : "rgba(255, 255, 255, 0.85)";
      const baseEdge = dark ? "rgba(142, 216, 173, 0.30)" : "rgba(120, 130, 140, 0.35)";
      const hoverActive = Boolean(hover);
      const k = anim;

      // interpolate each neighbour outward from centre for the entrance
      function pos(item) {
        return {
          x: center0.x + (item.x - center0.x) * k,
          y: center0.y + (item.y - center0.y) * k,
        };
      }

      // ---- edges ----
      for (const item of placed) {
        if (item.center) continue;
        const isH = hover === item.node;
        const dim = hoverActive && !isH ? 0.4 : 1;
        const p = pos(item);
        ctx.globalAlpha = k * dim;
        ctx.strokeStyle = isH ? nodeColor(item.node) : baseEdge;
        ctx.lineWidth = isH ? 1.7 : 1;
        ctx.beginPath();
        ctx.moveTo(center0.x, center0.y);
        ctx.lineTo(p.x, p.y);
        ctx.stroke();
      }
      ctx.globalAlpha = 1;

      // ---- nodes ----
      for (const item of placed) {
        const isCenter = item.center;
        const isH = hover === item.node;
        const dim = hoverActive && !isCenter && !isH ? 0.5 : 1;
        const p = isCenter ? { x: item.x, y: item.y } : pos(item);
        const r = isCenter ? item.r : item.r * (0.4 + 0.6 * k);
        ctx.globalAlpha = isCenter ? 1 : k * dim;
        ctx.fillStyle = nodeColor(item.node);
        ctx.beginPath();
        ctx.arc(p.x, p.y, isH ? r + 1.5 : r, 0, Math.PI * 2);
        ctx.fill();
        if (isCenter) {
          ctx.lineWidth = 3;
          ctx.strokeStyle = dark ? "#101815" : "#ffffff";
          ctx.stroke();
        }
        item._px = p.x;
        item._py = p.y;
        item._pr = r;
      }
      ctx.globalAlpha = 1;

      // ---- labels ----
      for (const item of placed) item.labelBox = null;
      function drawTitle(item) {
        const isCenter = item.center;
        const isH = hover === item.node;
        const dim = hoverActive && !isCenter && !isH ? 0.5 : 1;
        const cap = isCenter ? (narrow ? 24 : 32) : narrow ? 16 : 20;
        const raw = String(item.node.label || item.node.title || "");
        const text = raw.slice(0, cap) + (raw.length > cap ? "…" : "");
        ctx.font = isH
          ? "700 13px 'Alegreya Sans', sans-serif"
          : isCenter
          ? "600 14px Raleway, sans-serif"
          : "12px 'Alegreya Sans', sans-serif";
        ctx.textAlign = "left";
        ctx.textBaseline = "alphabetic";
        const tw = ctx.measureText(text).width;
        let tx;
        let ty;
        if (isCenter) {
          tx = Math.min(Math.max(3, item._px - tw / 2), w - tw - 3);
          ty = item._py + item._pr + 16;
        } else {
          // put the label on the node's outward side (away from centre) and
          // clamp it inside the canvas — never flip it across the middle.
          if (item._px < center0.x) {
            tx = Math.max(3, item._px - item._pr - 6 - tw);
          } else {
            tx = Math.min(w - tw - 3, item._px + item._pr + 6);
          }
          ty = item._py + 4;
        }
        ctx.globalAlpha = isCenter ? 1 : k * dim;
        ctx.fillStyle = chipBg;
        ctx.fillRect(tx - 3, ty - 12, tw + 6, 16);
        if (isH && !isCenter) {
          ctx.fillStyle = nodeColor(item.node);
          ctx.fillText(text, tx, ty);
          ctx.fillRect(tx, ty + 2, tw, 1.5);
        } else {
          ctx.fillStyle = labelText;
          ctx.fillText(text, tx, ty);
        }
        if (!isCenter) item.labelBox = { x: tx - 5, y: ty - 14, w: tw + 10, h: 19 };
      }
      for (const item of placed) {
        if (item.center || item.node === hover) continue;
        drawTitle(item);
      }
      // centre label sits above neighbour labels so it stays readable
      drawTitle(placed[0]);
      if (hover) {
        const hItem = placed.find((s) => s.node === hover);
        if (hItem) drawTitle(hItem);
      }
      ctx.globalAlpha = 1;

      drawLegend(dark, labelText);
    }

    function drawLegend(dark, labelText) {
      const pad = 8;
      const rowH = 15;
      const x = 10;
      const y = 10;
      ctx.textAlign = "left";
      ctx.textBaseline = "middle";
      ctx.font = "11px 'Alegreya Sans', sans-serif";
      const boxW = 92;
      const boxH = pad * 2 + LEGEND.length * rowH;
      ctx.globalAlpha = 0.9;
      ctx.fillStyle = dark ? "rgba(16, 24, 21, 0.72)" : "rgba(255, 255, 255, 0.78)";
      ctx.fillRect(x, y, boxW, boxH);
      ctx.strokeStyle = dark ? "rgba(255,255,255,0.12)" : "rgba(0,0,0,0.1)";
      ctx.lineWidth = 1;
      ctx.strokeRect(x, y, boxW, boxH);
      let ly = y + pad + 5;
      for (const [key, name] of LEGEND) {
        ctx.fillStyle = colors[key];
        ctx.beginPath();
        ctx.arc(x + pad + 3, ly, 4.5, 0, Math.PI * 2);
        ctx.fill();
        ctx.fillStyle = labelText;
        ctx.fillText(name, x + pad + 14, ly + 1);
        ly += rowH;
      }
      ctx.globalAlpha = 1;
    }

    function pick(px, py) {
      for (let i = placed.length - 1; i >= 0; i -= 1) {
        const item = placed[i];
        const dx = (item._px == null ? item.x : item._px) - px;
        const dy = (item._py == null ? item.y : item._py) - py;
        if (Math.sqrt(dx * dx + dy * dy) <= (item._pr || item.r) + 6) return item;
      }
      for (let i = placed.length - 1; i >= 0; i -= 1) {
        const item = placed[i];
        if (!item.labelBox) continue;
        const b = item.labelBox;
        if (px >= b.x && px <= b.x + b.w && py >= b.y && py <= b.y + b.h) return item;
      }
      return null;
    }

    // ---- interaction ----
    canvas.addEventListener("mousemove", (event) => {
      const rect = canvas.getBoundingClientRect();
      const hit = pick(event.clientX - rect.left, event.clientY - rect.top);
      const next = hit && !hit.center ? hit.node : null;
      canvas.style.cursor = hit && !hit.center ? "pointer" : "default";
      if (next !== hover) {
        hover = next;
        draw();
      }
    });
    canvas.addEventListener("mouseleave", () => {
      if (hover) {
        hover = null;
        draw();
      }
    });
    canvas.addEventListener("click", (event) => {
      const rect = canvas.getBoundingClientRect();
      const hit = pick(event.clientX - rect.left, event.clientY - rect.top);
      if (!hit || hit.center) return; // clicking the centre does nothing
      window.location.href = nodeUrl(hit.node);
    });

    let resizeTimer = null;
    window.addEventListener("resize", () => {
      window.clearTimeout(resizeTimer);
      resizeTimer = window.setTimeout(() => {
        resize();
        draw();
      }, 120);
    });

    // redraw on theme toggle so colours follow light/dark
    const themeObserver = new MutationObserver(() => draw());
    themeObserver.observe(document.documentElement, {
      attributes: true,
      attributeFilter: ["class"],
    });

    resize();
    if (REDUCED) {
      anim = 1;
      draw();
    } else {
      const start = performance.now();
      const step = (now) => {
        const raw = Math.min(1, (now - start) / DURATION);
        anim = raw < 0.5 ? 4 * raw * raw * raw : 1 - Math.pow(-2 * raw + 2, 3) / 2;
        draw();
        if (raw < 1) requestAnimationFrame(step);
      };
      requestAnimationFrame(step);
    }
  }

  function render(root, graph, node, degreeById, opts) {
    if (!node) {
      root.hidden = true;
      return;
    }
    const linked = linkedNodes(graph, node, degreeById);
    if (!linked.length) {
      root.hidden = true;
      return;
    }
    buildEgo(root, node, linked, degreeById, opts);
  }

  fetch(siteUrl("/graph/graph.json"))
    .then((response) => response.json())
    .then((graph) => {
      const degreeById = new Map();
      const seen = new Map();
      for (const link of graph.links || []) {
        let set = seen.get(link.source);
        if (!set) seen.set(link.source, (set = new Set()));
        set.add(link.target);
        set = seen.get(link.target);
        if (!set) seen.set(link.target, (set = new Set()));
        set.add(link.source);
      }
      for (const [id, set] of seen) degreeById.set(id, set.size);
      const currentPageNode = currentNode(graph);
      for (const root of roots) {
        if (root.hasAttribute("data-graph-random")) {
          const reroll = () =>
            render(root, graph, pickRandomCenter(graph, degreeById), degreeById, {
              random: true,
              onReroll: reroll,
            });
          reroll();
        } else {
          render(root, graph, currentPageNode, degreeById, { random: false });
        }
      }
    })
    .catch(() => {
      for (const root of roots) root.hidden = true;
    });
})();
