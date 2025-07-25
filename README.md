# Simplest Bitcoin Book Translation Tool

A Python script that automatically translates Markdown files for the Simplest Bitcoin Book while preserving their formatting using Google's Gemini AI.

## What it does

- Translates all `.md` files in a directory to any language
- Keeps all Markdown formatting intact (headers, links, code blocks, etc.)
- Copies non-markdown files as-is
- Maintains directory structure
- Translates code comments but leaves code unchanged

## Installation

### 1. Install Python
Make sure you have Python 3.7+ installed on your computer.

### 2. Install required packages
```bash
pip install google-genai pathlib
```

### 3. Get a Gemini API key
1. Go to [Google AI Studio](https://aistudio.google.com/app/apikey)
2. Create a new API key
3. Copy the key (you'll need it in step 4)

### 4. Set up your API key
**On Windows:**
```cmd
set GEMINI_API_KEY=your_api_key_here
```

**On Mac/Linux:**
```bash
export GEMINI_API_KEY=your_api_key_here
```

## How to use

### Basic usage
```bash
python gemini_translation_script.py source_folder target_language
```

### Examples
```bash
# Translate English docs to Spanish
python gemini_translation_script.py english spanish

# Translate docs to French
python gemini_translation_script.py my_docs french

# Translate to any language
python gemini_translation_script.py content "simplified chinese"
```

### Advanced options
```bash
# Specify source language (default is English)
python gemini_translation_script.py docs spanish --source_language english

# Use a different AI model
python gemini_translation_script.py docs french --model_name gemini-2.0-flash-001

# Overwrite existing files without asking
python gemini_translation_script.py docs spanish --force_overwrite
```

## File structure

**Before translation:**
```
project/
├── english/
│   ├── intro.md
│   ├── guide.md
│   └── images/
│       └── screenshot.png
└── gemini_translation_script.py
```

**After running:** `python gemini_translation_script.py english spanish`
```
project/
├── english/
│   ├── intro.md
│   ├── guide.md
│   └── images/
│       └── screenshot.png
├── spanish/
│   ├── intro.md          ← Translated!
│   ├── guide.md          ← Translated!
│   └── images/
│       └── screenshot.png ← Copied as-is
└── gemini_translation_script.py
```

## What gets translated

✅ **Translates:**
- Text content in Markdown files
- Headings and paragraphs
- List items
- Table content
- Code comments
- Alt text for images

❌ **Keeps unchanged:**
- File names
- Folder names
- URLs and links
- Image file paths
- Code (except comments)
- Non-markdown files

## Troubleshooting

### "API key not set" error
Make sure you've set the `GEMINI_API_KEY` environment variable correctly.

### "Translation blocked" messages
Some content might be blocked by safety filters. The original text will be kept with a warning message.

### "Permission denied" errors
Make sure you have write permissions in the target directory.

### Files already exist
The script will ask before overwriting files. Use `--force_overwrite` to skip confirmations.

## Tips

- Test with a small folder first
- Review translations for accuracy
- Keep backups of your original files
- Use descriptive language names (e.g., "spanish" instead of "es")

## Supported languages

You can translate to any language that Gemini supports. Use natural language names:
- `spanish`, `french`, `german`, `italian`
- `chinese`, `japanese`, `korean`
- `portuguese`, `russian`, `arabic`
- `hindi`, `bengali`, `turkish`
- And many more!

## Need help?

If you encounter issues:
1. Check that your API key is set correctly
2. Make sure you have an internet connection
3. Verify the source directory exists and contains `.md` files
4. Try with a smaller test directory first

## Combining Chapters into a Single File

The `combine_language_chapters.py` script can be used to merge all chapter `index.md` files from a specific language folder (located in the project root) into a single Markdown document. This is useful for creating a full-text version of the book in a given language.

### How to use `combine_language_chapters.py`

**Basic usage:**
```bash
python combine_language_chapters.py <language_folder_name> <output_markdown_filename>
```

**Arguments:**
-   `<language_folder_name>`: The name of the language folder in your project root (e.g., `english`, `swahili`, `french`). This folder should contain subdirectories for each chapter (e.g., `01-why-we-need/`, `02-bitcoin-fixes-this/`), each with an `index.md` file.
-   `<output_markdown_filename>`: The desired name for the combined Markdown file (e.g., `Swahili_FullBook.md`).

**Examples:**
```bash
# Combine all chapters from the 'swahili' folder into 'Swahili_Book.md'
python combine_language_chapters.py swahili Swahili_Book.md

# Combine all chapters from the 'english' folder into 'English_Complete.md'
python combine_language_chapters.py english English_Complete.md
```

**Advanced options:**
```bash
# Specify a different source base directory (if language folders are not in the current dir)
python combine_language_chapters.py swahili Swahili_Book.md --source_base_dir path/to/language_folders/

# Change the Markdown heading level for chapter titles (default is 1 for H1)
python combine_language_chapters.py french French_Book.md --title_level 2
```

**What the script does:**
-   Looks for a language folder (e.g., `swahili/`) in the specified source base directory (defaults to the current directory).
-   Finds all chapter subfolders (e.g., `01-some-topic/`, `02-another-topic/`) within that language folder.
-   Sorts these chapter folders alphanumerically.
-   For each chapter folder:
    -   Derives a chapter title from the folder name (e.g., "01-Why We Need" becomes "Why We Need").
    -   Reads the `index.md` file from the chapter folder.
    -   Strips any existing YAML frontmatter from this `index.md`.
    -   Prepends the derived chapter title as a Markdown heading (default H1).
    -   Appends the chapter's content to the combined output.
-   Saves the complete combined content to the specified output file.

## Repairing Google-Docs-Edited Chapters

When collaborators make edits in **Google Docs** the Markdown formatting (blockquotes, heading hashes, new-line spacing, list markers) and, most importantly, the inline image tags (e.g. `![alt text](image.png)`) are frequently stripped out.  
The `chapter_fixer.py` utility takes two Markdown files – the **pristine original** and the **edited / broken** version – and automatically merges them so that:

1. All human text edits from the Google Docs draft are kept.
2. The exact Markdown structure from the original file is restored.
3. Every image tag contained in the original is re-inserted into its correct position.

Internally the script sends both chapter versions to Google Gemini and instructs it to return a single, fixed Markdown chapter.  Each chapter is processed independently so the book structure is preserved.

### How to use `chapter_fixer.py`

```bash
python chapter_fixer.py <original_markdown> <changed_markdown> <output_markdown>
```

**Arguments**
- `<original_markdown>` – The file that contains the correct Markdown formatting and images.
- `<changed_markdown>` – The Google Docs export containing the new wording but broken formatting.
- `<output_markdown>` – Where the merged, fixed chapter(s) will be written.

**Example**
```bash
# Merge edits from editors back into the original English book
python chapter_fixer.py english/01-why-we-need/index.md edited_branch/01-why-we-need/index.md fixed/01-why-we-need.md
```

### What the script does
1. Splits both input files into chapters by looking for headings that match `# Chapter N`.
2. For every chapter found in the original it tries to locate the corresponding chapter in the changed file.
3. If a chapter exists in both versions it calls Gemini with a specialised prompt that:
   - Constrains Gemini to keep all sentences from the changed version.
   - Forces it to copy Markdown syntax and image tags from the original.
4. Chapters that are missing in the changed file are copied as-is from the original, preventing data loss.
5. The fixed chapters are concatenated together (separated by `---`) and saved to the output file.

### Requirements
- Same Python and dependency set as the translation script (`google-genai`, `pathlib`, etc.).
- A valid `GEMINI_API_KEY` exported in your environment.

## Google Docs Drafts For Review

Simplest Bitcoin Book Translations 1: This document contains full book translations in Swahili, Luganda, French, Yoruba, Hindi, Russian, Rukiga, Bulgarian, German, Hausa, Zulu, and Italian.

Link: https://docs.google.com/document/d/14Mc0iri-sFQ963Q0ohZCFQMOclYDHQalAilAnTt0M-8/edit?usp=sharing

Simplest Bitcoin Book Translations 2: This document includes full book translations in Bahasa Indonesia, Xhosa, Korean, Japanese, and Mandarin Chinese.

Link: https://docs.google.com/document/d/1qkRmABEflINoaZXRJ-mC_NCAjQlUSq0M4V_3skum1q4/edit?usp=sharing