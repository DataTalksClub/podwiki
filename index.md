---
layout: default
title: Podcast Wiki
---

{% assign pages = site.wiki | sort_natural: "title" %}

{%- comment -%} Count total + tagged topics for the format tiles {%- endcomment -%}
{% assign c_total = 0 %}
{% assign c_guide = 0 %}{% assign c_comparison = 0 %}{% assign c_roadmap = 0 %}{% assign c_howto = 0 %}
{%- for item in pages -%}
  {%- unless item.redirect_to -%}
    {% assign c_total = c_total | plus: 1 %}
    {%- if item.tags -%}
      {%- for t in item.tags -%}
        {%- if t == "guide" -%}{% assign c_guide = c_guide | plus: 1 %}{%- endif -%}
        {%- if t == "comparison" -%}{% assign c_comparison = c_comparison | plus: 1 %}{%- endif -%}
        {%- if t == "roadmap" -%}{% assign c_roadmap = c_roadmap | plus: 1 %}{%- endif -%}
        {%- if t == "how-to" -%}{% assign c_howto = c_howto | plus: 1 %}{%- endif -%}
      {%- endfor -%}
    {%- endif -%}
  {%- endunless -%}
{%- endfor -%}

<h1 class="sr-only">DataTalks.Club Podcast Wiki</h1>

<form class="home-search" action="{{ '/search.html' | relative_url }}" method="get" role="search">
  <input name="q" type="search" aria-label="Search the wiki" placeholder="Search RAG, career transitions, feature stores..." />
</form>

{% if c_total > 0 %}

{%- comment -%} ---------- Explore by format ---------- {%- endcomment -%}
<h2 class="wiki-section-head">Explore by format</h2>
<div class="wiki-formats">
  {% if c_guide > 0 %}
  <a class="wiki-format" href="{{ '/guides-page/' | relative_url }}">
    <span class="wiki-format-count">{{ c_guide }}</span>
    <span class="wiki-format-name">Guides</span>
    <span class="wiki-format-desc">Practical, keyword-driven walkthroughs of a topic.</span>
  </a>
  {% endif %}
  {% if c_comparison > 0 %}
  <a class="wiki-format" href="{{ '/comparisons-page/' | relative_url }}">
    <span class="wiki-format-count">{{ c_comparison }}</span>
    <span class="wiki-format-name">Comparisons</span>
    <span class="wiki-format-desc">Head-to-head breakdowns to help you choose.</span>
  </a>
  {% endif %}
  {% if c_roadmap > 0 %}
  <a class="wiki-format" href="{{ '/roadmaps-page/' | relative_url }}">
    <span class="wiki-format-count">{{ c_roadmap }}</span>
    <span class="wiki-format-name">Roadmaps</span>
    <span class="wiki-format-desc">Step-by-step paths to learn or level up a skill.</span>
  </a>
  {% endif %}
  {% if c_howto > 0 %}
  <a class="wiki-format" href="{{ '/how-tos-page/' | relative_url }}">
    <span class="wiki-format-count">{{ c_howto }}</span>
    <span class="wiki-format-name">How-tos</span>
    <span class="wiki-format-desc">Task-focused checklists and project recipes.</span>
  </a>
  {% endif %}
</div>

{%- comment -%} ---------- Start here: curated foundational hubs ---------- {%- endcomment -%}
{% assign featured_slugs = "retrieval-augmented-generation,llms,mlops,machine-learning,data-engineering,feature-stores,experimentation,vector-databases" | split: "," %}
{%- capture featured_cards -%}
{%- for slug in featured_slugs -%}
  {%- capture target -%}/wiki/{{ slug }}/{%- endcapture -%}
  {%- for item in pages -%}
    {%- unless item.redirect_to -%}
      {%- assign item_path = item.url | remove_first: site.baseurl -%}
      {%- if item_path == target -%}
      <a class="wiki-card" href="{{ item.url | relative_url }}">
        <span class="wiki-card-title">{{ item.title }}</span>
        {% if item.summary %}<span class="wiki-card-summary">{{ item.summary }}</span>{% endif %}
      </a>
      {%- endif -%}
    {%- endunless -%}
  {%- endfor -%}
{%- endfor -%}
{%- endcapture -%}
{% assign featured_cards = featured_cards | strip %}
{% if featured_cards != "" %}
<h2 class="wiki-section-head">Start here</h2>
<p class="wiki-section-lede">Foundational topic hubs that anchor the rest of the wiki.</p>
<div class="wiki-grid">
{{ featured_cards }}
</div>
{% endif %}

{%- comment -%} ---------- Browse the full catalog ---------- {%- endcomment -%}
<a class="wiki-catalog-cta" href="{{ '/wiki/' | relative_url }}">
  <span class="wiki-catalog-cta-text">
    <span class="wiki-catalog-cta-title">Browse the full catalog</span>
    <span class="wiki-catalog-cta-sub">Search across all {{ c_total }} topics A-Z.</span>
  </span>
  <span class="wiki-catalog-cta-arrow" aria-hidden="true">&rarr;</span>
</a>

{% else %}
<p class="muted">Wiki pages are being drafted from the archive analysis.</p>
{% endif %}

<section class="home-graph graph-connections" data-graph-connections data-graph-random hidden></section>

<script src="{{ '/assets/page-graph.js' | relative_url }}"></script>
