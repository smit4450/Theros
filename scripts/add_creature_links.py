"""
Add markdown links to creature statblocks for conditions, spells, senses, and other game terms.
"""

import re
from pathlib import Path
from typing import Dict, Set


# Condition names to link
CONDITIONS = {
    'blinded': 'Blinded',
    'charmed': 'Charmed',
    'deafened': 'Deafened',
    'exhaustion': 'Exhaustion',
    'frightened': 'Frightened',
    'grappled': 'Grappled',
    'incapacitated': 'Incapacitated',
    'invisible': 'Invisible',
    'paralyzed': 'Paralyzed',
    'petrified': 'Petrified',
    'poisoned': 'Poisoned',
    'prone': 'Prone',
    'restrained': 'Restrained',
    'stunned': 'Stunned',
    'unconscious': 'Unconscious',
}

# Sense names to link
SENSES = {
    'blindsight': 'Blindsight',
    'darkvision': 'Darkvision',
    'tremorsense': 'Tremorsense',
    'truesight': 'Truesight',
}

# Rules concepts to link
RULES_CONCEPTS = {
    'hit points': ('variant-rules/hit-points-xphb.md', 'Hit Points'),
    'advantage': ('variant-rules/advantage-xphb.md', 'Advantage'),
    'disadvantage': ('variant-rules/disadvantage-xphb.md', 'Disadvantage'),
    'emanation': ('variant-rules/emanation-area-of-effect-xphb.md', 'Emanation'),
}

# Common spell patterns (lowercase for matching)
COMMON_SPELLS = [
    'animate dead', 'animate objects', 'antimagic field', 'augury', 
    'awaken', 'banishment', 'barkskin', 'beacon of hope', 'bestow curse',
    'bless', 'blight', 'blur', 'burning hands', 'calm emotions', 
    'chain lightning', 'charm person', 'chill touch', 'circle of death',
    'clairvoyance', 'cloudkill', 'color spray', 'command', 'compulsion', 
    'cone of cold', 'confusion', 'conjure animals', 'conjure celestial',
    'conjure elemental', 'conjure fey', 'conjure minor elementals',
    'continual flame', 'control water', 'control weather', 'counterspell',
    'create undead', 'creation', 'cure wounds', 'dancing lights',
    'darkness', 'daylight', 'death ward', 'delayed blast fireball',
    'detect evil and good', 'detect magic', 'detect poison or disease', 
    'detect thoughts', 'dimension door', 'disguise self', 'disintegrate',
    'dispel evil and good', 'dispel magic', 'divination', 'dominate beast',
    'dominate monster', 'dominate person', 'druidcraft', 'earthquake',
    'eldritch blast', 'entangle', 'enthrall', 'etherealness', 
    'expeditious retreat', 'eyebite', 'fabricate', 'faerie fire', 'false life',
    'fear', 'feather fall', 'feeblemind', 'find familiar', 'find steed',
    'find the path', 'find traps', 'finger of death', 'fire bolt', 
    'fire shield', 'fire storm', 'fireball', 'flame blade', 'flame strike',
    'flaming sphere', 'flesh to stone', 'fly', 'fog cloud', 'freedom of movement',
    'gate', 'geas', 'giant insect', 'globe of invulnerability', 'glyph of warding',
    'goodberry', 'grease', 'greater invisibility', 'greater restoration',
    'guardian of faith', 'guiding bolt', 'gust of wind', 'hallow',
    'hallucinatory terrain', 'harm', 'haste', 'heal', 'healing word',
    'heat metal', 'hellish rebuke', 'hex', 'hold monster',
    'hold person', 'holy aura', 'hunger of hadar', 'hypnotic pattern',
    'ice storm', 'identify', 'imprisonment', 'incendiary cloud', 'inflict wounds',
    'insect plague', 'invisibility', 'irresistible dance', 'jump',
    'knock', 'legend lore', 'lesser restoration', 'levitate', 'light',
    'lightning bolt', 'locate animals or plants', 'locate creature', 'locate object',
    'longstrider', 'mage armor', 'mage hand', 'magic circle', 'magic jar',
    'magic missile', 'magic weapon', 'major image', 'mass cure wounds',
    'mass heal', 'mass healing word', 'mass suggestion', 'maze', 'meld into stone',
    'mending', 'meteor swarm', 'mind blank', 'minor illusion', 'mirror image',
    'misty step', 'moonbeam', 'move earth', 'nondetection', 'pass without trace',
    'passwall', 'phantasmal killer', 'phantom steed', 'planar ally', 'planar binding',
    'plane shift', 'plant growth', 'polymorph', 'power word kill', 'power word stun',
    'prayer of healing', 'prestidigitation', 'prismatic spray', 'prismatic wall',
    'produce flame', 'project image', 'protection from energy', 'protection from evil and good',
    'protection from poison', 'raise dead', 'ray of enfeeblement', 'ray of frost',
    'regenerate', 'reincarnate', 'remove curse', 'resilient sphere', 'resistance',
    'resurrection', 'reverse gravity', 'revivify', 'rope trick', 'sacred flame',
    'sanctuary', 'scorching ray', 'scrying', 'see invisibility', 'seeming',
    'sending', 'sequester', 'shapechange', 'shatter', 'shield', 'shield of faith',
    'shillelagh', 'shocking grasp', 'silence', 'silent image', 'simulacrum',
    'sleep', 'sleet storm', 'slow', 'spare the dying', 'speak with animals',
    'speak with dead', 'speak with plants', 'spider climb', 'spike growth',
    'spirit guardians', 'spiritual weapon', 'stinking cloud', 'stone shape',
    'stoneskin', 'storm of vengeance', 'suggestion', 'sunbeam', 'sunburst',
    'symbol', 'telekinesis', 'telepathy', 'teleport', 'teleportation circle',
    'thaumaturgy', 'thorn whip', 'thunderwave', 'time stop', 'tongues',
    'transport via plants', 'tree stride', 'true polymorph', 'true resurrection',
    'true seeing', 'true strike', 'tsunami', 'unseen servant', 'vampiric touch',
    'vicious mockery', 'wall of fire', 'wall of force', 'wall of ice',
    'wall of stone', 'wall of thorns', 'warding bond', 'water breathing',
    'water walk', 'web', 'weird', 'wind walk', 'wind wall', 'wish',
    'word of recall', 'zone of truth', 'divine favor',
]


