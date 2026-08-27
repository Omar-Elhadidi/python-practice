"""
Mini Project: Substitution Cipher
Encrypt a message by swapping characters with a shuffled key list, and decrypt it back.
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
