---
layout: default
title: Search
permalink: /search/
---

# Search

<form id="search-form" class="search-panel" role="search" aria-label="Search the podcast wiki">
  <label class="sr-only" for="search-input">Search the podcast wiki</label>
  <input id="search-input" type="search" placeholder="Search topics, guides, comparisons, roadmaps, transitions, how-tos, podcasts, people, and books" autocomplete="off" />
  <button id="search-button" type="submit">Search</button>
</form>

<div class="search-filters" role="group" aria-labelledby="search-filter-label">
  <span id="search-filter-label" class="sr-only">Search result type</span>
  <button type="button" class="search-filter active" data-search-filter="all" aria-pressed="true">All</button>
  <button type="button" class="search-filter" data-search-filter="topic" aria-pressed="false">Topics</button>
  <button type="button" class="search-filter" data-search-filter="guide" aria-pressed="false">Guides</button>
  <button type="button" class="search-filter" data-search-filter="comparison" aria-pressed="false">Comparisons</button>
  <button type="button" class="search-filter" data-search-filter="roadmap" aria-pressed="false">Roadmaps</button>
  <button type="button" class="search-filter" data-search-filter="transition" aria-pressed="false">Transitions</button>
  <button type="button" class="search-filter" data-search-filter="how-to" aria-pressed="false">How-tos</button>
  <button type="button" class="search-filter" data-search-filter="podcast_summary" aria-pressed="false">Podcasts</button>
  <button type="button" class="search-filter" data-search-filter="person" aria-pressed="false">People</button>
  <button type="button" class="search-filter" data-search-filter="book" aria-pressed="false">Books</button>
  <button type="button" class="search-filter" data-search-filter="section" aria-pressed="false">Sections</button>
</div>

<div id="search-status" class="muted" role="status" aria-live="polite" aria-atomic="true"></div>
<div id="search-results" class="results" aria-live="polite" aria-busy="false"></div>

<script>
  window.PODWIKI_SEARCH_API = "{{ site.search_api_url }}"
</script>
<script src="{{ '/assets/search.js' | relative_url }}"></script>
