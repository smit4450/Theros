"""
Script to find duplicate file names in the content directory.
This helps identify files that may cause wikilink resolution issues in Quartz.
"""

import os
from pathlib import Path
from collections import defaultdict

def find_duplicate_filenames(root_dir):
    """
    Find all files with duplicate names in the content directory.
    
    Returns:
        dict: Dictionary mapping filename to list of full paths
    """
    filename_map = defaultdict(list)
    
    # Walk through all files in content directory
    for root, dirs, files in os.walk(root_dir):
        # Skip hidden directories and node_modules
        dirs[:] = [d for d in dirs if not d.startswith('.') and d != 'node_modules']
        
        for file in files:
            # Only process markdown files
            if file.endswith('.md'):
                full_path = os.path.join(root, file)
                filename_map[file].append(full_path)
    
    # Filter to only duplicates
    duplicates = {name: paths for name, paths in filename_map.items() if len(paths) > 1}
    
    return duplicates

def print_duplicates(duplicates, content_dir):
    """Print duplicates in a readable format."""
    if not duplicates:
        print("No duplicate filenames found!")
        return
    
    print(f"Found {len(duplicates)} duplicate filename(s):\n")
    print("=" * 80)
    
    for filename, paths in sorted(duplicates.items()):
        print(f"\n📄 {filename} ({len(paths)} instances)")
        print("-" * 80)
        for path in sorted(paths):
            # Show relative path from content directory
            rel_path = os.path.relpath(path, content_dir)
            print(f"  • {rel_path}")
    
    print("\n" + "=" * 80)
    print(f"\nTotal: {len(duplicates)} duplicate filename(s)")
    print(f"Total files affected: {sum(len(paths) for paths in duplicates.values())}")

def analyze_duplicates(duplicates, content_dir):
    """Analyze duplicate patterns to suggest renaming strategies."""
    print("\n\n" + "=" * 80)
    print("ANALYSIS & SUGGESTIONS")
    print("=" * 80)
    
    # Group by category
    categories = defaultdict(list)
    
    for filename, paths in duplicates.items():
        # Analyze the parent directories
        parent_dirs = []
        for path in paths:
            rel_path = os.path.relpath(path, content_dir)
            parts = Path(rel_path).parts
            if len(parts) > 1:
                parent_dirs.append(parts[-2])  # Get immediate parent directory
            else:
                parent_dirs.append("(root)")
        
        # Check if duplicates are in different parent directories
        unique_parents = set(parent_dirs)
        if len(unique_parents) > 1:
            categories['different_folders'].append((filename, paths, parent_dirs))
        else:
            categories['same_folder'].append((filename, paths, parent_dirs))
    
    if categories['different_folders']:
        print("\n🔍 Files with same name in DIFFERENT folders:")
        print("-" * 80)
        for filename, paths, parent_dirs in categories['different_folders']:
            print(f"\n  {filename}")
            for path, parent in zip(paths, parent_dirs):
                rel_path = os.path.relpath(path, content_dir)
                print(f"    → {rel_path}")
        
        print("\n💡 Suggested Strategy:")
        print("  Rename files to include their parent directory or context:")
        print("  Example: 'index.md' → 'Backgrounds-index.md' or 'Compendium-index.md'")
        print("  Or use descriptive names based on content category.")
    
    if categories['same_folder']:
        print("\n🔍 Files with same name in SAME folder:")
        print("-" * 80)
        for filename, paths, parent_dirs in categories['same_folder']:
            print(f"\n  {filename}")
            for path in paths:
                rel_path = os.path.relpath(path, content_dir)
                print(f"    → {rel_path}")
        
        print("\n⚠️  Warning: Same filename in the same directory - this shouldn't happen!")
        print("   Please verify the file system.")

def main():
    # Get the content directory
    script_dir = Path(__file__).parent
    project_root = script_dir.parent
    content_dir = project_root / "content"
    
    if not content_dir.exists():
        print(f"Error: Content directory not found at {content_dir}")
        return
    
    print(f"Scanning for duplicate filenames in: {content_dir}\n")
    
    # Find duplicates
    duplicates = find_duplicate_filenames(content_dir)
    
    # Print results
    print_duplicates(duplicates, content_dir)
    
    # Analyze and suggest strategies
    if duplicates:
        analyze_duplicates(duplicates, content_dir)
    
    # Generate a detailed report file
    if duplicates:
        report_file = project_root / "duplicate_filenames_report.md"
        with open(report_file, 'w', encoding='utf-8') as f:
            f.write("# Duplicate Filenames Report\n\n")
            f.write(f"Generated: {os.path.basename(__file__)}\n\n")
            f.write(f"Total duplicate filenames: {len(duplicates)}\n\n")
            
            for filename, paths in sorted(duplicates.items()):
                f.write(f"## {filename}\n\n")
                for path in sorted(paths):
                    rel_path = os.path.relpath(path, content_dir)
                    f.write(f"- `{rel_path}`\n")
                f.write("\n")
        
        print(f"\n\n📝 Detailed report saved to: {report_file}")

if __name__ == "__main__":
    main()
