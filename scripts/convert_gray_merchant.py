#!/usr/bin/env python3
"""
Convert Gray Merchant of Asphodel PDF text to Obsidian markdown files.
"""

import os
import re
from pathlib import Path

# Paths
SCRIPT_DIR = Path(__file__).parent
REPO_ROOT = SCRIPT_DIR.parent
PDF_TEXT_PATH = REPO_ROOT / "pdf_full_text.txt"
OUTPUT_DIR = REPO_ROOT / "content" / "Compendium" / "items"
BESTIARY_OUTPUT_DIR = REPO_ROOT / "content" / "Compendium" / "bestiary"

# Source tag for this supplement
SOURCE_TAG = "ttrpg-cli/compendium/src/5e/gmoa"

# OCR error corrections
OCR_FIXES = [
    (r"Percep!on", "Perception"),
    (r"a\.ack", "attack"),
    (r"A\.ack", "Attack"),
    (r"Aack", "Attack"),
    ("Mulaack", "Multiattack"),  # Not regex, just string replacement
    ("Mulattack", "Multiattack"),
    (r"Immunies", "Immunities"),
    (r"Condion", "Condition"),
    (r"exhaus!on", "exhaustion"),
    (r"ac!on", "action"),
    (r"ac!vate", "activate"),
    (r"\ba !me\b", "a time"),
    (r"!me\b", "time"),
    (r"hos!le", "hostile"),
    (r"a\.unement", "attunement"),
    # The PDF uses \x0b (vertical tab) instead of "ft" in distances
    (r"(\d+) " + "\x0b" + r"\.", r"\1 ft."),  # "10 \x0b." -> "10 ft."
    (r"(\d+) \.", r"\1 ft."),  # Also handle regular period just in case
]

def fix_ocr_errors(text: str) -> str:
    """Fix common OCR errors from PDF extraction."""
    # First, strip all control characters except newlines and tabs
    cleaned = ""
    for char in text:
        if char == '\n' or char == '\t' or (ord(char) >= 32 and ord(char) != 127):
            cleaned += char
        elif char == '\x0b':  # Vertical tab - used instead of "ft" in distances
            cleaned += char  # Keep for now, handled by pattern below
    text = cleaned
    
    for pattern, replacement in OCR_FIXES:
        text = re.sub(pattern, replacement, text)
    return text

def slugify(name: str) -> str:
    """Convert item name to filename slug."""
    slug = name.lower()
    slug = re.sub(r"[''']", "", slug)
    slug = re.sub(r"[^a-z0-9]+", "-", slug)
    slug = slug.strip("-")
    return slug + "-gmoa"

def get_rarity_tag(rarity: str) -> str:
    """Convert rarity string to tag format."""
    rarity_lower = rarity.lower()
    # Check uncommon BEFORE common (since "uncommon" contains "common")
    if "uncommon" in rarity_lower:
        return "ttrpg-cli/item/rarity/uncommon"
    elif "common" in rarity_lower:
        return "ttrpg-cli/item/rarity/common"
    elif "very rare" in rarity_lower:
        return "ttrpg-cli/item/rarity/very-rare"
    elif "rare" in rarity_lower:
        return "ttrpg-cli/item/rarity/rare"
    elif "legendary" in rarity_lower:
        return "ttrpg-cli/item/rarity/legendary"
    elif "artifact" in rarity_lower:
        return "ttrpg-cli/item/rarity/artifact"
    elif "story" in rarity_lower:
        return "ttrpg-cli/item/rarity/story"
    return "ttrpg-cli/item/rarity/unknown"

def get_item_type_tag(item_type: str) -> list:
    """Get tags based on item type."""
    tags = []
    item_type_lower = item_type.lower()
    
    if "weapon" in item_type_lower:
        tags.append("ttrpg-cli/item/weapon")
        if "trident" in item_type_lower:
            tags.append("ttrpg-cli/item/weapon/martial")
            tags.append("ttrpg-cli/item/weapon/melee")
        elif "shortbow" in item_type_lower:
            tags.append("ttrpg-cli/item/weapon/martial")
            tags.append("ttrpg-cli/item/weapon/ranged")
        elif "warhammer" in item_type_lower:
            tags.append("ttrpg-cli/item/weapon/martial")
            tags.append("ttrpg-cli/item/weapon/melee")
        elif "whip" in item_type_lower:
            tags.append("ttrpg-cli/item/weapon/martial")
            tags.append("ttrpg-cli/item/weapon/melee")
        elif "scimitar" in item_type_lower:
            tags.append("ttrpg-cli/item/weapon/martial")
            tags.append("ttrpg-cli/item/weapon/melee")
        elif "dagger" in item_type_lower:
            tags.append("ttrpg-cli/item/weapon/simple")
            tags.append("ttrpg-cli/item/weapon/melee")
        elif "sickle" in item_type_lower:
            tags.append("ttrpg-cli/item/weapon/simple")
            tags.append("ttrpg-cli/item/weapon/melee")
        elif "spear" in item_type_lower:
            tags.append("ttrpg-cli/item/weapon/simple")
            tags.append("ttrpg-cli/item/weapon/melee")
        elif "shortsword" in item_type_lower:
            tags.append("ttrpg-cli/item/weapon/martial")
            tags.append("ttrpg-cli/item/weapon/melee")
    elif "armor" in item_type_lower:
        tags.append("ttrpg-cli/item/armor")
        if "plate" in item_type_lower:
            tags.append("ttrpg-cli/item/armor/heavy")
    elif "shield" in item_type_lower:
        tags.append("ttrpg-cli/item/armor/shield")
    elif "potion" in item_type_lower:
        tags.append("ttrpg-cli/item/potion")
    elif "ring" in item_type_lower:
        tags.append("ttrpg-cli/item/ring")
    elif "rod" in item_type_lower:
        tags.append("ttrpg-cli/item/rod")
    elif "staff" in item_type_lower:
        tags.append("ttrpg-cli/item/staff")
    elif "wondrous" in item_type_lower:
        tags.append("ttrpg-cli/item/wondrous")
    elif "adventuring gear" in item_type_lower:
        tags.append("ttrpg-cli/item/gear")
    
    return tags

