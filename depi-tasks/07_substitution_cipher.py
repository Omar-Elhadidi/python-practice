"""
Problem: Substitution Cipher (Encryption & Decryption)

Requirements:
1. Generate a character vocabulary containing whitespace, punctuation, numeric digits, and ASCII letters using the `string` module.
2. Create an encryption key by creating a shallow copy of the character set and shuffling it with `random.shuffle()`.
3. Encrypt plain text: Map each input character from its index in the base character list to the corresponding character in the shuffled key list.
4. Decrypt cipher text: Map each encrypted character from its index in the key list back to the original character in the base character list.
5. Display side-by-side verification of original, encrypted, and decrypted strings.

Concepts: `string` constants, list copying/slicing (`[:]`), in-place shuffling (`random.shuffle()`), index-based character substitution (`.index()`).
"""

import random
import string

# Build character set (including whitespace)
chars = " " + string.punctuation + string.digits + string.ascii_letters
chars = list(chars)

# Create shuffled substitution key
keys = chars[:]
random.shuffle(keys)

print(f"Base Chars ({len(chars)}): {''.join(chars[:20])}...")
print(f"Shuffled Key:       {''.join(keys[:20])}...")
print("-" * 50)

# --- ENCRYPTION ---
plain_text = input("Enter text to encrypt: ")
print()

cipher_text = ""
for char in plain_text:
    if char in chars:
        cipher_text += keys[chars.index(char)]
    else:
        cipher_text += char  # Fallback for untracked characters

print(f"Plain text    : {plain_text}")
print(f"Encrypted text: {cipher_text}")
print("-" * 50)

# --- DECRYPTION ---
cipher_input = input("Enter encrypted message to decrypt: ")
print()

decrypted_text = ""
for char in cipher_input:
    if char in keys:
        decrypted_text += chars[keys.index(char)]
    else:
        decrypted_text += char

print(f"Encrypted text: {cipher_input}")
print(f"Decrypted text: {decrypted_text}")
