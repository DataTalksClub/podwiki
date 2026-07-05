---
layout: default
title: How-to Pages
permalink: /special-pages/how-tos/
---

# How-to Pages

Procedural guides for building, setting up, and operating data and AI systems.

{% assign items = site.wiki | sort: "title" %}
{% if items.size > 0 %}
<div class="grid">
{% for item in items %}
  {% if item.tags contains 'how-to' and item.redirect_to == nil %}
  <a class="card" href="{{ item.url | relative_url }}">
    <strong>{{ item.title }}</strong>
    {% if item.summary %}<span>{{ item.summary }}</span>{% endif %}
  </a>
  {% endif %}
{% endfor %}
</div>
{% else %}
<p class="muted">How-tos are being grouped from podcast-backed content.</p>
{% endif %}
