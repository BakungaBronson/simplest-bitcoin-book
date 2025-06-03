import os
import shutil
import argparse
from google import genai
from google.genai import types
from pathlib import Path

# Configure the API key
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
DEFAULT_SOURCE_LANG = "english"
# Recommended to use a newer model that is good with instruction following.
# Check https://ai.google.dev/gemini-api/docs/models/gemini for available models.
DEFAULT_MODEL_NAME = "gemini-2.0-flash" 

def translate_text(client: genai.Client, model_name: str, text_content: str, target_language: str, source_language: str, safety_settings: list) -> str | None:
    """
    Translates the given text content using the Gemini API via the client.

    Args:
        client: The configured genai.Client instance.
        model_name: The name of the model to use (e.g., "gemini-2.0-flash-001").
        text_content: The text to translate.
        target_language: The language to translate to.
        source_language: The language to translate from.
        safety_settings: Safety settings for the generation.

    Returns:
        The translated text, or a fallback string with error/block information.
    """
    system_instruction_prompt = f"""You are an expert Markdown translator. Your primary task is to translate Markdown text from {source_language} to {target_language}.

IMPORTANT RULES:
1.  Preserve the original Markdown formatting EXACTLY. This includes, but is not limited to:
    *   Headings (e.g., #, ##, ###)
    *   Lists (ordered and unordered, nested lists)
    *   Bold (e.g., **text** or __text__)
    *   Italics (e.g., *text* or _text_)
    *   Strikethrough (e.g., ~~text~~)
    *   Code blocks (e.g., ```python ... ``` or indented code blocks)
    *   Inline code (e.g., `code`)
    *   Links (e.g., [text](url))
    *   Images (e.g., ![alt text](image_url))
    *   Tables
    *   Blockquotes (e.g., > quote)
    *   Horizontal rules (e.g., --- or ***)
    *   HTML tags embedded in Markdown (e.g., <details>, <summary>, <div>) - translate content within these tags if it's text, but leave tags themselves.
2.  Only translate the textual content. Do NOT alter Markdown syntax elements, URLs, image paths, or code within code blocks (except for comments within code).
3.  If you encounter code blocks:
    *   Translate any comments (e.g., # comment in Python, // comment in JS) within the code block into {target_language}.
    *   Leave the code itself UNCHANGED.
4.  If you encounter HTML tags, translate the text content within these tags, but leave the HTML tags themselves and their attributes unchanged.
5.  Translate the text accurately and naturally into {target_language}.
6.  Ensure that relative paths in links and images (e.g., `../images/foo.png` or `./another-doc.md`) are preserved exactly as they are.
7.  Do not add any introductory or concluding phrases like "Here is the translated text:". Only output the translated Markdown.
8.  Pay special attention to frontmatter (e.g., YAML block at the start of the file, enclosed in ---). Translate the values in the frontmatter, but keep the keys and structure intact. For example:
    ---
    title: My English Title
    author: John Doe
    ---
    should become (for French translation):
    ---
    title: Mon Titre Français
    author: John Doe
    ---
When you are given the Markdown text, provide only the translated version of it.
"""
    
    try:
        response = client.models.generate_content(
            model=model_name,
            contents=text_content, # Actual markdown to translate
            config=types.GenerateContentConfig(
                system_instruction=system_instruction_prompt,
                safety_settings=safety_settings
                # Add other config like temperature here if needed
            )
        )
        if response.candidates and response.candidates[0].content:
            return response.text
        else:
            # Handling cases where the response might be blocked or empty
            print(f"Warning: Received no valid content in response for a chunk. Blocked: {response.prompt_feedback.block_reason if response.prompt_feedback else 'N/A'}")
            if response.prompt_feedback and response.prompt_feedback.block_reason:
                print(f"Block reason details: {response.prompt_feedback.block_reason_message}")
            return f"[[TranslationBlocked: {response.prompt_feedback.block_reason if response.prompt_feedback else 'Unknown reason'}]]\n\n{text_content}"

    except Exception as e:
        print(f"Error during translation: {e}")
        # Fallback: return original content with an error marker
        return f"[[TranslationError: {e}]]\n\n{text_content}"
    return None


