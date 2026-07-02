---
layout: default
title: Roadmaps
permalink: /roadmaps-page/
---

# Roadmaps

Podcast-backed learning paths for roles, transitions, and project sequences.

{% assign items = site.wiki | where_exp: "item", "item.tags contains 'roadmap'" | sort: "title" %}
{% if items.size > 0 %}
<div class="grid">
{% for item in items %}
  {% unless item.redirect_to %}
  <a class="card" href="{{ item.url | relative_url }}">
    <strong>{{ item.title }}</strong>
    {% if item.summary %}<span>{{ item.summary }}</span>{% endif %}
  </a>
  {% endunless %}
{% endfor %}
</div>
{% else %}
<p class="muted">Roadmaps are being grouped from podcast-backed content.</p>
{% endif %}
