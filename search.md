---
layout: default
title: Search
permalink: /search.html
---

# Search

<div class="search-panel">
  <input id="search-input" type="search" placeholder="Search wiki, guides, comparisons, roadmaps, how-tos, people, and podcasts" autocomplete="off" />
  <button id="search-button" type="button">Search</button>
</div>

<div class="search-filters" aria-label="Search result type">
  <button type="button" class="search-filter active" data-search-filter="all">All</button>
  <button type="button" class="search-filter" data-search-filter="wiki">Wiki</button>
  <button type="button" class="search-filter" data-search-filter="guide">Guides</button>
  <button type="button" class="search-filter" data-search-filter="comparison">Comparisons</button>
  <button type="button" class="search-filter" data-search-filter="roadmap">Roadmaps</button>
  <button type="button" class="search-filter" data-search-filter="transition">Transitions</button>
  <button type="button" class="search-filter" data-search-filter="how_to">How-tos</button>
  <button type="button" class="search-filter" data-search-filter="podcast_summary">Podcasts</button>
  <button type="button" class="search-filter" data-search-filter="person">People</button>
  <button type="button" class="search-filter" data-search-filter="book">Books</button>
  <button type="button" class="search-filter" data-search-filter="section">Sections</button>
</div>

<div id="search-status" class="muted"></div>
<div id="search-results" class="results"></div>

<script>
  window.PODWIKI_SEARCH_API = "{{ site.search_api_url }}"
</script>
<script src="{{ '/assets/search.js' | relative_url }}"></script>
