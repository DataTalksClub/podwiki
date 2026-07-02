---
layout: default
title: Special Pages
permalink: /special-pages/
---

<h1>Special Pages</h1>

<p class="lede">Guides, comparisons, roadmaps, how-tos, and career transitions — all grounded in DataTalks.Club podcast episodes.</p>

<div class="tag-filter" id="tag-filter">
  <button class="tag-btn active" data-tag="all">All</button>
  <button class="tag-btn" data-tag="guide">Guides</button>
  <button class="tag-btn" data-tag="comparison">Comparisons</button>
  <button class="tag-btn" data-tag="roadmap">Roadmaps</button>
  <button class="tag-btn" data-tag="transition">Transitions</button>
  <button class="tag-btn" data-tag="how-to">How-Tos</button>
</div>

<p class="filter-count" id="filter-count"></p>

<div class="grid" id="special-grid">
  {% assign items = site.wiki | sort: "title" %}
  {% for item in items %}
    {% if item.tags.size > 0 and item.redirect_to == nil %}
    <a class="card special-card"
       href="{{ item.url | relative_url }}"
       data-tags="{{ item.tags | join: ',' }}">
      <strong>{{ item.title }}</strong>
      {% if item.summary %}<span>{{ item.summary }}</span>{% endif %}
      <span class="card-tags">
        {% for tag in item.tags %}<em>{{ tag }}</em>{% endfor %}
      </span>
    </a>
    {% endif %}
  {% endfor %}
</div>

<script>
(function() {
  var buttons = document.querySelectorAll('.tag-btn');
  var cards = document.querySelectorAll('.special-card');
  var count = document.getElementById('filter-count');

  function apply(tag) {
    var shown = 0;
    cards.forEach(function(card) {
      var tags = card.getAttribute('data-tags');
      var match = tag === 'all' || (tags && tags.split(',').map(function(t){return t.trim();}).indexOf(tag) !== -1);
      card.style.display = match ? '' : 'none';
      if (match) shown++;
    });
    if (count) count.textContent = shown + (shown === 1 ? ' page' : ' pages');
  }

  buttons.forEach(function(btn) {
    btn.addEventListener('click', function() {
      buttons.forEach(function(b) { b.classList.remove('active'); });
      btn.classList.add('active');
      apply(btn.getAttribute('data-tag'));
    });
  });

  apply('all');
})();
</script>
