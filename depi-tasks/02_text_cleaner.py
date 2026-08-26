"""
Problem: Text Normalization & Slang Cleaner

Requirements:
1. Strip leading and trailing whitespace from an uncleaned input string.
2. Collapse multiple internal spaces between words into a single space.
3. Replace informal shorthand slang words ('u' -> 'you', 'r' -> 'are').
4. Capitalize the first letter of the resulting cleaned sentence.

Concepts: String methods chaining (`strip()`, `split()`, `join()`, `replace()`, `capitalize()`).
"""

text = "  hey   u  r awesome! lol  "

# Strip outer spaces and normalize internal whitespace
text = text.strip().split()
text = " ".join(text)

# Replace shorthand slang and capitalize
text = text.replace("u", "you").replace("r", "are")
text = text.capitalize()

print(text)
