import os
import re
import argparse
from pathlib import Path
from google import genai
from google.genai import types
from google.genai import errors

def setup_api_key():
    """
    Configures the Gemini API client using an environment variable.
    Exits if the API key is not found.
    """
    try:
        api_key = os.environ.get("GEMINI_API_KEY")
        if not api_key:
            print("FATAL: GEMINI_API_KEY environment variable not set.")
            print("Please set it before running the script:")
            print("  - On Linux/macOS: export GEMINI_API_KEY='YOUR_API_KEY'")
            print("  - On Windows: set GEMINI_API_KEY='YOUR_API_KEY'")
            exit(1)
        # Configure the API key
        # In a real application, you might want to use a more secure way to handle API keys.
        return genai.Client(api_key=api_key)
    except Exception as e:
        print(f"An error occurred during API configuration: {e}")
        exit(1)

def split_into_chapters(markdown_content: str) -> dict[str, str]:
    """
    Splits a Markdown string into a dictionary of chapters.
    The key is the full chapter heading line (e.g., '# Chapter 1'),
    and the value is the content of that chapter.
    """
    # This pattern looks for lines starting with one or more '#' followed by 'Chapter' and a number.
    chapter_heading_pattern = re.compile(r'(^#+\s+Chapter\s+\d+.*$)', re.MULTILINE)
    parts = chapter_heading_pattern.split(markdown_content)
    
    # If no chapters are found, return the whole document as one entry.
    if len(parts) < 3:
        return {"Document": markdown_content}

    # The split results in a list where parts[0] is content before the first chapter,
    # and then alternating headings and contents.
    headings = parts[1::2]
    contents = parts[2::2]
    
    # Combine headings and their corresponding content into a dictionary.
    chapters = {heading.strip(): (heading + content).strip() for heading, content in zip(headings, contents)}
    return chapters

def fix_chapter_with_gemini(client, original_chapter: str, changed_chapter: str) -> str:
    """
    Uses the Gemini 2.0 Flash model to merge an original and a changed chapter.
    """
    model = "gemini-2.0-flash-001"
    
    # Construct the detailed prompt for the LLM.
    # This prompt provides clear instructions and context to get the desired output.
    prompt = [
        types.Content(
            role="user",
            parts=[
                types.Part.from_text(
                    text=f"""
You are an expert Markdown editor. Your task is to merge two versions of a document chapter.

**Context:**
- **ORIGINAL Version**: This version has the correct and precise Markdown syntax, formatting (like blockquotes and newlines), and all necessary image tags (e.g., `![alt text](image.png)`).
- **CHANGED Version**: This version contains legitimate text edits and rephrasing from a human editor. However, it was processed through a tool like Google Docs, so its Markdown formatting may be broken, and ALL image tags have been lost.

**Your Goal:**
Produce a single "FIXED" version that combines the best of both files. You must follow these rules precisely:
1. **Preserve Text Edits**: You MUST keep all sentence-level edits, rephrasing, and corrections from the CHANGED version.
2. **Restore Markdown Syntax**: You MUST use the markdown structure (headings, exact blockquote formatting, newlines, lists, bold/italic markers) from the ORIGINAL version as the source of truth.
3. **Restore Image Tags**: You MUST re-insert all image tags (e.g., `![alt text](image.png)`) from the ORIGINAL version into their correct locations within the newly edited text. The final output must contain all images from the original.

**CRITICAL**: Do NOT add any commentary, explanations, or introductory text. Only output the raw, fixed Markdown content for the chapter.

---
**ORIGINAL Version (Correct Syntax and Images):**
```markdown
{original_chapter}
```
---
**CHANGED Version (User Edits, Broken Syntax, No Images):**
```markdown
{changed_chapter}
```
---
**FIXED MARKDOWN OUTPUT:**
"""
                )
            ]
        )
    ]

    try:
        # Generate content with streaming to handle large responses efficiently.
        result = ""
        # The configuration helps control the creativity and length of the response.
        config = types.GenerateContentConfig(
            temperature=0.3,       # Lower temperature for more deterministic, less creative output.
            max_output_tokens=4096 # Allow for larger outputs if a chapter is long.
        )
        
        # Call the API and stream the response.
        response_stream = client.models.generate_content_stream(
            model=model,
            contents=prompt,
            config=config
        )
        
        for chunk in response_stream:
            result += chunk.text
        return result.strip()
    except errors.APIError as e:
        print(f"  ERROR: API error occurred: {e.code} - {e.message}")
        return original_chapter  # Fallback to original to prevent data loss on API failure.
    except Exception as e:
        print(f"  ERROR: Could not get response from Gemini API: {e}")
        return original_chapter  # Fallback for other unexpected errors.

def main():
    """
    Main function to parse arguments and process the markdown files.
    """
    # Set up command-line argument parsing.
    parser = argparse.ArgumentParser(
        description="Fixes a Markdown file edited in Google Docs by comparing it to the original, using an LLM.",
        formatter_class=argparse.RawTextHelpFormatter
    )
    parser.add_argument(
        "original_file",
        type=Path,
        help="Path to the original Markdown file with correct syntax and images."
    )
    parser.add_argument(
        "changed_file",
        type=Path,
        help="Path to the changed Markdown file with user edits but broken syntax."
    )
    parser.add_argument(
        "output_file",
        type=Path,
        help="Path for the final, fixed Markdown output file."
    )
    
    args = parser.parse_args()

    # Setup the API client.
    client = setup_api_key()

    # Ensure input files exist before proceeding.
    if not args.original_file.is_file() or not args.changed_file.is_file():
        print("Error: One or both input files not found. Please check the paths.")
        return

    print(f"Reading original file: {args.original_file}")
    original_content = args.original_file.read_text(encoding='utf-8')
    
    print(f"Reading changed file: {args.changed_file}")
    changed_content = args.changed_file.read_text(encoding='utf-8')

    # Split both documents into chapters to process them individually.
    original_chapters = split_into_chapters(original_content)
    changed_chapters = split_into_chapters(changed_content)
    
    fixed_document_parts = []
    
    print("\nProcessing chapters...")
    # Iterate through the original chapters to ensure the final document has the correct structure.
    for heading, original_chapter_text in original_chapters.items():
        print(f"- Processing '{heading}'...")
        
        changed_chapter_text = changed_chapters.get(heading)
        
        if not changed_chapter_text:
            print(f"  Warning: Chapter '{heading}' not found in the changed file. Using original version.")
            fixed_document_parts.append(original_chapter_text)
            continue
            
        # Use the LLM to fix the chapter by merging the two versions.
        fixed_chapter = fix_chapter_with_gemini(client, original_chapter_text, changed_chapter_text)
        fixed_document_parts.append(fixed_chapter)

    # Join the fixed chapters back into a single document.
    # A separator is added between chapters for clarity.
    final_content = "\n\n---\n\n".join(fixed_document_parts)

    # Write the final, merged content to the output file.
    args.output_file.parent.mkdir(parents=True, exist_ok=True)
    args.output_file.write_text(final_content, encoding='utf-8')
    print(f"\n✅ Successfully created fixed markdown file: {args.output_file}")

if __name__ == "__main__":
    main()
