import carDetails
from carDetails import carDetails
class Registration:
    circle = []
    newtown = []
    def __init__(self,Area1,Area2):
        self.Area1 = Area1
        self.Area2 = Area2
    def Display(self,Area):
        if Area==1:
            if len(Registration.circle)==1:
                print('sorry Circle is Full')
            else:
                Registration.circle.append(self.Area1)
                print('Circle at',Registration.circle)
        elif Area==2:
            Registration.newtown.append(self.Area2)
            print('Circle ',Registration.newtown)
        else:
            print('Please the selected AREA does not exit')


car = Registration('GT 0001 V','GA 1010 C')
car.Display(int(input('\nSelect a parking Area:\n1--> Circle\n2--> NewTown\n***********************************************\nSelect your Option: ')))