def slugify(text: str) -> str:
    """Convert spell name to slug."""
    text = text.lower()
    text = re.sub(r"['']", '', text)  # Remove apostrophes
    text = re.sub(r'[^\w\s-]', '', text)
    text = re.sub(r'[-\s]+', '-', text)
    return text.strip('-')


def link_conditions(text: str) -> str:
    """Add markdown links to condition names."""
    for condition_lower, condition_title in CONDITIONS.items():
        # Match whole words, case-insensitive
        pattern = r'\b' + condition_lower + r'\b'
        replacement = f'[{condition_lower}](Compendium/rules/conditions.md#{condition_title})'
        text = re.sub(pattern, replacement, text, flags=re.IGNORECASE)
    return text


def link_senses(text: str) -> str:
    """Add markdown links to sense names."""
    for sense_lower, sense_title in SENSES.items():
        # Match case-insensitive
        pattern = r'\b' + sense_lower + r'\b'
        replacement = f'[{sense_title}](Compendium/rules/senses.md#{sense_title})'
        text = re.sub(pattern, replacement, text, flags=re.IGNORECASE)
    return text


def link_spells_in_text(text: str) -> str:
    """Add markdown links to spell names in descriptions."""
    # Sort spells by length (longest first) to avoid partial matches
    sorted_spells = sorted(COMMON_SPELLS, key=len, reverse=True)
    
    for spell in sorted_spells:
        spell_slug = slugify(spell)
        spell_title = spell.title()
        
        # Pattern 1: _spell_ in markdown italic (already in italics)
        pattern_italic = r'_' + re.escape(spell) + r'_'
        replacement = f'[{spell_title}](Compendium/spells/{spell_slug}-xphb.md)'
        text = re.sub(pattern_italic, replacement, text, flags=re.IGNORECASE)
        
        # Pattern 2: plain spell names in spell lists
        # Match: "spell", spell followed by comma/period, or spell at end of line
        pattern_plain = r'\b(' + re.escape(spell) + r')(?=\s*[,.]|\s*$|\s+\d)'
        
        def replace_in_spell_context(match):
            return f'[{match.group(1).title()}](Compendium/spells/{spell_slug}-xphb.md)'
        
        # Only apply in lines that contain spellcasting indicators
        lines = text.split('\n')
        for i, line in enumerate(lines):
            # Check if this line is in a spell list context
            if any(indicator in line.lower() for indicator in ['innate', 'spellcasting', 'spell save', 'at will:', '/day', 'cantrip']):
                lines[i] = re.sub(pattern_plain, replace_in_spell_context, line, flags=re.IGNORECASE)
        text = '\n'.join(lines)
    
    return text


