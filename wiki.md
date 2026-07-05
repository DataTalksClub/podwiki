---
layout: default
title: Wiki Catalog
permalink: /wiki/
---

{% assign pages = site.wiki | sort_natural: "title" %}

{%- comment -%} Count public wiki topics for the catalog header {%- endcomment -%}
{% assign c_total = 0 %}
{% assign c_topic_hub = 0 %}
{% assign c_guide = 0 %}
{% assign c_comparison = 0 %}
{% assign c_roadmap = 0 %}
{% assign c_transition = 0 %}
{% assign c_howto = 0 %}
{%- for item in pages -%}
  {%- unless item.redirect_to -%}
    {% assign c_total = c_total | plus: 1 %}
    {%- if item.tags and item.tags.size > 0 -%}
      {%- if item.tags contains "guide" -%}
        {% assign c_guide = c_guide | plus: 1 %}
      {%- endif -%}
      {%- if item.tags contains "comparison" -%}
        {% assign c_comparison = c_comparison | plus: 1 %}
      {%- endif -%}
      {%- if item.tags contains "roadmap" -%}
        {% assign c_roadmap = c_roadmap | plus: 1 %}
      {%- endif -%}
      {%- if item.tags contains "transition" -%}
        {% assign c_transition = c_transition | plus: 1 %}
      {%- endif -%}
      {%- if item.tags contains "how-to" -%}
        {% assign c_howto = c_howto | plus: 1 %}
      {%- endif -%}
    {%- else -%}
      {% assign c_topic_hub = c_topic_hub | plus: 1 %}
    {%- endif -%}
  {%- endunless -%}
{%- endfor -%}

<div class="wiki-pagehead">
  <p class="wiki-back"><a href="{{ '/' | relative_url }}">Home</a></p>
  <h1 class="wiki-pagehead-title">Wiki Catalog <span class="wiki-pagehead-count">{{ c_total }} pages</span></h1>
  <p class="wiki-pagehead-lede">Browse topic hubs, guides, comparisons, roadmaps, transitions, and how-tos.</p>
</div>

{% if c_total > 0 %}
<nav class="wiki-type-nav" aria-label="Browse wiki by type">
  <a class="wiki-type-tab" href="#topic-hubs"><span>Topic Hubs</span><span class="wiki-type-tab-count">{{ c_topic_hub }}</span></a>
  <a class="wiki-type-tab" href="#guides"><span>Guides</span><span class="wiki-type-tab-count">{{ c_guide }}</span></a>
  <a class="wiki-type-tab" href="#comparisons"><span>Comparisons</span><span class="wiki-type-tab-count">{{ c_comparison }}</span></a>
  <a class="wiki-type-tab" href="#roadmaps"><span>Roadmaps</span><span class="wiki-type-tab-count">{{ c_roadmap }}</span></a>
  <a class="wiki-type-tab" href="#transitions"><span>Transitions</span><span class="wiki-type-tab-count">{{ c_transition }}</span></a>
  <a class="wiki-type-tab" href="#how-tos"><span>How-tos</span><span class="wiki-type-tab-count">{{ c_howto }}</span></a>
</nav>

