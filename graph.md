---
layout: default
title: Podcast Graph
permalink: /graph.html
---

# Podcast Graph

Start from any page and explore what it connects to across the DataTalks.Club
podcast archive — wiki topics, guides, comparisons, roadmaps, how-tos, people,
topics, podcasts, and books. Click any connection to move to it and keep
exploring.

<section class="graph-controls" aria-label="Graph controls">
  <div class="graph-search">
    <span>Find a starting point</span>
    <input id="graph-search" type="search" placeholder="LLMs, feature stores, a guest's name..." autocomplete="off" aria-expanded="false" aria-haspopup="listbox" />
    <ul id="graph-search-results" class="graph-search-results" role="listbox" hidden></ul>
  </div>
  <button id="graph-random" type="button">Show me a random page</button>
</section>

<nav id="graph-trail" class="graph-trail" aria-label="Exploration trail"></nav>

<section class="graph-shell">
  <div class="graph-stage">
    <canvas id="podcast-graph-canvas" width="1100" height="720"></canvas>
  </div>
  <aside class="graph-panel" id="graph-panel">
    <p class="muted">Loading the graph…</p>
  </aside>
</section>

<script src="{{ '/assets/graph.js' | relative_url }}"></script>
