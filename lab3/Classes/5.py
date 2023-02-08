class BankAccount:
    def __init__(self,owner,balance):
        self.owner= owner
        self.balance=balance
    def deposit(self, amount):
        self.balance += amount
        print(f"{amount} deposited to the account of {self.owner}.")
    def withdraw(self, amount):
        if amount > self.balance:
            print(f"Withdrawal failed. Insufficient balance.")
        else:
            self.balance -= amount
            print(f"{amount} withdrawn from the account of {self.owner}.")