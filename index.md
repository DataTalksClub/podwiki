---
layout: default
title: Podcast Wiki
---

# DataTalks.Club Podcast Wiki

Explore DataTalks.Club podcast episodes by topic, guest, and transcript segment.

<form class="home-search" action="/search.html" method="get">
  <input name="q" type="search" placeholder="Search RAG, career transitions, feature stores..." />
  <button type="submit">Search</button>
</form>

<div class="quick-actions">
  <a class="button" href="/graph.html">Open podcast graph</a>
  <a class="button secondary" href="/wiki/">Read wiki</a>
  <a class="button secondary" href="/podcasts/">Browse summaries</a>
  <a class="button secondary" href="/people/">Browse people</a>
  <a class="button secondary" href="/search.html">Search transcripts</a>
</div>

## Wiki

{% assign wiki_pages = site.wiki | sort: "title" %}
{% if wiki_pages.size > 0 %}
<div class="grid">
{% for item in wiki_pages %}
  <a class="card" href="{{ item.url }}">
    <strong>{{ item.title }}</strong>
    {% if item.summary %}<span>{{ item.summary }}</span>{% endif %}
  </a>
{% endfor %}
</div>
{% else %}
<p class="muted">Wiki pages are being drafted from archive evidence.</p>
{% endif %}

## Articles

{% assign articles = site.articles | sort: "title" %}
{% if articles.size > 0 %}
<div class="list">
{% for item in articles limit: 12 %}
  <a class="row" href="{{ item.url }}">
    <strong>{{ item.title }}</strong>
    {% if item.keyword %}<span>{{ item.keyword }}</span>{% endif %}
  </a>
{% endfor %}
</div>
{% else %}
<p class="muted">Article drafts will be created from selected keyword opportunities.</p>
{% endif %}