def parse_item_header(header_text: str):
    """Parse item header to extract type, rarity, and attunement."""
    # Pattern: Type, rarity (requires attunement...) — see card
    # Examples:
    # "Wondrous item, rare — see card"
    # "Weapon (trident), artifact (requires attunement by a creature that worships Thassa) — see card"
    # "Armor (plate), very rare (requires attunement by a creature that doesn't worship any Theran god)"
    
    # Normalize the header - join multi-line headers and clean up
    header_text = re.sub(r"\s+", " ", header_text)  # Normalize whitespace
    
    # Remove "— see card" or "— see" suffix (anywhere in string, handles line breaks)
    header_text = re.sub(r"\s*[—-]\s*see(\s+card)?", "", header_text, flags=re.IGNORECASE)
    
    attunement = None
    attunement_match = re.search(r"\(requires attunement([^)]*)\)", header_text, re.IGNORECASE)
    if attunement_match:
        attunement_detail = attunement_match.group(1).strip()
        if attunement_detail:
            # Ensure there's a space after "attunement" if detail starts with letter
            if attunement_detail and attunement_detail[0].isalpha():
                attunement = f"requires attunement {attunement_detail}"
            else:
                attunement = f"requires attunement{attunement_detail}"
        else:
            attunement = "requires attunement"
    
    # Extract rarity
    rarity = "unknown"
    for r in ["legendary", "artifact", "very rare", "rare", "uncommon", "common", "story"]:
        if r in header_text.lower():
            rarity = r
            break
    
    # Extract item type (everything before the rarity, without the rarity itself)
    # First, remove attunement clause
    clean_header = re.sub(r"\s*\(requires attunement[^)]*\)", "", header_text, flags=re.IGNORECASE)
    # Remove rarity words to get just the item type
    item_type = clean_header
    for r in ["legendary", "artifact", "very rare", "rare", "uncommon", "common", "story"]:
        item_type = re.sub(rf",?\s*{r}\s*", "", item_type, flags=re.IGNORECASE)
    # Clean up stray dashes and extra punctuation
    item_type = re.sub(r"[—-]+\s*$", "", item_type)  # Remove trailing dashes
    item_type = re.sub(r"[—-]+\s*,", ",", item_type)  # Remove dashes before commas
    item_type = item_type.strip().rstrip(",").strip()
    if not item_type:
        item_type = "Wondrous item"
    
    return item_type, rarity, attunement

