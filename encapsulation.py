class BankAccount:
    def __init__(self, initial_balance=0):
        self.__balance = initial_balance  # Private attribute

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited ${amount}. New balance: ${self.__balance}")
        else:
            print("Invalid deposit amount. Please enter a positive value.")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.__balance}")
        elif amount <= 0:
            print("Invalid withdrawal amount. Please enter a positive value.")
        else:
            print("Insufficient balance for withdrawal.")

    def get_balance(self):
        return self.__balance


if __name__ == "__main__":
    account = BankAccount(1000)

    print(f"Initial balance: ${account.get_balance()}")

    account.deposit(500)
    account.withdraw(200)

    print(f"Final balance: ${account.get_balance()}")
    try:
        print(account.__balance)
    except AttributeError:
        print("Cannot access balance directly. Use get_balance() method instead.")
