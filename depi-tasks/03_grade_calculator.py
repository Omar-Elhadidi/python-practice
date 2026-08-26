"""
Problem: Student Grade Classifier with Input Validation

Requirements:
1. Accept a user's name and an integer score between 1 and 100.
2. Validate that the input score falls strictly within the [1, 100] boundary; output an error message if out of bounds.
3. Categorize valid scores into quartile grade tiers:
   - 1 to 25   -> D
   - 26 to 50  -> C
   - 51 to 75  -> B
   - 76 to 100 -> A
4. If a student achieves an 'A' and their name is "Ahmed", print a specialized commendation message.

Concepts: Conditional branching (`if`, `elif`, `else`), logical operators (`or`), nested conditionals, range boundaries.
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
