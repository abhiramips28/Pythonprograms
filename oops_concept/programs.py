
"""Q. Create a class with instance attributes."""

class Vehicle:
    def __init__(self,name,model):
        self.name = name
        self.model = model

v = Vehicle('strack',2022)
print(f'{v.name} is {v.model} model vechicle')





""" python class and object """

class bike:
    name = ""
    gear = 0

obj = bike()

obj.name = 'honda'
obj.gear = 20

print(f'Name = {obj.name} , Gear = {obj.gear}')



""" Create Multiple Objects of Python Class """

# define a class
class Employee:
    # define an attribute
    employee_id = 0

# create two objects of the Employee class
employee1 = Employee()
employee2 = Employee()

# access attributes using employee1
employee1.employeeID = 1001
print(f"Employee ID: {employee1.employeeID}")

# access attributes using employee2
employee2.employeeID = 1002
print(f"Employee ID: {employee2.employeeID}")



"""Python method"""


# create a class
class Room:
    length = 0.0
    breadth = 0.0

    # method to calculate area
    def calculate_area(self):
        print("Area of Room =", self.length * self.breadth)


# create object of Room class
study_room = Room()

# assign values to all the attributes
study_room.length = 42.5
study_room.breadth = 30.8

# access method inside class
study_room.calculate_area()