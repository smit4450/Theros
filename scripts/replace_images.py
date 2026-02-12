"""
Replace scryfall image links with local assets from the Assets directory.
"""

import os
import re
import shutil
from pathlib import Path
from difflib import SequenceMatcher


def slugify(text: str) -> str:
    """Convert text to a slug suitable for filenames."""
    text = text.lower()
    text = re.sub(r'[^\w\s-]', '', text)
    text = re.sub(r'[-\s]+', '-', text)
    return text.strip('-')


def similarity_ratio(a: str, b: str) -> float:
    """Calculate similarity between two strings."""
    return SequenceMatcher(None, a.lower(), b.lower()).ratio()


def normalize_name(name: str) -> str:
    """Normalize creature name for matching."""
    name = name.lower()
    # Remove punctuation but keep spaces
    name = re.sub(r'[^\w\s]', '', name)
    name = re.sub(r'\s+', ' ', name).strip()
    return name


def find_best_match(creature_name: str, asset_files: list) -> tuple:
    """Find best matching asset file for a creature."""
    best_match = None
    best_score = 0.0
    
    normalized_creature = normalize_name(creature_name)
    creature_words = set(normalized_creature.split())
    
    for asset_file in asset_files:
        # Get filename without extension
        asset_name = asset_file.stem
        normalized_asset = normalize_name(asset_name)
        
        # Check for exact match first (ignoring case and punctuation)
        if normalized_creature == normalized_asset:
            return asset_file, 1.0
        
        # Calculate string similarity
        string_similarity = similarity_ratio(normalized_creature, normalized_asset)
        
        # Calculate word overlap - all creature words must be in asset
        asset_words = set(normalized_asset.split())
        
        # Check if all significant words from creature name are in asset name
        if len(creature_words) > 0:
            words_in_asset = len(creature_words & asset_words)
            word_coverage = words_in_asset / len(creature_words)
        else:
            word_coverage = 0
        
        # Very strict scoring: require high string similarity AND good word coverage
        # Use minimum of both to ensure both criteria are met
        if word_coverage < 0.7:  # At least 70% of words must match
            score = 0
        else:
            score = min(string_similarity, word_coverage) * 0.5 + (string_similarity * word_coverage) * 0.5
        
        if score > best_score:
            best_score = score
            best_match = asset_file
    
    return best_match, best_score


def process_bestiary_files(repo_root: Path, assets_dir: Path, min_similarity: float = 0.85):
    """Process all bestiary markdown files and replace scryfall links."""
    
    # Get all asset files
    asset_files = list(assets_dir.rglob('*.webp')) + list(assets_dir.rglob('*.jpg')) + list(assets_dir.rglob('*.png'))
    print(f"Found {len(asset_files)} asset files")
    
    # Get all bestiary markdown files
    bestiary_dir = repo_root / 'content' / 'Compendium' / 'bestiary'
    md_files = list(bestiary_dir.rglob('*.md'))
    print(f"Found {len(md_files)} bestiary files\n")
    
    stats = {
        'processed': 0,
        'matched': 0,
        'no_scryfall': 0,
        'no_match': 0,
        'copied': 0,
        'updated': 0
    }
    
    for md_file in md_files:
        # Read the file
        with open(md_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Check if it has a scryfall link
        scryfall_match = re.search(r'!\[([^\]]+)\]\(https://img\.scryfall\.com/[^\)]+\)', content)
        
        if not scryfall_match:
            stats['no_scryfall'] += 1
            continue
        
        stats['processed'] += 1
        
        # Extract creature name from the markdown
        title_match = re.search(r'^title:\s*(.+)$', content, re.MULTILINE)
        if not title_match:
            print(f"  WARNING: No title found in {md_file.name}")
            continue
        
        creature_name = title_match.group(1).strip()
        
        # Remove source suffix from creature name for matching
        clean_name = re.sub(r'\s*\([A-Z]+\)$', '', creature_name)
        creature_name_for_matching = re.sub(r'\s*-\s*[a-z]+$', '', clean_name)
        
        # Find best matching asset
        best_asset, score = find_best_match(creature_name_for_matching, asset_files)
        
        if best_asset and score >= min_similarity:
            stats['matched'] += 1
            
            # Determine the creature type folder (parent directory name)
            type_folder = md_file.parent.name
            
            # Create img directory if it doesn't exist
            img_dir = md_file.parent / 'img'
            img_dir.mkdir(exist_ok=True)
            
            # Create destination filename (creature slug without source identifier)
            # Extract just the base name without the source suffix like -tbvi
            base_name = md_file.stem
            # Remove source suffix (like -tbvi, -tbvii, etc.)
            base_name = re.sub(r'-tbv[a-z]*$', '', base_name)
            dest_filename = f"{base_name}.webp"
            dest_path = img_dir / dest_filename
            
            # Copy the asset file
            try:
                shutil.copy2(best_asset, dest_path)
                stats['copied'] += 1
                print(f"✓ {creature_name}")
                print(f"  Matched: {best_asset.name} (score: {score:.2f})")
                print(f"  Copied to: {type_folder}/img/{dest_filename}")
            except Exception as e:
                print(f"  ERROR copying {best_asset.name}: {e}")
                continue
            
            # Update markdown file with new image path
            old_image_pattern = r'!\[([^\]]+)\]\(https://img\.scryfall\.com/[^\)]+\)'
            new_image_path = f"![{creature_name_for_matching}](Compendium/bestiary/{type_folder}/img/{dest_filename}#right)"
            
            new_content = re.sub(old_image_pattern, new_image_path, content)
            
            # Write updated content
            try:
                with open(md_file, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                stats['updated'] += 1
            except Exception as e:
                print(f"  ERROR updating {md_file.name}: {e}")
        else:
            stats['no_match'] += 1
            if best_asset:
                print(f"✗ {creature_name}")
                print(f"  Best match: {best_asset.name} (score: {score:.2f}) - below threshold")
            else:
                print(f"✗ {creature_name} - no match found")
    
    # Print summary
    print(f"\n{'='*60}")
    print("SUMMARY")
    print(f"{'='*60}")
    print(f"Total bestiary files: {len(md_files)}")
    print(f"Files with scryfall links: {stats['processed']}")
    print(f"Files without scryfall links: {stats['no_scryfall']}")
    print(f"Successfully matched: {stats['matched']}")
    print(f"No match found: {stats['no_match']}")
    print(f"Images copied: {stats['copied']}")
    print(f"Files updated: {stats['updated']}")
    print(f"{'='*60}")


def main():
    """Main function."""
    script_dir = Path(__file__).parent
    repo_root = script_dir.parent
    assets_dir = repo_root / 'content' / 'Assets'
    
    print(f"Repository root: {repo_root}")
    print(f"Assets directory: {assets_dir}")
    print()
    
    if not assets_dir.exists():
        print(f"ERROR: Assets directory not found: {assets_dir}")
        return
    
    process_bestiary_files(repo_root, assets_dir, min_similarity=0.85)


if __name__ == '__main__':
    main()
