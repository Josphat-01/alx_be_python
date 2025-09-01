
class BankAccount:
    def __init__(self, current_balance=0.0):
        """Initialize the account with an optional initial balance (default = 0)."""
        self.__account_balance = float(current_balance)

    def deposit(self, amount):
        """Deposit a positive amount into the account."""
        if amount > 0:
            self.__account_balance += amount
            return True
        return False

    def withdraw(self, amount):
        """Withdraw an amount if sufficient balance exists.
        Returns True if successful, otherwise False.
        """
        if 0 < amount <= self.__account_balance:
            self.__account_balance -= amount
            return True
        return False

    def display_balance(self):
        """Return a formatted string with the current balance."""
        return ("Current balance: ${self.__account_balance:.2f}")
