"""
Task: Safe Input Validator (Custom Exceptions & Error Handling)

Build a function that:
1. Takes a string input for a username.
2. Validates that the input is at least 3 characters long and contains letters only.
3. Raises a custom exception (notStringError) if the input is invalid.
4. Uses a while loop with a try/except block to catch the error and retry until valid.
"""

class notStringError(Exception):
    pass


def checkString(string):
    if len(string) < 3:
        raise notStringError("String must be more than 3 character")
    if not string.isalpha():
        raise notStringError("String must be letters only ")
    return True


while True:
    try:
        name = input("Enter username: ")
        if checkString(name):
            print("valid username:")
            break
    except notStringError as e:
        print(f"Error: {e}")