def main():
    if not GEMINI_API_KEY:
        print("Error: GEMINI_API_KEY environment variable not set.")
        print("Please set it before running the script: export GEMINI_API_KEY='your_api_key'")
        return

    parser = argparse.ArgumentParser(
        description="Translates Markdown files in a directory structure using the Gemini API."
    )
    parser.add_argument(
        "source_dir",
        type=str,
        help="The source directory containing .md files to translate (e.g., 'english').",
    )
    parser.add_argument(
        "target_language",
        type=str,
        help="The target language for translation (e.g., 'french', 'spanish', 'luganda'). This will also be the name of the output directory.",
    )
    parser.add_argument(
        "--source_language",
        type=str,
        default=DEFAULT_SOURCE_LANG,
        help=f"The source language of the content (default: {DEFAULT_SOURCE_LANG}).",
    )
    parser.add_argument(
        "--model_name",
        type=str,
        default=DEFAULT_MODEL_NAME,
        help=f"The Gemini model to use for translation (default: {DEFAULT_MODEL_NAME})."
    )
    parser.add_argument(
        "--force_overwrite",
        action="store_true",
        help="Overwrite existing translated files without asking.",
    )

    args = parser.parse_args()

    source_path = Path(args.source_dir).resolve()
    target_language_name = args.target_language.lower()
    # Create target_dir in the parent of source_path, i.e. workspace root if source_dir is 'english/'
    target_path_root = source_path.parent / target_language_name
    
    if not source_path.is_dir():
        print(f"Error: Source directory '{source_path}' not found.")
        return

    try:
        target_path_root.mkdir(parents=True, exist_ok=True)
        print(f"Target directory created/exists: '{target_path_root}'")
    except OSError as e:
        print(f"Error creating target directory '{target_path_root}': {e}")
        return

    # Configure safety settings
    safety_settings = [ # Adjust safety settings if needed, e.g., for less restrictive blocking.
        types.SafetySetting(
            category="HARM_CATEGORY_HARASSMENT", 
            threshold="BLOCK_MEDIUM_AND_ABOVE"
        ),
        types.SafetySetting(
            category="HARM_CATEGORY_HATE_SPEECH", 
            threshold="BLOCK_MEDIUM_AND_ABOVE"
        ),
        types.SafetySetting(
            category="HARM_CATEGORY_SEXUALLY_EXPLICIT", 
            threshold="BLOCK_MEDIUM_AND_ABOVE"
        ),
        types.SafetySetting(
            category="HARM_CATEGORY_DANGEROUS_CONTENT", 
            threshold="BLOCK_MEDIUM_AND_ABOVE"
        ),
    ]
    
    try:
        client = genai.Client(api_key=GEMINI_API_KEY)
        print(f"Using Gemini model: {args.model_name} via Client")
    except Exception as e:
        print(f"Error initializing Gemini Client or validating model '{args.model_name}': {e}")
        return

    print(f"Starting translation from '{source_path}' ({args.source_language}) to '{target_path_root}' ({args.target_language})...")

    for root, dirs, files in os.walk(source_path):
        relative_path = Path(root).relative_to(source_path)
        target_dir_current = target_path_root / relative_path

        try:
            target_dir_current.mkdir(parents=True, exist_ok=True)
        except OSError as e:
            print(f"Warning: Could not create directory {target_dir_current}: {e}. Skipping.")
            continue

        for file_name in files:
            source_file_path = Path(root) / file_name
            target_file_path = target_dir_current / file_name

            if not args.force_overwrite and target_file_path.exists():
                user_input = input(
                    f"File '{target_file_path}' already exists. Overwrite? (y/N/all): "
                ).lower()
                if user_input == 'all':
                    args.force_overwrite = True
                elif user_input != 'y':
                    print(f"Skipping '{source_file_path}'.")
                    continue
            
            print(f"Processing '{source_file_path}' -> '{target_file_path}'")

            if source_file_path.suffix.lower() == ".md":
                try:
                    with open(source_file_path, "r", encoding="utf-8") as f:
                        original_content = f.read()
                    
                    if not original_content.strip():
                        print(f"Skipping empty file: '{source_file_path}'")
                        with open(target_file_path, "w", encoding="utf-8") as f:
                            f.write("") # Create empty file in target
                        continue

                    translated_content = translate_text(
                        client, args.model_name, original_content, target_language_name, args.source_language, safety_settings
                    )

                    if translated_content:
                        with open(target_file_path, "w", encoding="utf-8") as f:
                            f.write(translated_content)
                        print(f"Successfully translated and saved '{target_file_path}'")
                    else:
                        print(f"Failed to translate '{source_file_path}'. Original content may have been saved with error markers.")
                        # If translate_text returned None (unexpected), or error-marked content, it's already handled by saving it.
                except Exception as e:
                    print(f"Error processing Markdown file '{source_file_path}': {e}")
                    try: # Try to copy original on error
                        shutil.copy2(source_file_path, target_file_path)
                        print(f"Copied original '{source_file_path}' to '{target_file_path}' due to processing error.")
                    except Exception as copy_e:
                        print(f"Could not even copy original file {source_file_path}: {copy_e}")

            else: # Non-markdown files
                try:
                    shutil.copy2(source_file_path, target_file_path)
                    print(f"Copied non-markdown file '{target_file_path}'")
                except Exception as e:
                    print(f"Error copying file '{source_file_path}': {e}")
    
    print("Translation process finished.")
    print(f"Please check the '{target_path_root}' directory for translated files.")
    print("Remember to review translations, especially for complex Markdown or nuanced language.")

if __name__ == "__main__":
    main()