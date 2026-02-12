"""
Convert 5etools JSON creature files to markdown format for the bestiary.
"""

import json
import os
import re
from pathlib import Path
from typing import Dict, List, Any, Optional


# Map volume names to abbreviations
VOLUME_MAP = {
    "Vol. I": "TBVI",
    "Vol. II": "TBVII",
    "Vol. III": "TBVIII",
    "Vol. IV": "TBVIV",
    "Vol. V": "TBVV",
    "Vol. VI": "TBVVI",
    "Vol. VII": "TBVVII",
    "Vol. VIII": "TBVVIII",
    "Vol. IX": "TBVIX",
    "Vol. X": "TBVX",
    "Vol. XI": "TBVXI",
    "Vol. XII": "TBVXII",
    "Vol. XIII": "TBVXIII",
    "Vol. XIV": "TBVXIV",
    "Vol. XV": "TBVXV",
    "Vol. XVI": "TBVXVI",
    "Vol. XVII": "TBVXVII",
    "Vol. XVIII": "TBVXVIII",
    "Vol. XIX": "TBVXIX",
    "Vol. XX": "TBVXX",
    "Vol. XXI": "TBVXXI",
    "Vol. XXII": "TBVXXII",
    "Vol. XXIII": "TBVXXIII",
    "Vol. XXIV": "TBVXXIV",
    "Vol. XXV": "TBVXXV",
}


def extract_volume_abbr(source: str) -> str:
    """Extract and convert volume number to abbreviation."""
    # Extract volume using regex to find Roman numerals after "Vol."
    import re
    match = re.search(r'Vol\.\s+([IVXL]+)', source)
    if match:
        vol_numeral = match.group(1)
        # Map Roman numerals to abbreviations
        roman_to_abbr = {
            'I': 'TBVI',
            'II': 'TBVII',
            'III': 'TBVIII',
            'IV': 'TBVIV',
            'V': 'TBVV',
            'VI': 'TBVVI',
            'VII': 'TBVVII',
            'VIII': 'TBVVIII',
            'IX': 'TBVIX',
            'X': 'TBVX',
            'XI': 'TBVXI',
            'XII': 'TBVXII',
            'XIII': 'TBVXIII',
            'XIV': 'TBVXIV',
            'XV': 'TBVXV',
            'XVI': 'TBVXVI',
            'XVII': 'TBVXVII',
            'XVIII': 'TBVXVIII',
            'XIX': 'TBVXIX',
            'XX': 'TBVXX',
            'XXI': 'TBVXXI',
            'XXII': 'TBVXXII',
            'XXIII': 'TBVXXIII',
            'XXIV': 'TBVXXIV',
            'XXV': 'TBVXXV',
        }
        return roman_to_abbr.get(vol_numeral, 'TBV')
    return "TBV"  # fallback


def slugify(text: str) -> str:
    """Convert text to a slug suitable for filenames."""
    text = text.lower()
    text = re.sub(r'[^\w\s-]', '', text)
    text = re.sub(r'[-\s]+', '-', text)
    return text.strip('-')


def format_ability_mod(score: Optional[int]) -> int:
    """Calculate ability modifier from score."""
    if score is None:
        return 0
    return (score - 10) // 2


def format_cr_tag(cr: str) -> str:
    """Format CR for tags."""
    cr_str = str(cr)
    if '/' in cr_str:
        return cr_str.replace('/', '-')
    return cr_str


def get_creature_type_folder(creature_type: Any) -> str:
    """Determine the folder based on creature type."""
    if isinstance(creature_type, dict):
        base_type = creature_type.get('type', 'miscellaneous')
    else:
        base_type = creature_type
    
    # Extract just the base type if there are multiple words
    base_type = str(base_type).lower().split()[0]
    
    # Map to valid folders
    valid_folders = {
        'aberration': 'aberration',
        'beast': 'beast',
        'celestial': 'celestial',
        'construct': 'construct',
        'dragon': 'dragon',
        'elemental': 'elemental',
        'fey': 'fey',
        'fiend': 'fiend',
        'giant': 'giant',
        'humanoid': 'humanoid',
        'monstrosity': 'monstrosity',
        'ooze': 'ooze',
        'plant': 'plant',
        'undead': 'undead',
    }
    
    return valid_folders.get(base_type, 'miscellaneous')


def format_type_and_subtype(creature_type: Any) -> tuple[str, Optional[str]]:
    """Extract type and subtype from creature type field."""
    if isinstance(creature_type, dict):
        base_type = creature_type.get('type', 'unknown')
        tags = creature_type.get('tags', [])
        if tags:
            subtype = ', '.join(str(t) for t in tags)
            return str(base_type), subtype
        return str(base_type), None
    else:
        return str(creature_type), None


