"""
Problem: Terminal Contact Management System (CRUD)

Requirements:
1. Store contacts in memory using a dictionary with names as keys and phone numbers as values.
2. Provide an interactive command-line interface supporting four primary operations:
   - Add a new contact (with automatic duplicate updating).
   - Search for a contact by name and display their registered number.
   - Delete an existing contact with existence verification.
   - Show all saved contacts formatted in a structured list.
3. Validate user inputs: Ensure contact names contain only alphabetic characters (spaces allowed) and phone numbers contain only numeric digits.
4. Normalize contact names to title case for consistent search and display formatting.

Concepts: Python dictionaries, infinite while loops, input validation (`isalpha()`, `isdigit()`), custom functions, string formatting.
"""

contacts = {
    "Omar Tamer": "01061984638",
    "Ahmed Azab": "0123456789",
    "Mohammed": "097654321",
}

def add_contact(name, num):
    contacts.update({name.title(): num})
    print(f"{name} added to contacts ✅")

def search_contact(name):
    number = contacts.get(name.title())
    if number is None:
        print(f"{name} isn't in contacts ❌")
    else:
        print(f"Name: {name:10}  Number: {number}")

def delete_contact(name):
    name = name.title()
    if name in contacts:
        contacts.pop(name)
        print(f"Contact {name} deleted ✅")
    else:
        print(f"{name} isn't in contacts")

def show_contacts():
    print("-----------Contacts----------")
    for contact, number in contacts.items():
        print(f"Name: {contact.title():10}  Number: {number}")


while True:
    action = input("""
What would like to do ?
Add a new contact --> add
Search for contact ---> search
Delete a contact --> delete
Show all contacts --> show
To quit --> q

""").strip().lower()

    if action == "add":
        name = input("Enter new contact's name: ")
        while not name.replace(" ", "").isalpha():
            print("Enter a valid name")
            name = input("Enter new contact's name: ")

        num = input("Enter new contact's number: ")
        while not num.isdigit():
            print("Enter a valid number")
            num = input("Enter new contact's number: ")
        print()
        add_contact(name, num)

    elif action == "search":
        name = input("Enter Contact's name: ")
        while not name.replace(" ", "").isalpha():
            print("Enter a valid name")
            name = input("Enter Contact's name: ")
        print()
        search_contact(name)

    elif action == "delete":
        name = input("Enter Contact's name to delete: ")
        while not name.replace(" ", "").isalpha():
            print("Enter a valid name")
            name = input("Enter Contact's name to delete: ")
        print()
        delete_contact(name)

    elif action == "show":
        show_contacts()

    elif action == "q":
        break

    else:
        print("Enter a valid action")
