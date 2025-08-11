# bank_account.py

class BankAccount:
    def __init__(self, initial_balance=0.0):
        """
        Initialize a new bank account with an optional initial balance.
        """
        self.account_balance = initial_balance

    def deposit(self, amount):
        """
        Deposit a specified amount into the account.
        """
        if amount > 0:
            self.account_balance += amount
            return True
        return False

    def withdraw(self, amount):
        """
        Withdraw a specified amount from the account if funds are sufficient.
        Returns True if successful, False otherwise.
        """
        if 0 < amount <= self.account_balance:
            self.account_balance -= amount
            return True
        return False

    def display_balance(self):
        """
        Print the current balance in a user-friendly format.
        """
        print(f"Current balance: ${self.account_balance:,.2f}")

# main-0.py

import sys
#from bank_account import BankAccount

def main():
    if len(sys.argv) < 2:
        print("Usage: python main-0.py <operation> [amount]")
        print("Operations: deposit <amount>, withdraw <amount>, balance")
        sys.exit(1)

    operation = sys.argv[1].lower()
    account = BankAccount(100.0)  # Start with a sample balance

    if operation == "deposit":
        if len(sys.argv) != 3:
            print("Usage: python main-0.py deposit <amount>")
            sys.exit(1)
        amount = float(sys.argv[2])
        if account.deposit(amount):
            print(f"Deposited ${amount:,.2f}")
        else:
            print("Deposit amount must be positive.")

    elif operation == "withdraw":
        if len(sys.argv) != 3:
            print("Usage: python main-0.py withdraw <amount>")
            sys.exit(1)
        amount = float(sys.argv[2])
        if account.withdraw(amount):
            print(f"Withdrew ${amount:,.2f}")
        else:
            print("Insufficient funds or invalid amount.")

    elif operation == "balance":
        account.display_balance()

    else:
        print("Invalid operation. Use: deposit, withdraw, or balance.")

if __name__ == "__main__":
    main()
