---
layout: default
title: Podcast Wiki
---

# DataTalks.Club Podcast Wiki

Explore DataTalks.Club podcast episodes by topic, guest, transcript segment,
and podcast-backed content.

<form class="home-search" action="{{ '/search.html' | relative_url }}" method="get">
  <input name="q" type="search" placeholder="Search RAG, career transitions, feature stores..." />
  <button type="submit">Search</button>
</form>

<div class="quick-actions">
  <a class="button" href="{{ '/graph.html' | relative_url }}">Open podcast graph</a>
  <a class="button secondary" href="{{ '/wiki/' | relative_url }}">Read wiki</a>
  <a class="button secondary" href="{{ '/guides-page/' | relative_url }}">Browse guides</a>
  <a class="button secondary" href="{{ '/comparisons-page/' | relative_url }}">Browse comparisons</a>
  <a class="button secondary" href="{{ '/roadmaps-page/' | relative_url }}">Browse roadmaps</a>
  <a class="button secondary" href="{{ '/how-tos-page/' | relative_url }}">Browse how-tos</a>
  <a class="button secondary" href="{{ '/podcasts/' | relative_url }}">Browse summaries</a>
  <a class="button secondary" href="{{ '/books-page/' | relative_url }}">Browse books</a>
  <a class="button secondary" href="{{ '/people/' | relative_url }}">Browse people</a>
  <a class="button secondary" href="{{ '/search.html' | relative_url }}">Search content</a>
</div>

## Wiki

{% assign wiki_pages = site.wiki | sort: "title" %}
{% if wiki_pages.size > 0 %}
<div class="grid">
{% for item in wiki_pages %}
  {% unless item.redirect_to %}
  <a class="card" href="{{ item.url | relative_url }}">
    <strong>{{ item.title }}</strong>
    {% if item.summary %}<span>{{ item.summary }}</span>{% endif %}
  </a>
  {% endunless %}
{% endfor %}
</div>
{% else %}
<p class="muted">Wiki pages are being drafted from archive evidence.</p>
{% endif %}

## Guides

{% assign guides = site.wiki  | sort: "title" %}
{% if guides.size > 0 %}
<div class="list">
{% for item in guides limit: 8 %}
  <a class="row" href="{{ item.url | relative_url }}">
    <strong>{{ item.title }}</strong>
    {% if item.summary %}<span>{{ item.summary }}</span>{% endif %}
  </a>
{% endfor %}
</div>
{% else %}
<p class="muted">Guides are being grouped from podcast-backed editorial pages.</p>
{% endif %}

## Comparisons

{% assign comparisons = site.wiki  | sort: "title" %}
{% if comparisons.size > 0 %}
<div class="list">
{% for item in comparisons limit: 6 %}
  {% unless item.redirect_to %}
  <a class="row" href="{{ item.url | relative_url }}">
    <strong>{{ item.title }}</strong>
    {% if item.summary %}<span>{{ item.summary }}</span>{% endif %}
  </a>
  {% endunless %}
{% endfor %}
</div>
{% else %}
<p class="muted">Comparison pages are being grouped from archive-backed pages.</p>
{% endif %}

## Roadmaps

{% assign roadmaps = site.wiki  | sort: "title" %}
{% if roadmaps.size > 0 %}
<div class="list">
{% for item in roadmaps limit: 6 %}
  <a class="row" href="{{ item.url | relative_url }}">
    <strong>{{ item.title }}</strong>
    {% if item.summary %}<span>{{ item.summary }}</span>{% endif %}
  </a>
{% endfor %}
</div>
{% else %}
<p class="muted">Roadmaps are being grouped from archive-backed pages.</p>
{% endif %}

## How-Tos

{% assign howtos = site.wiki  | sort: "title" %}
{% if howtos.size > 0 %}
<div class="list">
{% for item in howtos limit: 6 %}
  <a class="row" href="{{ item.url | relative_url }}">
    <strong>{{ item.title }}</strong>
    {% if item.summary %}<span>{{ item.summary }}</span>{% endif %}
  </a>
{% endfor %}
</div>
{% else %}
<p class="muted">How-tos are being grouped from archive-backed pages.</p>
{% endif %}
