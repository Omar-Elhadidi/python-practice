"""
Problem: Basic String Operations & Manipulations

Requirements:
1. Extract the username prefix from an email address using string slicing and `.find()`.
2. Count the total number of vowels (a, e, i, o, u) in a full name using iteration and membership checks.
3. Sanitize user input by removing outer whitespace and converting characters to lowercase.
4. Output structured user profile information using f-strings.

Concepts: String slicing, membership operators (`in`), for loops, string sanitization (`strip()`, `lower()`), f-strings.
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
