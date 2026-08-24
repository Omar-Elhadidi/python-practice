"""
Mini Project: Text Cleaner
Goal: Clean and format a messy string using built-in string methods.

Steps implemented:
1. Strip leading and trailing whitespace.
2. Remove extra spaces between words (using split and join).
3. Replace shorthand text ("u" -> "you", "r" -> "are").
4. Capitalize the first letter of the sentence.
"""

text = "  hey   u  r awesome! lol  "

# Strip outer spaces and remove extra spaces between words
text = text.strip().split()
text = " ".join(text)

# Replace shorthand and format
text = text.replace("u", "you").replace("r", "are")
text = text.capitalize()

print(text)
