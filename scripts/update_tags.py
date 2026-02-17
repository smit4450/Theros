"""
Script to update tags in all markdown files:
- Remove 'compendium/' prefix from tags
- Change 'source/' prefix to 'src/'
"""

import os
import re
from pathlib import Path

def update_tags_in_file(file_path):
    """Update tags in a single markdown file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        
        # Replace compendium/src/ with src/
        content = content.replace('- compendium/src/', '- src/')
        content = content.replace('  - compendium/src/', '  - src/')
        
        # Replace source/ with src/
        content = content.replace('- source/', '- src/')
        content = content.replace('  - source/', '  - src/')
        
        # Only write if content changed
        if content != original_content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            return True
        return False
    except Exception as e:
        print(f"Error processing {file_path}: {e}")
        return False

def main():
    """Update tags in all markdown files in the content directory."""
    content_dir = Path(__file__).parent.parent / 'content'
    
    if not content_dir.exists():
        print(f"Content directory not found: {content_dir}")
        return
    
    updated_count = 0
    total_count = 0
    
    # Find all markdown files
    md_files = list(content_dir.rglob('*.md'))
    print(f"Found {len(md_files)} markdown files")
    
    for md_file in md_files:
        total_count += 1
        if update_tags_in_file(md_file):
            updated_count += 1
            print(f"Updated: {md_file.relative_to(content_dir)}")
    
    print(f"\nProcessed {total_count} files")
    print(f"Updated {updated_count} files")

if __name__ == '__main__':
    main()
