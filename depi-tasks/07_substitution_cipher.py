"""
Problem: Substitution Cipher (Encryption & Decryption)

Requirements:
1. Generate a base character list containing whitespace, letters, digits, and punctuation using the `string` module.
2. Create an encryption key by creating a copy of the characters and shuffling them with `random.shuffle()`.
3. Encrypt a plain text message by finding each character's index in `chars` and replacing it with the character at the same index in `keys`.
4. Decrypt the secret message by finding each character's index in `keys` and getting back the original character from `chars`.
5. Print both the encrypted and decrypted results to verify accuracy.

Concepts: `string` constants, list slicing/copying (`[:]`), `random.shuffle()`, index-based mapping (`.index()`).
"""

import random
import string

chars = " " + string.ascii_letters + string.digits + string.punctuation
chars = list(chars)
keys = chars[:]
random.shuffle(keys)

print(chars)
print(keys)

# encrypt
plain_text = input("Enter text to encrypt: ")
print()

cipher_text = ""
for char in plain_text:
    cipher_text = cipher_text + keys[chars.index(char)]

print(f"Plain text   : {plain_text}")
print(f"Enrypted text: {cipher_text}")
print()

# decrypt
cipher_text = input("Enter encrypted message to decrypt: ")
print()

plain_text = ""
for char in cipher_text:
    plain_text = plain_text + chars[keys.index(char)]

print(f"Enrypted text: {cipher_text}")
print(f"Plain text   : {plain_text}")
