class BankAcc():
    def __init__(self, name, balance):
        self.name = name 
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Balance:", self.balance)

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Balance:", self.balance)
        else: 
            print("Unsufficient funds")

acc = BankAcc("Miras", 1000)
acc.withdraw(200)
acc.deposit(350)


