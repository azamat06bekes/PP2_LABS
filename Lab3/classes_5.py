# 5th Task

class BankAccount:
    def __init__(self, power, balance = 0):
        self.power = power 
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}. New balance: {self.balance}")
        else:
            print("Deposit amount must be positive.")

    def withdrawal(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance: {self.balance}")
        else:
            print(f"Insufficient balance. You have {self.balance}, but tried to withdraw {amount}.")

account = BankAccount(power=5, balance=1000)

account.deposit(500)
account.deposit(200)

account.withdrawal(300)
account.withdrawal(2000)

print(f"Final balance: {account.balance}")
