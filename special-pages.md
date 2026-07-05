---
layout: default
title: Special Pages
permalink: /special-pages/
---

<h1>Special Pages</h1>

<p class="lede">Guides, comparisons, roadmaps, how-tos, and career transitions, all grounded in DataTalks.Club podcast episodes.</p>

<div class="tag-filter" id="tag-filter" aria-label="Special page type">
  <button type="button" class="tag-btn active" data-tag="all" aria-pressed="true">All</button>
  <button type="button" class="tag-btn" data-tag="guide" aria-pressed="false">Guides</button>
  <button type="button" class="tag-btn" data-tag="comparison" aria-pressed="false">Comparisons</button>
  <button type="button" class="tag-btn" data-tag="roadmap" aria-pressed="false">Roadmaps</button>
  <button type="button" class="tag-btn" data-tag="transition" aria-pressed="false">Transitions</button>
  <button type="button" class="tag-btn" data-tag="how-to" aria-pressed="false">How-Tos</button>
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
    buttons.forEach(function(btn) {
      var active = btn.getAttribute('data-tag') === tag;
      btn.classList.toggle('active', active);
      btn.setAttribute('aria-pressed', active ? 'true' : 'false');
    });
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
      var tag = btn.getAttribute('data-tag');
      if (window.history && window.history.replaceState) {
        window.history.replaceState(null, '', tag === 'all' ? window.location.pathname : '#' + tag);
      }
      apply(tag);
    });
  });

  var initial = window.location.hash ? window.location.hash.slice(1) : 'all';
  var valid = Array.prototype.some.call(buttons, function(btn) {
    return btn.getAttribute('data-tag') === initial;
  });
  apply(valid ? initial : 'all');
})();
</script>
