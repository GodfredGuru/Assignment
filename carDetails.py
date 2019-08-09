class carDetails:
    def __init__(self,car_driver,car_num,car_color):
        self.car_num = car_num
        self.car_driver = car_driver
        self.car_color = car_color

    def __str__(self):
        return f"\n                  CAR DETAILS\n*********************************************\nCar Owner: {self.car_driver}\nCar Color: {self.car_color} \nCar Number: {self.car_num}\n*********************************************"

car = carDetails('DeGREAT','GT 1010 A','Black Range Rover')
#car.registration()
print(car)

#if __name__=="__main__":
