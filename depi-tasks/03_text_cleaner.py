"""
=============================================================================
Mini Project: Text Cleaner & Normalizer
=============================================================================

Problem Statement / Question:
Write a Python script to take a raw, messy string with irregular whitespace 
and internet slang (e.g., "  hey   u  r awesome! lol  ") and transform it into 
a clean, properly formatted sentence.

Requirements:
1. Strip leading and trailing whitespace.
2. Normalize spaces between words so only a single space separates each word.
3. Replace internet slang/abbreviations:
   - "u"  -> "you"
   - "r"  -> "are"
4. Capitalize the first letter of the resulting sentence.

Key Concepts:
- `.strip()`, `.split()`, `' '.join()` for whitespace normalization
- Chained `.replace()` calls
- `.capitalize()` for sentence-case formatting
=============================================================================
"""

text = "  hey   u  r awesome! lol  "

# 1 & 2: Strip outer spaces and normalize multiple inner spaces
text = text.strip().split()
text = " ".join(text)

# 3 & 4: Replace shorthand text and format sentence
text = text.replace("u", "you").replace("r", "are")
text = text.capitalize()

print(text)
