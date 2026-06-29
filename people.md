---
layout: default
title: People
permalink: /people/
---

# People

Guests and contributors extracted from the DataTalks.Club source records, with
links to the concepts, articles, and podcast summaries they support.

{% assign pages = site.people | sort: "title" %}
{% if pages.size > 0 %}
<div class="grid">
{% for item in pages %}
  <a class="card" href="{{ item.url }}">
    <strong>{{ item.title }}</strong>
    {% if item.summary %}<span>{{ item.summary }}</span>{% endif %}
  </a>
{% endfor %}
</div>
{% else %}
<p class="muted">People pages are being prepared from the source archive.</p>
{% endif %}