def format_alignment(alignment: List[str]) -> str:
    """Format alignment from list to string."""
    if not alignment:
        return "Unaligned"
    
    align_map = {
        'L': 'Lawful',
        'N': 'Neutral',
        'C': 'Chaotic',
        'G': 'Good',
        'E': 'Evil',
        'U': 'Unaligned',
        'A': 'Any alignment'
    }
    
    parts = [align_map.get(a, a) for a in alignment]
    if len(parts) == 1:
        return parts[0]
    return ' '.join(parts)


def format_ac(ac_list: List[Dict]) -> tuple[str, Optional[str]]:
    """Format AC value and source."""
    if not ac_list:
        return "10", None
    
    ac_entry = ac_list[0]
    ac_value = str(ac_entry.get('ac', '10'))
    ac_from = ac_entry.get('from', [])
    
    if ac_from:
        ac_class = ', '.join(str(f).lower() for f in ac_from)
        return ac_value, ac_class
    return ac_value, None


def format_speed(speed: Dict) -> str:
    """Format speed dictionary to string."""
    if not speed:
        return "30 ft."
    
    parts = []
    for movement_type, value in speed.items():
        if movement_type == 'walk':
            parts.insert(0, f"{value} ft.")
        else:
            parts.append(f"{movement_type} {value} ft.")
    
    return ', '.join(parts)


def format_senses(senses: List[str], passive: int) -> str:
    """Format senses list to string."""
    sense_parts = []
    for sense in senses:
        sense_parts.append(sense)
    sense_parts.append(f"passive Perception {passive}")
    return ', '.join(sense_parts)


def format_languages(languages: List[str]) -> str:
    """Format languages list."""
    if not languages:
        return '""'
    lang_str = ', '.join(str(lang) for lang in languages)
    return f'"{lang_str}"'


def format_damage_list(damage_list: List[str]) -> str:
    """Format damage immunities/resistances/vulnerabilities."""
    if not damage_list:
        return '""'
    return ', '.join(str(d) for d in damage_list)


def format_condition_list(condition_list: List[str]) -> str:
    """Format condition immunities."""
    if not condition_list:
        return '""'
    return ', '.join(str(c) for c in condition_list)


def format_saves(saves: Dict, stats: Dict) -> Optional[List[Dict]]:
    """Format saving throw bonuses."""
    if not saves:
        return None
    
    save_list = []
    ability_map = {
        'str': 'strength',
        'dex': 'dexterity',
        'con': 'constitution',
        'int': 'intelligence',
        'wis': 'wisdom',
        'cha': 'charisma'
    }
    
    for ability, bonus in saves.items():
        full_name = ability_map.get(ability.lower(), ability)
        save_list.append(f'  - "{full_name}": !!int "{bonus}"')
    
    return save_list


def format_skills(skills: Dict) -> Optional[List[Dict]]:
    """Format skill bonuses."""
    if not skills:
        return None
    
    skill_list = []
    for skill_name, bonus in skills.items():
        # Convert snake_case to Title Case for linking
        display_name = skill_name.replace('_', ' ').title()
        skill_list.append({
            'name': f'[{display_name}](Compendium/rules/skills.md#{display_name})',
            'desc': f'+{bonus}' if isinstance(bonus, int) and bonus >= 0 else str(bonus)
        })
    
    return skill_list


def format_trait_entry(entry: str) -> str:
    """Format a trait/action entry, handling special formatting."""
    # Convert basic markdown-style formatting
    entry = entry.replace('<i>', '_').replace('</i>', '_')
    entry = entry.replace('<b>', '**').replace('</b>', '**')
    
    # Remove HTML tags that break YAML
    entry = re.sub(r'<li>', '- ', entry)
    entry = re.sub(r'</li>', '', entry)
    entry = re.sub(r'</?[^>]+>', '', entry)
    
    # Replace newlines with spaces to keep it on one line for YAML
    entry = entry.replace('\n', ' ')
    entry = re.sub(r'\s+', ' ', entry)
    
    # Escape quotes within the string
    entry = entry.replace('"', '\\"')
    
    return entry.strip()


