"""
Mini Project: Substitution Cipher
Build an encryption and decryption program:
1. Create a character list containing spaces, letters, digits, and punctuation using the string module.
2. Create a shuffled copy of the characters to act as the secret key.
3. Encrypt: Swap each character of the plain text with the character at the same index in the key.
4. Decrypt: Swap each encrypted character back to its original character from the base list.
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
