class University:
    def __init__(self):
        self.name = 'Yele University'
        print('You are in university class constructor')

    def test(self):
        print("Test Function")

class College(University):
    def __init__(self):
        self.name = 'Yale school of medicine'
        print("you are in college class constructor")

    def show(self):
        print("College class instance method : ",self.name)

u = University()
u .test()

c = College()
c.show()
c.test()



#another example


class Vehicle:  #parent class
    def Vehicle_info(self):
        print('inside vehicle class')

class Car(Vehicle):   #child class
    def car_info(self):
        print('inside car class')

car = Car()
car.car_info()

car.Vehicle_info()




# A Python program to demonstrate inheritance

# Base or Super class. Note object in bracket.
# (Generally, object is made ancestor of all classes)
# In Python 3.x "class Person" is
# equivalent to "class Person(object)"


class Person(object):

	# Constructor
	def __init__(self, name):
		self.name = name

	# To get name
	def getName(self):
		return self.name

	# To check if this person is an employee
	def isEmployee(self):
		return False


# Inherited or Subclass (Note Person in bracket)
class Employee(Person):

	# Here we return true
	def isEmployee(self):
		return True


# Driver code
emp = Person("Geek1") # An Object of Person
print(emp.getName(), emp.isEmployee())

emp = Employee("Geek2") # An Object of Employee
print(emp.getName(), emp.isEmployee())
