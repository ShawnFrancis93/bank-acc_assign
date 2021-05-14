class BankAccount:
    def __init__(self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount

        return self
    
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds: $35 fee will be charged to account.")
            self.balance -= 35
        self.balance -= amount

        return self

    def display_account_info(self):
        print(f"Current balance: {self.balance}")

        return self

    def yield_interest(self):
        self.balance += self.balance * self.int_rate

        return self

Acc1 = BankAccount(0.2, 100)
Acc2 = BankAccount(0.1, 100)


Acc1.deposit(200).deposit(300).deposit(500).withdraw(400).yield_interest().display_account_info()

Acc2.deposit(750).deposit(120).withdraw(100).withdraw(100).withdraw(200).withdraw(20).yield_interest().display_account_info()