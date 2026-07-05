---
layout: default
title: Transitions
permalink: /transitions-page/
---

# Transitions

Career-change pages for moving from one background into another data or AI role.

{% assign items = site.wiki | sort: "title" %}
<div class="grid">
{% for item in items %}
  {% if item.tags contains "transition" %}
  <a class="card" href="{{ item.url | relative_url }}">
    <strong>{{ item.title }}</strong>
    {% if item.summary %}<span>{{ item.summary }}</span>{% endif %}
  </a>
  {% endif %}
{% endfor %}
</div>
