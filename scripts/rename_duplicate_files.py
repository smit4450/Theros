"""
Script to rename duplicate files according to a consistent naming strategy.
This fixes wikilink resolution issues in Quartz.

Strategy:
1. Index files: Rename to parent directory name (e.g., crafting/index.md → crafting/crafting.md)
2. Legendary groups: Add '-legendary' before source suffix
3. Rules vs Spells: Add '-rules' or '-table' to rules/tables versions
4. Items in multiple categories: Add category descriptor
5. Book chapters: Add book abbreviation prefix
"""

import os
import re
from pathlib import Path
from collections import defaultdict

# Define the renaming mappings based on the strategy
RENAME_MAPPINGS = {
    # Index files - rename to parent directory name
    r"Compendium[/\\]crafting[/\\]index\.md$": 
        r"Compendium/crafting/crafting.md",
    r"Compendium[/\\]crafting[/\\]enchantments[/\\]index\.md$": 
        r"Compendium/crafting/enchantments/enchantments.md",
    r"Compendium[/\\]crafting[/\\]enchantments[/\\]armor[/\\]index\.md$": 
        r"Compendium/crafting/enchantments/armor/armor.md",
    r"Compendium[/\\]crafting[/\\]enchantments[/\\]universal[/\\]index\.md$": 
        r"Compendium/crafting/enchantments/universal/universal.md",
    r"Compendium[/\\]crafting[/\\]enchantments[/\\]weapon[/\\]index\.md$": 
        r"Compendium/crafting/enchantments/weapon/weapon.md",
    r"Compendium[/\\]crafting[/\\]forging[/\\]index\.md$": 
        r"Compendium/crafting/forging/forging.md",
    
    # Legendary groups - add '-legendary' suffix
    r"Compendium[/\\]bestiary[/\\]legendary-group[/\\]aboleth-xmm\.md$": 
        r"Compendium/bestiary/legendary-group/aboleth-legendary-xmm.md",
    r"Compendium[/\\]bestiary[/\\]legendary-group[/\\]beholder-xmm\.md$": 
        r"Compendium/bestiary/legendary-group/beholder-legendary-xmm.md",
    r"Compendium[/\\]bestiary[/\\]legendary-group[/\\]unicorn-xmm\.md$": 
        r"Compendium/bestiary/legendary-group/unicorn-legendary-xmm.md",
    r"Compendium[/\\]bestiary[/\\]legendary-group[/\\]shadow-dragon-xmm\.md$": 
        r"Compendium/bestiary/legendary-group/shadow-dragon-legendary-xmm.md",
    r"Compendium[/\\]bestiary[/\\]legendary-group[/\\]arch-hag-xmm\.md$": 
        r"Compendium/bestiary/legendary-group/arch-hag-legendary-xmm.md",
    r"Compendium[/\\]bestiary[/\\]legendary-group[/\\]death-tyrant-xmm\.md$": 
        r"Compendium/bestiary/legendary-group/death-tyrant-legendary-xmm.md",
    r"Compendium[/\\]bestiary[/\\]legendary-group[/\\]demilich-xmm\.md$": 
        r"Compendium/bestiary/legendary-group/demilich-legendary-xmm.md",
    r"Compendium[/\\]bestiary[/\\]legendary-group[/\\]dracolich-xmm\.md$": 
        r"Compendium/bestiary/legendary-group/dracolich-legendary-xmm.md",
    r"Compendium[/\\]bestiary[/\\]legendary-group[/\\]lich-xmm\.md$": 
        r"Compendium/bestiary/legendary-group/lich-legendary-xmm.md",
    r"Compendium[/\\]bestiary[/\\]legendary-group[/\\]mummy-lord-xmm\.md$": 
        r"Compendium/bestiary/legendary-group/mummy-lord-legendary-xmm.md",
    r"Compendium[/\\]bestiary[/\\]legendary-group[/\\]vampire-xmm\.md$": 
        r"Compendium/bestiary/legendary-group/vampire-legendary-xmm.md",
    r"Compendium[/\\]bestiary[/\\]legendary-group[/\\]kraken-xmm\.md$": 
        r"Compendium/bestiary/legendary-group/kraken-legendary-xmm.md",
    r"Compendium[/\\]bestiary[/\\]legendary-group[/\\]arasta-mot\.md$": 
        r"Compendium/bestiary/legendary-group/arasta-legendary-mot.md",
    r"Compendium[/\\]bestiary[/\\]legendary-group[/\\]hythonia-mot\.md$": 
        r"Compendium/bestiary/legendary-group/hythonia-legendary-mot.md",
    r"Compendium[/\\]bestiary[/\\]legendary-group[/\\]tromokratis-mot\.md$": 
        r"Compendium/bestiary/legendary-group/tromokratis-legendary-mot.md",
    
    # Rules vs Spells - add '-rules' to rules, keep spells unchanged
    r"Compendium[/\\]rules[/\\]variant-rules[/\\]cover-xphb\.md$": 
        r"Compendium/rules/variant-rules/cover-rules-xphb.md",
    r"Compendium[/\\]rules[/\\]variant-rules[/\\]darkness-xphb\.md$": 
        r"Compendium/rules/variant-rules/darkness-rules-xphb.md",
    r"Compendium[/\\]rules[/\\]variant-rules[/\\]resistance-xphb\.md$": 
        r"Compendium/rules/variant-rules/resistance-rules-xphb.md",
    r"Compendium[/\\]rules[/\\]variant-rules[/\\]telepathy-xphb\.md$": 
        r"Compendium/rules/variant-rules/telepathy-rules-xphb.md",
    r"Compendium[/\\]rules[/\\]variant-rules[/\\]explosives-xdmg\.md$": 
        r"Compendium/rules/variant-rules/explosives-rules-xdmg.md",
    r"Compendium[/\\]rules[/\\]variant-rules[/\\]firearms-xdmg\.md$": 
        r"Compendium/rules/variant-rules/firearms-rules-xdmg.md",
    
    # Tables with duplicate names - add '-table' suffix
    r"Compendium[/\\]tables[/\\]cover-xphb\.md$": 
        r"Compendium/tables/cover-table-xphb.md",
    r"Compendium[/\\]tables[/\\]explosives-xdmg\.md$": 
        r"Compendium/tables/explosives-table-xdmg.md",
    r"Compendium[/\\]tables[/\\]firearms-xdmg\.md$": 
        r"Compendium/tables/firearms-table-xdmg.md",
    
    # Decks - add '-cards' to deck folder versions
    r"Compendium[/\\]decks[/\\]deck-of-illusions-xdmg\.md$": 
        r"Compendium/decks/deck-of-illusions-cards-xdmg.md",
    r"Compendium[/\\]decks[/\\]deck-of-many-things-xdmg\.md$": 
        r"Compendium/decks/deck-of-many-things-cards-xdmg.md",
    
    # Vehicles - add '-vehicle' suffix
    r"Compendium[/\\]vehicles[/\\]apparatus-of-kwalish-xdmg\.md$": 
        r"Compendium/vehicles/apparatus-of-kwalish-vehicle-xdmg.md",
    
    # Book credits - add book prefix
    r"Compendium[/\\]books[/\\]dungeon-masters-guide-2024[/\\]12-credits\.md$": 
        r"Compendium/books/dungeon-masters-guide-2024/dmg-12-credits.md",
    r"Compendium[/\\]books[/\\]players-handbook-2024[/\\]12-credits\.md$": 
        r"Compendium/books/players-handbook-2024/phb-12-credits.md",
    
    # Oracle NPC - add '-npc' suffix
    r"Compendium[/\\]bestiary[/\\]humanoid[/\\]oracle-mot\.md$": 
        r"Compendium/bestiary/humanoid/oracle-npc-mot.md",
    
    # Giant Insect spell vs bestiary - add '-spell' to spell
    r"Compendium[/\\]spells[/\\]giant-insect-xphb\.md$": 
        r"Compendium/spells/giant-insect-spell-xphb.md",
}