def detect_and_extract_statblock(text: str) -> tuple:
    """
    Detect and extract a statblock from the description text.
    Returns (remaining_description, statblock_yaml) where statblock_yaml is None if no statblock found.
    Must be called BEFORE paragraph joining since statblocks need line structure.
    """
    # Pattern to detect statblock start: ALL CAPS NAME followed by size/type line
    statblock_pattern = re.compile(
        r"^([A-Z][A-Z\s]+)\n"  # Creature name in caps
        r"(Small|Medium|Large|Tiny|Huge|Gargantuan)\s+"  # Size
        r"(construct|undead|beast|fiend|celestial|humanoid|monstrosity|elemental|fey|giant|aberration|dragon|ooze|plant)"  # Type
        r",?\s*([^\n]*)\n",  # Alignment
        re.MULTILINE
    )
    
    match = statblock_pattern.search(text)
    if not match:
        return text, None
    
    # Extract the statblock text from match to end
    statblock_start = match.start()
    statblock_text = text[statblock_start:]
    remaining_text = text[:statblock_start].strip()
    
    # Fix OCR errors in statblock
    statblock_text = fix_ocr_errors(statblock_text)
    
    # Re-parse the fixed text to get the corrected values
    fixed_match = statblock_pattern.search(statblock_text)
    if fixed_match:
        creature_name = fixed_match.group(1).strip().title()
        size = fixed_match.group(2).strip()
        creature_type = fixed_match.group(3).strip().lower()
        alignment = fixed_match.group(4).strip() if fixed_match.group(4) else "Unaligned"
    else:
        # Fallback to original match if fixed text doesn't match
        creature_name = match.group(1).strip().title()
        size = match.group(2).strip()
        creature_type = match.group(3).strip().lower()
        alignment = match.group(4).strip() if match.group(4) else "Unaligned"
    
    # Parse the rest of the statblock line by line
    lines = statblock_text.split("\n")
    
    ac = ""
    hp = ""
    hit_dice = ""
    speed = ""
    stats = {"str": 10, "dex": 10, "con": 10, "int": 10, "wis": 10, "cha": 10}
    skills = []
    damage_immunities = ""
    condition_immunities = ""
    senses = ""
    languages = ""
    cr = ""
    xp = ""
    traits = []
    actions = []
    
    current_section = "stats"  # stats, traits, actions
    current_trait = None
    current_action = None
    
    i = 1  # Skip the name/type line
    while i < len(lines):
        line = lines[i].strip()
        
        if line.startswith("Armor Class"):
            ac = re.search(r"Armor Class (\d+)", line)
            ac = ac.group(1) if ac else "10"
        elif line.startswith("Hit Points"):
            hp_match = re.search(r"Hit Points (\d+)\s*\(([^)]+)\)", line)
            if hp_match:
                hp = hp_match.group(1)
                hit_dice = hp_match.group(2)
        elif line.startswith("Speed"):
            speed = line.replace("Speed", "").strip()
        elif line == "STR":
            # Ability scores header - values are on separate lines after DEX, CON, INT, WIS, CHA
            # Skip past the header lines (STR, DEX, CON, INT, WIS, CHA)
            ability_values = []
            j = i
            while j < len(lines) and len(ability_values) < 6:
                j += 1
                if j >= len(lines):
                    break
                next_line = lines[j].strip()
                # Check if this is an ability header (skip it) or a value
                if next_line in ["STR", "DEX", "CON", "INT", "WIS", "CHA"]:
                    continue
                # Check if this line has an ability score (number with modifier in parens)
                score_match = re.match(r"^(\d+)\s*\([+-]?\d+\)", next_line)
                if score_match:
                    ability_values.append(int(score_match.group(1)))
                    # Also check if there are multiple values on this line
                    all_scores = re.findall(r"(\d+)\s*\([+-]?\d+\)", next_line)
                    if len(all_scores) > 1:
                        ability_values = [int(s) for s in all_scores]
                        break
            
            if len(ability_values) == 6:
                stats = {
                    "str": ability_values[0],
                    "dex": ability_values[1],
                    "con": ability_values[2],
                    "int": ability_values[3],
                    "wis": ability_values[4],
                    "cha": ability_values[5]
                }
            i = j  # Move past the ability scores
        elif line.startswith("Skills"):
            skills_text = line.replace("Skills", "").strip()
            # Parse skills like "Perception +3"
            skill_matches = re.findall(r"([A-Za-z]+)\s+([+-]\d+)", skills_text)
            skills = [{"name": f"[{s[0]}](Compendium/rules/skills.md#{s[0]})", "desc": s[1]} for s in skill_matches]
        elif line.startswith("Damage Immunit"):
            damage_immunities = line.replace("Damage Immunities", "").replace("Damage Immunity", "").strip()
        elif line.startswith("Condition Immunit"):
            condition_immunities = line.replace("Condition Immunities", "").replace("Condition Immunity", "").strip()
        elif line.startswith("Senses"):
            senses = line.replace("Senses", "").strip()
        elif line.startswith("Languages"):
            languages = line.replace("Languages", "").strip()
        elif line.startswith("Challenge"):
            cr_match = re.search(r"Challenge\s+([0-9/]+)\s*\((\d+)\s*XP\)", line)
            if cr_match:
                cr = cr_match.group(1)
                xp = cr_match.group(2)
            current_section = "traits"
        elif current_section == "traits" or current_section == "actions":
            # Check for standalone "A" or "ACTIONS" (Actions header in OCR-mangled text)
            if line == "A" or line.upper() == "ACTIONS":
                current_section = "actions"
                current_trait = None  # End current trait before switching
                i += 1
                continue
            
            # Check if this is a new trait/action header (Name. description)
            header_match = re.match(r"^([A-Z][^.]+)\.\s*(.*)$", line)
            if header_match:
                trait_name = header_match.group(1)
                trait_desc = header_match.group(2)
                
                if current_section == "traits":
                    current_trait = {"name": trait_name, "desc": trait_desc}
                    traits.append(current_trait)
                    current_action = None
                else:
                    current_action = {"name": trait_name, "desc": trait_desc}
                    actions.append(current_action)
                    current_trait = None
            elif line and (current_trait or current_action):
                # Check if this continuation line is "A" - switch to actions
                if line == "A":
                    current_section = "actions"
                    current_trait = None
                    i += 1
                    continue
                    
                # Continuation of previous trait/action
                if current_section == "traits" and current_trait:
                    current_trait["desc"] += " " + line
                elif current_section == "actions" and current_action:
                    current_action["desc"] += " " + line
        
        i += 1
    
    # Build YAML statblock
    yaml_lines = [
        '```statblock',
        f'"name": "{creature_name} (GMOA)"',
        f'"size": "{size}"',
        f'"type": "{creature_type}"',
        f'"alignment": "{alignment.capitalize()}"',
        f'"ac": !!int "{ac}"',
        f'"hp": !!int "{hp}"',
        f'"hit_dice": "{hit_dice}"',
        f'"stats":',
        f'  - !!int "{stats["str"]}"',
        f'  - !!int "{stats["dex"]}"',
        f'  - !!int "{stats["con"]}"',
        f'  - !!int "{stats["int"]}"',
        f'  - !!int "{stats["wis"]}"',
        f'  - !!int "{stats["cha"]}"',
        f'"speed": "{speed}"',
    ]
    
    if skills:
        yaml_lines.append('"skillsaves":')
        for skill in skills:
            yaml_lines.append(f'  - "name": "{skill["name"]}"')
            yaml_lines.append(f'    "desc": "{skill["desc"]}"')
    
    if damage_immunities:
        yaml_lines.append(f'"damage_immunities": "{damage_immunities}"')
    
    if condition_immunities:
        yaml_lines.append(f'"condition_immunities": "{condition_immunities}"')
    
    if senses:
        yaml_lines.append(f'"senses": "{senses}"')
    
    if languages:
        yaml_lines.append(f'"languages": "{languages}"')
    
    if cr:
        yaml_lines.append(f'"cr": "{cr}"')
    
    if traits:
        yaml_lines.append('"traits":')
        for trait in traits:
            # Escape quotes in description
            desc = trait["desc"].replace('"', '\\"')
            yaml_lines.append(f'  - "desc": "{desc}"')
            yaml_lines.append(f'    "name": "{trait["name"]}"')
    
    if actions:
        yaml_lines.append('"actions":')
        for action in actions:
            # Escape quotes in description
            desc = action["desc"].replace('"', '\\"')
            yaml_lines.append(f'  - "desc": "{desc}"')
            yaml_lines.append(f'    "name": "{action["name"]}"')
    
    yaml_lines.append('"source":')
    yaml_lines.append('  - "GMOA"')
    yaml_lines.append('```')
    yaml_lines.append('^statblock')
    
    statblock_yaml = "\n".join(yaml_lines)
    
    return remaining_text, statblock_yaml

