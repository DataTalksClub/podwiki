---
layout: default
title: Comparisons
permalink: /special-pages/comparisons/
---

# Comparisons

Side-by-side comparisons of data and AI tools, roles, and architectures.

{% assign items = site.wiki | sort: "title" %}
{% if items.size > 0 %}
<div class="grid">
{% for item in items %}
  {% if item.tags contains 'comparison' and item.redirect_to == nil %}
  <a class="card" href="{{ item.url | relative_url }}">
    <strong>{{ item.title }}</strong>
    {% if item.summary %}<span>{{ item.summary }}</span>{% endif %}
  </a>
  {% endif %}
{% endfor %}
</div>
{% else %}
<p class="muted">Comparisons are being grouped from podcast-backed content.</p>
{% endif %}
