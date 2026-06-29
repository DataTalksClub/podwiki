---
layout: default
title: Podcast Graph
permalink: /graph.html
---

# Podcast Graph

Explore how wiki pages, articles, people, topics, and podcast summaries connect
across the DataTalks.Club podcast archive.

<section class="graph-controls" aria-label="Graph controls">
  <label class="graph-search">
    <span>Find</span>
    <input id="graph-search" type="search" placeholder="LLMs, feature stores, RAG..." autocomplete="off" />
  </label>
  <div class="graph-toggles" aria-label="Visible node types">
    <label><input class="graph-type" type="checkbox" value="topic" checked /> Topics</label>
    <label><input class="graph-type" type="checkbox" value="wiki" checked /> Wiki</label>
    <label><input class="graph-type" type="checkbox" value="article" checked /> Articles</label>
    <label><input class="graph-type" type="checkbox" value="podcast" checked /> Podcasts</label>
    <label><input class="graph-type" type="checkbox" value="person" checked /> People</label>
  </div>
  <button id="graph-reset" type="button">Reset</button>
</section>

<section class="graph-shell">
  <div class="graph-stage">
    <canvas id="podcast-graph-canvas" width="1100" height="720"></canvas>
  </div>
  <aside class="graph-panel" id="graph-panel">
    <p class="muted">Search or click a node to inspect links.</p>
  </aside>
</section>

<script src="{{ '/assets/graph.js' | relative_url }}"></script>
