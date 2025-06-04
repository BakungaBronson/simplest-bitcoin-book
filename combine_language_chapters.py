import os
from pathlib import Path
import argparse
import re

def derive_chapter_title(folder_name: str) -> str:
    """Derives a chapter title from the folder name."""
    # Remove numeric prefix if it exists (e.g., "01-", "010-")
    title_base = re.sub(r"^\d+-?", "", folder_name)
    # Basic formatting: replace hyphens/underscores with spaces, title case
    title_formatted = title_base.replace("-", " ").replace("_", " ")
    # Capitalize words, handling potential multiple spaces
    title_formatted = " ".join(word.capitalize() for word in title_formatted.split())
    return title_formatted

def combine_chapters(language_folder_name: str, source_base_dir: str, output_file: str, title_heading_level: int = 1):
    """
    Combines all index.md files from chapter folders of a given language 
    from the project root into a single Markdown file, prepending chapter titles.
    """
    lang_path = Path(source_base_dir) / language_folder_name

    if not lang_path.is_dir():
        print(f"Error: Language content directory not found: '{lang_path}'")
        return

    print(f"Processing language: '{language_folder_name}' from path: '{lang_path}'")

    # Chapter folders are expected to be direct children of lang_path
    # and typically have names like '01-some-topic', '02-another-topic'
    chapter_folders = sorted(
        [d for d in lang_path.iterdir() if d.is_dir() and re.match(r"^\d+-", d.name)],
        key=lambda d: d.name
    )

    if not chapter_folders:
        print(f"No chapter folders (e.g., '01-something') found in '{lang_path}'.")
        # If you have a main index.md directly in the language folder (e.g., swahili/index.md)
        # and want to include it, that logic would need to be added here or handled separately.
        # This script currently focuses on combining chapter sub-folders.
        return

    combined_content = ""
    heading_marker = "#" * title_heading_level

    # Optional: Include a main index.md from the root of the language folder itself, if it exists
    # This was not in the original request for root folders but might be desired.
    # For now, we focus only on the chapter subdirectories.

    for chapter_dir in chapter_folders:
        chapter_title = derive_chapter_title(chapter_dir.name)
        index_md_file = chapter_dir / "index.md"

        if index_md_file.exists():
            print(f"  Processing chapter: '{chapter_dir.name}' (Title: '{chapter_title}')")
            with open(index_md_file, 'r', encoding='utf-8') as f:
                chapter_content = f.read()
                frontmatter_match = re.match(r"^---\s*\n(.*?)\n---\s*\n", chapter_content, re.DOTALL)
                if frontmatter_match:
                    chapter_content = chapter_content[frontmatter_match.end():]
                
                combined_content += f"{heading_marker} {chapter_title}\n\n"
                combined_content += chapter_content.strip() + "\n\n"
        else:
            print(f"    Warning: '{index_md_file.name}' not found in '{chapter_dir.name}'. Skipping chapter.")

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
        description="Combines Markdown chapter files from a language folder in the project root."
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
        "--title_level",
        type=int,
        default=1,
        choices=[1, 2, 3, 4, 5, 6],
        help="Markdown heading level for chapter titles (default: 1 for H1)."
    )

    args = parser.parse_args()

    combine_chapters(args.language_folder, args.source_base_dir, args.output_filename, args.title_level) 