Customer = {'cust1':{'AcntNo': 4010206845,'name':'Gidfred A. Assamoah','type':'Savings','balance':100},
            'cust2':{'AcntNo': 4010226845,'name':'John Doe','type':'Savings','balance':500}
           }

def deposit(Dept):
    Customer['cust1']['balance']= Dept + Customer['cust1']['balance']
    balance = Customer['cust1']['balance']
    print('Your account has been credited with a sum of US$',Dept,'\nBalance is US$', balance,'\n')

def Withdrawal(Wid):
    balance = Customer['cust1']['balance']
    balance = Customer['cust1']['balance'] - Wid
    print('Your account has been debited with a sum of US$',Wid,'\n Balance is US$', balance)



deposit(500)
deposit(500)
Withdrawal(800)

#print(Customer['cust2'])
