---
layout: default
title: Roadmaps
permalink: /roadmaps/
---

# Roadmaps

Podcast-backed learning paths for roles, transitions, and project sequences.

{% assign pages = site.roadmaps | sort: "title" %}
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
<p class="muted">Roadmaps are being grouped from podcast-backed content.</p>
{% endif %}
