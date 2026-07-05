---
layout: default
title: Special Pages
permalink: /special-pages/
---

<h1>Special Pages</h1>

<p class="lede">Browse the guides, comparisons, roadmaps, transitions, and how-tos in the wiki.</p>

{% assign items = site.wiki | sort_natural: "title" %}
{% assign guide_count = 0 %}
{% assign comparison_count = 0 %}
{% assign roadmap_count = 0 %}
{% assign transition_count = 0 %}
{% assign howto_count = 0 %}
{% assign all_count = 0 %}
{%- for item in items -%}
  {%- unless item.redirect_to -%}
    {%- if item.tags contains "guide" -%}
      {% assign guide_count = guide_count | plus: 1 %}
      {% assign all_count = all_count | plus: 1 %}
    {%- endif -%}
    {%- if item.tags contains "comparison" -%}
      {% assign comparison_count = comparison_count | plus: 1 %}
      {% assign all_count = all_count | plus: 1 %}
    {%- endif -%}
    {%- if item.tags contains "roadmap" -%}
      {% assign roadmap_count = roadmap_count | plus: 1 %}
      {% assign all_count = all_count | plus: 1 %}
    {%- endif -%}
    {%- if item.tags contains "transition" -%}
      {% assign transition_count = transition_count | plus: 1 %}
      {% assign all_count = all_count | plus: 1 %}
    {%- endif -%}
    {%- if item.tags contains "how-to" -%}
      {% assign howto_count = howto_count | plus: 1 %}
      {% assign all_count = all_count | plus: 1 %}
    {%- endif -%}
  {%- endunless -%}
{%- endfor -%}

<div class="tag-filter" id="tag-filter" aria-label="Special page type">
  <button type="button" class="tag-btn active" data-tag="all" aria-pressed="true">All {{ all_count }}</button>
  <button type="button" class="tag-btn" data-tag="guide" aria-pressed="false">Guides {{ guide_count }}</button>
  <button type="button" class="tag-btn" data-tag="comparison" aria-pressed="false">Comparisons {{ comparison_count }}</button>
  <button type="button" class="tag-btn" data-tag="roadmap" aria-pressed="false">Roadmaps {{ roadmap_count }}</button>
  <button type="button" class="tag-btn" data-tag="transition" aria-pressed="false">Transitions {{ transition_count }}</button>
  <button type="button" class="tag-btn" data-tag="how-to" aria-pressed="false">How-tos {{ howto_count }}</button>
</div>

<p class="filter-count" id="filter-count"></p>

<div class="grid" id="special-grid">
  {% for item in items %}
    {% assign is_special = false %}
    {% if item.tags contains "guide" %}
      {% assign is_special = true %}
    {% endif %}
    {% if item.tags contains "comparison" %}
      {% assign is_special = true %}
    {% endif %}
    {% if item.tags contains "roadmap" %}
      {% assign is_special = true %}
    {% endif %}
    {% if item.tags contains "transition" %}
      {% assign is_special = true %}
    {% endif %}
    {% if item.tags contains "how-to" %}
      {% assign is_special = true %}
    {% endif %}
    {% if is_special and item.redirect_to == nil %}
    <a class="card special-card"
       href="{{ item.url | relative_url }}"
       data-tags="{{ item.tags | join: ',' }}">
      <strong>{{ item.title }}</strong>
      {% if item.summary %}<span>{{ item.summary }}</span>{% endif %}
      <span class="card-tags">
        {% for tag in item.tags %}<em>{{ tag }}</em>{% endfor %}
      </span>
    </a>
    {% endif %}
  {% endfor %}
</div>

<script src="{{ '/assets/special-pages.js' | relative_url }}"></script>
