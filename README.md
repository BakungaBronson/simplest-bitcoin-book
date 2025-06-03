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