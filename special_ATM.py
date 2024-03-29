import datetime

class account:
    account_number = None
    owner =  None
    pin = None
    balance = None
    type = None

    def __init__(self,type,owner,account_number,pin,balance):
        self.type = type
        self.owner = owner
        self.account_number = account_number
        self.pin = pin
        self.balance = balance

        owner = "Martin Ampem Affram"
        type = "Checking Account" or "Savings Account"
        account_number = int(12345678)
        pin = int(1234)
        balance = int(20000)

    def debit(self,amount):
        debit_balance = self.balance - amount
        return str(debit_balance)

    def credit(self,amount):
        credit_balance = self.balance + amount
        return str(credit_balance)
    #End of the class.

class ATM(account):

    print('\nATM booted up successfully....\n')

    def atm_print(self,message):
        print('*'*50)
        print(message)
        print('*'*50)

    def format_option(self,number,option):
        return "\t{}.\t{}".format(number,option)


    def atm_options(self):
        return "\n\n{}\n{}\n{}\n{}\n{}\n".format(self.format_option("1","Withdraw cash"), self.format_option("2","Deposit Cash"), self.format_option("3","Check Balance"), self.format_option("4","View History"), self.format_option("5", "Exit"))

    def validate_input(self, inputValue):
            try:
                return inputValue.isdigit() and int(inputValue) >0
            except AttributeError:
                return False

    def validate_and_return_amount(self):
        amount = input("Enter 'x' to terminate.\tAmount in GHC\n")
        while self.validate_input(amount)==False or int(amount)%10 != 0 or amount.lower() =='x':
            if amount.lower() =='x':
                return False
            self.atm_print("Invalid amount. Please enter a correct value.\nAmount should be multiple of 10 ")
            amount = input("Enter 'x' to terminate.\tAmount in GHC\n")
        return int(amount)

    def validate_option(self,inputValue):
        return self.validate_input(inputValue) and int(inputValue) <= 5

    def print_options(self):
        self.atm_print(self.atm_options())
        # option = input("\n")

    def enter_options_screen(self):
        self.print_options()
        choice = self.prompt_chooose_option()
        while self.validate_option(choice)==False or  choice == '5':
            if self.validate_option(choice) and choice == '5':
                self.say_goodbye()
            self.atm_print("Invalid selection. Enter number 1 -5 ")
            choice = self.prompt_chooose_option()
        return choice

    def get_account_details(self, retry,pin_attempts_left):
        if retry:
            self.atm_print("\nError.\nInvalid account number/PIN. Try again\nPin Attempts left:\t{}".format(str(pin_attempts_left)))

        while True:
                try:
                    pin = input("Enter PIN\n")
                    account_number = input("\nEnter account number\n")
                    self.atm_print("Validating details.....")
                    if pin == self.pin and account_number == self.account_number:
                        print("Login successful.")
                except ValueError:
                    print("Invalid account number or pin. \nPlease try again. Attempts left:\t{}".format(str(pin_attempts_left)))
                else:
                    break
                return {"account_number": account_number, "pin" : pin}

    def welcome_message(self):
        self.atm_print("\nWelcome. Please enter account details\n")

    def print_yes_or_no(self):
        self.atm_print("\n\n{}\n{}\n".format(self.format_option("1", "YES"),self.format_option("2", "NO")))
        return input("\t\tEnter 1 or 2\n")


    def return_boolean_from_input(self, message=None):
        message = "Continue ?\n" if message == None  else message
        print(message)
        inputValue = self.print_yes_or_no()
        while self.validate_input(inputValue) == False and (inputValue!='1' or inputValue !='2'):
            print("Invalid selection.")
            inputValue = self.print_yes_or_no()
        return int(inputValue)==1

    def enter_withdrawal_option(self,account):
        self.atm_print("Please enter amount to withdraw from account\nAmount should be multiple of 10")
        amount = self.validate_and_return_amount()
        if amount == False:
            self.atm_print("Transaction terminated")

        else:
            debit = self.debit(amount)
            return debit
        #Amount is deducted from account

        self.atm_print("Transaction successful.\nNew Balance : " + debit)


    def enter_deposit_option(self,account):
        self.atm_print("Please enter amount to deposit into account\nAmount should be multiple of 10")
        amount = self.validate_and_return_amount()
        if amount == False:
            self.atm_print("Transaction terminated")
            return
        else:
            new_balance = self.credit(amount)
            return new_balance
        #Amount is added to account

        self.atm_print("Transaction successful.\nNew Balance : " + new_balance)

    def enter_check_balance_option(self,account):
        self.atm_print("Account balance is : GHC {}".format(self.balance))

    def enter_view_history_option(self,account):
        transaction_history = []
        transaction = {'date': datetime.datetime.now().strftime('%c'), 'amount' : self.balance}
        transaction_history.append(transaction)
        self.atm_print("printing history...")
        self.atm_print(str(transaction_history))

    def prompt_chooose_option(self):
        return input("Select a valid option\n")

    def say_goodbye(self,message=None):
        message = "" if message == None else message
        self.atm_print("{}\n\tThank you for using our services.\n\t\tGoodbye\n\t{}".format(message,datetime.datetime.now().strftime("%c")))
        exit()

    def run_atm(self):
        self.welcome_message()
        account_details = self.get_account_details(False,3)
        # # check if account details are correct
        #correct_details = account.checkDetails(account_details)
        # #correct_details = False
        pin_attempts_left= 3
        # # account number and pin tries
        while account_details==False:
             pin_attempts_left-=1
             if pin_attempts_left==0:
                 self.say_goodbye("You have attempted 3 wrong PIN.\nCard retained")
             account_details = self.get_account_details(True, pin_attempts_left)
             if account_details.get("pin")=="1234":
                 account_details = True
        # #end pin tries

        self.atm_print("Details validated. Welcome")

        # = self.prompt_chooose_option()
        continue_transaction = True
        while continue_transaction:
            choice = self.enter_options_screen()
            if choice == '1': #withdrawal option
                self.enter_withdrawal_option(account)
            elif choice == '2':
                self.enter_deposit_option(account)
            elif choice == '3':
                self.enter_check_balance_option(account)
            elif choice == '4':
                self.enter_view_history_option(account)

            continue_transaction = self.return_boolean_from_input()
        # say goodbye when no more transaction left
        self.say_goodbye()

#Class to hold account information for the bank.

atm = ATM("Martin Ampem Affram", "Checking Account",str(12345678), int(1234), int(20000))
atm.run_atm()
