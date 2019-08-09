class Account():
    charge = 0.1
    def __init__(self,name,balance):
        self.name=name
        self.balance=balance
    def __str__(self):
        return f"your balance is {self.balance}"
    def withdraw(self,amount):
        self.balance=self.balance-amount-(amount*Account.charge)
        print(self.balance)
acnt = Account('Isaac',4000)
acnt.withdraw(4)
print(acnt)
