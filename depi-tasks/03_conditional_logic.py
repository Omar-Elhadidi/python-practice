"""
Task 2: If Conditions
Goal: Practice using conditional statements (`if`, `elif`, `else`), logical operators (`or`), and nested conditions.

Program behavior:
- Takes a user's name and a number between 1-100.
- Validates the range (must be between 1 and 100).
- Assigns a grade category (A, B, C, D) based on the number.
- Prints a special message if the grade is A and the name is "ahmed".
"""

name = input("Enter Your Name: ")
num = int(input("Enter number between 1-100: "))

# Range validation
if num > 100 or num < 1:
    print(f"out of range {name}")
else:
    # Grade assignment
    if num <= 25:
        print("D")
    elif num <= 50:
        print("C")
    elif num <= 75:
        print("B")
    else:
        print("A")
        # Nested condition
        if name.lower() == "ahmed":
            print("excellent ahmed")
