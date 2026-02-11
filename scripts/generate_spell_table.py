"""
Generates a sortable/filterable spell table as a markdown file with embedded HTML/CSS/JS.
Works in both Obsidian (static styled table) and Quartz (full interactive sorting/filtering).
"""

import os
import re
from pathlib import Path

SPELLS_DIR = Path(__file__).parent.parent / "content" / "Compendium" / "spells"
OUTPUT_FILE = Path(__file__).parent.parent / "content" / "Utilities" / "spell-table.md"

LEVEL_ORDER = {
    "cantrip": 0,
    "1st-level": 1,
    "2nd-level": 2,
    "3rd-level": 3,
    "4th-level": 4,
    "5th-level": 5,
    "6th-level": 6,
    "7th-level": 7,
    "8th-level": 8,
    "9th-level": 9,
}

LEVEL_DISPLAY = {
    "cantrip": "Cantrip",
    "1st-level": "1st",
    "2nd-level": "2nd",
    "3rd-level": "3rd",
    "4th-level": "4th",
    "5th-level": "5th",
    "6th-level": "6th",
    "7th-level": "7th",
    "8th-level": "8th",
    "9th-level": "9th",
}


def parse_frontmatter(text: str):
    """Extract YAML frontmatter as raw text between --- delimiters."""
    match = re.match(r"^---\s*\n(.*?)\n---", text, re.DOTALL)
    if not match:
        return "", text
    return match.group(1), text[match.end() :]


def extract_tags(frontmatter: str):
    """Extract ttrpg-cli tags from frontmatter."""
    tags = []
    in_tags = False
    for line in frontmatter.splitlines():
        stripped = line.strip()
        if stripped.startswith("tags:"):
            in_tags = True
            continue
        if in_tags:
            if stripped.startswith("- "):
                tags.append(stripped[2:].strip())
            else:
                in_tags = False
    return tags


def extract_title(frontmatter: str):
    """Extract title from frontmatter."""
    for line in frontmatter.splitlines():
        if line.strip().startswith("title:"):
            return line.split(":", 1)[1].strip().strip('"').strip("'")
    return ""


def extract_body_field(body: str, field: str):
    """Extract a field like 'Casting time', 'Range', etc. from the body."""
    pattern = rf"\*\*{re.escape(field)}:\*\*\s*(.+)"
    match = re.search(pattern, body, re.IGNORECASE)
    if match:
        value = match.group(1).strip()
        # Clean up markdown links
        value = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", value)
        return value
    return ""


def extract_classes_from_tags(tags: list):
    """Extract base class names from ttrpg-cli/spell/class/* tags."""
    classes = []
    for tag in tags:
        m = re.match(r"ttrpg-cli/spell/class/(.+)", tag)
        if m:
            cls = m.group(1).replace("-", " ").title()
            classes.append(cls)
    return sorted(set(classes))


def extract_subclasses_from_tags(tags: list):
    """Extract subclass names from ttrpg-cli/spell/subclass/* tags."""
    subclasses = []
    for tag in tags:
        m = re.match(r"ttrpg-cli/spell/subclass/(.+)", tag)
        if m:
            subcls = m.group(1).replace("-", " ").title()
            subclasses.append(subcls)
    return sorted(set(subclasses))


def extract_feats_from_tags(tags: list):
    """Extract feat names from ttrpg-cli/spell/feat/* tags."""
    feats = []
    for tag in tags:
        m = re.match(r"ttrpg-cli/spell/feat/(.+)", tag)
        if m:
            feat = m.group(1).replace("-", " ").title()
            feats.append(feat)
    return sorted(set(feats))


def extract_races_from_tags(tags: list):
    """Extract race names from ttrpg-cli/spell/race/* tags."""
    races = []
    for tag in tags:
        m = re.match(r"ttrpg-cli/spell/race/(.+)", tag)
        if m:
            race = m.group(1).replace("-", " ").replace("/", " - ").title()
            races.append(race)
    return sorted(set(races))


def extract_optfeatures_from_tags(tags: list):
    """Extract optional feature names from ttrpg-cli/spell/optfeature/* tags."""
    optfeatures = []
    for tag in tags:
        m = re.match(r"ttrpg-cli/spell/optfeature/(.+)", tag)
        if m:
            optfeat = m.group(1).replace("-", " ").title()
            optfeatures.append(optfeat)
    return sorted(set(optfeatures))


def is_ritual_from_tags(tags: list):
    """Check if spell has ritual tag."""
    return "ttrpg-cli/spell/ritual" in tags


def extract_level_from_tags(tags: list):
    """Extract spell level from tags."""
    for tag in tags:
        m = re.match(r"ttrpg-cli/spell/level/(.+)", tag)
        if m:
            return m.group(1)
    return ""


def extract_school_from_tags(tags: list):
    """Extract spell school from tags."""
    for tag in tags:
        m = re.match(r"ttrpg-cli/spell/school/(.+)", tag)
        if m:
            return m.group(1).title()
    return ""


