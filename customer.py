import BANK, Debit
class Customer:
    name = ''
    Cust_Add = ''
    DoB = ''
    def __init__(self,Cust_name,Cust_Address,DoB):
        self.Cust_name = Cust_name
        self.Cust_Address = Cust_Address
        self.DoB = DoB
    def Own(self):
        print('Customer Name:',self.Cust_name,'Customer Address:',self.Cust_Address,'Date of Birth:',self.DoB)


aman = Customer(input('Please enter your name: '),input('Please enter your Address: '),input('Please enter your Date of Birth: '))
aman.Own()
