---
layout: default
title: How-Tos
permalink: /how-tos-page/
---

# How-Tos

Procedural guides for building, setting up, and operating data and AI systems.

{% assign items = site.wiki | where_exp: "item", "item.tags contains 'how-to'" | sort: "title" %}
{% if items.size > 0 %}
<div class="list">
{% for item in items %}
  {% unless item.redirect_to %}
  <a class="row" href="{{ item.url | relative_url }}">
    <strong>{{ item.title }}</strong>
    {% if item.summary %}<span>{{ item.summary }}</span>{% endif %}
  </a>
  {% endunless %}
{% endfor %}
</div>
{% else %}
<p class="muted">How-tos are being grouped from podcast-backed content.</p>
{% endif %}
