"""
Mini Project: Text Cleaner
Take a messy input string and clean it up:
1. Remove extra leading/trailing whitespace and multiple spaces between words.
2. Replace shorthand words like 'u' with 'you' and 'r' with 'are'.
3. Capitalize the first letter of the cleaned sentence.
"""

text = "  hey   u  r awesome! lol  "

# Strip outer spaces and remove extra spaces between words
text = text.strip().split()
text = " ".join(text)

# Replace shorthand words and capitalize
text = text.replace("u", "you").replace("r", "are")
text = text.capitalize()

print(text)