def link_rules_concepts(text: str) -> str:
    """Add markdown links to rules concepts."""
    for concept_lower, (path, display) in RULES_CONCEPTS.items():
        pattern = r'\b' + re.escape(concept_lower) + r'\b'
        replacement = f'[{display}](Compendium/rules/{path})'
        text = re.sub(pattern, replacement, text, flags=re.IGNORECASE)
    return text


def process_statblock(content: str) -> str:
    """Process a single creature file and add links."""
    lines = content.split('\n')
    in_statblock = False
    result_lines = []
    
    for line in lines:
        if line.strip().startswith('```statblock'):
            in_statblock = True
            result_lines.append(line)
            continue
        elif line.strip() == '```' and in_statblock:
            in_statblock = False
            result_lines.append(line)
            continue
        
        if in_statblock:
            # Process different parts of the statblock
            
            # Link conditions in condition_immunities
            if '"condition_immunities":' in line or '"condition_immune":' in line:
                line = link_conditions(line)
            
            # Link senses in senses field
            if '"senses":' in line:
                line = link_senses(line)
            
            # Link spells in trait/action descriptions
            if '"desc":' in line:
                line = link_spells_in_text(line)
                line = link_rules_concepts(line)
                line = link_conditions(line)
        
        result_lines.append(line)
    
    return '\n'.join(result_lines)


def process_file(filepath: Path) -> bool:
    """Process a single creature file. Returns True if modified."""
    try:
        content = filepath.read_text(encoding='utf-8')
        
        # Check if already has links (heuristic: check for condition links)
        if '[Compendium/rules/conditions.md#' in content:
            print(f"  Skipping {filepath.name} (already has links)")
            return False
        
        new_content = process_statblock(content)
        
        if new_content != content:
            filepath.write_text(new_content, encoding='utf-8')
            print(f"  Updated {filepath.name}")
            return True
        else:
            print(f"  No changes for {filepath.name}")
            return False
            
    except Exception as e:
        print(f"  ERROR processing {filepath.name}: {e}")
        return False


def main():
    """Main function to process all TBV creature files."""
    script_dir = Path(__file__).parent
    repo_root = script_dir.parent
    bestiary_dir = repo_root / 'content' / 'Compendium' / 'bestiary'
    
    print(f"Searching for TBV creature files in: {bestiary_dir}")
    print()
    
    # Find all TBV creature files
    tbv_files = list(bestiary_dir.glob('**/*-tbv*.md'))
    print(f"Found {len(tbv_files)} TBV creature files\n")
    
    modified_count = 0
    for filepath in sorted(tbv_files):
        if process_file(filepath):
            modified_count += 1
    
    print(f"\n{'='*60}")
    print(f"Processing complete!")
    print(f"Modified {modified_count} out of {len(tbv_files)} files")
    print(f"{'='*60}")


if __name__ == '__main__':
    main()
