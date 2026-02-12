"""
Matches GMOA item markdown files with artwork from the Assets folder based on name similarity.
Creates a report showing potential matches between items and images.
"""

import os
import re
from pathlib import Path
from difflib import SequenceMatcher
from collections import defaultdict

# Directories
ITEMS_DIR = Path(__file__).parent.parent / "content" / "Compendium" / "items"
ASSETS_DIR = Path(__file__).parent.parent / "content" / "Assets"
OUTPUT_FILE = Path(__file__).parent / "gmoa_artwork_matches.md"

def normalize_name(name: str) -> str:
    """
    Normalize a name for comparison by:
    - Converting to lowercase
    - Removing file extensions
    - Replacing underscores, hyphens, and spaces with a single space
    - Removing special characters and punctuation
    - Removing common words like 'of', 'the', 'a', 'an'
    """
    # Remove file extensions
    name = re.sub(r'\.(webp|png|jpg|jpeg|md)$', '', name, flags=re.IGNORECASE)
    
    # Convert to lowercase
    name = name.lower()
    
    # Replace separators with spaces
    name = re.sub(r'[_\-\s]+', ' ', name)
    
    # Remove possessive 's
    name = re.sub(r"'s\b", '', name)
    
    # Remove common filler words
    filler_words = ['of', 'the', 'a', 'an', 'and', 'in', 'on', 'at', 'to', 'for']
    words = name.split()
    words = [w for w in words if w not in filler_words]
    name = ' '.join(words)
    
    # Remove non-alphanumeric characters except spaces
    name = re.sub(r'[^a-z0-9\s]', '', name)
    
    # Remove extra spaces
    name = re.sub(r'\s+', ' ', name).strip()
    
    return name


def get_all_images():
    """Get all image files from the Assets directory with their paths."""
    images = []
    
    for root, dirs, files in os.walk(ASSETS_DIR):
        rel_root = Path(root).relative_to(ASSETS_DIR)
        for file in files:
            if file.lower().endswith(('.webp', '.png', '.jpg', '.jpeg')):
                images.append({
                    'filename': file,
                    'normalized': normalize_name(file),
                    'folder': str(rel_root),
                    'relative_path': str(rel_root / file)
                })
    
    return images


def get_gmoa_items():
    """Get all GMOA item markdown files."""
    items = []
    
    for file in ITEMS_DIR.glob('*-gmoa.md'):
        # Remove the -gmoa suffix for matching
        item_name = file.stem.replace('-gmoa', '')
        items.append({
            'filename': file.name,
            'item_name': item_name,
            'normalized': normalize_name(item_name),
            'path': file
        })
    
    return items


def similarity_score(s1: str, s2: str) -> float:
    """Calculate similarity between two strings (0.0 to 1.0)."""
    return SequenceMatcher(None, s1, s2).ratio()


def find_keyword_matches(item_normalized: str, image_normalized: str) -> list:
    """Find common keywords between item and image names."""
    item_words = set(item_normalized.split())
    image_words = set(image_normalized.split())
    return list(item_words & image_words)


def find_matches(items, images, threshold=0.6):
    """
    Find potential matches between items and images.
    Returns a dict mapping item names to lists of potential image matches.
    """
    matches = defaultdict(list)
    
    for item in items:
        item_matches = []
        
        for image in images:
            # Calculate similarity score
            score = similarity_score(item['normalized'], image['normalized'])
            
            # Find common keywords
            common_keywords = find_keyword_matches(item['normalized'], image['normalized'])
            
            # Consider it a match if:
            # 1. Similarity score is above threshold, OR
            # 2. There are 2+ common keywords (for multi-word items), OR
            # 3. There is 1 common keyword and it's 4+ characters (for specific names)
            is_match = False
            if score >= threshold:
                is_match = True
            elif len(common_keywords) >= 2:
                is_match = True
            elif len(common_keywords) == 1 and len(common_keywords[0]) >= 4:
                is_match = True
            
            if is_match:
                item_matches.append({
                    'image': image,
                    'score': score,
                    'keywords': common_keywords
                })
        
        # Sort by score (descending)
        item_matches.sort(key=lambda x: x['score'], reverse=True)
        
        if item_matches:
            matches[item['filename']] = {
                'item': item,
                'matches': item_matches
            }
    
    return matches


