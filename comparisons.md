---
layout: default
title: Comparisons
permalink: /comparisons/
---

# Comparisons

Podcast-backed pages for role boundaries, architecture tradeoffs, and
terminology that people often compare directly.

{% assign pages = site.comparisons | sort: "title" %}
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
<p class="muted">Comparison pages are being grouped from podcast-backed content.</p>
{% endif %}
