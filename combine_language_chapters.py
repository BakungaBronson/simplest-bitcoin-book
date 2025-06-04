import os
from pathlib import Path
import argparse
import re

def combine_chapters(language_folder_name: str, source_base_dir: str, output_file: str, chapter_heading_level: int = 1):
    """
    Combines all index.md files from chapter folders of a given language 
    from the project root into a single Markdown file, prepending 'Chapter XX' titles.
    """
    lang_path = Path(source_base_dir) / language_folder_name

    if not lang_path.is_dir():
        print(f"Error: Language content directory not found: '{lang_path}'")
        return

    print(f"Processing language: '{language_folder_name}' from path: '{lang_path}'")

    chapter_folders = sorted(
        [d for d in lang_path.iterdir() if d.is_dir() and re.match(r"^\d+-", d.name)],
        key=lambda d: int(re.match(r"^(\d+)-?", d.name).group(1)) if re.match(r"^(\d+)-?", d.name) else float('inf')
    )

    if not chapter_folders:
        print(f"No chapter folders (e.g., '01-something') found in '{lang_path}'.")
        return

    combined_content = ""
    heading_marker = "#" * chapter_heading_level
    chapter_counter = 1 # Fallback counter

    for chapter_dir in chapter_folders:
        folder_name_match = re.match(r"^(\d+)-?", chapter_dir.name)
        if folder_name_match:
            chapter_number_str = folder_name_match.group(1).lstrip('0')
            if not chapter_number_str: # Handles cases like "00-"
                chapter_number_str = "0"
            chapter_prefix_title = f"Chapter {chapter_number_str}"
        else:
            # Fallback if folder name doesn't start with numbers like "01-"
            chapter_prefix_title = f"Section {chapter_counter}" # Or just use chapter_counter if preferred
        
        index_md_file = chapter_dir / "index.md"

        if index_md_file.exists():
            print(f"  Processing chapter folder: '{chapter_dir.name}' (as '{chapter_prefix_title}')")
            with open(index_md_file, 'r', encoding='utf-8') as f:
                chapter_content = f.read()
                # Remove existing frontmatter from chapter file
                frontmatter_match = re.match(r"^---\s*\n(.*?)\n---\s*\n", chapter_content, re.DOTALL)
                if frontmatter_match:
                    chapter_content = chapter_content[frontmatter_match.end():]
                
                combined_content += f"{heading_marker} {chapter_prefix_title}\n\n"
                combined_content += chapter_content.strip() + "\n\n"
        else:
            print(f"    Warning: '{index_md_file.name}' not found in '{chapter_dir.name}'. Skipping chapter.")
        chapter_counter += 1

    try:
        output_path = Path(output_file)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(combined_content.strip())
        print(f"\nSuccessfully combined chapters into '{output_path}'")
    except Exception as e:
        print(f"\nError writing to output file '{output_file}': {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Combines Markdown chapter files from a language folder in the project root, prepending 'Chapter XX' style titles."
    )
    parser.add_argument(
        "language_folder", 
        type=str, 
        help="Name of the language folder in the project root (e.g., 'swahili', 'french', 'english')."
    )
    parser.add_argument(
        "output_filename", 
        type=str, 
        help="Name of the output Markdown file (e.g., 'Swahili_Book.md')."
    )
    parser.add_argument(
        "--source_base_dir", 
        type=str, 
        default=".",
        help="Base directory containing the language folders (default: current directory '.')."
    )
    parser.add_argument(
        "--chapter_heading_level",
        type=int,
        default=1,
        choices=[1, 2, 3, 4, 5, 6],
        help="Markdown heading level for 'Chapter XX' prefixes (default: 1 for H1)."
    )

    args = parser.parse_args()

    combine_chapters(args.language_folder, args.source_base_dir, args.output_filename, args.chapter_heading_level) 