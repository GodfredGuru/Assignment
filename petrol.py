print('===============================================\n WELCOME TO FELT PETROL FILLING STATION \n===============================================')
class Petrol:
    # PORT 1 IS FOR MOSES
    PortA = 0
    # PORT 2 IS FOR DANIEL
    PortB = []
    Attendants = ['MOSES','DANIEL']


    # PORT SELECTION
    def Port(self,port_selxn=1):
        self.port_selxn = port_selxn
        #selecting a port to buy 1--> Port A
        self.port_selxn = int(input('Choose a Filling Port:\n1-->Port A\n2-->Port B\nSelect your port: '))

        if self.port_selxn ==1:
            # entrying amount to buy at port A
            purchase_time = int(input('Enter the number of times to purchase: '))
            while purchase_time < 3:
                price = int(input('\nEnter Amount to Purchase: '))
            # Adding amount purchased to port
                Petrol.PortA = Petrol.PortA + price
                print(Petrol.PortA)
            purchase_time  = + 1

            # this section is for port B
        elif self.port_selxn==2:
            price = int(input('\nEnter Amount to Purchase: '))
            # adding amount purchased to port
            Petrol.PortB = Petrol.PortB + price
            print(Petrol.PortB)



a = Petrol()
a.Port()