def generate_report(matches, images, items):
    """Generate a markdown report of the matches."""
    report_lines = []
    
    # Header
    report_lines.append("# GMOA Item to Artwork Matching Report\n")
    report_lines.append(f"**Generated**: {Path(__file__).name}\n")
    report_lines.append(f"**Total GMOA Items**: {len(items)}")
    report_lines.append(f"**Total Images**: {len(images)}")
    report_lines.append(f"**Items with Matches**: {len(matches)}")
    report_lines.append(f"**Items without Matches**: {len(items) - len(matches)}\n")
    
    # Summary statistics
    report_lines.append("## Summary Statistics\n")
    
    folder_counts = defaultdict(int)
    for image in images:
        folder_counts[image['folder']] += 1
    
    report_lines.append("### Images by Folder\n")
    for folder, count in sorted(folder_counts.items()):
        report_lines.append(f"- **{folder}**: {count} images")
    report_lines.append("")
    
    # Normalized lists
    report_lines.append("## Normalized Lists\n")
    
    report_lines.append("### All Images (Normalized)\n")
    report_lines.append("<details><summary>Click to expand</summary>\n")
    for image in sorted(images, key=lambda x: x['normalized']):
        report_lines.append(f"- `{image['normalized']}` → {image['relative_path']}")
    report_lines.append("</details>\n")
    
    report_lines.append("### All GMOA Items (Normalized)\n")
    report_lines.append("<details><summary>Click to expand</summary>\n")
    for item in sorted(items, key=lambda x: x['normalized']):
        report_lines.append(f"- `{item['normalized']}` → {item['filename']}")
    report_lines.append("</details>\n")
    
    # Matched items
    report_lines.append("## Matched Items\n")
    report_lines.append("Items with potential artwork matches, sorted by match quality.\n")
    
    for item_filename in sorted(matches.keys()):
        match_data = matches[item_filename]
        item = match_data['item']
        item_matches = match_data['matches']
        
        report_lines.append(f"### {item['item_name']}")
        report_lines.append(f"**File**: `{item_filename}`")
        report_lines.append(f"**Normalized**: `{item['normalized']}`")
        report_lines.append(f"**Potential Matches**: {len(item_matches)}\n")
        
        for i, match in enumerate(item_matches[:5], 1):  # Show top 5 matches
            img = match['image']
            report_lines.append(f"{i}. **{img['filename']}** (Score: {match['score']:.2f})")
            report_lines.append(f"   - Path: `Assets/{img['relative_path']}`")
            report_lines.append(f"   - Normalized: `{img['normalized']}`")
            if match['keywords']:
                report_lines.append(f"   - Common Keywords: {', '.join(match['keywords'])}")
            report_lines.append("")
        
        report_lines.append("")
    
    # Unmatched items
    unmatched_items = [item for item in items if item['filename'] not in matches]
    if unmatched_items:
        report_lines.append("## Unmatched Items\n")
        report_lines.append(f"**Count**: {len(unmatched_items)}\n")
        report_lines.append("<details><summary>Click to expand</summary>\n")
        for item in sorted(unmatched_items, key=lambda x: x['normalized']):
            report_lines.append(f"- **{item['item_name']}** (`{item['normalized']}`)")
        report_lines.append("</details>\n")
    
    return '\n'.join(report_lines)


def main():
    print("Scanning for images...")
    images = get_all_images()
    print(f"Found {len(images)} images")
    
    print("\nScanning for GMOA items...")
    items = get_gmoa_items()
    print(f"Found {len(items)} GMOA items")
    
    print("\nFinding matches...")
    matches = find_matches(items, images, threshold=0.7)
    print(f"Found matches for {len(matches)} items")
    
    print("\nGenerating report...")
    report = generate_report(matches, images, items)
    
    print(f"\nWriting report to {OUTPUT_FILE}...")
    OUTPUT_FILE.write_text(report, encoding='utf-8')
    
    print(f"\n✓ Report generated successfully!")
    print(f"  - Total items: {len(items)}")
    print(f"  - Items with matches: {len(matches)}")
    print(f"  - Items without matches: {len(items) - len(matches)}")
    print(f"\nOpen {OUTPUT_FILE.name} to view the results.")


if __name__ == "__main__":
    main()
