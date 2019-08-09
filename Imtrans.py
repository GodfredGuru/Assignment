Customer = {'cust1':{'AcntNo': 4010206845,'name':'Gidfred A. Assamoah','type':'Savings','balance':100},
            'cust2':{'AcntNo': 4010226845,'name':'John Doe','type':'Savings','balance':500}
           }

def deposit(Dept):

    Customer['cust1']['balance']= Dept + Customer['cust1']['balance']
    balance = Customer['cust1']['balance']
    print('Your account has been credited with a sum of US$',Dept,'\nBalance is US$', balance,'\n')

def Withdrawal(Wid):
    if Customer['cust1']['balance'] < Wid :
        balance = Customer['cust1']['balance']
        #balance = Customer['cust1']['balance'] - Wid
        print(' Sorry Insufficient balance \n')
    else:
        balance = Customer['cust1']['balance'] - Wid
        print('Your account has been debited with a sum of US$',Wid,'\nBalance is US$', balance,'\n')



deposit(500)
Withdrawal(800)
deposit(500)


#print(Customer['cust2'])
