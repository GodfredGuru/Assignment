class Customer:
    Cust_Cars = []

    def __init__(self,Owner,no_of_Cars):
        self.no_of_Cars = no_of_Cars
        self.Owner = Owner
    def __str__(self):
        return f"\n **** Customer Car Wash **** \nCustomer Cars --> {Customer.Cust_Cars}\n"

    def CarHistory(self,Cars_no):
        Cust_no = 0

        while  Cust_no < self.no_of_Cars:
            newCar = input('Enter new Car Number: ')
            Customer.Cust_Cars.append(newCar)
            print('CAR HISTORY',Customer.Cust_Cars)
            Cust_no = Cust_no + 1
        else:
            print(self.Owner,'Cars at Service:',Customer.Cust_Cars)


cust = Customer('AMA',int(input('Enter number of cars to be Washed: ')))
print(cust)
cust.CarHistory(0)
