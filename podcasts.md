---
layout: default
title: Podcasts
permalink: /podcasts/
---

# Podcasts

Local podcast pages are the internal citation targets for the wiki and articles.
Each page links to the original DataTalks.Club episode.

{% assign pages = site.podcast_summaries | sort: "season" | reverse %}
{% if pages.size > 0 %}
<div class="podcast-list">
{% for item in pages %}
  <article class="podcast-list-item">
    <div class="podcast-list-meta">
      {% if item.season %}<span>Season {{ item.season }}</span>{% endif %}
      {% if item.episode %}<span>Episode {{ item.episode }}</span>{% endif %}
    </div>
    <h2><a href="{{ item.url | relative_url }}">{{ item.title }}</a></h2>
    {% if item.topics %}
      <p class="muted">{{ item.topics | join: ", " }}</p>
    {% endif %}
    <p>
      <a href="{{ item.url | relative_url }}">Open local notes</a>
      {% if item.source_url %} · <a href="{{ item.source_url }}">Original episode</a>{% endif %}
    </p>
  </article>
{% endfor %}
</div>
{% else %}
<p class="muted">Podcast pages are being drafted from the source archive.</p>
{% endif %}