def parse_spell_file(filepath: Path):
    """Parse a single spell markdown file and return a dict of spell data."""
    text = filepath.read_text(encoding="utf-8")
    frontmatter, body = parse_frontmatter(text)
    if not frontmatter:
        return None

    tags = extract_tags(frontmatter)
    title = extract_title(frontmatter)
    if not title:
        return None

    level = extract_level_from_tags(tags)
    school = extract_school_from_tags(tags)
    classes = extract_classes_from_tags(tags)
    subclasses = extract_subclasses_from_tags(tags)
    feats = extract_feats_from_tags(tags)
    races = extract_races_from_tags(tags)
    optfeatures = extract_optfeatures_from_tags(tags)
    is_ritual = is_ritual_from_tags(tags)

    casting_time = extract_body_field(body, "Casting time")
    range_val = extract_body_field(body, "Range")
    components = extract_body_field(body, "Components")
    duration = extract_body_field(body, "Duration")

    # Clean components: remove material descriptions in parens for the table
    components_short = re.sub(r"\s*\(.*\)", "", components)

    return {
        "title": title,
        "filename": filepath.stem,
        "level": level,
        "level_sort": LEVEL_ORDER.get(level, 99),
        "level_display": LEVEL_DISPLAY.get(level, level),
        "school": school,
        "casting_time": casting_time,
        "range": range_val,
        "components": components_short,
        "components_full": components,
        "duration": duration,
        "classes": classes,
        "subclasses": subclasses,
        "feats": feats,
        "races": races,
        "optfeatures": optfeatures,
        "is_ritual": is_ritual,
    }


