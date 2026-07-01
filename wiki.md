---
layout: default
title: Podcast Wiki
permalink: /wiki/
---

# Podcast Wiki

Comprehensive, evidence-backed guides synthesized from the DataTalks.Club podcast
archive.

{% assign pages = site.wiki | sort: "title" %}
{% if pages.size > 0 %}
<div class="grid">
{% for item in pages %}
  {% unless item.redirect_to %}
  <a class="card" href="{{ item.url | relative_url }}">
    <strong>{{ item.title }}</strong>
    {% if item.summary %}<span>{{ item.summary }}</span>{% endif %}
  </a>
  {% endunless %}
{% endfor %}
</div>
{% else %}
<p class="muted">Wiki pages are being drafted from the archive analysis.</p>
{% endif %}
