---
layout: default
title: Search
permalink: /search.html
---

# Search

<div class="search-panel">
  <input id="search-input" type="search" placeholder="Search wiki, articles, people, and podcast summaries" autocomplete="off" />
  <button id="search-button" type="button">Search</button>
</div>

<div id="search-status" class="muted"></div>
<div id="search-results" class="results"></div>

<script>
  window.PODWIKI_SEARCH_API = "{{ site.search_api_url }}";
</script>
<script src="/assets/search.js"></script>
