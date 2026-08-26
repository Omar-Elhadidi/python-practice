"""
=============================================================================
Mini Project: ATM / Banking CLI Application
=============================================================================

Problem Statement / Requirements:
Build a realistic terminal-based ATM machine / banking application that allows 
a user to manage their account balance securely.

Requirements:
1. Operations:
   - Option 1: Show current account balance formatted nicely with decimals and currency.
   - Option 2: Deposit an amount into the account.
   - Option 3: Withdraw an amount from the account.
   - Option 4: Exit the program cleanly.
2. Financial & Business Rules:
   - Starting balance is $0.00.
   - Deposited amounts must be positive numbers.
   - Overdraft Protection: Prevent withdrawals that exceed the current balance.
   - Currency display must show comma separators and 2 decimal places (e.g. $1,250.50).
3. Code Architecture:
   - Use dedicated pure functions for `deposit()`, `withdraw()`, and `show_balance()`.
   - Separate business logic from user input/output.
   - Encapsulate execution under standard `if __name__ == '__main__':` block.

Key Concepts:
- Pure functions and return value state management
- Numerical validation and loop guards
- Advanced f-string formatting (`{balance:,.2f}$`)
- Clean terminal menu flow
=============================================================================
"""

def show_balance(balance):
    print("---------------------------------------")
    print(f"Your current balance is {balance:,.2f}$")
    print("---------------------------------------")
    print()


def deposit(amount, balance):
    amount = float(amount)
    return balance + amount


def withdraw(amount, balance):
    amount = float(amount)
    return balance - amount


def check_amount(amount):
    while not amount.replace(".", "").replace("-", "").isdigit() or float(amount) <= 0:
        amount = input("Enter a valid positive number: ")
    print()
    return amount


def main():
    balance = 0.0

    while True:
        print("1: Show Balance")
        print("2: Deposit")
        print("3: Withdraw")
        print("4: Exit")
        action = input("choose number between (1, 2, 3, 4): ").strip()
        print()

        if action == "1":
            show_balance(balance)

        elif action == "2":
            amount_deposit = input("Enter amount to deposit: ").strip()
            amount_deposit = check_amount(amount_deposit)
            balance = deposit(amount_deposit, balance)
            print(f"{amount_deposit}$ deposited successfully\n")

        elif action == "3":
            amount_withdraw = input("Enter amount to withdraw: ").strip()
            amount_withdraw = check_amount(amount_withdraw)
            if float(amount_withdraw) > balance:
                print("Insufficient balance\n")
                continue

            balance = withdraw(amount_withdraw, balance)
            print(f"{amount_withdraw}$ withdrawn successfully\n")

        elif action == "4":
            print("Thank you for using our banking system. Goodbye!")
            break

        else:
            print("Choose a valid option (1, 2, 3, 4)\n")


if __name__ == "__main__":
    main()
