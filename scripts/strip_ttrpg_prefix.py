"""
Strip the 'ttrpg-cli/' prefix from all tags in YAML frontmatter
across the vault's markdown files, producing a unified tag system.

Only modifies tags inside the YAML frontmatter block (between --- markers).
Does NOT touch inline tags in body text.
Skips .obsidian and z_Templates folders.
"""

import os
import re
import sys

CONTENT_DIR = r"C:\Users\harri\source\repos\Theros\content"
SKIP_DIRS = {".obsidian", "z_Templates"}
DRY_RUN = "--dry-run" in sys.argv

# Match YAML frontmatter block
FRONTMATTER_RE = re.compile(r"^(---\s*\n)(.*?\n)(---\s*\n)", re.DOTALL)

# Match a tag line like "  - ttrpg-cli/something"
TAG_LINE_RE = re.compile(r"^(\s*-\s+)ttrpg-cli/(.+)$", re.MULTILINE)


def process_file(filepath: str) -> tuple[bool, int]:
    """Process a single file. Returns (was_modified, replacement_count)."""
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    match = FRONTMATTER_RE.match(content)
    if not match:
        return False, 0

    opening = match.group(1)  # ---\n
    yaml_body = match.group(2)
    closing = match.group(3)  # ---\n
    rest = content[match.end():]

    # Count and perform replacements only within the YAML block
    new_yaml, count = TAG_LINE_RE.subn(r"\1\2", yaml_body)

    if count == 0:
        return False, 0

    new_content = opening + new_yaml + closing + rest

    if not DRY_RUN:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(new_content)

    return True, count


def main():
    total_files = 0
    modified_files = 0
    total_replacements = 0

    for root, dirs, files in os.walk(CONTENT_DIR):
        # Skip excluded directories
        dirs[:] = [d for d in dirs if d not in SKIP_DIRS]

        for fname in files:
            if not fname.endswith(".md"):
                continue

            filepath = os.path.join(root, fname)
            total_files += 1

            try:
                was_modified, count = process_file(filepath)
                if was_modified:
                    modified_files += 1
                    total_replacements += count
                    if DRY_RUN:
                        print(f"  [DRY RUN] Would modify: {filepath} ({count} tags)")
            except Exception as e:
                print(f"  ERROR: {filepath}: {e}", file=sys.stderr)

    mode = "[DRY RUN] " if DRY_RUN else ""
    print(f"\n{mode}Done!")
    print(f"  Files scanned:  {total_files}")
    print(f"  Files modified: {modified_files}")
    print(f"  Tags renamed:   {total_replacements}")


if __name__ == "__main__":
    main()
