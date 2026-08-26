"""
Problem: ATM / Bank Account Simulation CLI

Requirements:
1. Maintain and display a stateful account balance formatted as standard currency with two decimal places (e.g., $1,250.00).
2. Implement a deposit function that takes a validated positive numeric amount and returns the updated account balance.
3. Implement a withdrawal function with overdraft protection that rejects transactions exceeding available funds.
4. Validate all numerical user inputs defensively against negative numbers and non-numeric values.
5. Structure the application using modular pure functions and an `if __name__ == '__main__':` entry point.

Concepts: Modular function architecture, state tracking, currency f-string formatting (`{balance:,.2f}$`), input validation, entry-point modularity.
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
