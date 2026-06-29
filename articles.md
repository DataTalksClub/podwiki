---
layout: default
title: Articles
permalink: /articles/
---

# Articles

SEO-focused editorial articles will be created from the keyword list you provide.

{% assign pages = site.articles | sort: "title" %}
{% if pages.size > 0 %}
<div class="grid">
{% for item in pages %}
  <a class="card" href="{{ item.url }}">
    <strong>{{ item.title }}</strong>
    {% if item.keyword %}<span>{{ item.keyword }}</span>{% endif %}
  </a>
{% endfor %}
</div>
{% else %}
<p class="muted">No keyword-driven articles have been generated yet.</p>
{% endif %}
