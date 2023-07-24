"""Create a class called Vehicle with the following attributes and methods:

Attributes:
make: a string representing the make of the vehicle
model: a string representing the model of the vehicle
year: an integer representing the year the vehicle was made
color: a string representing the color of the vehicle
mileage: a float representing the current mileage of the vehicle

Methods:
__init__(self, make, model, year, color, mileage): initializes the attributes with the given values
drive(self, distance): takes a float representing the distance driven and updates the mileage attribute accordingly
get_info(self): returns a string with the vehicle's make, model, year, color, and mileage attributes in a formatted way

Create a subclass called Car that inherits from the Vehicle class with the following additional attributes and methods:

Attributes:
num_doors: an integer representing the number of doors the car has
engine_type: a string representing the type of engine the car has

Methods:
__init__(self, make, model, year, color, mileage, num_doors, engine_type): initializes the attributes with
the given values
get_info(self): overrides the get_info method of the Vehicle class to include the num_doors and engine_type attributes
Create an instance of the Vehicle class and call the drive method with a distance of 100. Then call the get_info
 to print out the vehicle's information.

Create an instance of the Car class and call the drive method with a distance of 50. Then call the get_info method
to print out the car's information.

"""

class Vehicle:
    def __init__(self,make,model,year,color,mileage):
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        self.mileage = mileage

    def drive(self):
        