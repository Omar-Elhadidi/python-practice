"""
Task: Grade Calculator
Write a program that takes a student's name and a score between 1 and 100:
1. If the score is out of the 1-100 range, print an 'out of range' message.
2. Otherwise, assign and print a grade tier:
   - 1 to 25   -> D
   - 26 to 50  -> C
   - 51 to 75  -> B
   - 76 to 100 -> A
3. If the score is an 'A' and the name is 'ahmed', print a special commendation message.
"""

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
