---
layout: default
title: Book of the Week
permalink: /books-page/
---

# Book of the Week

Local book pages are the internal citation targets for the wiki, guides,
comparisons, roadmaps, and how-tos. Each page links to the original
DataTalks.Club Book of the Week discussion.

{% assign pages = site.books | sort: "title" %}
{% if pages.size > 0 %}
<div class="podcast-list">
{% for item in pages %}
  <article class="podcast-list-item">
    <div class="podcast-list-meta">
      {% if item.author_names %}<span>by {{ item.author_names | join: ", " }}</span>{% endif %}
      {% if item.qa_count %}<span>{{ item.qa_count }} Q&A threads</span>{% endif %}
    </div>
    <h2><a href="{{ item.url | relative_url }}">{{ item.title }}</a></h2>
    {% if item.topics %}
      <p class="muted">{{ item.topics | join: ", " }}</p>
    {% endif %}
    <p>
      <a href="{{ item.url | relative_url }}">Open local notes</a>
      {% if item.source_url %} · <a href="{{ item.source_url }}">Original book page</a>{% endif %}
    </p>
  </article>
{% endfor %}
</div>
{% else %}
<p class="muted">Book pages are being drafted from the source archive.</p>
{% endif %}
