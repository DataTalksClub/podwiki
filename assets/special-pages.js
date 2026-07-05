(function () {
  var buttons = document.querySelectorAll(".tag-btn")
  var cards = document.querySelectorAll(".special-card")
  var count = document.getElementById("filter-count")

  function tagList(card) {
    var tags = card.getAttribute("data-tags") || ""
    return tags.split(",").map(function (tag) {
      return tag.trim()
    })
  }

  function countText(shown) {
    if (shown === 1) return "1 page"
    return shown + " pages"
  }

  function apply(tag) {
    var shown = 0

    buttons.forEach(function (btn) {
      var active = btn.getAttribute("data-tag") === tag
      btn.classList.toggle("active", active)
      btn.setAttribute("aria-pressed", active ? "true" : "false")
    })

    cards.forEach(function (card) {
      var match = tag === "all" || tagList(card).indexOf(tag) !== -1
      card.style.display = match ? "" : "none"
      if (match) shown += 1
    })

    if (count) count.textContent = countText(shown)
  }

  buttons.forEach(function (btn) {
    btn.addEventListener("click", function () {
      var tag = btn.getAttribute("data-tag")
      var targetPath = tag === "all" ? window.location.pathname : "#" + tag

      if (window.history && window.history.replaceState) {
        window.history.replaceState(null, "", targetPath)
      }

      apply(tag)
    })
  })

  var initial = window.location.hash ? window.location.hash.slice(1) : "all"
  var valid = Array.prototype.some.call(buttons, function (btn) {
    return btn.getAttribute("data-tag") === initial
  })

  apply(valid ? initial : "all")
})()
