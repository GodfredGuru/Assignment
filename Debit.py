import BANK
class Debit_Card:
    CardNo:''
    OwnedBy = ''
    def __init__(self,Card,Owner):
        self.Card = Card
        self.Owner = Owner
    def Access(self):
        print('Card Number:',self.Card,' Card Owner: ',self.Owner,'\n**********************************************************')
        #return f"Card Number: {self.Card}\nCard Owner:{self.Owner}"
aman = Debit_Card('4010206845','fred amnugui')
aman.Access()
#print(aman)
