import os
import shutil
from pathlib import Path
import argparse

IMAGE_EXTENSIONS = [".png", ".jpg", ".jpeg", ".gif", ".webp", ".svg"]

def copy_images_from_chapter_subfolders(
    base_source_lang_dir: str, 
    target_output_folder_path: str
):
    """
    Scans through all chapter subfolders in a base source language directory,
    copies all image files (based on common extensions) from each chapter 
    subfolder directly into a single target output folder.
    """
    base_source_path = Path(base_source_lang_dir).resolve()
    target_path = Path(target_output_folder_path).resolve()

    if not base_source_path.is_dir():
        print(f"Error: Base source language directory not found or not a directory: '{base_source_path}'")
        return
    
    if not target_path.is_dir():
        print(f"Error: Target output folder not found or not a directory: '{target_path}'")
        return

    print(f"Scanning for chapter subfolders in: '{base_source_path}'...")
    total_copied_image_count = 0
    total_found_image_count = 0
    processed_chapter_folders = 0

    for chapter_folder in base_source_path.iterdir():
        if chapter_folder.is_dir():
            processed_chapter_folders += 1
            print(f"  Processing chapter folder: '{chapter_folder.name}'")
            current_folder_found_images = 0
            current_folder_copied_images = 0
            for item in chapter_folder.iterdir():
                if item.is_file() and item.suffix.lower() in IMAGE_EXTENSIONS:
                    total_found_image_count += 1
                    current_folder_found_images +=1
                    target_file_path = target_path / item.name
                    try:
                        shutil.copy2(item, target_file_path)
                        # print(f"    Copied '{item.name}' to '{target_file_path}'")
                        total_copied_image_count += 1
                        current_folder_copied_images +=1
                    except Exception as e:
                        print(f"    Error copying image '{item.name}' from '{chapter_folder.name}': {e}")
            if current_folder_found_images > 0:
                print(f"    Found {current_folder_found_images} image(s) in '{chapter_folder.name}', copied {current_folder_copied_images}.")
            else:
                print(f"    No images found in '{chapter_folder.name}'.")

    if processed_chapter_folders == 0:
        print(f"No chapter subfolders found in '{base_source_path}'.")
    else:
        print(f"\nProcessed {processed_chapter_folders} chapter folder(s).")
        print(f"Total images found across all chapters: {total_found_image_count}.")
        print(f"Total images copied to '{target_path}': {total_copied_image_count}.")

    print("\nImage copying finished.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Copies all images from chapter subfolders of a source language directory into a target folder."
    )
    parser.add_argument(
        "base_source_lang_dir", 
        type=str, 
        help="Path to the base source language directory (e.g., 'english/') containing chapter subfolders."
    )
    parser.add_argument(
        "target_output_folder", 
        type=str, 
        help="Path to the target directory where images will be copied (e.g., 'full_language_books/')."
    )
    
    args = parser.parse_args()

    copy_images_from_chapter_subfolders(args.base_source_lang_dir, args.target_output_folder) 