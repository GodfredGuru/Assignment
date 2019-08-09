import datetime, calendar
today = datetime.date.today()
print('\nHello, Welcome to ZENITH BANK: ')
name= input('\nPlease what is your name: ')
print('Hope, you are good:   ',name)
Atype1, Atype2= ['Savings','Current']

Account_No = [4010206845,4010206846,4010206849]


open_Account=int(input('Open Account with Us: 1-->yes:  '))
if open_Account ==1:
    A_type = int(input('What is your prefered account type: 1-->savings, 2-->Current: '))
    Initial_Deposit = float(input('Please how much would like to Deposit: $'))
    if A_type ==1:
        print('You have Successfully Opened a',Atype1,'account with Zenith Bank')
        print('\nAccount Details:\nAccount Name:',name,'\nAccount type:',Atype1,'\nAccount No.: ',Account_No[0],'\nCurrent Balance:$',Initial_Deposit,'\nOpened on:',today)
    elif A_type ==2:
        print('You have Successfully Opened a',Atype2,'account with Zenith Bank')
        print('\nAccount Details:\nAccount Name:',name,'\nAccount type:',Atype2,'\nAccount No.:',Account_No[1],'\nCurrent Balance:$',Initial_Deposit,'\nOpened on:',today)
