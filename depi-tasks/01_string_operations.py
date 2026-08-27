# Task 1: String Operations
# Practice string indexing, slicing, counting vowels, and f-strings.

# 1. Extract username from email
email = "omar@gmail.com"
username = email[:email.find("@")]
print(username)

# 2. Count vowels in a name
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
