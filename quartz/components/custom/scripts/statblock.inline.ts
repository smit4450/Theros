/**
 * Fantasy Statblocks — Client-side Renderer for Quartz
 *
 * Finds all elements with class "fantasy-statblock-container" and
 * data-statblock-yaml attributes, parses the YAML, and renders
 * a styled D&D 5e–style stat block in place.
 *
 * This file is imported as raw text by the Quartz transformer plugin
 * and injected as an inline script that runs after DOM ready.
 */

// ---------------------------------------------------------------------------
// Minimal YAML parser (handles the subset used by fantasy-statblocks)
// ---------------------------------------------------------------------------

function parseStatblockYaml(src: string): Record<string, any> {
  const result: Record<string, any> = {}
  const lines = src.split("\n")
  let i = 0

  function getIndent(line: string): number {
    const match = line.match(/^(\s*)/)
    return match ? match[1].length : 0
  }

  function parsePrimitive(val: string): any {
    // Handle !!int tag
    val = val.replace(/^!!int\s+/, "")
    // Remove surrounding quotes and unescape
    if (val.startsWith('"') && val.endsWith('"')) {
      val = val.slice(1, -1)
      // Unescape common YAML/JSON escape sequences in double-quoted strings
      val = val.replace(/\\n/g, "\n")
      val = val.replace(/\\t/g, "\t")
      val = val.replace(/\\\\/g, "\\")
      val = val.replace(/\\"/g, '"')
      return val
    }
    if (val.startsWith("'") && val.endsWith("'")) {
      return val.slice(1, -1)
    }
    if (val === "true") return true
    if (val === "false") return false
    if (val === "null" || val === "~" || val === "") return null
    const num = Number(val)
    if (!isNaN(num) && val.trim() !== "") return num
    return val
  }

  function parseFlowSequence(text: string): any[] {
    // Remove brackets
    text = text.trim()
    if (text.startsWith("[")) text = text.slice(1)
    if (text.endsWith("]")) text = text.slice(0, -1)
    // Handle !!int tags inside flow sequences
    return text.split(",").map((item) => {
      let s = item.trim()
      s = s.replace(/^!!int\s+/, "")
      if (
        (s.startsWith('"') && s.endsWith('"')) ||
        (s.startsWith("'") && s.endsWith("'"))
      ) {
        return s.slice(1, -1)
      }
      const n = Number(s)
      if (!isNaN(n) && s !== "") return n
      return s
    })
  }

  function parseFlowMapping(text: string): Record<string, any> {
    text = text.trim()
    if (text.startsWith("{")) text = text.slice(1)
    if (text.endsWith("}")) text = text.slice(0, -1)
    const obj: Record<string, any> = {}
    const parts = text.split(",")
    for (const part of parts) {
      const colonIdx = part.indexOf(":")
      if (colonIdx === -1) continue
      const k = part.slice(0, colonIdx).trim().replace(/^["']|["']$/g, "")
      const v = part.slice(colonIdx + 1).trim()
      obj[k] = parsePrimitive(v)
    }
    return obj
  }

  function parseBlock(baseIndent: number): Record<string, any> {
    const obj: Record<string, any> = {}

    while (i < lines.length) {
      const line = lines[i]
      if (line.trim() === "" || line.trim().startsWith("#")) {
        i++
        continue
      }

      const currentIndent = getIndent(line)
      if (currentIndent < baseIndent) break

      const trimmed = line.trim()

      // Array item
      if (trimmed.startsWith("- ")) {
        break // arrays are handled in the caller
      }

      // Key: value pair
      const colonMatch = trimmed.match(/^("(?:[^"\\]|\\.)*"|'(?:[^'\\]|\\.)*'|[^:]+?):\s*(.*)$/)
      if (colonMatch) {
        let key = colonMatch[1].replace(/^["']|["']$/g, "").trim()
        let value = colonMatch[2].trim()

        // Handle multiline string continuations
        if (value === ">-" || value === ">" || value === "|" || value === "|-") {
          const isLiteral = value.startsWith("|")
          i++
          const parts: string[] = []
          while (i < lines.length) {
            const nextLine = lines[i]
            if (nextLine.trim() === "") {
              if (parts.length > 0) parts.push("")
              i++
              continue
            }
            const nextIndent = getIndent(nextLine)
            if (nextIndent <= currentIndent) break
            parts.push(nextLine.trim())
            i++
          }
          obj[key] = isLiteral ? parts.join("\n") : parts.join(" ")
          continue
        }

        // Handle folded multiline with backslash continuation
        if (value.endsWith("\\")) {
          const parts: string[] = [value.slice(0, -1).trim()]
          i++
          while (i < lines.length) {
            let nextLine = lines[i].trim()
            if (nextLine === "") break
            const nextIndent = getIndent(lines[i])
            if (nextIndent <= currentIndent) break
            // Strip leading \ (backslash-space) continuation artifact
            if (nextLine.startsWith("\\ ")) nextLine = nextLine.slice(1)
            if (nextLine.endsWith("\\")) {
              parts.push(nextLine.slice(0, -1).trim())
              i++
            } else {
              parts.push(nextLine)
              i++
              break
            }
          }
          obj[key] = parsePrimitive(parts.join(" "))
          continue
        }

        i++

        if (value === "") {
          // Check if next lines are indented (nested block or array)
          if (i < lines.length) {
            const nextLine = lines[i]
            if (nextLine.trim() === "") {
              // Skip blank
              let peekI = i
              while (peekI < lines.length && lines[peekI].trim() === "") peekI++
              if (peekI < lines.length && getIndent(lines[peekI]) > currentIndent) {
                i = peekI
                const nextTrimmed = lines[i].trim()
                if (nextTrimmed.startsWith("- ")) {
                  obj[key] = parseArray(getIndent(lines[i]))
                } else {
                  obj[key] = parseBlock(getIndent(lines[i]))
                }
              } else {
                obj[key] = null
              }
            } else {
              const nextIndent = getIndent(nextLine)
              const nextTrimmed = nextLine.trim()
              if (nextIndent > currentIndent) {
                if (nextTrimmed.startsWith("- ")) {
                  obj[key] = parseArray(nextIndent)
                } else {
                  obj[key] = parseBlock(nextIndent)
                }
              } else {
                obj[key] = null
              }
            }
          } else {
            obj[key] = null
          }
        } else {
          // Inline value
          if (value.startsWith("[")) {
            obj[key] = parseFlowSequence(value)
          } else if (value.startsWith("{")) {
            obj[key] = parseFlowMapping(value)
          } else {
            obj[key] = parsePrimitive(value)
          }
        }
        continue
      }

      i++
    }

    return obj
  }

  function parseArray(baseIndent: number): any[] {
    const arr: any[] = []

    while (i < lines.length) {
      const line = lines[i]
      if (line.trim() === "" || line.trim().startsWith("#")) {
        i++
        continue
      }

      const currentIndent = getIndent(line)
      if (currentIndent < baseIndent) break

      const trimmed = line.trim()

      if (trimmed.startsWith("- ")) {
        const itemValue = trimmed.slice(2).trim()

        // Check if it's a "- key: value" mapping start
        const kvMatch = itemValue.match(
          /^("(?:[^"\\]|\\.)*"|'(?:[^'\\]|\\.)*'|[^:]+?):\s*(.*)$/,
        )
        if (kvMatch) {
          // Start of a mapping item
          const key = kvMatch[1].replace(/^["']|["']$/g, "").trim()
          let val = kvMatch[2].trim()

          const mapItem: Record<string, any> = {}

          if (val === "") {
            i++
            // Nested block under this key
            if (i < lines.length && getIndent(lines[i]) > currentIndent) {
              const nestedTrimmed = lines[i].trim()
              if (nestedTrimmed.startsWith("- ")) {
                mapItem[key] = parseArray(getIndent(lines[i]))
              } else {
                mapItem[key] = parseBlock(getIndent(lines[i]))
              }
            } else {
              mapItem[key] = null
            }
          } else {
            // Handle multiline continuations for array item values
            if (val.endsWith("\\")) {
              const parts: string[] = [val.slice(0, -1).trim()]
              i++
              while (i < lines.length) {
                let nextLine = lines[i].trim()
                if (nextLine === "") break
                const nextIndent = getIndent(lines[i])
                if (nextIndent <= currentIndent + 2) break
                // Strip leading \ (backslash-space) continuation artifact
                if (nextLine.startsWith("\\ ")) nextLine = nextLine.slice(1)
                if (nextLine.endsWith("\\")) {
                  parts.push(nextLine.slice(0, -1).trim())
                  i++
                } else {
                  parts.push(nextLine)
                  i++
                  break
                }
              }
              mapItem[key] = parsePrimitive(parts.join(" "))
            } else if (val.startsWith("[")) {
              mapItem[key] = parseFlowSequence(val)
              i++
            } else if (val.startsWith("{")) {
              mapItem[key] = parseFlowMapping(val)
              i++
            } else {
              mapItem[key] = parsePrimitive(val)
              i++
            }
          }

          // Continue reading more keys at the child indent level
          const childIndent = currentIndent + 2
          while (i < lines.length) {
            const nextLine = lines[i]
            if (nextLine.trim() === "" || nextLine.trim().startsWith("#")) {
              i++
              continue
            }
            const nextIndent = getIndent(nextLine)
            if (nextIndent < childIndent) break
            if (nextIndent === childIndent || nextIndent > childIndent) {
              const nextTrimmed = nextLine.trim()
              if (nextTrimmed.startsWith("- ")) break // new array at same level
              const nextKv = nextTrimmed.match(
                /^("(?:[^"\\]|\\.)*"|'(?:[^'\\]|\\.)*'|[^:]+?):\s*(.*)$/,
              )
              if (nextKv) {
                const nk = nextKv[1].replace(/^["']|["']$/g, "").trim()
                let nv = nextKv[2].trim()
                i++

                if (nv === "") {
                  if (i < lines.length && getIndent(lines[i]) > nextIndent) {
                    const nt = lines[i].trim()
                    if (nt.startsWith("- ")) {
                      mapItem[nk] = parseArray(getIndent(lines[i]))
                    } else {
                      mapItem[nk] = parseBlock(getIndent(lines[i]))
                    }
                  } else {
                    mapItem[nk] = null
                  }
                } else if (nv.endsWith("\\")) {
                  const parts: string[] = [nv.slice(0, -1).trim()]
                  while (i < lines.length) {
                    let nl = lines[i].trim()
                    if (nl === "") break
                    const ni = getIndent(lines[i])
                    if (ni <= nextIndent) break
                    // Strip leading \ (backslash-space) continuation artifact
                    if (nl.startsWith("\\ ")) nl = nl.slice(1)
                    if (nl.endsWith("\\")) {
                      parts.push(nl.slice(0, -1).trim())
                      i++
                    } else {
                      parts.push(nl)
                      i++
                      break
                    }
                  }
                  mapItem[nk] = parsePrimitive(parts.join(" "))
                } else if (nv.startsWith("[")) {
                  mapItem[nk] = parseFlowSequence(nv)
                } else if (nv.startsWith("{")) {
                  mapItem[nk] = parseFlowMapping(nv)
                } else {
                  mapItem[nk] = parsePrimitive(nv)
                }
              } else {
                break
              }
            } else {
              break
            }
          }

          arr.push(mapItem)
        } else {
          // Simple scalar array item
          if (itemValue.startsWith("[")) {
            arr.push(parseFlowSequence(itemValue))
          } else if (itemValue.startsWith("{")) {
            arr.push(parseFlowMapping(itemValue))
          } else {
            arr.push(parsePrimitive(itemValue))
          }
          i++
        }
      } else {
        break
      }
    }

    return arr
  }

  // Start parsing at the top level
  while (i < lines.length) {
    if (lines[i].trim() === "" || lines[i].trim().startsWith("#")) {
      i++
      continue
    }
    const indent = getIndent(lines[i])
    const trimmed = lines[i].trim()
    if (trimmed.startsWith("- ")) {
      // top-level array
      return parseArray(indent) as any
    }
    Object.assign(result, parseBlock(indent))
  }

  return result
}

// ---------------------------------------------------------------------------
// CR → XP lookup table
// ---------------------------------------------------------------------------

const CR_XP: Record<string, number> = {
  "0": 10,
  "1/8": 25,
  "0.125": 25,
  "1/4": 50,
  "0.25": 50,
  "1/2": 100,
  "0.5": 100,
  "1": 200,
  "2": 450,
  "3": 700,
  "4": 1100,
  "5": 1800,
  "6": 2300,
  "7": 2900,
  "8": 3900,
  "9": 5000,
  "10": 5900,
  "11": 7200,
  "12": 8400,
  "13": 10000,
  "14": 11500,
  "15": 13000,
  "16": 15000,
  "17": 18000,
  "18": 20000,
  "19": 22000,
  "20": 25000,
  "21": 33000,
  "22": 41000,
  "23": 50000,
  "24": 62000,
  "25": 75000,
  "26": 90000,
  "27": 105000,
  "28": 120000,
  "29": 135000,
  "30": 155000,
}

// ---------------------------------------------------------------------------
// CR → Proficiency Bonus
// ---------------------------------------------------------------------------

function proficiencyBonus(cr: string | number): string {
  const val = typeof cr === "string" ? parseFloat(cr) || 0 : cr
  if (val <= 4) return "+2"
  if (val <= 8) return "+3"
  if (val <= 12) return "+4"
  if (val <= 16) return "+5"
  if (val <= 20) return "+6"
  if (val <= 24) return "+7"
  if (val <= 28) return "+8"
  return "+9"
}

// ---------------------------------------------------------------------------
// Utility helpers
// ---------------------------------------------------------------------------

function abilityModifier(score: number): string {
  const mod = Math.floor((score - 10) / 2)
  return mod >= 0 ? `+${mod}` : `${mod}`
}

function escapeHtml(text: string): string {
  const div = document.createElement("div")
  div.textContent = text
  return div.innerHTML
}

function formatNumber(n: number): string {
  return n.toLocaleString("en-US")
}

/** Get the site base path from the document for resolving relative URLs */
function getBasePath(): string {
  // Try to extract from <base> tag
  const base = document.querySelector("base")
  if (base?.href) {
    const url = new URL(base.href)
    return url.pathname.replace(/\/$/, "")
  }
  // Fallback: check CSS links to infer the base path
  try {
    const cssLink = document.querySelector('link[rel="stylesheet"]') as HTMLLinkElement
    if (cssLink?.href) {
      const cssUrl = new URL(cssLink.href)
      const cssParts = cssUrl.pathname.split("/").filter(Boolean)
      if (cssParts.length > 1) {
        return "/" + cssParts.slice(0, -1).join("/")
      }
    }
  } catch { /* ignore */ }
  return ""
}

/** Resolve a content-relative path to a site URL */
function resolveContentPath(path: string): string {
  if (!path) return path
  // Already absolute
  if (path.startsWith("/") || path.startsWith("http://") || path.startsWith("https://")) {
    return path
  }
  const base = getBasePath()
  return `${base}/${path}`
}

/** Convert a markdown .md link to an HTML-friendly URL */
function resolveLink(href: string): string {
  let resolved = href
  // Remove .md extension but preserve anchors
  resolved = resolved.replace(/\.md(#|$)/, "$1")
  return resolveContentPath(resolved)
}

/** Convert Obsidian wiki-links and markdown-links in text to plain HTML anchors */
function linkifyText(text: string): string {
  if (!text) return ""
  // Clean up YAML folded-string backslash artifacts (e.g. " \ " → " ")
  let result = text.replace(/ \\ /g, " ")
  // Also handle trailing " \" at line boundaries that survived joining
  result = result.replace(/\\\s*$/gm, "")
  // Convert wiki-links: [[target|display]] or [[target]]
  result = result.replace(
    /\[\[([^\]|]+?)(?:\|([^\]]+?))?\]\]/g,
    (_m, target, display) => {
      const label = display || target
      // Convert spaces to hyphens and resolve to absolute path
      const href = target.replace(/ /g, "-")
      return `<a href="${escapeHtml(resolveContentPath(href))}">${escapeHtml(label)}</a>`
    },
  )
  // Convert markdown links: [display](url)
  result = result.replace(
    /\[([^\]]+?)\]\(([^)]+?)\)/g,
    (_m, display, href) => {
      return `<a href="${escapeHtml(resolveLink(href))}">${escapeHtml(display)}</a>`
    },
  )
  return result
}

/** Render text: linkify, then convert markdown bold/italic to HTML */
function renderText(text: string | number | null | undefined): string {
  if (text === null || text === undefined) return ""
  let s = String(text)
  // Linkify wiki-links and markdown links
  s = linkifyText(s)
  // Convert markdown bold+italic: ***text*** or ___text___
  s = s.replace(/\*\*\*(.+?)\*\*\*/g, "<b><i>$1</i></b>")
  s = s.replace(/___(.+?)___/g, "<b><i>$1</i></b>")
  // Convert markdown bold: **text** or __text__
  s = s.replace(/\*\*(.+?)\*\*/g, "<b>$1</b>")
  s = s.replace(/__(.+?)__/g, "<b>$1</b>")
  // Convert markdown italic: *text* or _text_
  s = s.replace(/\*(.+?)\*/g, "<i>$1</i>")
  s = s.replace(/(?<![a-zA-Z0-9])_(.+?)_(?![a-zA-Z0-9])/g, "<i>$1</i>")
  // Convert literal newlines to <br> for paragraph breaks
  s = s.replace(/\n\n/g, "<br><br>")
  s = s.replace(/\n/g, "<br>")
  return s
}

// ---------------------------------------------------------------------------
// Renderer — builds the statblock HTML from parsed YAML data
// ---------------------------------------------------------------------------

interface Trait {
  name?: string
  desc?: string
  [key: string]: any
}

function renderStatblock(data: Record<string, any>): string {
  const parts: string[] = []

  // Resolve stats array — can be top-level array or nested
  let stats: number[] | null = null
  if (Array.isArray(data.stats)) {
    stats = data.stats
  }

  parts.push('<div class="statblock">')

  // === Top Bar ===
  parts.push('<div class="bar"></div>')

  // === Content ===
  parts.push('<div class="statblock-content">')
  parts.push('<div class="column">')

  // --- Heading (name) ---
  if (data.name) {
    parts.push('<div class="statblock-item-container heading-container">')
    parts.push(`<h1 class="heading">${renderText(data.name)}</h1>`)
    parts.push("</div>")
  }

  // --- Subheading (size, type, subtype, alignment) ---
  const subParts: string[] = []
  if (data.size) subParts.push(String(data.size))
  if (data.type) {
    let typeStr = String(data.type)
    if (data.subtype) typeStr += ` (${data.subtype})`
    subParts.push(typeStr)
  }
  if (data.alignment) subParts.push(String(data.alignment))
  if (subParts.length > 0) {
    parts.push('<div class="statblock-item-container subheading-container">')
    parts.push(`<div class="subheading">${escapeHtml(subParts.join(", "))}</div>`)
    parts.push("</div>")
  }

  // --- Image (if in the heading area) ---
  if (data.image) {
    const imgSrc = resolveContentPath(String(data.image))
    parts.push('<div class="statblock-item-container image-container">')
    parts.push(`<div class="statblock-image"><img src="${escapeHtml(imgSrc)}" alt="${escapeHtml(data.name || "")}" onerror="this.parentElement.parentElement.style.display='none'" /></div>`)
    parts.push("</div>")
  }

  // === Tapered Rule ===
  parts.push('<div class="tapered-rule"></div>')

  // --- AC, HP, Speed ---
  parts.push('<div class="statblock-item-container property-container">')
  if (data.ac !== undefined && data.ac !== null) {
    const acText = String(data.ac)
    parts.push(`<div class="property-line"><span class="property-name">Armor Class</span> <span class="property-text">${renderText(acText)}</span></div>`)
  }
  if (data.hp !== undefined && data.hp !== null) {
    let hpText = String(data.hp)
    if (data.hit_dice) hpText += ` (${data.hit_dice})`
    parts.push(`<div class="property-line"><span class="property-name">Hit Points</span> <span class="property-text">${renderText(hpText)}</span></div>`)
  }
  if (data.speed) {
    parts.push(`<div class="property-line"><span class="property-name">Speed</span> <span class="property-text">${renderText(data.speed)}</span></div>`)
  }
  parts.push("</div>")

  // === Tapered Rule ===
  parts.push('<div class="tapered-rule"></div>')

  // --- Ability Scores Table ---
  if (stats && stats.length >= 6) {
    const headers = ["Str", "Dex", "Con", "Int", "Wis", "Cha"]
    parts.push('<div class="statblock-item-container table-container">')
    parts.push('<div class="ability-table">')
    for (let idx = 0; idx < 6; idx++) {
      const score = stats[idx]
      const mod = abilityModifier(score)
      parts.push('<div class="ability-item">')
      parts.push(`<span class="ability-heading">${headers[idx]}</span>`)
      parts.push(`<span class="ability-score">${score} <span class="ability-modifier">(${mod})</span></span>`)
      parts.push("</div>")
    }
    parts.push("</div>")
    parts.push("</div>")
  }

  // === Tapered Rule ===
  parts.push('<div class="tapered-rule"></div>')

  // --- Saves, Skills, Resistances, Immunities, Senses, Languages, CR ---
  parts.push('<div class="statblock-item-container property-container">')

  // Saving Throws
  if (data.saves && Array.isArray(data.saves) && data.saves.length > 0) {
    parts.push(renderSaves("Saving Throws", data.saves))
  }

  // Skills
  if (data.skillsaves && Array.isArray(data.skillsaves) && data.skillsaves.length > 0) {
    parts.push(renderSaves("Skills", data.skillsaves))
  }

  // Property lines for resistances, immunities, etc.
  const conditionedProperties = [
    { key: "damage_resistances", label: "Damage Resistances" },
    { key: "damage_immunities", label: "Damage Immunities" },
    { key: "condition_immunities", label: "Condition Immunities" },
    { key: "damage_vulnerabilities", label: "Damage Vulnerabilities" },
    { key: "senses", label: "Senses" },
    { key: "languages", label: "Languages" },
  ]

  for (const { key, label } of conditionedProperties) {
    const val = data[key]
    if (val !== undefined && val !== null && val !== "") {
      parts.push(
        `<div class="property-line"><span class="property-name">${escapeHtml(label)}</span> <span class="property-text">${renderText(val)}</span></div>`,
      )
    }
  }

  // Challenge Rating + Proficiency Bonus
  if (data.cr !== undefined && data.cr !== null) {
    const crStr = String(data.cr)
    const xp = CR_XP[crStr]
    const xpStr = xp !== undefined ? ` (${formatNumber(xp)} XP)` : ""
    const pb = proficiencyBonus(crStr)
    parts.push('<div class="cr-proficiency">')
    parts.push(
      `<div class="property-line"><span class="property-name">Challenge</span> <span class="property-text">${escapeHtml(crStr)}${escapeHtml(xpStr)}</span></div>`,
    )
    parts.push(
      `<div class="property-line"><span class="property-name">Proficiency Bonus</span> <span class="property-text">${escapeHtml(pb)}</span></div>`,
    )
    parts.push("</div>")
  }

  parts.push("</div>")

  // === Tapered Rule ===
  parts.push('<div class="tapered-rule"></div>')

  // --- Traits ---
  if (data.traits && Array.isArray(data.traits) && data.traits.length > 0) {
    parts.push(renderTraitBlock(null, data.traits))
  }

  // --- Spells / Spellcasting ---
  if (data.spells && Array.isArray(data.spells) && data.spells.length > 0) {
    parts.push(renderSpells(data.spells))
  }

  // --- Actions ---
  if (data.actions && Array.isArray(data.actions) && data.actions.length > 0) {
    parts.push(renderTraitBlock("Actions", data.actions))
  }

  // --- Bonus Actions ---
  if (data.bonus_actions && Array.isArray(data.bonus_actions) && data.bonus_actions.length > 0) {
    parts.push(renderTraitBlock("Bonus Actions", data.bonus_actions))
  }

  // --- Reactions ---
  if (data.reactions && Array.isArray(data.reactions) && data.reactions.length > 0) {
    parts.push(renderTraitBlock("Reactions", data.reactions))
  }

  // --- Legendary Actions ---
  if (data.legendary_actions && Array.isArray(data.legendary_actions) && data.legendary_actions.length > 0) {
    const desc = data.legendary_description || null
    parts.push(renderTraitBlock("Legendary Actions", data.legendary_actions, desc))
  }

  // --- Mythic Actions ---
  if (data.mythic_actions && Array.isArray(data.mythic_actions) && data.mythic_actions.length > 0) {
    const desc = data.mythic_description || null
    parts.push(renderTraitBlock("Mythic Actions", data.mythic_actions, desc))
  }

  // --- Lair Actions ---
  if (data.lair_actions && Array.isArray(data.lair_actions) && data.lair_actions.length > 0) {
    parts.push(renderTraitBlock("Lair Actions", data.lair_actions))
  }

  // --- Regional Effects ---
  if (data.regional_effects && Array.isArray(data.regional_effects) && data.regional_effects.length > 0) {
    parts.push(renderTraitBlock("Regional Effects", data.regional_effects))
  }

  parts.push("</div>") // .column
  parts.push("</div>") // .statblock-content

  // === Bottom Bar ===
  parts.push('<div class="bar"></div>')

  parts.push("</div>") // .statblock

  return parts.join("\n")
}

// ---------------------------------------------------------------------------
// Sub-renderers
// ---------------------------------------------------------------------------

function renderSaves(label: string, saves: any[]): string {
  const entries: string[] = []
  for (let idx = 0; idx < saves.length; idx++) {
    const entry = saves[idx]
    if (typeof entry === "object" && entry !== null) {
      // Check if this is a trait-style entry {name: "Arcana", desc: "+6"}
      if ("name" in entry && "desc" in entry) {
        const comma = entries.length > 0 ? ", " : ""
        entries.push(
          `${comma}<span class="save-entry"><span class="save-name">${renderText(entry.name)}</span> <span class="save-value">${renderText(entry.desc)}</span></span>`,
        )
      } else {
        // Standard format {arcana: 6}
        for (const [name, value] of Object.entries(entry)) {
          const sign = Number(value) >= 0 ? "+" : ""
          const comma = entries.length > 0 ? ", " : ""
          entries.push(
            `${comma}<span class="save-entry"><span class="save-name">${escapeHtml(name)}</span> <span class="save-value">${escapeHtml(sign + String(value))}</span></span>`,
          )
        }
      }
    }
  }
  return `<div class="saves-line"><span class="property-name">${escapeHtml(label)}</span> ${entries.join("")}</div>`
}

function renderTraitBlock(
  heading: string | null,
  traits: Trait[],
  description?: string | null,
): string {
  const parts: string[] = []
  parts.push('<div class="statblock-item-container traits-container">')

  if (heading) {
    parts.push(`<h3 class="section-heading">${escapeHtml(heading)}</h3>`)
  }

  if (description) {
    parts.push(`<div class="trait-item"><span class="trait-desc">${renderText(description)}</span></div>`)
  }

  for (const trait of traits) {
    parts.push('<div class="trait-item">')
    if (trait.name) {
      parts.push(`<span class="trait-name">${renderText(trait.name)}.</span>`)
    }
    if (trait.desc) {
      parts.push(`<span class="trait-desc">${renderText(trait.desc)}</span>`)
    }
    parts.push("</div>")
  }

  parts.push("</div>")
  return parts.join("\n")
}

function renderSpells(spells: any[]): string {
  const parts: string[] = []
  parts.push('<div class="statblock-item-container spells-container">')

  for (const spell of spells) {
    if (typeof spell === "string") {
      parts.push(`<div class="spell-header">${renderText(spell)}</div>`)
    } else if (typeof spell === "object" && spell !== null) {
      for (const [level, list] of Object.entries(spell)) {
        parts.push(
          `<div class="spell-level"><span class="spell-level-name">${escapeHtml(level)}:</span> ${renderText(String(list))}</div>`,
        )
      }
    }
  }

  parts.push("</div>")
  return parts.join("\n")
}

// ---------------------------------------------------------------------------
// DOM initialization — runs on page load and SPA navigation
// ---------------------------------------------------------------------------

function renderAllStatblocks() {
  const containers = document.querySelectorAll<HTMLElement>(
    ".fantasy-statblock-container:not([data-rendered])",
  )

  for (const container of containers) {
    const yamlStr = container.getAttribute("data-statblock-yaml")
    if (!yamlStr) continue

    try {
      const data = parseStatblockYaml(yamlStr)
      const html = renderStatblock(data)
      container.innerHTML = html
      container.setAttribute("data-rendered", "true")
    } catch (e) {
      console.error("Fantasy Statblocks: failed to render statblock", e)
      // Fallback: show raw YAML in a <pre> block
      container.innerHTML = `<pre><code>${escapeHtml(yamlStr)}</code></pre>`
      container.setAttribute("data-rendered", "error")
    }
  }
}

// Initial render
renderAllStatblocks()

// Re-render on SPA navigation (Quartz uses a custom "nav" event)
document.addEventListener("nav", () => {
  renderAllStatblocks()
})
