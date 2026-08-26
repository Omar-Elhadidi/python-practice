"""
=============================================================================
Task: Conditional Statements & Input Range Validation
=============================================================================

Problem Statement / Question:
Write a Python program that asks the user for their name and a score/number 
between 1 and 100, then performs the following:
1. Validate if the number is within the range [1, 100]. If out of range, 
   print "out of range {name}".
2. Assign letter grades based on quartile ranges:
   - Score <= 25: Grade "D"
   - Score <= 50: Grade "C"
   - Score <= 75: Grade "B"
   - Score > 75:  Grade "A"
3. Special case: If the grade is "A" and the user's name is "ahmed", 
   print "excellent ahmed".

Key Concepts:
- `input()` with type conversion (`int()`)
- Conditional logic (`if`, `elif`, `else`)
- Logical operators (`or`)
- Nested condition branching
=============================================================================
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