def convert_creature_to_markdown(creature: Dict, source_abbr: str) -> str:
    """Convert a single creature JSON to markdown format."""
    name = creature.get('name', 'Unknown')
    size = creature.get('size', ['M'])[0] if creature.get('size') else 'M'
    
    # Size mapping
    size_map = {'T': 'Tiny', 'S': 'Small', 'M': 'Medium', 'L': 'Large', 'H': 'Huge', 'G': 'Gargantuan'}
    size_full = size_map.get(size, 'Medium')
    
    creature_type, subtype = format_type_and_subtype(creature.get('type', 'unknown'))
    alignment = format_alignment(creature.get('alignment', []))
    cr = creature.get('cr', '0')
    
    # Get tags
    type_folder = get_creature_type_folder(creature.get('type'))
    cr_tag = format_cr_tag(cr)
    
    # Environment tags (if available)
    environment = creature.get('environment', [])
    env_tags = []
    if environment and environment[0]:
        for env in environment:
            if env:
                env_tags.append(f'- ttrpg-cli/monster/environment/{slugify(env)}')
    
    # AC
    ac_value, ac_class = format_ac(creature.get('ac', []))
    
    # HP
    hp_avg = creature.get('hp', {}).get('average', 1)
    hp_formula = creature.get('hp', {}).get('formula', '1d8')
    
    # Speed
    speed = format_speed(creature.get('speed', {}))
    
    # Ability Scores
    str_score = creature.get('str', 10)
    dex_score = creature.get('dex', 10)
    con_score = creature.get('con', 10)
    int_score = creature.get('int', 10)
    wis_score = creature.get('wis', 10)
    cha_score = creature.get('cha', 10)
    
    # Calculate modifier for statblock
    dex_mod = format_ability_mod(dex_score)
    
    # Senses
    senses = creature.get('senses', [])
    passive = creature.get('passive', 10)
    senses_str = format_senses(senses, passive)
    
    # Languages
    languages = format_languages(creature.get('languages', []))
    
    # Saves and Skills
    saves = creature.get('save', {})
    skills = creature.get('skill', {})
    
    # Damage/Condition Immunities
    immune = format_damage_list(creature.get('immune', []))
    resist = format_damage_list(creature.get('resist', []))
    vulnerable = format_damage_list(creature.get('vulnerable', []))
    condition_immune = format_condition_list(creature.get('conditionImmune', []))
    
    # Build frontmatter
    slug = slugify(name)
    filename_slug = f"{slug}-{source_abbr.lower()}.md"
    
    frontmatter = f"""---
title: {name}
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- ttrpg-cli/compendium/src/5e/{source_abbr.lower()}
- ttrpg-cli/monster/cr/{cr_tag}
- ttrpg-cli/monster/size/{size.lower()}
- ttrpg-cli/monster/type/{type_folder}"""
    
    if env_tags:
        frontmatter += "\n" + "\n".join(env_tags)
    
    frontmatter += f"""
statblock: inline
aliases: ["{name}"]
---
"""
    
    # Build content section
    content = f"""# {name}
*Source: Theros Bestiary {source_abbr}*  
"""
    
    # Add fluff if available
    fluff = creature.get('fluff', {})
    if fluff:
        entries = fluff.get('entries', [])
        if entries:
            content += "\n"
            for entry in entries:
                if isinstance(entry, str):
                    content += f"{entry}\n\n"
        
        # Add image if available
        images = fluff.get('images', [])
        if images:
            img_url = images[0].get('href', {}).get('url', '')
            if img_url:
                content += f"![{name}]({img_url}#right)  \n\n"
    
    # Build statblock
    statblock = f"""```statblock
"name": "{name} ({source_abbr})"
"size": "{size_full}"
"type": "{creature_type}"
"""
    
    if subtype:
        statblock += f'"subtype": "{subtype}"\n'
    
    statblock += f""""alignment": "{alignment}"
"ac": !!int "{ac_value}"
"""
    
    if ac_class:
        statblock += f'"ac_class": "{ac_class}"\n'
    
    statblock += f""""hp": !!int "{hp_avg}"
"hit_dice": "{hp_formula}"
"modifier": !!int "{dex_mod}"
"stats":
  - !!int "{str_score}"
  - !!int "{dex_score}"
  - !!int "{con_score}"
  - !!int "{int_score}"
  - !!int "{wis_score}"
  - !!int "{cha_score}"
"speed": "{speed}"
"""
    
    # Add saves if present
    if saves:
        statblock += '"saves":\n'
        for ability, bonus in saves.items():
            ability_map = {
                'str': 'strength', 'dex': 'dexterity', 'con': 'constitution',
                'int': 'intelligence', 'wis': 'wisdom', 'cha': 'charisma'
            }
            full_name = ability_map.get(ability.lower(), ability)
            # Clean the bonus value - remove + prefix if present
            bonus_val = str(bonus).lstrip('+')
            statblock += f'  - "{full_name}": !!int "{bonus_val}"\n'
    
    # Add skills if present
    if skills:
        statblock += '"skillsaves":\n'
        for skill_name, bonus in skills.items():
            display_name = skill_name.replace('_', ' ').title()
            bonus_str = f'+{bonus}' if isinstance(bonus, int) and bonus >= 0 else str(bonus)
            statblock += f'  - "name": "[{display_name}](Compendium/rules/skills.md#{display_name})"\n'
            statblock += f'    "desc": "{bonus_str}"\n'
    
    # Add immunities/resistances
    if vulnerable and vulnerable != '""':
        statblock += f'"damage_vulnerabilities": "{vulnerable}"\n'
    if resist and resist != '""':
        statblock += f'"damage_resistances": "{resist}"\n'
    if immune and immune != '""':
        statblock += f'"damage_immunities": "{immune}"\n'
    if condition_immune and condition_immune != '""':
        statblock += f'"condition_immunities": "{condition_immune}"\n'
    
    statblock += f'"senses": "{senses_str}"\n'
    statblock += f'"languages": {languages}\n'
    statblock += f'"cr": "{cr}"\n'
    
    # Add traits
    traits = creature.get('trait', [])
    if traits:
        statblock += '"traits":\n'
        for trait in traits:
            trait_name = trait.get('name', 'Unknown')
            trait_entries = trait.get('entries', [])
            trait_desc = ' '.join(format_trait_entry(str(e)) for e in trait_entries)
            statblock += f'  - "desc": "{trait_desc}"\n'
            statblock += f'    "name": "{trait_name}"\n'
    
    # Add actions
    actions = creature.get('action', [])
    if actions:
        statblock += '"actions":\n'
        for action in actions:
            action_name = action.get('name', 'Unknown')
            action_entries = action.get('entries', [])
            action_desc = ' '.join(format_trait_entry(str(e)) for e in action_entries)
            statblock += f'  - "desc": "{action_desc}"\n'
            statblock += f'    "name": "{action_name}"\n'
    
    # Add reactions
    reactions = creature.get('reaction', [])
    if reactions:
        statblock += '"reactions":\n'
        for reaction in reactions:
            reaction_name = reaction.get('name', 'Unknown')
            reaction_entries = reaction.get('entries', [])
            reaction_desc = ' '.join(format_trait_entry(str(e)) for e in reaction_entries)
            statblock += f'  - "desc": "{reaction_desc}"\n'
            statblock += f'    "name": "{reaction_name}"\n'
    
    # Add legendary actions
    legendaries = creature.get('legendary', [])
    if legendaries:
        legendary_desc = creature.get('legendaryDescription', '')
        if legendary_desc:
            statblock += f'"legendary_description": "{legendary_desc}"\n'
        statblock += '"legendary_actions":\n'
        for legendary in legendaries:
            legendary_name = legendary.get('name', 'Unknown')
            legendary_entries = legendary.get('entries', [])
            legendary_desc = ' '.join(format_trait_entry(str(e)) for e in legendary_entries)
            statblock += f'  - "desc": "{legendary_desc}"\n'
            statblock += f'    "name": "{legendary_name}"\n'
    
    statblock += f'"source":\n  - "{source_abbr}"\n'
    statblock += f'"image": "Compendium/bestiary/{type_folder}/token/{slug}-{source_abbr.lower()}.webp"\n'
    statblock += '```\n^statblock'
    
    return frontmatter + content + statblock, filename_slug, type_folder


