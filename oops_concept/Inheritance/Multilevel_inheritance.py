
class Vehicle:  #parent class
    def Vehicle_info(self):
        print('inside vehicle class')

class Car(Vehicle):   #child class
    def car_info(self):
        print('inside car class')

class Sportscar(Car):
    def sports_car_info(self):
        print('inside sports car class')

car = Car()
car.car_info()

car.Vehicle_info()

sportscar = Sportscar()

sportscar.sports_car_info()


#another example

class Grandfather:
    def ownhouse(self):
        print("Grandpa House")

class Father(Grandfather):
    def ownbike(self):
        print("Father's Bike")

class Son(Father):
    def ownbook(self):
        print("son have a book")

a = Grandfather()
a.ownhouse()

b = Father()
b.ownbike()

c = Son()
c.ownbook()