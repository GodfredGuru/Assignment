import datetime,calendar
today = datetime.date.today()
decision=[1,2,3]
Atype1, Atype2= ['Savings','Current']
Account_No = [4010206845,4010206846,4010206849]
class ATM():

    def __init__(self,name,Account_type,decicion,Account_No,balance,pin):
        self.name=name
        self.Account_type=Account_type
        self.balance=balance
        self.Account_No=Account_No
        self.pin=pin
        self.decision=decision
    def __repr__(self):
          return f"\nAccount Name: {self.name}\nAccount Type: {self.Account_type}\nAccount Number: {self.Account_No}\nAccount Pin: {self.pin}\nCurrent Balance: ${self.balance}\nDate Opened: {today}"
    def Condition(self,decision):
        decision = int(input('What would you like to do:\n 1-->check Balance\n2-->Withdrawal\n3-->Deposit: '))
        if self.decision ==1:
            print('\nAccount Details:\nAccount Name:',{self.name},'\nAccount type:',Atype1,'\nAccount No.: ',Account_No[0],'\nCurrent Balance:$',{self.balance},'\nOpened on:',today)
        elif self.decision==2:
            def Withdrawal(self,W_Amt):
                if W_Amt >= self.balance: #self.balance = self.balance - W_Amt
                    print('\nSorry',self.name,'\nInsufficient balance for withdrawal','\nCurrent Balance: $',self.balance)
                else:
                    self.balance = self.balance - W_Amt
                    print('Remaining Balance: $',self.balance)
        else:
            def Deposit(self,Dept_Amt):
                self.balance = self.balance + Dept_Amt
                print('Your Account',self.Account_No,'has been credit with a sum of: $',Dept_Amt)
                print('Current Balance: $',self.balance)


cust_1=ATM(input('Enter your name: '),input('Enter preferred type of Acount: '),int(input('What would you like to do:\n 1-->check Balance\n2-->Withdrawal\n3-->Deposit:')),'4010206845',500,'123')
#cust_1.Deposit(1000)
cust_1.Condition(decision)
print(cust_1)
