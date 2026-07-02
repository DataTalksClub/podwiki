---
layout: default
title: Wiki Catalog
permalink: /wiki/
---

{% assign pages = site.wiki | sort_natural: "title" %}

{%- comment -%} Count public wiki topics for the catalog header {%- endcomment -%}
{% assign c_total = 0 %}
{%- for item in pages -%}
  {%- unless item.redirect_to -%}
    {% assign c_total = c_total | plus: 1 %}
  {%- endunless -%}
{%- endfor -%}

<div class="wiki-pagehead">
  <p class="wiki-back"><a href="{{ '/' | relative_url }}">&larr; Home</a></p>
  <h1 class="wiki-pagehead-title">Wiki Catalog <span class="wiki-pagehead-count">{{ c_total }} topics</span></h1>
</div>

{% if c_total > 0 %}
<div class="wiki-controls" role="search">
  <div class="wiki-controls-row">
    <div class="wiki-search">
      <svg class="wiki-search-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
        <circle cx="11" cy="11" r="7"></circle>
        <line x1="21" y1="21" x2="16.65" y2="16.65"></line>
      </svg>
      <input id="wiki-filter" type="search" autocomplete="off" placeholder="Filter {{ c_total }} topics by name or keyword…" aria-label="Filter topics">
      <button class="wiki-search-clear" type="button" aria-label="Clear filter" hidden>&times;</button>
    </div>
  </div>
</div>

<p class="wiki-count">Showing <b id="wiki-count">{{ c_total }}</b> of {{ c_total }} topics</p>

<div class="wiki-sections">
{% assign current_letter = "__none__" %}
{%- for item in pages -%}
  {%- unless item.redirect_to -%}
    {%- assign L = item.title | slice: 0 | upcase -%}
    {%- if L != current_letter -%}
      {%- unless current_letter == "__none__" -%}
    </div>
  </section>
      {%- endunless -%}
  <section class="wiki-section" data-letter="{{ L }}">
    <h2 class="wiki-letter" id="letter-{{ L }}"><span class="wiki-letter-badge">{{ L }}</span></h2>
    <div class="wiki-grid">
      {%- assign current_letter = L -%}
    {%- endif -%}
      <a class="wiki-card" href="{{ item.url | relative_url }}" data-letter="{{ L }}" data-tags="{{ item.tags | join: ' ' }}" data-search="{{ item.title | append: ' ' | append: item.summary | downcase | escape }}">
        <span class="wiki-card-title">{{ item.title }}</span>
        {% if item.summary %}<span class="wiki-card-summary">{{ item.summary }}</span>{% endif %}
        {%- if item.tags and item.tags.size > 0 -%}
        <span class="wiki-card-tags">{% for t in item.tags %}<span class="wiki-badge">{{ t }}</span>{% endfor %}</span>
        {%- endif -%}
      </a>
  {%- endunless -%}
{%- endfor -%}
    </div>
  </section>
</div>

<p class="wiki-empty" hidden>No topics match your filter. Try a different keyword.</p>

<script>
(function () {
  var input = document.getElementById('wiki-filter');
  var clear = document.querySelector('.wiki-search-clear');
  var cards = Array.prototype.slice.call(document.querySelectorAll('.wiki-card'));
  var sections = Array.prototype.slice.call(document.querySelectorAll('.wiki-section'));
  var countEl = document.getElementById('wiki-count');
  var emptyEl = document.querySelector('.wiki-empty');
  if (!cards.length) return;

  var query = '';

  function apply() {
    var q = query.trim().toLowerCase();
    var visible = 0;
    var lettersShown = {};
    for (var i = 0; i < cards.length; i++) {
      var c = cards[i];
      var matchQuery = !q || (c.getAttribute('data-search') || '').indexOf(q) !== -1;
      var show = matchQuery;
      c.hidden = !show;
      if (show) { visible++; lettersShown[c.getAttribute('data-letter')] = true; }
    }
    for (var s = 0; s < sections.length; s++) {
      sections[s].hidden = !lettersShown[sections[s].getAttribute('data-letter')];
    }
    countEl.textContent = visible;
    emptyEl.hidden = visible !== 0;
    if (clear) clear.hidden = q === '';
  }

  if (input) {
    input.addEventListener('input', function () { query = input.value; apply(); });
  }
  if (clear) {
    clear.addEventListener('click', function () {
      query = ''; if (input) { input.value = ''; input.focus(); } apply();
    });
  }

  apply();
})();
</script>
{% else %}
<p class="muted">Wiki pages are being drafted from the archive analysis.</p>
{% endif %}
