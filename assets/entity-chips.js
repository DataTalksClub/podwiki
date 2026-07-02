(function () {
  // Entity-chip extension for wiki pages.
  // Inside article prose, turn links that point at a known entity into a compact,
  // typed chip (colour + icon per type, matching the graph legend). Podcast chips
  // also carry a timestamp badge when the reference includes one.
  var scopes = document.querySelectorAll(".knowledge-page");
  if (!scopes.length) return;

  var TYPES = [
    { type: "podcast", test: /\/podcasts?\//, icon: "🎙" },
    { type: "person", test: /\/(people|guests)\//, icon: "‹›" },
    { type: "book", test: /\/books?\//, icon: "▮" },
    { type: "wiki", test: /\/wiki\//, icon: "◆" },
  ];
  var reTitleTime = /^(.*\S)\s+at\s+(\d{1,2}:\d{2}(?::\d{2})?)$/;
  var reTime = /^(\d{1,2}:\d{2}(?::\d{2})?)$/;

  function classify(href) {
    for (var i = 0; i < TYPES.length; i += 1) {
      if (TYPES[i].test.test(href)) return TYPES[i];
    }
    return null;
  }

  function build(link, def, label, time) {
    link.classList.add("chip", "chip--" + def.type);
    link.setAttribute("data-chip", def.type);
    link.setAttribute("title", link.textContent.trim());
    link.textContent = "";
    var icon = document.createElement("span");
    icon.className = "chip-ic";
    icon.setAttribute("aria-hidden", "true");
    icon.textContent = def.icon;
    link.appendChild(icon);
    if (label) {
      var l = document.createElement("span");
      l.className = "chip-label";
      l.textContent = label;
      link.appendChild(l);
    }
    if (time) {
      var t = document.createElement("span");
      t.className = "chip-time";
      t.textContent = time;
      link.appendChild(t);
    }
  }

  scopes.forEach(function (scope) {
    var links = scope.querySelectorAll("p a, li a, td a");
    Array.prototype.forEach.call(links, function (link) {
      if (link.classList.contains("chip")) return;
      var href = link.getAttribute("href") || "";
      var def = classify(href);
      if (!def) return;
      var text = link.textContent.trim();
      if (!text) return;

      if (def.type === "podcast") {
        var m = text.match(reTitleTime);
        if (m) return build(link, def, m[1], m[2]);
        var mt = text.match(reTime);
        if (mt) return build(link, def, null, mt[1]);
        return build(link, def, text, null);
      }
      build(link, def, text, null);
    });
  });
})();