def normalize_path(path):
    """Normalize path for comparison (use forward slashes)."""
    return str(path).replace('\\', '/')


def get_rename_plan(content_dir):
    """
    Generate a rename plan based on the mappings.
    
    Returns:
        list of tuples: (old_path, new_path)
    """
    rename_plan = []
    
    for old_pattern, new_path_template in RENAME_MAPPINGS.items():
        # Search for files matching the pattern
        pattern_regex = re.compile(old_pattern, re.IGNORECASE)
        
        for root, dirs, files in os.walk(content_dir):
            for file in files:
                if file.endswith('.md'):
                    full_path = os.path.join(root, file)
                    rel_path = os.path.relpath(full_path, content_dir)
                    normalized_rel = normalize_path(rel_path)
                    
                    if pattern_regex.search(normalized_rel):
                        # Construct new path
                        new_rel_path = new_path_template
                        new_full_path = os.path.join(content_dir, new_rel_path.replace('/', os.sep))
                        
                        rename_plan.append((full_path, new_full_path))
                        break
    
    return rename_plan


def create_wikilink_mapping(rename_plan):
    """
    Create a mapping of old wikilink names to new wikilink names.
    
    Returns:
        dict: {old_wikilink: new_wikilink}
    """
    wikilink_map = {}
    
    for old_path, new_path in rename_plan:
        # Extract filename without extension
        old_name = Path(old_path).stem
        new_name = Path(new_path).stem
        
        if old_name != new_name:
            wikilink_map[old_name] = new_name
    
    return wikilink_map


