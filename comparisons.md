---
layout: default
title: Comparisons
permalink: /comparisons-page/
---

# Comparisons

Side-by-side comparisons of data and AI tools, roles, and architectures.

{% assign items = site.wiki | where_exp: "item", "item.tags contains 'comparison'" | sort: "title" %}
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
<p class="muted">Comparisons are being grouped from podcast-backed content.</p>
{% endif %}
