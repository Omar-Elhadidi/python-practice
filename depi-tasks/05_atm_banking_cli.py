"""
Problem: ATM / Bank Account Simulation CLI

Requirements:
1. Maintain and display a stateful account balance formatted as currency with two decimal places.
2. Implement a deposit function that takes a validated positive numeric amount and returns the updated account balance.
3. Implement a withdrawal function that checks for sufficient funds before updating balance.
4. Validate user inputs so deposit and withdrawal amounts are positive numbers.
5. Structure the application using functions and an `if __name__ == '__main__':` entry point.

Concepts: Function return values, state tracking, currency formatting (`{balance:,.2f}$`), input validation, `if __name__ == '__main__'`.
"""

def show_balance(balance):
    print("---------------------------------------")
    print(f"Your current balance is {balance:,.2f}$")
    print("---------------------------------------"), print()


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
            print(f"{amount_deposit}$ deposited sucessfully")
            print()

        elif action == "3":
            amount_withdraw = input("Enter amount to withdraw: ").strip()
            amount_withdraw = check_amount(amount_withdraw)
            if float(amount_withdraw) > balance:
                print("insuffcient balance")
                print()
                continue

            balance = withdraw(amount_withdraw, balance)
            print(f"{amount_withdraw}$ withdrwan sucessfully")
            print()

        elif action == "4":
            break

        else:
            print("choose valid number from (1, 2, 3, 4)")


if __name__ == "__main__":
    main()
