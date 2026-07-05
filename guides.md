---
layout: default
title: Guides
permalink: /special-pages/guides/
---

# Guides

Practical guides for data and AI roles, tools, projects, and workflows.

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

<p class="filter-count">{{ guide_count }} {% if guide_count == 1 %}page{% else %}pages{% endif %}</p>

<nav class="tag-filter" aria-label="Format categories">
  <a class="tag-btn active" href="{{ '/special-pages/guides/' | relative_url }}">Guides {{ guide_count }}</a>
  <a class="tag-btn" href="{{ '/special-pages/comparisons/' | relative_url }}">Comparisons {{ comparison_count }}</a>
  <a class="tag-btn" href="{{ '/special-pages/roadmaps/' | relative_url }}">Roadmaps {{ roadmap_count }}</a>
  <a class="tag-btn" href="{{ '/special-pages/transitions/' | relative_url }}">Transitions {{ transition_count }}</a>
  <a class="tag-btn" href="{{ '/special-pages/how-tos/' | relative_url }}">How-tos {{ howto_count }}</a>
  <a class="tag-btn" href="{{ '/special-pages/' | relative_url }}">All {{ all_count }}</a>
</nav>

{% if guide_count > 0 %}
<div class="grid">
{% for item in items %}
  {% if item.tags contains 'guide' and item.redirect_to == nil %}
  <a class="card" href="{{ item.url | relative_url }}">
    <strong>{{ item.title }}</strong>
    {% if item.summary %}<span>{{ item.summary }}</span>{% endif %}
  </a>
  {% endif %}
{% endfor %}
</div>
{% else %}
<p class="muted">No guides yet.</p>
{% endif %}
