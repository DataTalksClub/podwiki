(function () {
  var input = document.getElementById("wiki-filter")
  var clear = document.querySelector(".wiki-search-clear")
  var cards = Array.prototype.slice.call(document.querySelectorAll(".wiki-card"))
  var sections = Array.prototype.slice.call(document.querySelectorAll(".wiki-section"))
  var countEl = document.getElementById("wiki-count")
  var emptyEl = document.querySelector(".wiki-empty")
  var query = ""

  if (!cards.length) return

  function apply() {
    var q = query.trim().toLowerCase()
    var visible = 0
    var lettersShown = {}

    for (var i = 0; i < cards.length; i++) {
      var card = cards[i]
      var searchText = card.getAttribute("data-search") || ""
      var show = !q || searchText.indexOf(q) !== -1
      card.hidden = !show
      if (show) {
        visible += 1
        lettersShown[card.getAttribute("data-letter")] = true
      }
    }

    for (var s = 0; s < sections.length; s++) {
      var section = sections[s]
      section.hidden = !lettersShown[section.getAttribute("data-letter")]
    }

    countEl.textContent = visible
    emptyEl.hidden = visible !== 0
    if (clear) clear.hidden = q === ""
  }

  if (input) {
    input.addEventListener("input", function () {
      query = input.value
      apply()
    })
  }

  if (clear) {
    clear.addEventListener("click", function () {
      query = ""
      if (input) {
        input.value = ""
        input.focus()
      }
      apply()
    })
  }

  apply()
})()
