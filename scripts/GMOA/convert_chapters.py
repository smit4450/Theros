#!/usr/bin/env python3
"""
Convert Gray Merchant of Asphodel chapters from PDF text to markdown.
This script extracts Chapter 1 and Chapter 3 from the PDF text file.
"""

from pathlib import Path
import re

# Paths
SCRIPT_DIR = Path(__file__).parent
REPO_ROOT = SCRIPT_DIR.parent.parent
PDF_TEXT_PATH = SCRIPT_DIR / "pdf_full_text.txt"
OUTPUT_DIR = REPO_ROOT / "content" / "Compendium" / "books" / "gray-merchant-of-asphodel"

def fix_ocr_errors(text: str) -> str:
    """Fix common OCR errors from PDF extraction."""
    fixes = [
        (r"ci!zens", "citizens"),
        (r"Mele!s\b", "Meletis"),
        (r"ac!on", "action"),
        (r"a\.ack", "attack"),
        (r"A\.ack", "Attack"),
        (r"Aack", "Attack"),
        (r"Immunies", "Immunities"),
        (r"Condion", "Condition"),
        (r"exhaus!on", "exhaustion"),
        (r"a\.unement", "attunement"),
        (r"Percep!on", "Perception"),
        (r"hos!le", "hostile"),
        (r"ar!fact", "artifact"),
        (r"essen!ally", "essentially"),
        # Fix ft. notation
        (r"(\d+) " + "\x0b" + r"\.", r"\1 ft."),
        (r"(\d+) \.", r"\1 ft."),
    ]
    
    for pattern, replacement in fixes:
        text = re.sub(pattern, replacement, text)
    return text

def extract_chapter_1(pdf_text: str) -> str:
    """Extract Chapter 1 content from PDF text."""
    # Find start and end of Chapter 1
    start = pdf_text.find("CHAPTER 1: ENCOUNTERING THE GRAY MERCHANT")
    end = pdf_text.find("CHAPTER 2: THE GRAY MERCHANT'S WARES")
    
    if start == -1 or end == -1:
        print("Could not find Chapter 1 boundaries")
        return ""
    
    chapter_text = pdf_text[start:end]
    
    # Apply OCR fixes
    chapter_text = fix_ocr_errors(chapter_text)
    
    # The content is in the PDF - you can manually copy it
    # or enhance this script to parse the specific sections
    
    return chapter_text

def extract_chapter_3(pdf_text: str) -> str:
    """Extract Chapter 3 content from PDF text."""
    start = pdf_text.find("CHAPTER 3: RANDOM ROLL TABLES")
    end = pdf_text.find("CREDITS")
    
    if start == -1 or end == -1:
        print("Could not find Chapter 3 boundaries")
        return ""
    
    chapter_text = pdf_text[start:end]
    chapter_text = fix_ocr_errors(chapter_text)
    
    return chapter_text

def main():
    """Main conversion function."""
    print("Reading PDF text...")
    pdf_text = PDF_TEXT_PATH.read_text(encoding='utf-8')
    
    print("\nChapter 1 found:")
    ch1 = extract_chapter_1(pdf_text)
    print(f"Length: {len(ch1)} characters")
    
    print("\nChapter 3 found:")
    ch3 = extract_chapter_3(pdf_text)
    print(f"Length: {len(ch3)} characters")
    
    print("\nTo complete the conversion:")
    print("1. Review the template files created in:")
    print(f"   {OUTPUT_DIR}")
    print("2. The PDF text is in:")
    print(f"   {PDF_TEXT_PATH}")
    print("3. Copy content from the PDF text file to the markdown templates")
    print("4. Format tables using markdown table syntax")
    print("5. Add statblocks using ```statblock format")
    print("\nThe sections you need are between the page markers in pdf_full_text.txt")

if __name__ == "__main__":
    main()
