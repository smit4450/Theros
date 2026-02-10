document.addEventListener("nav", () => {
  const table = document.getElementById("spell-data-table") as HTMLTableElement | null
  if (!table) return

  const tbody = table.querySelector("tbody")
  if (!tbody) return

  const rows = Array.from(tbody.querySelectorAll("tr"))
  const searchInput = document.getElementById("spell-search") as HTMLInputElement | null
  const levelFilter = document.getElementById("spell-level-filter") as HTMLSelectElement | null
  const schoolFilter = document.getElementById("spell-school-filter") as HTMLSelectElement | null
  const classFilter = document.getElementById("spell-class-filter") as HTMLSelectElement | null
  const resetBtn = document.getElementById("spell-reset-btn") as HTMLButtonElement | null
  const countEl = document.getElementById("spell-count")
  const headers = table.querySelectorAll("th")

  if (!searchInput || !levelFilter || !schoolFilter || !classFilter || !resetBtn || !countEl) return

  let sortCol: number | null = null
  let sortDir = 1

  function updateCount() {
    const visible = rows.filter((r) => r.style.display !== "none").length
    countEl!.textContent = visible + " of " + rows.length + " spells"
  }

  function filterRows() {
    const search = searchInput!.value.toLowerCase()
    const level = levelFilter!.value
    const school = schoolFilter!.value
    const cls = classFilter!.value.toLowerCase()

    rows.forEach((row) => {
      const name = row.getAttribute("data-name") || ""
      const rLevel = row.getAttribute("data-level") || ""
      const rSchool = row.getAttribute("data-school") || ""
      const rClasses = row.getAttribute("data-classes") || ""

      const matchName = !search || name.includes(search)
      const matchLevel = !level || rLevel === level
      const matchSchool = !school || rSchool === school
      const matchClass = !cls || rClasses.includes(cls)

      row.style.display = matchName && matchLevel && matchSchool && matchClass ? "" : "none"
    })
    updateCount()
  }

  function sortTable(colIndex: number) {
    const getCellValue = (row: HTMLTableRowElement, idx: number) => {
      const cell = row.children[idx] as HTMLTableCellElement
      return cell.getAttribute("data-sort") || cell.textContent!.trim().toLowerCase()
    }

    rows.sort((a, b) => {
      const aVal = getCellValue(a, colIndex)
      const bVal = getCellValue(b, colIndex)
      const aNum = parseFloat(aVal)
      const bNum = parseFloat(bVal)
      if (!isNaN(aNum) && !isNaN(bNum)) {
        return (aNum - bNum) * sortDir
      }
      return aVal.localeCompare(bVal) * sortDir
    })

    rows.forEach((row) => tbody!.appendChild(row))
    updateCount()

    headers.forEach((h, i) => {
      const indicator = h.querySelector(".sort-indicator")
      if (indicator) {
        if (i === colIndex) {
          indicator.classList.add("active")
          indicator.textContent = sortDir === 1 ? "↑" : "↓"
        } else {
          indicator.classList.remove("active")
          indicator.textContent = "⇅"
        }
      }
    })
  }

  function onHeaderClick(this: HTMLTableCellElement) {
    const index = Array.from(headers).indexOf(this)
    if (sortCol === index) {
      sortDir *= -1
    } else {
      sortCol = index
      sortDir = 1
    }
    sortTable(index)
  }

  function onReset() {
    searchInput!.value = ""
    levelFilter!.value = ""
    schoolFilter!.value = ""
    classFilter!.value = ""
    filterRows()
  }

  headers.forEach((header) => {
    header.addEventListener("click", onHeaderClick)
  })

  searchInput.addEventListener("input", filterRows)
  levelFilter.addEventListener("change", filterRows)
  schoolFilter.addEventListener("change", filterRows)
  classFilter.addEventListener("change", filterRows)
  resetBtn.addEventListener("click", onReset)

  // Cleanup on SPA navigation
  window.addCleanup(() => {
    headers.forEach((header) => {
      header.removeEventListener("click", onHeaderClick)
    })
    searchInput!.removeEventListener("input", filterRows)
    levelFilter!.removeEventListener("change", filterRows)
    schoolFilter!.removeEventListener("change", filterRows)
    classFilter!.removeEventListener("change", filterRows)
    resetBtn!.removeEventListener("click", onReset)
  })

  updateCount()
})
