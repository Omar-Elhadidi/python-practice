"""
Task 1: String Operations
Goal: Practice string slicing, searching, iteration, and formatting.

Exercises included:
1. Extract a username from an email address using string slicing and `find()`.
2. Count the number of vowels in a given string using a for loop.
3. Sanitize user input using `strip()` and `lower()`.
4. Use f-strings for string interpolation.
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
