---
layout: default
title: How-Tos
permalink: /how-tos/
---

# How-Tos

Podcast-backed procedural pages for building, setting up, or operating a
specific workflow.

{% assign pages = site.how_tos | sort: "title" %}
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
<p class="muted">How-tos are being grouped from podcast-backed content.</p>
{% endif %}