# Known table names that get corrupted by PDF extraction
# Maps the corrupted version (after control char removal) to the actual name
TABLE_NAMES = {
    "T ' B": "Thassa's Blessings",
    "T  ' B": "Thassa's Blessings",
    "T' B": "Thassa's Blessings",
    "T  '  B": "Thassa's Blessings",
    "T A": "Truths of Atris",
    "T  A": "Truths of Atris",
    # Add more as we discover them
}

# Fragments of corrupted table names that should be removed
TABLE_NAME_FRAGMENTS = ["T", "'", "' B", "B", "A"]

def format_tables(text: str) -> str:
    """
    Detect and format tables in the description.
    Tables in the PDF follow pattern: Table Name, dice column (d4/d6/etc), Effect, then numbered rows.
    Uses double newlines to preserve table as separate block during paragraph joining.
    """
    lines = text.split("\n")
    result_lines = []
    i = 0
    
    while i < len(lines):
        line = lines[i].strip()
        
        # Check if this might be the start of a table
        # Look for a line that's just a dice type followed by a column header (Effect, Response, etc.)
        if i + 1 < len(lines) and re.match(r"^d\d+$|^d\d{2,3}$", line):
            next_line = lines[i + 1].strip()
            if next_line in ["Effect", "Response"]:
                column_header = next_line
                # Found a table! Look backwards for table name
                table_name = None
                lines_to_remove = 0
                
                if result_lines:
                    # Check if previous line(s) might be table name or fragments
                    # Table names are often split across lines with control chars
                    potential_name_parts = []
                    for j in range(min(8, len(result_lines))):
                        potential_part = result_lines[-(j+1)].strip()
                        if potential_part:
                            # Check if this is a known fragment
                            if potential_part in TABLE_NAME_FRAGMENTS:
                                potential_name_parts.insert(0, potential_part)
                                lines_to_remove = j + 1
                            # Check combined parts against known names
                            combined = " ".join(potential_name_parts).strip()
                            if combined in TABLE_NAMES:
                                table_name = TABLE_NAMES[combined]
                                break
                
                # If no table name found, use default
                if not table_name:
                    table_name = "Table"
                
                # Always try to remove fragment lines even if we didn't find table name
                # Look for isolated single-letter or short fragment lines
                if lines_to_remove == 0:
                    for j in range(min(5, len(result_lines))):
                        potential_part = result_lines[-(j+1)].strip()
                        if potential_part in TABLE_NAME_FRAGMENTS or (len(potential_part) <= 3 and potential_part):
                            lines_to_remove = j + 1
                        elif potential_part:
                            break
                
                # Remove corrupted table name lines
                if lines_to_remove > 0:
                    result_lines = result_lines[:-lines_to_remove]
                
                dice = line  # e.g., "d4"
                
                # Now collect the table rows
                table_rows = []
                i += 2  # Skip dice and "Effect" lines
                
                while i < len(lines):
                    row_line = lines[i].strip()
                    # Check if this is a row number (1, 2, 3, etc. or ranges like 1-2, 01-10)
                    row_match = re.match(r"^(\d+(?:-\d+)?)\s*$", row_line)
                    if row_match:
                        row_num = row_match.group(1)
                        # Collect the description for this row (could be multiple lines)
                        row_desc_parts = []
                        i += 1
                        while i < len(lines):
                            desc_line = lines[i].strip()
                            # Stop if we hit another number or end of table indicators
                            if re.match(r"^\d+(?:-\d+)?$", desc_line):
                                break
                            if desc_line.startswith("Overpaid.") or desc_line.startswith("Paid.") or desc_line.startswith("Curse."):
                                break
                            if not desc_line:
                                i += 1
                                break
                            row_desc_parts.append(desc_line)
                            i += 1
                        
                        row_desc = " ".join(row_desc_parts)
                        table_rows.append((row_num, row_desc))
                    else:
                        # Not a row number, table has ended
                        break
                
                # Format as markdown table with double newlines before and after
                # This ensures it stays as a separate "paragraph" and doesn't get joined
                table_md = [
                    "",  # Empty line before
                    "",  # Another empty line (will become double newline)
                    f"**{table_name}**",
                    "",
                    f"| {dice} | {column_header} |",
                    "| --- | --- |"
                ]
                for row_num, row_desc in table_rows:
                    table_md.append(f"| {row_num} | {row_desc} |")
                table_md.append("")  # Empty line after
                table_md.append("")  # Another empty line
                
                result_lines.extend(table_md)
                continue  # Don't increment i again, already positioned
        
        result_lines.append(lines[i])
        i += 1
    
    return "\n".join(result_lines)

