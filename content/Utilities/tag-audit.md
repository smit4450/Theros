---
title: Tag Audit Dashboard
obsidianUIMode: preview
cssclasses:
  - json5e-note
tags:
  - utility/
  - status/active
aliases:
  - Tag Audit
---

# Tag Audit Dashboard

> [!tip] Usage
> Run this note periodically to catch tag violations. **Some queries are commented out** to prevent performance issues — uncomment them one at a time if needed. Use **Tag Wrangler** to fix issues (right-click tags in the tag pane).

> [!warning] Performance
> This dashboard processes thousands of files. If Obsidian freezes, close the note and wait a moment before reopening.

---

## Notes Missing All Tags

Notes with no tags at all — these need attention first.

```dataview
TABLE file.folder AS "Folder", file.size AS "Size"
FROM ""
WHERE length(file.tags) = 0
  AND file.name != "broken links output"
  AND !contains(file.path, ".obsidian")
  AND !contains(file.path, "Assets")
  AND !contains(file.path, "Backgrounds")
  AND !contains(file.path, "z_Templates")
SORT file.folder ASC, file.name ASC
LIMIT 50
```

---

## Notes Missing Status Tags

Notes (location, npc, lore, etc.) without a `status/` tag.

```dataview
TABLE file.tags AS "Current Tags"
FROM #location OR #npc OR #lore OR #event OR #quest
WHERE !any(file.tags, (t) => startswith(t, "status/")) 
  AND !contains(file.tags, "utility/")
  AND !contains(file.path, "z_Templates")
SORT file.name ASC
LIMIT 30
```

---

## Location Notes Missing Place Tags

Notes tagged `location/` but missing a `place/` tag.

```dataview
TABLE file.tags AS "Current Tags"
FROM #location
WHERE !any(file.tags, (t) => startswith(t, "place/")) 
  AND !contains(file.tags, "utility/")
  AND !contains(file.path, "z_Templates")
SORT file.name ASC
LIMIT 30
```

---

## Top 50 Tags by Usage

Most common tags — look for typos or duplicates. **Warning: Expensive query.**

```dataview
TABLE length(rows) AS "Count"
FROM ""
WHERE length(file.tags) > 0
  AND !contains(file.path, "z_Templates")
FLATTEN file.tags AS tag
GROUP BY tag
SORT length(rows) DESC
LIMIT 50
```

---

## Custom Tags (Top 30)

Non-standard tags. **Warning: Expensive query.**

```dataview
TABLE length(rows) AS "Count"
FROM "Mystic Arts" OR "Lore" OR "Utilities"
WHERE length(file.tags) > 0
  AND !contains(file.tags, "utility/")
  AND !contains(file.path, "z_Templates")
FLATTEN file.tags AS tag
WHERE !startswith(tag, "src/")
GROUP BY tag
SORT length(rows) DESC
LIMIT 30
```

---

## Tags Without Hierarchy (No Slashes)

Tags missing the `/` hierarchy. Excludes valid non-hierarchical tags like `quest`, `npc`, `event`, `lore`, `location`, `faction`, `feat`, `background`, `bastion`, `utility`.

```dataview
TABLE file.tags AS "Problematic Tags"
FROM "Mystic Arts" OR "Lore" OR "Utilities"
WHERE any(file.tags, (t) => !contains(t, "/") AND t != "quest" AND t != "npc" AND t != "event" AND t != "lore" AND t != "location" AND t != "faction" AND t != "feat" AND t != "background" AND t != "bastion" AND t != "utility")
  AND !contains(file.path, "z_Templates")
SORT file.name ASC
LIMIT 20
```

---

## WIP Notes (Work in Progress)

Notes still marked as work in progress.

```dataview
TABLE file.folder AS "Folder", file.mtime AS "Last Modified"
FROM #status/wip
WHERE !contains(file.path, "z_Templates")
SORT file.mtime DESC
```

---

## Recently Modified Notes (Last 30 Days)

Quick check for recent edits that may need tag review.

```dataview
TABLE file.tags AS "Tags", file.mtime AS "Modified"
FROM ""
WHERE file.mtime >= date(today) - dur(30 days)
  AND !contains(file.path, ".obsidian")
  AND !contains(file.path, "Assets")
  AND !contains(file.path, "z_Templates")
SORT file.mtime DESC
LIMIT 25
```
---

## Related
- [[tag-reference|Tag Conventions]] — Approved tag list and rules
