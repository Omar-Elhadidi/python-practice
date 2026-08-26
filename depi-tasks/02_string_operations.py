"""
=============================================================================
Task: String Manipulation, Indexing, and Formatting
=============================================================================

Problem Statement / Questions:
Solve the following 4 string manipulation exercises:

1. Email Username Extractor:
   Given an email address (e.g., "omar@gmail.com"), extract and print the 
   username portion before the "@" symbol using string slicing and `.find()`.

2. Vowel Counter:
   Given a string containing a full name (e.g., "Omar Elhadidi"), iterate through 
   the string using a loop and count how many vowels (a, e, i, o, u) it contains.

3. User Input Sanitization:
   Prompt the user for their name, remove all leading/trailing whitespace 
   using `.strip()`, convert it to lowercase using `.lower()`, and display it.

4. F-String Formatting:
   Given variables `name` and `age`, print: "My name is {name}, i am {age} years old"
   using modern Python f-strings.

Key Concepts:
- String slicing: `string[:index]`
- Methods: `.find()`, `.lower()`, `.strip()`
- Iterating over sequences with `for` loops
- Formatted string literals (f-strings)
=============================================================================
"""

# 1. Extract username from email
email = "omar@gmail.com"
username = email[:email.find("@")]
print(username)

# 2. Count vowels in a string
name = "Omar Elhadidi"
vowels = ["a", "e", "i", "o", "u"]
count = 0
name = name.lower()

for i in name:
    if i in vowels:
        count += 1

print(f"vowels = {count}")

# 3. Sanitize user input
username = input("enter your name: ").strip().lower()
print(username)

# 4. F-string formatting
name = "omar"
age = 22
print(f"My name is {name}, i am {age} years old")
