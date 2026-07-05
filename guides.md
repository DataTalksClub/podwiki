---
layout: default
title: Guides
permalink: /special-pages/guides/
---

# Guides

Practical, keyword-driven guides grounded in DataTalks.Club podcast episodes.

{% assign items = site.wiki | sort: "title" %}
{% if items.size > 0 %}
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
<p class="muted">Guides are being grouped from podcast-backed content.</p>
{% endif %}