def create_item_markdown(name: str, header: str, description: str, price_line: str = None) -> str:
    """Create markdown content for an item."""
    item_type, rarity, attunement = parse_item_header(header)
    
    # Build tags
    tags = [SOURCE_TAG]
    if attunement:
        tags.append("ttrpg-cli/item/attunement/required")
    tags.append(get_rarity_tag(rarity))
    tags.extend(get_item_type_tag(item_type))
    
    # Build frontmatter
    tags_yaml = "\n".join([f"- {tag}" for tag in tags])
    
    # Build header line
    if attunement:
        header_line = f"*{item_type}, {rarity} ({attunement})*"
    else:
        header_line = f"*{item_type}, {rarity}*"
    
    # Format price if present
    price_section = ""
    if price_line:
        # Clean up price line - remove leading dashes, "see card", etc.
        price_line = re.sub(r"^[—-]\s*", "", price_line)
        price_line = re.sub(r"see card\s*", "", price_line, flags=re.IGNORECASE)
        price_line = price_line.strip()
        if price_line:
            price_section = f"\n**Price:** {price_line}\n"
    
    # Clean up description
    description = description.strip()
    
    # Remove "— see card" or "- see card" or just "see card" from description
    description = re.sub(r"^[—-]?\s*see card\s*\n?", "", description, flags=re.IGNORECASE)
    description = re.sub(r"\n[—-]?\s*see card\s*", "\n", description, flags=re.IGNORECASE)
    
    # Fix common OCR/extraction issues
    description = re.sub(r"(\w)- (\w)", r"\1\2", description)  # Fix hyphenated words
    description = re.sub(r"\n{3,}", "\n\n", description)  # Remove excessive newlines
    
    # Remove duplicate item name at end of description (artifact from PDF layout)
    # Pattern: item name appearing on its own line near the end
    name_escaped = re.escape(name)
    description = re.sub(rf"\n{name_escaped}\s*\n*$", "", description, flags=re.IGNORECASE)
    # Also handle multi-line item names at end
    description = re.sub(r"\n[A-Z][a-z]+(?: [A-Za-z]+)*(?: of [A-Za-z]+)*\s*\n*$", "", description)
    
    # Remove random other item names that leaked in (from PDF column layout)
    # These appear as isolated lines with just an item name or image captions
    leaked_items = [
        "Sorrowful Lekythos", "Soul-Guide Lantern", "Nyx Lotus",
        r"Hammer of the Forged\s*\nof Purphoros", "Hammer of the Forged of Purphoros",
        "Fleetfeather Sandals", "Staff of Athreos", "Rings of Kynaios and Tiro",
        "Bident of Thassa's Beloved", "Sun Spear", "Archon Armor",
        "Gray Merchant's Mask",  # Image caption
    ]
    for leaked in leaked_items:
        description = re.sub(rf"\n{leaked}\s*", "\n", description)
    
    # Apply OCR fixes to description (strip control characters, fix common errors)
    description = fix_ocr_errors(description)
    
    # Detect and extract statblock BEFORE paragraph joining
    # Statblocks need line structure to be parsed properly
    statblock_yaml = None
    description, statblock_yaml = detect_and_extract_statblock(description)
    
    # Handle tables BEFORE paragraph joining
    # Tables look like: "Table Name\nd4/d6/etc\nEffect\n1\ntext\n2\ntext..."
    # Convert to markdown tables
    description = format_tables(description)
    
    # Join lines within paragraphs first (before adding headers)
    # Replace single newlines with spaces, keep double newlines as paragraph breaks
    description = re.sub(r"\n\n+", "\n\n", description)  # Normalize multiple newlines to exactly 2
    
    # Split by double newlines to get paragraphs
    paragraphs = description.split("\n\n")
    
    joined_paragraphs = []
    for para in paragraphs:
        # Don't join lines in tables (lines starting with | or table headers)
        if para.strip().startswith("|") or para.strip().startswith("| "):
            # This is a table block, preserve newlines
            joined_paragraphs.append(para)
        else:
            # Join single newlines within paragraph into spaces
            joined = re.sub(r"\n", " ", para)
            # Clean up multiple spaces
            joined = re.sub(r"  +", " ", joined).strip()
            joined_paragraphs.append(joined)
    
    description = "\n\n".join(joined_paragraphs)
    
    # Convert sections to headers (add newline after header)
    description = re.sub(r"^(Paid)\.\s*", r"## \1\n\n", description, flags=re.MULTILINE)
    description = re.sub(r"^(Overpaid)\.\s*", r"## \1\n\n", description, flags=re.MULTILINE)
    description = re.sub(r"^(Curse)\.\s*", r"## \1\n\n", description, flags=re.MULTILINE)
    description = re.sub(r"^(Story)\.\s*", r"## \1\n\n", description, flags=re.MULTILINE)
    description = re.sub(r"^(Destroying the [^.]+)\.\s*", r"## \1\n\n", description, flags=re.MULTILINE)
    
    # Also handle Paid/Overpaid that appear mid-paragraph (after joining)
    description = re.sub(r"\s+(Paid)\.\s+", r"\n\n## \1\n\n", description)
    description = re.sub(r"\s+(Overpaid)\.\s+", r"\n\n## \1\n\n", description)
    description = re.sub(r"\s+(Curse)\.\s+", r"\n\n## \1\n\n", description)
    description = re.sub(r"\s+(Story)\.\s+", r"\n\n## \1\n\n", description)
    # Handle "Destroying the X" that appears mid-paragraph
    description = re.sub(r"\s+(Destroying the [^.]+)\.\s+", r"\n\n## \1\n\n", description)
    
    # Clean trailing whitespace
    description = description.strip()
    
    # Build statblock section if present
    statblock_section = ""
    statblock_frontmatter = ""
    if statblock_yaml:
        statblock_section = f"\n{statblock_yaml}\n"
        statblock_frontmatter = "statblock: inline\n"
    
    markdown = f"""---
title: "{name}"
obsidianUIMode: preview
cssclasses: json5e-item
{statblock_frontmatter}tags:
{tags_yaml}
aliases: 
- "{name}"
---
# {name}
{header_line}
{price_section}
{description}
{statblock_section}
*Source: The Gray Merchant of Asphodel*
"""
    return markdown

