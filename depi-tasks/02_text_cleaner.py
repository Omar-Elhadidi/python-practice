# Mini Project: Text Cleaner
# Clean a messy string: remove extra spaces, replace shorthand words (u -> you, r -> are), and capitalize.

text = "  hey   u  r awesome! lol  "

# Strip outer spaces and remove extra spaces between words
text = text.strip().split()
text = " ".join(text)

# Replace shorthand words and capitalize
text = text.replace("u", "you").replace("r", "are")
text = text.capitalize()

print(text)