def process_json_file(json_path: Path, output_base: Path):
    """Process a single JSON file and create markdown files for all creatures."""
    print(f"Processing {json_path.name}...")
    
    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    # Extract source abbreviation
    meta = data.get('_meta', {})
    sources = meta.get('sources', [])
    source_name = sources[0].get('full', '') if sources else ''
    source_abbr = extract_volume_abbr(source_name)
    
    print(f"  Source: {source_name} -> {source_abbr}")
    
    # Process each monster
    monsters = data.get('monster', [])
    print(f"  Found {len(monsters)} creatures")
    
    created_files = []
    for monster in monsters:
        try:
            markdown, filename, type_folder = convert_creature_to_markdown(monster, source_abbr)
            
            # Create output directory
            output_dir = output_base / type_folder
            output_dir.mkdir(parents=True, exist_ok=True)
            
            # Write file
            output_file = output_dir / filename
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(markdown)
            
            created_files.append(str(output_file))
            print(f"    Created: {type_folder}/{filename}")
        except Exception as e:
            print(f"    ERROR processing {monster.get('name', 'Unknown')}: {e}")
    
    return created_files


def main():
    """Main conversion function."""
    # Setup paths
    script_dir = Path(__file__).parent
    repo_root = script_dir.parent
    input_dir = repo_root / 'content' / 'new_creatures'
    output_dir = repo_root / 'content' / 'Compendium' / 'bestiary'
    
    print(f"Input directory: {input_dir}")
    print(f"Output directory: {output_dir}")
    print()
    
    # Find all JSON files
    json_files = list(input_dir.glob('*.json'))
    print(f"Found {len(json_files)} JSON files to process\n")
    
    all_created_files = []
    for json_file in json_files:
        try:
            created = process_json_file(json_file, output_dir)
            all_created_files.extend(created)
        except Exception as e:
            print(f"ERROR processing file {json_file.name}: {e}")
        print()
    
    print(f"\nConversion complete!")
    print(f"Created {len(all_created_files)} creature files")


if __name__ == '__main__':
    main()