def parse_items_from_text(text: str) -> list:
    """Parse items from the PDF text content."""
    items = []
    
    # Find Chapter 2 content - find ALL occurrences and use the right ones
    ch2_matches = list(re.finditer(r"CHAPTER 2[:\s]+THE GRAY MERCHANT", text, re.IGNORECASE))
    ch3_matches = list(re.finditer(r"CHAPTER 3[:\s]+RANDOM ROLL", text, re.IGNORECASE))
    
    if not ch2_matches:
        print("Could not find Chapter 2!")
        return items
    if not ch3_matches:
        print("Could not find Chapter 3!")
        return items
    
    # Use the LAST occurrence (actual chapter, not TOC)
    ch2_start = ch2_matches[-1].start()
    ch3_start = ch3_matches[-1].start()
    
    print(f"Chapter 2 starts at position {ch2_start}")
    print(f"Chapter 3 starts at position {ch3_start}")
    
    if ch3_start <= ch2_start:
        print("Error: Chapter 3 found before Chapter 2!")
        return items
    
    ch2_text = text[ch2_start:ch3_start]
    print(f"Chapter 2 text length: {len(ch2_text)} characters")
    
    # Item name patterns - ALL CAPS headers
    # Match item names that are all uppercase followed by description
    item_pattern = re.compile(
        r"^([A-Z][A-Z\s'''\-]+(?:\([^)]+\))?)\n"  # Item name in caps
        r"([^\n]+(?:item|Weapon|Armor|Potion|Ring|Rod|Staff|gear)[^\n]*)\n"  # Type/rarity line
        r"(?:Price:\s*([^\n]+)\n)?"  # Optional price line
        r"([\s\S]+?)(?=\n[A-Z][A-Z\s'''\-]{3,}\n[^\n]+(?:item|Weapon|Armor|Potion|Ring|Rod|Staff|gear)|\Z)",
        re.MULTILINE
    )
    
    # Simpler approach: split by known item headers
    item_headers = [
        "ADVENTURER'S PODIUM",
        "AKROAN ROCKING HORSE",
        "ALSEID'S GIFT",
        "ANVILWROUGHT RAPTOR",
        "ARCHON ARMOR",
        "ARCHON CAPE",
        "ARROWHEAD SHARD",
        "ASPECT ICONS",
        "DEER ICON",
        "DOLPHIN ICON",
        "DONKEY ICON",
        "DOVE ICON",
        "GORGON ICON",
        "HORSE ICON",
        "HYDRA ICON",
        "LAMPREY ICON",
        "MANTICORE ICON",
        "MONGOOSE ICON",
        "OWL ICON",
        "PEACOCK ICON",
        "PIG ICON",
        "SWAN ICON",
        "TORTOISE ICON",
        "VULTURE ICON",
        "WOLF ICON",
        "ASTRAL CORNUCOPIA",
        "BIDENT OF THASSA'S BELOVED",
        "BIDET OF THASSA",
        "BLADE OF HUBRIS",
        "BOUNTIFUL LEKYTHOS",
        "BOW OF NYLEA'S HUNTER",
        "CALLAPHE'S COMPASS",
        "CAP OF AUTHORITY",
        "CHAPPARAL GRASS",
        "CHORUS MASK",
        "CLAY OWL",
        "CONSPIRATOR'S WHISTLE",
        "CROWN OF ATRIS",
        "DIARY OF THRASIOS",
        "DRAGON TEETH",
        "DUST OF NYX",
        "ENTRANCING LYRE",
        "EUKLISIA OF EPHARA",
        "FLAMECAST WHEEL",
        "FLEETFEATHER SANDALS",
        "FLINT OF PHENAX",
        "FLOATING DRIFTWOOD",
        "FRAGMENT OF ANGER",
        "FRAGMENT OF JOY",
        "FRAGMENT OF MISERA",
        "FRUIT OF TIZERUS",
        "FUNERARY MASK",
        "GOLDEN FUNERAL MASK OF THE GRAY MERCHANT",
        "GOLDEN FUNERAL MASK OF ASPHODEL",
        "GOLDEN FUNERAL MASK OF ODUNOS",
        "GOLDEN FUNERAL MASKS OF THE PHALANX",
        "GOLDEN FUNERAL MASK OF THE PSEUDAMMA",
        "GRAY MERCHANT'S GOLD COIN",
        "HAMMER OF THE FORGED OF PURPHOROS",
        "HELIOD'S GLORY",
        "IRIDESCENT PEARL NECKLACE",
        "IROAN PLEDGE",
        "JUDGY GOLDEN APPLE",
        "KARAMETRAN SICKLE",
        "LAUREL WREATH",
        "LEONIN HAIRBRUSH",
        "LEONIN SNARE",
        "LIGHTNING DIADEM",
        "MELETIS AGORA LICENSE",
        "MIRROR OF ALIRIOS",
        "MIRROR SHIELD",
        "NYX LOTUS",
        "ORESKOS HERESY",
        "PHARIKA'S CURE",
        "PHARIKA'S LIBATION JAR",
        "PHOENIX FEATHER",
        "POTION OF PARADOX",
        "PROWLER'S HELM",
        "PYXIS OF PANDEMONIUM",
        "QUILL OF EPHARA",
        "RING OF ANAX",
        "RING OF CYMEDE",
        "RING OF PROMISED REUNION",
        "RINGS OF KYNAIOS AND TIRO",
        "ROD OF GALLIA",
        "ROD OF KERANOS",
        "SACRIFICIAL KNIFE",
        "SATYR'S PILOI",
        "SCARF OF ATHREOS",
        "SCRAP OF EPIC POETRY",
        "SETESSAN JOKE BASKET",
        "SETESSAN LASSO",
        "SIGILED STARFISH",
        "SKEIN OF SKOPHOS",
        "SORROWFUL LEKYTHOS",
        "SOUL-GUIDE LANTERN",
        "SPRINGLEAF DRUM",
        "STAFF OF ATHREOS",
        "STARLIT MANTLE",
        "STRAND OF ARASTA",
        "STUBBORN BOULDER",
        "SUN SPEAR",
        "TABLET OF OSTRACISM",
        "TELESCOPE",
        "TENDRIL OF ARIXMETHES",
        "THREE-HEADED COLLAR",
        "TRAVELER'S AMULET",
        "TRICKSTER'S COIN",
        "UNDYING ASPHODEL",
        "VAPORS OF THE ORACLE",
        "VASE OF TALES",
        "VEIL OF FAVOR",
        "WARHORN OF MOGIS",
        "WHIP OF EREBOS' AGENT",
        "WINGS OF HUBRIS",
        "WITCHES' EYE",
        "XEBEC OF KRUPHIX",
        "YOKE OF CAREFUL UNBURDENING",
        "ZEPHYR SADDLE",
    ]
    
    # Find each item in the text
    for i, header in enumerate(item_headers):
        # Normalize apostrophes for searching
        search_variants = [
            header,
            header.replace("'", "'"),
            header.replace("'", "'"),
            header.replace("'", "`"),
            header.replace("'", "'").replace("'", "'"),
        ]
        
        start_idx = -1
        matched_header = header
        
        # Special handling for ICON items (rarity in parentheses on same line)
        if header.endswith(" ICON") and header != "ASPECT ICONS":
            # Icons have format like "DEER ICON (Uncommon)"
            icon_pattern = re.compile(re.escape(header) + r"\s*\([^)]+\)")
            match = icon_pattern.search(ch2_text)
            if match:
                start_idx = match.start()
                matched_header = match.group()
        # Special handling for multi-line mask names
        elif "GOLDEN FUNERAL MASK" in header:
            # Try with line break after "OF THE" or "OF"
            variants_to_try = [
                header,
                header.replace("OF THE GRAY", "OF THE\nGRAY"),
                header.replace("OF THE PSEUDAMMA", "OF THE\nPSEUDAMMA"),
                header.replace("OF THE PHALANX", "OF THE\nPHALANX"),
                header.replace("MASKS OF THE PHALANX", "MASKS OF THE\nPHALANX"),
                header.replace("OF ASPHODEL", "OF\nASPHODEL"),
                header.replace("OF ODUNOS", "OF\nODUNOS"),
            ]
            for variant in variants_to_try:
                test_idx = ch2_text.find(variant)
                if test_idx != -1:
                    start_idx = test_idx
                    matched_header = variant
                    break
        # Special handling for HAMMER
        elif "HAMMER" in header:
            # Try original and variants with line breaks
            variants_to_try = [
                header,
                "HAMMER OF THE FORGED\nOF PURPHOROS",
                "HAMMER OF THE\nFORGED OF PURPHOROS",
                "HAMMER OF THE FORGED OF\nPURPHOROS",
            ]
            for variant in variants_to_try:
                test_idx = ch2_text.find(variant)
                if test_idx != -1:
                    start_idx = test_idx
                    matched_header = variant
                    break
        else:
            for variant in search_variants:
                start_idx = ch2_text.find(variant + "\n")
                if start_idx != -1:
                    matched_header = variant
                    break
        
        if start_idx == -1:
            print(f"Could not find: {header}")
            continue
        
        # Find the end (start of next item or end of chapter)
        end_idx = len(ch2_text)
        for j, next_header in enumerate(item_headers):
            if j <= i:
                continue
            # Try all apostrophe variants
            next_variants = [
                next_header,
                next_header.replace("'", "'"),
                next_header.replace("'", "'"),
                next_header.replace("'", "`"),
            ]
            
            # Add multi-line variants for mask names
            if "GOLDEN FUNERAL MASK" in next_header:
                next_variants.extend([
                    next_header.replace("OF THE GRAY", "OF THE\nGRAY"),
                    next_header.replace("OF THE PSEUDAMMA", "OF THE\nPSEUDAMMA"),
                    next_header.replace("OF THE PHALANX", "OF THE\nPHALANX"),
                    next_header.replace("MASKS OF THE PHALANX", "MASKS OF THE\nPHALANX"),
                    next_header.replace("OF ASPHODEL", "OF\nASPHODEL"),
                    next_header.replace("OF ODUNOS", "OF\nODUNOS"),
                ])
            
            for next_variant in next_variants:
                # Try with newline (normal items)
                next_start = ch2_text.find(next_variant + "\n", start_idx + len(matched_header))
                if next_start != -1 and next_start < end_idx:
                    end_idx = next_start
                    break
                # Also try finding variant at exact position (for multi-line names already ending with \n)
                if "\n" in next_variant:
                    next_start = ch2_text.find(next_variant, start_idx + len(matched_header))
                    if next_start != -1 and next_start < end_idx:
                        end_idx = next_start
                        break
                # Try with parenthesis (icons with rarity on same line)
                if next_variant.endswith(" ICON"):
                    next_start = ch2_text.find(next_variant + " (", start_idx + len(matched_header))
                    if next_start != -1 and next_start < end_idx:
                        end_idx = next_start
                        break
        
        item_text = ch2_text[start_idx:end_idx].strip()
        
        # Parse the item
        lines = item_text.split("\n")
        if len(lines) < 2:
            continue
        
        name = lines[0].strip()
        
        # Handle icon format: "DEER ICON (Uncommon)" - extract rarity from name
        icon_rarity = ""
        icon_match = re.match(r"(.+ICON)\s*\(([^)]+)\)", name)
        if icon_match:
            name = icon_match.group(1).strip()
            icon_rarity = icon_match.group(2).strip()
        
        # Handle multi-line names (for masks)
        if name.endswith(" OF THE") or name.endswith(" OF"):
            # Merge with next line if it continues the name
            if len(lines) > 1 and lines[1].isupper() and not any(x in lines[1].lower() for x in ["wondrous", "weapon", "armor", "price"]):
                name = name + " " + lines[1].strip()
                lines = [name] + lines[2:]  # Remove the merged line
        
        # Title case the name
        name = " ".join(word.capitalize() if word.lower() not in ["of", "the", "and", "a", "an"] else word.lower() 
                        for word in name.split())
        # Fix first word always capitalized
        words = name.split()
        if words:
            words[0] = words[0].capitalize()
            name = " ".join(words)
        
        # Find the type/rarity line
        type_line = ""
        price_line = ""
        desc_start = 1
        
        # For icons, construct type line from extracted rarity
        if icon_rarity:
            type_line = f"Wondrous item, {icon_rarity.lower()}"
            desc_start = 1
            # Check if next line is Price:
            if len(lines) > 1 and lines[1].startswith("Price:"):
                price_line = lines[1].replace("Price:", "").strip()
                desc_start = 2
        else:
            # Find the type line - may span multiple lines for complex attunement
            type_line_parts = []
            for idx, line in enumerate(lines[1:], start=1):
                line_lower = line.lower()
                # Check if this line starts a type declaration
                if not type_line_parts:
                    if any(x in line_lower for x in ["wondrous item", "weapon", "armor", "potion", "ring", "rod", "staff", "adventuring gear", "story,"]):
                        type_line_parts.append(line.strip())
                        desc_start = idx + 1
                        # Check if type line is complete (has both type and rarity)
                        has_rarity = any(r in line_lower for r in ["common", "uncommon", "rare", "very rare", "legendary", "artifact", "story"])
                        # Check if line ends with incomplete attunement
                        if "(requires" in line_lower and ")" not in line[line_lower.find("(requires"):]:
                            continue  # Need more lines
                        if has_rarity:
                            break
                else:
                    # Continue collecting type line parts
                    type_line_parts.append(line.strip())
                    desc_start = idx + 1
                    # Check if we've completed the type line
                    combined = " ".join(type_line_parts).lower()
                    has_rarity = any(r in combined for r in ["common", "uncommon", "rare", "very rare", "legendary", "artifact", "story"])
                    # Check if attunement clause is complete
                    if "(requires" in combined:
                        if ")" in combined[combined.find("(requires"):]:
                            break  # Attunement clause complete
                    elif has_rarity:
                        break
            
            type_line = " ".join(type_line_parts)
        
        # Skip past "see card" lines if present (including standalone "card" from line break)
        while desc_start < len(lines):
            if lines[desc_start].strip().lower() in ["see card", "— see card", "- see card", "card"]:
                desc_start += 1
            else:
                break
        
        # Check for price line - may span multiple lines
        if desc_start < len(lines) and lines[desc_start].startswith("Price:"):
            price_parts = [lines[desc_start].replace("Price:", "").strip()]
            desc_start += 1
            # Check if price continues on next line (e.g., "high\nsentimentality")
            while desc_start < len(lines):
                next_line = lines[desc_start].strip().lower()
                # Check if this is a continuation of price (contains sentimentality or similar)
                if next_line in ["sentimentality", "low sentimentality", "medium sentimentality", "high sentimentality"]:
                    price_parts.append(lines[desc_start].strip())
                    desc_start += 1
                elif next_line.endswith("sentimentality"):
                    price_parts.append(lines[desc_start].strip())
                    desc_start += 1
                    break
                else:
                    break
            price_line = " ".join(price_parts)
        
        description = "\n".join(lines[desc_start:]).strip()
        
        if type_line and description:
            items.append({
                "name": name,
                "header": type_line,
                "price": price_line,
                "description": description
            })
            print(f"Parsed: {name}")
    
    return items