def generate_html_table(spells: list):
    """Generate the HTML table with embedded CSS and JS for sorting/filtering."""
    # Collect unique values for filter dropdowns
    all_levels = sorted(
        set(s["level"] for s in spells if s["level"]),
        key=lambda x: LEVEL_ORDER.get(x, 99),
    )
    all_schools = sorted(set(s["school"] for s in spells if s["school"]))
    all_classes = sorted(
        set(cls for s in spells for cls in s["classes"])
    )
    all_subclasses = sorted(
        set(subcls for s in spells for subcls in s["subclasses"])
    )
    all_feats = sorted(
        set(feat for s in spells for feat in s["feats"])
    )
    all_races = sorted(
        set(race for s in spells for race in s["races"])
    )
    all_optfeatures = sorted(
        set(optfeat for s in spells for optfeat in s["optfeatures"])
    )

    # Sort spells by level then name
    spells.sort(key=lambda s: (s["level_sort"], s["title"].lower()))

    # Build filter controls HTML
    level_options = "".join(
        f'<option value="{lv}">{LEVEL_DISPLAY.get(lv, lv)}</option>'
        for lv in all_levels
    )
    school_options = "".join(
        f'<option value="{sc}">{sc}</option>' for sc in all_schools
    )
    class_options = "".join(
        f'<option value="{cl}">{cl}</option>' for cl in all_classes
    )
    subclass_options = "".join(
        f'<option value="{subcls}">{subcls}</option>' for subcls in all_subclasses
    )
    feat_options = "".join(
        f'<option value="{feat}">{feat}</option>' for feat in all_feats
    )
    race_options = "".join(
        f'<option value="{race}">{race}</option>' for race in all_races
    )
    optfeature_options = "".join(
        f'<option value="{optfeat}">{optfeat}</option>' for optfeat in all_optfeatures
    )

    # Build table rows - links now need to go up one level and into Compendium/spells
    rows = []
    for sp in spells:
        classes_str = ", ".join(sp["classes"])
        subclasses_str = ", ".join(sp["subclasses"])
        feats_str = ", ".join(sp["feats"])
        races_str = ", ".join(sp["races"])
        optfeatures_str = ", ".join(sp["optfeatures"])
        ritual_str = "yes" if sp["is_ritual"] else "no"
        # Update link to go from Utilities to Compendium/spells
        link = f'../Compendium/spells/{sp["filename"]}'
        row = (
            f'<tr data-level="{sp["level"]}" data-school="{sp["school"]}" '
            f'data-classes="{classes_str.lower()}" data-subclasses="{subclasses_str.lower()}" '
            f'data-feats="{feats_str.lower()}" data-races="{races_str.lower()}" '
            f'data-optfeatures="{optfeatures_str.lower()}" data-ritual="{ritual_str}" '
            f'data-name="{sp["title"].lower()}">'
            f'<td><a href="{link}">{sp["title"]}</a></td>'
            f'<td data-sort="{sp["level_sort"]}">{sp["level_display"]}</td>'
            f'<td>{sp["school"]}</td>'
            f'<td>{sp["casting_time"]}</td>'
            f'<td>{sp["range"]}</td>'
            f'<td title="{sp["components_full"]}">{sp["components"]}</td>'
            f'<td>{sp["duration"]}</td>'
            f'<td>{classes_str}</td>'
            f"</tr>"
        )
        rows.append(row)

    rows_html = "\n".join(rows)

    html = f"""<style>
/* Spell table styles - works in both Obsidian and Quartz */
#spell-filters {{
  display: flex;
  flex-wrap: wrap;
  gap: 0.5rem;
  margin-bottom: 1rem;
  align-items: center;
}}
#spell-filters input,
#spell-filters select {{
  padding: 0.4rem 0.6rem;
  border: 1px solid var(--lightgray, #ccc);
  border-radius: 4px;
  background: var(--light, #fff);
  color: var(--darkgray, #333);
  font-family: inherit;
  font-size: 0.85rem;
}}
#spell-filters input {{
  min-width: 200px;
}}
#spell-filters select {{
  min-width: 120px;
}}
#spell-table-container {{
  overflow-x: auto;
  margin: 0;
}}
#spell-count {{
  font-size: 0.85rem;
  color: var(--gray, #888);
  margin-bottom: 0.5rem;
}}
table#spell-data-table {{
  width: 100%;
  border-collapse: collapse;
  font-size: 0.85rem;
}}
table#spell-data-table th,
table#spell-data-table td {{
  padding: 0.35rem 0.6rem;
  border-bottom: 1px solid var(--lightgray, #ddd);
  text-align: left;
  white-space: nowrap;
}}
table#spell-data-table td:first-child {{
  white-space: normal;
}}
table#spell-data-table th {{
  cursor: pointer;
  user-select: none;
  position: sticky;
  top: 0;
  background: var(--light, #eee5ce);
  font-weight: bold;
  border-bottom: 2px solid var(--darkgray, #333);
}}
table#spell-data-table th:hover {{
  color: var(--secondary, #1d5c73);
}}
table#spell-data-table th .sort-indicator {{
  margin-left: 0.3rem;
  opacity: 0.4;
}}
table#spell-data-table th .sort-indicator.active {{
  opacity: 1;
}}
table#spell-data-table tr:hover {{
  background: var(--highlight, rgba(143, 159, 169, 0.15));
}}
table#spell-data-table a {{
  color: var(--secondary, #1d5c73);
  text-decoration: none;
}}
table#spell-data-table a:hover {{
  text-decoration: underline;
}}
#spell-reset-btn {{
  padding: 0.4rem 0.8rem;
  border: 1px solid var(--lightgray, #ccc);
  border-radius: 4px;
  background: var(--light, #fff);
  color: var(--darkgray, #333);
  cursor: pointer;
  font-family: inherit;
  font-size: 0.85rem;
}}
#spell-reset-btn:hover {{
  background: var(--highlight, rgba(143, 159, 169, 0.15));
}}
</style>

<div id="spell-filters">
  <input type="text" id="spell-search" placeholder="Search spells..." />
  <select id="spell-level-filter">
    <option value="">All Levels</option>
    {level_options}
  </select>
  <select id="spell-school-filter">
    <option value="">All Schools</option>
    {school_options}
  </select>
  <select id="spell-class-filter">
    <option value="">All Classes</option>
    {class_options}
  </select>
  <select id="spell-subclass-filter">
    <option value="">All Subclasses</option>
    {subclass_options}
  </select>
  <select id="spell-feat-filter">
    <option value="">All Feats</option>
    {feat_options}
  </select>
  <select id="spell-race-filter">
    <option value="">All Races</option>
    {race_options}
  </select>
  <select id="spell-optfeature-filter">
    <option value="">All Optional Features</option>
    {optfeature_options}
  </select>
  <select id="spell-ritual-filter">
    <option value="">All (Ritual)</option>
    <option value="yes">Ritual Only</option>
    <option value="no">Non-Ritual Only</option>
  </select>
  <button id="spell-reset-btn" type="button">Reset</button>
</div>

<div id="spell-count"></div>

<div id="spell-table-container">
<table id="spell-data-table">
<thead>
<tr>
  <th data-col="name">Spell<span class="sort-indicator">⇅</span></th>
  <th data-col="level">Level<span class="sort-indicator">⇅</span></th>
  <th data-col="school">School<span class="sort-indicator">⇅</span></th>
  <th data-col="casting">Casting Time<span class="sort-indicator">⇅</span></th>
  <th data-col="range">Range<span class="sort-indicator">⇅</span></th>
  <th data-col="components">Components<span class="sort-indicator">⇅</span></th>
  <th data-col="duration">Duration<span class="sort-indicator">⇅</span></th>
  <th data-col="classes">Classes<span class="sort-indicator">⇅</span></th>
</tr>
</thead>
<tbody>
{rows_html}
</tbody>
</table>
</div>"""

    return html


def main():
    spells = []
    for filepath in sorted(SPELLS_DIR.glob("*.md")):
        if filepath.name in ("spells.md", "spell-table.md"):
            continue
        spell = parse_spell_file(filepath)
        if spell:
            spells.append(spell)

    print(f"Parsed {len(spells)} spells")

    html_table = generate_html_table(spells)

    # Build the full markdown file
    md = f"""---
title: Spell Table
obsidianUIMode: preview
cssclasses:
  - json5e-note
tags:
  - ttrpg-cli/compendium/src/5e/xphb
---
# Spell Table

A sortable and filterable reference table of all available spells.

{html_table}
"""

    OUTPUT_FILE.write_text(md, encoding="utf-8")
    print(f"Generated {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
