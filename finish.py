import customer,datetime
myDate = datetime.datetime.now()
print('Attendant Asigned at: ',myDate,'\nCar would be ready in an Hour time')


class Finish:
    wash_charge  = 30.0
    delay_charge = 2.0

    def Take(self,taken,T_charge):
        #self.Ready = taken
# CUSTOMER ENTERS 0 OR 1 TO PICK CAR OR AN HOUR TIME BASED ON THE INPUT THE PRINT ACTIONS ARE EXECUTED.
        if taken ==0:

            print('Thanks for using our Service\nCharge: $',Finish.wash_charge)

        else:
            T_charge = Finish.wash_charge+Finish.delay_charge
            print('THANKS FOR USING OUR SERVICE\nCHARGE:',T_charge)

# INSTANTIATION OF THE CLASS FINISH
aman = Finish()
aman.Take(int(input('CAR WASHED SELECT ACTION:\n0-->Picked Up\n1--> An hour time\nWHEN ARE YOU PICKING UP: ')),20)
