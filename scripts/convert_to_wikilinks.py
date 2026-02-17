"""
Convert markdown-style links to wiki links for Quartz/Obsidian compatibility.
This converts all markdown links to .md files (both relative and absolute paths) into wikilinks.
This fixes path resolution issues where paths were being treated incorrectly.
"""

import re
from pathlib import Path
from typing import Dict, Set
from urllib.parse import unquote


def extract_filename_and_anchor(link_target: str) -> tuple[str, str | None]:
    """
    Extract filename (without .md) and anchor from a link target.
    
    Examples:
        'Compendium/rules/conditions.md#Charmed' -> ('conditions', 'Charmed')
        'Compendium/spells/fireball-xphb.md' -> ('fireball-xphb', None)
        'classes/sorcerer-xphb.md#Spellfire%20Burst%20(Level%203)' -> ('sorcerer-xphb', 'Spellfire Burst (Level 3)')
    """
    # Remove the .md extension and split on #
    parts = link_target.replace('.md', '').split('#')
    
    # Get just the filename from the path
    filename = parts[0].split('/')[-1]
    anchor = parts[1] if len(parts) > 1 else None
    
    # Decode URL-encoded characters in the anchor (e.g., %20 -> space)
    if anchor:
        anchor = unquote(anchor)
    
    return filename, anchor


def convert_markdown_link_to_wikilink(match: re.Match) -> str:
    """
    Convert a markdown link to a wiki link.
    
    [Display Text](path/to/file.md#anchor) -> [[file#anchor|Display Text]]
    [Display Text](path/to/file.md) -> [[file|Display Text]]
    """
    display_text = match.group(1)
    link_target = match.group(2)
    
    # Extract filename and anchor
    filename, anchor = extract_filename_and_anchor(link_target)
    
    # Build wiki link
    if anchor:
        wikilink = f'[[{filename}#{anchor}|{display_text}]]'
    else:
        wikilink = f'[[{filename}|{display_text}]]'
    
    return wikilink


def convert_file_links(content: str) -> str:
    """
    Convert all markdown links to .md files to wiki links in the content.
    """
    # Pattern to match markdown links ending in .md
    # Format: [text](path/to/file.md) or [text](./file.md#anchor) or [text](Compendium/path/to/file.md)
    # Uses (?:[^()]|\([^()]*\))* to allow balanced parentheses in the URL
    # (e.g., headings like "Spellfire Burst (Level 3)")
    pattern = r'\[([^\]]+)\]\(((?:[^()]|\([^()]*\))*\.md(?:#(?:[^()]|\([^()]*\))*)?)\)'
    
    # Replace all matches
    converted = re.sub(pattern, convert_markdown_link_to_wikilink, content)
    
    return converted


def process_file(filepath: Path) -> bool:
    """Process a single file. Returns True if modified."""
    try:
        content = filepath.read_text(encoding='utf-8')
        
        # Check if file has markdown links to .md files
        if '](' not in content or '.md' not in content:
            return False
        
        new_content = convert_file_links(content)
        
        if new_content != content:
            filepath.write_text(new_content, encoding='utf-8')
            print(f"  Converted links in {filepath.name}")
            return True
        else:
            return False
            
    except Exception as e:
        print(f"  ERROR processing {filepath.name}: {e}")
        return False


def main():
    """Main function to process all markdown files in content directory."""
    script_dir = Path(__file__).parent
    repo_root = script_dir.parent
    content_dir = repo_root / 'content'
    
    print(f"Converting markdown links to wiki links in: {content_dir}")
    print()
    
    # Find all markdown files in content directory
    md_files = list(content_dir.glob('**/*.md'))
    
    # Filter out .obsidian directory and other system files
    md_files = [f for f in md_files if '.obsidian' not in f.parts]
    
    print(f"Found {len(md_files)} markdown files\n")
    
    modified_count = 0
    for filepath in sorted(md_files):
        if process_file(filepath):
            modified_count += 1
    
    print(f"\n{'='*60}")
    print(f"Conversion complete!")
    print(f"Modified {modified_count} out of {len(md_files)} files")
    print(f"{'='*60}")


if __name__ == '__main__':
    main()
