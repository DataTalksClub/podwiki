---
layout: default
title: Roadmaps
permalink: /special-pages/roadmaps/
---

# Roadmaps

These roadmaps organize podcast-backed learning paths for roles, transitions,
and project sequences.

{% assign items = site.wiki | sort: "title" %}
{% if items.size > 0 %}
<div class="grid">
{% for item in items %}
  {% if item.tags contains 'roadmap' and item.redirect_to == nil %}
  <a class="card" href="{{ item.url | relative_url }}">
    <strong>{{ item.title }}</strong>
    {% if item.summary %}<span>{{ item.summary }}</span>{% endif %}
  </a>
  {% endif %}
{% endfor %}
</div>
{% else %}
<p class="muted">Roadmaps are being grouped from podcast-backed content.</p>
{% endif %}
