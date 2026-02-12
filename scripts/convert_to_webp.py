"""
Convert all JPG and PNG images in the Assets folder to WebP format.
"""
import os
from pathlib import Path
from PIL import Image

def convert_to_webp(assets_path: str, delete_originals: bool = False, quality: int = 90):
    """
    Convert all JPG and PNG images in the given path to WebP format.
    
    Args:
        assets_path: Path to the Assets folder
        delete_originals: Whether to delete original files after conversion
        quality: WebP quality (0-100, default 90)
    """
    assets_dir = Path(assets_path)
    
    if not assets_dir.exists():
        print(f"Error: Directory {assets_path} does not exist")
        return
    
    # Find all image files
    image_extensions = ['*.jpg', '*.jpeg', '*.png', '*.JPG', '*.JPEG', '*.PNG']
    image_files = []
    
    for ext in image_extensions:
        image_files.extend(assets_dir.rglob(ext))
    
    total = len(image_files)
    print(f"Found {total} images to convert")
    
    converted = 0
    errors = 0
    
    for i, img_path in enumerate(image_files, 1):
        try:
            # Create output path with .webp extension
            output_path = img_path.with_suffix('.webp')
            
            # Skip if WebP already exists
            if output_path.exists():
                print(f"[{i}/{total}] Skipping {img_path.name} (WebP already exists)")
                continue
            
            # Open and convert image
            with Image.open(img_path) as img:
                # Convert RGBA to RGB if necessary (WebP handles both, but this ensures compatibility)
                if img.mode in ('RGBA', 'LA', 'P'):
                    # For transparent images, keep transparency
                    img.save(output_path, 'WEBP', quality=quality, method=6)
                else:
                    # For non-transparent images
                    if img.mode != 'RGB':
                        img = img.convert('RGB')
                    img.save(output_path, 'WEBP', quality=quality, method=6)
            
            print(f"[{i}/{total}] Converted: {img_path.relative_to(assets_dir)}")
            converted += 1
            
            # Delete original if requested
            if delete_originals:
                img_path.unlink()
                print(f"           Deleted original: {img_path.name}")
                
        except Exception as e:
            print(f"[{i}/{total}] Error converting {img_path.name}: {e}")
            errors += 1
    
    print(f"\n{'='*60}")
    print(f"Conversion complete!")
    print(f"Successfully converted: {converted}")
    print(f"Errors: {errors}")
    print(f"Skipped (already exists): {total - converted - errors}")
    print(f"{'='*60}")

if __name__ == "__main__":
    assets_path = r"C:\Users\harri\source\repos\Theros\content\Assets"
    
    print("Converting images to WebP format...")
    print(f"Assets path: {assets_path}")
    print(f"Quality: 90")
    print(f"Delete originals: Yes")
    print()
    
    convert_to_webp(assets_path, delete_originals=True, quality=90)
