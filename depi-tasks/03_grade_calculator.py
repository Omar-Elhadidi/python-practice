# Task 2: Grade Calculator
# Takes a name and a score between 1-100, validates the range, and prints the grade tier (A, B, C, D).

name = input("Enter Your Name: ")
num = int(input("Enter number between 1-100: "))

if num > 100 or num < 1:
    print(f"out of range {name}")
else:
    if num <= 25:
        print("D")
    elif num <= 50:
        print("C")
    elif num <= 75:
        print("B")
    else:
        print("A")
        if name.lower() == "ahmed":
            print("excellent ahmed")
