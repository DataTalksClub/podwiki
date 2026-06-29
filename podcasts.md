---
layout: default
title: Podcast Summaries
permalink: /podcasts/
---

# Podcast Summaries

Agent-friendly episode notes. These pages summarize what each episode covers and
link back to the original DataTalks.Club podcast pages; they do not copy full
transcripts.

{% assign pages = site.podcast_summaries | sort: "title" %}
{% if pages.size > 0 %}
<div class="list">
{% for item in pages %}
  <a class="row" href="{{ item.url }}">
    <strong>{{ item.title }}</strong>
    <span>{% if item.season %}S{{ item.season }}E{{ item.episode }}{% endif %}</span>
  </a>
{% endfor %}
</div>
{% else %}
<p class="muted">Podcast summaries are being drafted from the source archive.</p>
{% endif %}
