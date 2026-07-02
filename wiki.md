---
layout: default
title: Wiki Catalog
permalink: /wiki/
---

{% assign pages = site.wiki | sort_natural: "title" %}

{%- comment -%} Count tagged topics for the filter pills {%- endcomment -%}
{% assign c_total = 0 %}
{% assign c_guide = 0 %}{% assign c_comparison = 0 %}{% assign c_roadmap = 0 %}{% assign c_howto = 0 %}{% assign c_transition = 0 %}
{%- for item in pages -%}
  {%- unless item.redirect_to -%}
    {% assign c_total = c_total | plus: 1 %}
    {%- if item.tags -%}
      {%- for t in item.tags -%}
        {%- if t == "guide" -%}{% assign c_guide = c_guide | plus: 1 %}{%- endif -%}
        {%- if t == "comparison" -%}{% assign c_comparison = c_comparison | plus: 1 %}{%- endif -%}
        {%- if t == "roadmap" -%}{% assign c_roadmap = c_roadmap | plus: 1 %}{%- endif -%}
        {%- if t == "how-to" -%}{% assign c_howto = c_howto | plus: 1 %}{%- endif -%}
        {%- if t == "transition" -%}{% assign c_transition = c_transition | plus: 1 %}{%- endif -%}
      {%- endfor -%}
    {%- endif -%}
  {%- endunless -%}
{%- endfor -%}

<div class="wiki-hero">
  <p class="wiki-back"><a href="{{ '/' | relative_url }}">&larr; Home</a></p>
  <h1>Wiki Catalog</h1>
  <p class="wiki-lede">Browse all {{ c_total }} topics — search, filter by type, or jump to a letter.</p>
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
    <div class="wiki-tags" role="group" aria-label="Filter by type">
      <button class="wiki-tag is-active" type="button" data-tag="all" aria-pressed="true">All</button>
      {% if c_guide > 0 %}<button class="wiki-tag" type="button" data-tag="guide" aria-pressed="false">Guides<span class="wiki-tag-count">{{ c_guide }}</span></button>{% endif %}
      {% if c_comparison > 0 %}<button class="wiki-tag" type="button" data-tag="comparison" aria-pressed="false">Comparisons<span class="wiki-tag-count">{{ c_comparison }}</span></button>{% endif %}
      {% if c_roadmap > 0 %}<button class="wiki-tag" type="button" data-tag="roadmap" aria-pressed="false">Roadmaps<span class="wiki-tag-count">{{ c_roadmap }}</span></button>{% endif %}
      {% if c_transition > 0 %}<button class="wiki-tag" type="button" data-tag="transition" aria-pressed="false">Transitions<span class="wiki-tag-count">{{ c_transition }}</span></button>{% endif %}
      {% if c_howto > 0 %}<button class="wiki-tag" type="button" data-tag="how-to" aria-pressed="false">How-to<span class="wiki-tag-count">{{ c_howto }}</span></button>{% endif %}
    </div>
  </div>
  <nav class="wiki-az" aria-label="Jump to letter">
    {% assign alphabet = "A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z" | split: "," %}
    {% for L in alphabet %}<a href="#letter-{{ L }}" data-letter="{{ L }}">{{ L }}</a>{% endfor %}
  </nav>
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

<p class="wiki-empty" hidden>No topics match your filter. Try a different keyword or reset the type filter.</p>

<script>
(function () {
  var input = document.getElementById('wiki-filter');
  var clear = document.querySelector('.wiki-search-clear');
  var tagBtns = Array.prototype.slice.call(document.querySelectorAll('.wiki-tag'));
  var cards = Array.prototype.slice.call(document.querySelectorAll('.wiki-card'));
  var sections = Array.prototype.slice.call(document.querySelectorAll('.wiki-section'));
  var azLinks = Array.prototype.slice.call(document.querySelectorAll('.wiki-az a'));
  var countEl = document.getElementById('wiki-count');
  var emptyEl = document.querySelector('.wiki-empty');
  if (!cards.length) return;

  var activeTag = 'all';
  var query = '';

  function apply() {
    var q = query.trim().toLowerCase();
    var visible = 0;
    var lettersShown = {};
    for (var i = 0; i < cards.length; i++) {
      var c = cards[i];
      var tags = (c.getAttribute('data-tags') || '').split(' ');
      var matchTag = activeTag === 'all' || tags.indexOf(activeTag) !== -1;
      var matchQuery = !q || (c.getAttribute('data-search') || '').indexOf(q) !== -1;
      var show = matchTag && matchQuery;
      c.hidden = !show;
      if (show) { visible++; lettersShown[c.getAttribute('data-letter')] = true; }
    }
    for (var s = 0; s < sections.length; s++) {
      sections[s].hidden = !lettersShown[sections[s].getAttribute('data-letter')];
    }
    for (var a = 0; a < azLinks.length; a++) {
      var has = !!lettersShown[azLinks[a].getAttribute('data-letter')];
      azLinks[a].classList.toggle('is-disabled', !has);
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
  tagBtns.forEach(function (b) {
    b.addEventListener('click', function () {
      activeTag = b.getAttribute('data-tag');
      tagBtns.forEach(function (x) {
        var on = x === b;
        x.classList.toggle('is-active', on);
        x.setAttribute('aria-pressed', on ? 'true' : 'false');
      });
      apply();
    });
  });
  azLinks.forEach(function (link) {
    link.addEventListener('click', function (e) {
      e.preventDefault();
      if (link.classList.contains('is-disabled')) return;
      var target = document.getElementById('letter-' + link.getAttribute('data-letter'));
      if (target) target.scrollIntoView({ behavior: 'smooth', block: 'start' });
    });
  });

  apply();
})();
</script>
{% else %}
<p class="muted">Wiki pages are being drafted from the archive analysis.</p>
{% endif %}