def main():
    """Main conversion function."""
    print("Reading PDF text file...")
    
    if not PDF_TEXT_PATH.exists():
        print(f"Error: {PDF_TEXT_PATH} not found!")
        return
    
    with open(PDF_TEXT_PATH, "r", encoding="utf-8") as f:
        text = f.read()
    
    print(f"Read {len(text)} characters")
    
    # Normalize various apostrophe characters to standard single quote
    text = text.replace("\u2019", "'")  # Right single quote '
    text = text.replace("\u2018", "'")  # Left single quote '
    text = text.replace("\u0027", "'")  # Standard apostrophe (no-op, for clarity)
    text = text.replace("`", "'")  # Backtick
    text = text.replace("\u00e2\u0080\u0099", "'")  # Mangled UTF-8 for '
    text = text.replace("\u00e2\u0080\u0098", "'")  # Mangled UTF-8 for '
    
    # Remove page markers
    text = re.sub(r"=== PAGE \d+ ===\n\d*\n?", "", text)
    
    print(f"After cleanup: {len(text)} characters")
    
    # Debug: check for chapter markers
    if "CHAPTER 2" in text:
        print("Found 'CHAPTER 2' in text")
    if "CHAPTER 3" in text:
        print("Found 'CHAPTER 3' in text")
    
    print("Parsing items...")
    items = parse_items_from_text(text)
    
    print(f"\nFound {len(items)} items")
    
    # Create output directory if needed
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    
    # Write item files
    for item in items:
        filename = slugify(item["name"]) + ".md"
        filepath = OUTPUT_DIR / filename
        
        markdown = create_item_markdown(
            item["name"],
            item["header"],
            item["description"],
            item["price"]
        )
        
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(markdown)
        
        print(f"Created: {filename}")
    
    print(f"\nDone! Created {len(items)} item files in {OUTPUT_DIR}")

if __name__ == "__main__":
    main()
