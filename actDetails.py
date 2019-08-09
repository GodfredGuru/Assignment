import datetime, calendar
today = datetime.date.today()

class ATM():
    def __init__(self,name,balance,pin,accountNo):
          self.name = name
          self.balance = balance
          self.pin = pin
          self.accountNo = accountNo

    def __str__(self):
         return f"\nAccount Name: {self.name}\nAccount Balance: ${self.balance}\nAccount Pin: {self.pin}\nAccount Number: {self.accountNo}\nDate:{today}"

    def Withdrawal(self,W_Amt):
        if W_Amt >= self.balance or self.balance<=50: #self.balance = self.balance - W_Amt
            print('\nSorry',self.name,'\nInsufficient balance for withdrawal','\nCurrent Balance: $',self.balance,'\n')
        else:
            self.balance = self.balance - W_Amt
            print('Remaining Balance: $',self.balance)
    def Deposit(self,Dept_Amt):
        self.balance = self.balance + Dept_Amt
        print('Your Account',self.accountNo,'has been credit with a sum of: $',Dept_Amt)
        print('Current Balance: $',self.balance)


Emmanuel = ATM('Mr. Emmanuel Appau',100,123,4010206445)
print(Emmanuel)

#DECISIONS TO BE TAKEN
Emmanuel.Withdrawal(100)
Emmanuel.Deposit(1000)
# Emmanuel.Withdrawal(500)
# Emmanuel.Withdrawal(400)
# Emmanuel.Withdrawal(100)
