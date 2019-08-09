import datetime,calendar
today = datetime.date.today()
print('==============================\n     Welcome to Zenith Bank    \n===============================')
Pin_code=input('Please Enter your Pin Code: ')

if Pin_code=='123':
    print('Welcome',Customer.name)
else:
    print('Pin codes dont match')


# ==========    1     ============
class Bank():
    code = [123]
    address = 'Box 45, East NewTown'
    def __init__(self,Bank_name,Bank_branch):
        self.Bank_name=Bank_name
        self.Bank_branch=Bank_branch
    def __str__(self):
        return f"\nBank Name: {self.Bank_name}\nBank Address: {Bank.address}\nBank Branch: {self.Bank_branch}\n"
#def Manages():
# def Mantains():

# ==========    2     ============
class ATM():
    location = 'Ring Road'
    managed_By = 'Mr. Emmanel Appau'
    def identifies(self):
    def transactions(self):

#
# # ==========    3     ============
class ATM_Transaction():
    transaction_ID
    date = today
    type = ['Visa','Master','Ready Cash']
#
#     # METHOD OF ATM TRANSACTION
#     def Update():
#
# # ==========    4     ============
class Withdrawal_transaction():
    amount= ''
    def withdrawal(self,Withdrawal_Amount):
#
# # ==========    5     ============
class Transfer_Transaction(ATM_Transaction):
    # amount = ''
    # account_no =''

# # ==========    6     ============
class Account(ATM_Transaction):
    # type = ''
    # owner= ''
    def check_balance():

# # ==========    7     ============
class Savings_Account(Account):
    Account_no = ''
    def debit():
    def credit():
#
# # ==========    8     ============
class check_account(Account):
    Account_no = ''
    def debit():
    def credit():
# #
# # # ==========    9     ============
class Customer():
    name = 'Winifred Ofori'
    Address ='Bantama East, Hse.No: 248/16'
    DoB = '10th May 2000'
    def owns(self,Pin_code):

# #
# # # ==========    10     ============
class Debit_card():
    Card_no = ''
    owned_by = ''
    def access():
ama=Bank('Zenith Bank','Patrice Lumamba Branch')
print(ama)
