# parent class1
class Vehicle:
    def vehicle_info(self):
        print('Inside vehicle class')

#parent class2
class Car:
    def car_info(self):
        print("Inside car class")

#child class
class SportsCar(Vehicle,Car):
    def sports_car_info(self):
        print("Inside sports car class")

obj = SportsCar()
obj.vehicle_info()
obj.car_info()
obj.sports_car_info()




#another example

class Mammal:
    def mammal_info(self):
        print("Mammals can give direct birth.")

class WingedAnimal:
    def winged_animal_info(self):
        print("Winged animals can flap.")

class Bat(Mammal, WingedAnimal):
    pass

# create an object of Bat class
b1 = Bat()

b1.mammal_info()
b1.winged_animal_info()







# Python example to show the working of multiple
# inheritance


class Base1(object):
	def __init__(self):
		self.str1 = "Geek1"
		print("Base1")


class Base2(object):
	def __init__(self):
		self.str2 = "Geek2"
		print("Base2")


class Derived(Base1, Base2):
	def __init__(self):

		# Calling constructors of Base1
		# and Base2 classes
		Base1.__init__(self)
		Base2.__init__(self)
		print("Derived")

	def printStrs(self):
		print(self.str1, self.str2)


ob = Derived()
ob.printStrs()
