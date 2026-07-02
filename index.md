---
layout: default
title: Podcast Wiki
---

# DataTalks.Club Podcast Wiki

<p class="lede">Explore the DataTalks.Club podcast archive by topic, guest, and
format — every page grounded in real episodes.</p>

<form class="home-search" action="{{ '/search.html' | relative_url }}" method="get">
  <input name="q" type="search" placeholder="Search RAG, career transitions, feature stores..." />
  <button type="submit">Search</button>
</form>

<div class="quick-actions">
  <a class="button" href="{{ '/wiki/' | relative_url }}">Read the wiki</a>
  <a class="button secondary" href="{{ '/graph.html' | relative_url }}">Open the graph</a>
  <a class="button secondary" href="{{ '/search.html' | relative_url }}">Search</a>
</div>

## Explore by format

{% assign guides = site.wiki | where_exp: "item", "item.tags contains 'guide'" %}
{% assign comparisons = site.wiki | where_exp: "item", "item.tags contains 'comparison'" %}
{% assign roadmaps = site.wiki | where_exp: "item", "item.tags contains 'roadmap'" %}
{% assign howtos = site.wiki | where_exp: "item", "item.tags contains 'how-to'" %}

<div class="format-list">
  <a class="format-item" href="{{ '/wiki/' | relative_url }}">
    <span class="format-text">
      <strong>Wiki topics</strong>
      <span>Evidence-backed topic pages synthesized from the archive</span>
    </span>
    <span class="format-arrow" aria-hidden="true">&rarr;</span>
  </a>
  <a class="format-item" href="{{ '/guides-page/' | relative_url }}">
    <span class="format-text">
      <strong>Guides</strong>
      <span>Practical, podcast-grounded walkthroughs</span>
    </span>
    <span class="format-arrow" aria-hidden="true">&rarr;</span>
  </a>
  <a class="format-item" href="{{ '/comparisons-page/' | relative_url }}">
    <span class="format-text">
      <strong>Comparisons</strong>
      <span>Side-by-side tools, roles, and architectures</span>
    </span>
    <span class="format-arrow" aria-hidden="true">&rarr;</span>
  </a>
  <a class="format-item" href="{{ '/roadmaps-page/' | relative_url }}">
    <span class="format-text">
      <strong>Roadmaps</strong>
      <span>Step-by-step learning paths</span>
    </span>
    <span class="format-arrow" aria-hidden="true">&rarr;</span>
  </a>
  <a class="format-item" href="{{ '/how-tos-page/' | relative_url }}">
    <span class="format-text">
      <strong>How-tos</strong>
      <span>Task-focused, answer-first pages</span>
    </span>
    <span class="format-arrow" aria-hidden="true">&rarr;</span>
  </a>
</div>

## Start exploring

{% assign wiki_pages = site.wiki | sort: "title" %}
<div class="grid">
{% for item in wiki_pages limit: 9 %}
  {% unless item.redirect_to %}
  <a class="card" href="{{ item.url | relative_url }}">
    <strong>{{ item.title }}</strong>
    {% if item.summary %}<span>{{ item.summary }}</span>{% endif %}
  </a>
  {% endunless %}
{% endfor %}
</div>

<p class="graph-open"><a class="button secondary" href="{{ '/wiki/' | relative_url }}">Browse all wiki topics →</a></p>
