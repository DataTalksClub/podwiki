---
layout: default
title: Guides
permalink: /guides/
---

# Guides

Practical, podcast-backed pages for editorial questions that need synthesis
rather than a dictionary-style topic page.

{% assign pages = site.guides | sort: "title" %}
{% if pages.size > 0 %}
<div class="grid">
{% for item in pages %}
  <a class="card" href="{{ item.url | relative_url }}">
    <strong>{{ item.title }}</strong>
    {% if item.summary %}<span>{{ item.summary }}</span>{% endif %}
  </a>
{% endfor %}
</div>
{% else %}
<p class="muted">Guide pages are being grouped from podcast-backed content.</p>
{% endif %}
