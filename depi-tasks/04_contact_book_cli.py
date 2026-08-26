"""
=============================================================================
Mini Project: Simple Contact Book CLI
=============================================================================

Problem Statement / Prompt:
Build a menu-driven, terminal-based contact book application using Python dictionaries.

Requirements:
1. Users must be able to:
   - Add a new contact (Name + Phone Number)
   - Search for a contact by name
   - Delete an existing contact by name
   - Show all saved contacts
   - Exit the application gracefully
2. Input Validation:
   - Names must contain only alphabetic characters and spaces (e.g. "Omar Tamer").
   - Phone numbers must contain only digits.
3. Architecture:
   - Use dictionaries for O(1) key-value lookups.
   - Use functions for each core action (`add_contact`, `search_contact`, etc.).
   - Normalize names with `.title()` to prevent casing duplication.

Key Concepts:
- Dictionary CRUD operations (`contacts[key] = val`, `.get()`, `.pop()`, `.items()`)
- `while True` main event loop
- Helper validation loops with `.isalpha()` and `.isdigit()`
=============================================================================
"""

contacts = {
    "Omar Tamer" : "01061984638",
    "Ahmed Azab ": "0123456789",
    "Mohammed": "097654321",
}

def add_contact(name, num):
  contacts.update({name.title() : num})
  print(f"{name} added to contacts ✅")

def search_contact(name):
 number = contacts.get(name.title())
 if number == None:
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
  action = input( """
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

  elif action =="q":
    break

  else:
    print("Enter a valid action")
