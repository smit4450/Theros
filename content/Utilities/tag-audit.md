---
title: Tag Audit Dashboard
obsidianUIMode: preview
cssclasses:
  - json5e-note
tags:
  - type/utility
  - status/active
aliases:
  - Tag Audit
---

# Tag Audit Dashboard

> [!tip] Usage
> Run this note periodically (monthly recommended) to catch tag violations and inconsistencies. Each section uses Dataview queries to surface issues. Fix problems as you find them using **Tag Wrangler** (right-click tags in the tag pane).

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
SORT file.folder ASC, file.name ASC
```

---

## Custom Notes Missing Type Tags

Homebrew/custom notes that don't have a `type/` tag (compendium content uses `ttrpg-cli/` instead).

```dataview
TABLE file.tags AS "Current Tags"
FROM ""
WHERE !contains(file.path, "Compendium")
  AND !contains(file.path, ".obsidian")
  AND !contains(file.path, "Assets")
  AND !contains(file.path, "Backgrounds")
  AND length(file.tags) > 0
  AND !any(file.tags, (t) => startswith(t, "type/"))
  AND !any(file.tags, (t) => startswith(t, "ttrpg-cli/"))
SORT file.name ASC
```

---

## Custom Notes Missing Status Tags

Notes with `type/` tags but no `status/` tag.

```dataview
TABLE file.tags AS "Current Tags"
FROM ""
WHERE any(file.tags, (t) => startswith(t, "type/"))
  AND !any(file.tags, (t) => startswith(t, "status/"))
SORT file.name ASC
```

---

## Location Notes Missing Place Tags

Notes tagged `type/location` but missing a `place/` tag.

```dataview
TABLE file.tags AS "Current Tags"
FROM #type/location
WHERE !any(file.tags, (t) => startswith(t, "place/"))
SORT file.name ASC
```

---

## All Unique Tags (Spot Inconsistencies)

Full tag inventory sorted by usage count — look for typos, duplicates, or non-standard tags.

```dataview
TABLE length(rows) AS "Count"
FROM ""
WHERE length(file.tags) > 0
FLATTEN file.tags AS tag
GROUP BY tag
SORT length(rows) DESC
```

---

## Custom Tags Only (Excluding ttrpg-cli)

Just the hand-curated tags — easier to spot issues without the noise of auto-generated tags.

```dataview
TABLE length(rows) AS "Count"
FROM ""
WHERE length(file.tags) > 0
FLATTEN file.tags AS tag
WHERE !startswith(tag, "ttrpg-cli/")
GROUP BY tag
SORT length(rows) DESC
```

---

## Tags Not Following Hierarchy Convention (No Slashes)

Tags that don't use the `/` hierarchy convention — may need review.

```dataview
TABLE file.tags AS "Problematic Tags"
FROM ""
WHERE any(file.tags, (t) => !contains(t, "/"))
SORT file.name ASC
```

---

## WIP Notes (Work in Progress)

Notes still marked as work in progress.

```dataview
TABLE file.folder AS "Folder", file.mtime AS "Last Modified"
FROM #status/wip
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
SORT file.mtime DESC
LIMIT 25
```

---

## Compendium Source Distribution

Overview of how compendium content is distributed by source book.

```dataview
TABLE length(rows) AS "Count"
FROM ""
WHERE length(file.tags) > 0
FLATTEN file.tags AS tag
WHERE startswith(tag, "ttrpg-cli/compendium/src/")
GROUP BY tag
SORT length(rows) DESC
```

---

## Related
- [[tag-reference|Tag Conventions]] — Approved tag list and rules
- [[spell-table|Spell Table]] — Spell reference
