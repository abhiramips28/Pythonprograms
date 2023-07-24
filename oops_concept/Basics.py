"""
class :

object :

constructor :

self :

__str__() :


"""





class Myclass:
    x = 6

obj = Myclass()
print(obj.x)



class Parrot:

    # class attribute
    name = ""
    age = 0

# create parrot1 object
parrot1 = Parrot()
parrot1.name = "Blu"
parrot1.age = 10

# create another object parrot2
parrot2 = Parrot()
parrot2.name = "Woo"
parrot2.age = 15

# access attributes
print(f"{parrot1.name} is {parrot1.age} years old")
print(f"{parrot2.name} is {parrot2.age} years old")


# class Car:
#     name = ' '
#     model = 2015
#
# car1 = Car()
# car1.name = 'vento'
# car1.model = 2015
#
# car2 = Car()
# car2.name = 'polo'
# car2.model = 2019
#
# print(f'{car1.name} is {car1.model} model car')
# print(f'{car2.name} is {car2.model} model car')
#

# class Car:
#     def __init__(self,name,model):
#         self.name = name
#         self.model = model
#     def test(self):
#         print('hi')
# car1 = Car("vento",2015)
# car1.test()
# print(f'{car1.name} is {car1.model} model car')



# class Car:
#     def __init__(self,name,model):
#         self.name = name
#         self.model = model
#
#     def __str__(self):
#         return f'{self.name}({self.model})'
#
# car1 = Car("vento",2015)
# print(car1)
# print(f'{car1.name} is {car1.model} model car')