<div class="wiki-type-sections">
  <section class="wiki-type-section" id="topic-hubs">
    <h2 class="wiki-type-title">Topic Hubs <span>{{ c_topic_hub }}</span></h2>
    <p class="wiki-type-lede">Core concepts and roles synthesized from podcast discussions.</p>
    <div class="wiki-type-grid">
      {%- for item in pages -%}
        {%- unless item.redirect_to -%}
          {%- unless item.tags and item.tags.size > 0 -%}
      <a class="wiki-type-card" href="{{ item.url | relative_url }}">
        <span class="wiki-card-title">{{ item.title }}</span>
        {% if item.summary %}<span class="wiki-card-summary">{{ item.summary }}</span>{% endif %}
      </a>
          {%- endunless -%}
        {%- endunless -%}
      {%- endfor -%}
    </div>
  </section>

  <section class="wiki-type-section" id="guides">
    <h2 class="wiki-type-title">Guides <span>{{ c_guide }}</span></h2>
    <p class="wiki-type-lede">Practical pages for choosing tools, framing work, and applying interview patterns.</p>
    <div class="wiki-type-grid">
      {%- for item in pages -%}
        {%- unless item.redirect_to -%}
          {%- if item.tags contains "guide" -%}
      <a class="wiki-type-card" href="{{ item.url | relative_url }}">
        <span class="wiki-card-title">{{ item.title }}</span>
        {% if item.summary %}<span class="wiki-card-summary">{{ item.summary }}</span>{% endif %}
      </a>
          {%- endif -%}
        {%- endunless -%}
      {%- endfor -%}
    </div>
  </section>

  <section class="wiki-type-section" id="comparisons">
    <h2 class="wiki-type-title">Comparisons <span>{{ c_comparison }}</span></h2>
    <p class="wiki-type-lede">Side-by-side tradeoffs across roles, platforms, and engineering choices.</p>
    <div class="wiki-type-grid">
      {%- for item in pages -%}
        {%- unless item.redirect_to -%}
          {%- if item.tags contains "comparison" -%}
      <a class="wiki-type-card" href="{{ item.url | relative_url }}">
        <span class="wiki-card-title">{{ item.title }}</span>
        {% if item.summary %}<span class="wiki-card-summary">{{ item.summary }}</span>{% endif %}
      </a>
          {%- endif -%}
        {%- endunless -%}
      {%- endfor -%}
    </div>
  </section>

  <section class="wiki-type-section" id="roadmaps">
    <h2 class="wiki-type-title">Roadmaps <span>{{ c_roadmap }}</span></h2>
    <p class="wiki-type-lede">Learning paths and role paths for data, ML, MLOps, and AI engineering work.</p>
    <div class="wiki-type-grid">
      {%- for item in pages -%}
        {%- unless item.redirect_to -%}
          {%- if item.tags contains "roadmap" -%}
      <a class="wiki-type-card" href="{{ item.url | relative_url }}">
        <span class="wiki-card-title">{{ item.title }}</span>
        {% if item.summary %}<span class="wiki-card-summary">{{ item.summary }}</span>{% endif %}
      </a>
          {%- endif -%}
        {%- endunless -%}
      {%- endfor -%}
    </div>
  </section>

  <section class="wiki-type-section" id="transitions">
    <h2 class="wiki-type-title">Transitions <span>{{ c_transition }}</span></h2>
    <p class="wiki-type-lede">Career-change paths between backgrounds, data roles, and AI roles.</p>
    <div class="wiki-type-grid">
      {%- for item in pages -%}
        {%- unless item.redirect_to -%}
          {%- if item.tags contains "transition" -%}
      <a class="wiki-type-card" href="{{ item.url | relative_url }}">
        <span class="wiki-card-title">{{ item.title }}</span>
        {% if item.summary %}<span class="wiki-card-summary">{{ item.summary }}</span>{% endif %}
      </a>
          {%- endif -%}
        {%- endunless -%}
      {%- endfor -%}
    </div>
  </section>

  <section class="wiki-type-section" id="how-tos">
    <h2 class="wiki-type-title">Procedural Guides <span>{{ c_howto }}</span></h2>
    <p class="wiki-type-lede">Procedural pages for building, setting up, and operating data and AI systems.</p>
    <div class="wiki-type-grid">
      {%- for item in pages -%}
        {%- unless item.redirect_to -%}
          {%- if item.tags contains "how-to" -%}
      <a class="wiki-type-card" href="{{ item.url | relative_url }}">
        <span class="wiki-card-title">{{ item.title }}</span>
        {% if item.summary %}<span class="wiki-card-summary">{{ item.summary }}</span>{% endif %}
      </a>
          {%- endif -%}
        {%- endunless -%}
      {%- endfor -%}
    </div>
  </section>
</div>

<h2 class="wiki-catalog-title" id="all-pages">All Pages</h2>

<div class="wiki-controls" role="search">
  <div class="wiki-controls-row">
    <div class="wiki-search">
      <svg class="wiki-search-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
        <circle cx="11" cy="11" r="7"></circle>
        <line x1="21" y1="21" x2="16.65" y2="16.65"></line>
      </svg>
      <input id="wiki-filter" type="search" autocomplete="off" placeholder="Filter {{ c_total }} pages by name or keyword…" aria-label="Filter pages">
      <button class="wiki-search-clear" type="button" aria-label="Clear filter" hidden>Clear</button>
    </div>
  </div>
</div>

<p class="wiki-count">Showing <span id="wiki-count">{{ c_total }}</span> of {{ c_total }} pages</p>

<div class="wiki-sections">
{% assign current_letter = "__none__" %}
{%- for item in pages -%}
  {%- unless item.redirect_to -%}
    {%- assign L = item.title | slice: 0 | upcase -%}
    {%- if L != current_letter -%}
      {%- unless current_letter == "__none__" -%}
    </div>
  </section>
      {%- endunless -%}
  <section class="wiki-section" data-letter="{{ L }}">
    <h2 class="wiki-letter" id="letter-{{ L }}"><span class="wiki-letter-badge">{{ L }}</span></h2>
    <div class="wiki-grid">
      {%- assign current_letter = L -%}
    {%- endif -%}
      <a class="wiki-card" href="{{ item.url | relative_url }}" data-letter="{{ L }}" data-tags="{{ item.tags | join: ' ' }}" data-search="{{ item.title | append: ' ' | append: item.summary | downcase | escape }}">
        <span class="wiki-card-title">{{ item.title }}</span>
        {% if item.summary %}<span class="wiki-card-summary">{{ item.summary }}</span>{% endif %}
        {%- if item.tags and item.tags.size > 0 -%}
        <span class="wiki-card-tags">{% for t in item.tags %}<span class="wiki-badge">{{ t }}</span>{% endfor %}</span>
        {%- endif -%}
      </a>
  {%- endunless -%}
{%- endfor -%}
    </div>
  </section>
</div>

<p class="wiki-empty" hidden>No pages match your filter. Try a different keyword.</p>

<script src="{{ '/assets/wiki-catalog.js' | relative_url }}"></script>
{% else %}
<p class="muted">Wiki pages are being drafted from the archive analysis.</p>
{% endif %}
