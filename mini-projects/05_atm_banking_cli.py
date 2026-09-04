"""
Mini Project: ATM / Banking Program
Build a simple terminal ATM program with a main menu:
1. Show Balance - Display current balance formatted with 2 decimal places ($0.00).
2. Deposit - Add a positive amount to balance.
3. Withdraw - Subtract amount from balance (check for sufficient funds).
4. Exit - Quit the program.
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