def update_wikilinks_in_file(file_path, wikilink_map):
    """
    Update wikilinks in a markdown file.
    
    Args:
        file_path: Path to the markdown file
        wikilink_map: Dictionary mapping old names to new names
    
    Returns:
        int: Number of replacements made
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        replacements = 0
        
        # Update wikilinks [[old_name]] to [[new_name]]
        # Also handle [[old_name|display text]] to [[new_name|display text]]
        for old_name, new_name in wikilink_map.items():
            # Pattern 1: [[old_name]]
            pattern1 = rf'\[\[{re.escape(old_name)}\]\]'
            replacement1 = f'[[{new_name}]]'
            new_content = re.sub(pattern1, replacement1, content)
            if new_content != content:
                replacements += content.count(f'[[{old_name}]]')
                content = new_content
            
            # Pattern 2: [[old_name|display]]
            pattern2 = rf'\[\[{re.escape(old_name)}\|([^\]]+)\]\]'
            replacement2 = rf'[[{new_name}|\1]]'
            new_content = re.sub(pattern2, replacement2, content)
            if new_content != content:
                replacements += len(re.findall(pattern2, content))
                content = new_content
        
        # Only write if changes were made
        if content != original_content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            return replacements
        
        return 0
    
    except Exception as e:
        print(f"  ⚠️  Error updating {file_path}: {e}")
        return 0


def update_all_wikilinks(content_dir, wikilink_map):
    """
    Update all wikilinks in all markdown files in the content directory.
    
    Returns:
        tuple: (files_updated, total_replacements)
    """
    files_updated = 0
    total_replacements = 0
    
    print("\n📝 Updating wikilinks in all markdown files...")
    print("=" * 80)
    
    for root, dirs, files in os.walk(content_dir):
        # Skip hidden directories
        dirs[:] = [d for d in dirs if not d.startswith('.')]
        
        for file in files:
            if file.endswith('.md'):
                file_path = os.path.join(root, file)
                replacements = update_wikilinks_in_file(file_path, wikilink_map)
                
                if replacements > 0:
                    files_updated += 1
                    total_replacements += replacements
                    rel_path = os.path.relpath(file_path, content_dir)
                    print(f"  ✓ {rel_path}: {replacements} link(s) updated")
    
    return files_updated, total_replacements


def perform_renames(rename_plan, dry_run=True):
    """
    Perform the actual file renames.
    
    Args:
        rename_plan: List of (old_path, new_path) tuples
        dry_run: If True, only print what would be done
    
    Returns:
        int: Number of files renamed
    """
    renamed_count = 0
    
    print("\n📋 Rename Plan:")
    print("=" * 80)
    
    for old_path, new_path in rename_plan:
        old_name = os.path.basename(old_path)
        new_name = os.path.basename(new_path)
        old_dir = os.path.dirname(old_path)
        
        print(f"\n  {old_name} → {new_name}")
        print(f"    Location: {old_dir}")
        
        if not dry_run:
            try:
                # Ensure target directory exists
                os.makedirs(os.path.dirname(new_path), exist_ok=True)
                
                # Rename the file
                os.rename(old_path, new_path)
                renamed_count += 1
                print("    ✓ Renamed")
            except Exception as e:
                print(f"    ✗ Error: {e}")
        else:
            print("    [DRY RUN - no changes made]")
    
    return renamed_count


def main():
    import sys
    
    # Get the content directory
    script_dir = Path(__file__).parent
    project_root = script_dir.parent
    content_dir = project_root / "content"
    
    if not content_dir.exists():
        print(f"Error: Content directory not found at {content_dir}")
        return
    
    # Check if dry run mode
    dry_run = '--execute' not in sys.argv
    
    print("=" * 80)
    print("DUPLICATE FILE RENAMING SCRIPT")
    print("=" * 80)
    print(f"\nContent directory: {content_dir}")
    print(f"Mode: {'DRY RUN (use --execute to apply changes)' if dry_run else 'EXECUTE'}")
    
    # Generate rename plan
    rename_plan = get_rename_plan(content_dir)
    
    if not rename_plan:
        print("\n✓ No files need to be renamed!")
        return
    
    print(f"\nFound {len(rename_plan)} file(s) to rename")
    
    # Perform renames
    renamed_count = perform_renames(rename_plan, dry_run)
    
    if not dry_run:
        print("\n" + "=" * 80)
        print(f"✓ Successfully renamed {renamed_count} file(s)")
        
        # Update wikilinks
        wikilink_map = create_wikilink_mapping(rename_plan)
        files_updated, total_replacements = update_all_wikilinks(content_dir, wikilink_map)
        
        print("\n" + "=" * 80)
        print("WIKILINK UPDATE SUMMARY")
        print("=" * 80)
        print(f"Files with updated links: {files_updated}")
        print(f"Total link updates: {total_replacements}")
        print("\n✓ All done!")
    else:
        print("\n" + "=" * 80)
        print("DRY RUN COMPLETE - No changes were made")
        print("Run with --execute flag to apply these changes")
        print("=" * 80)


if __name__ == "__main__":
    main()
