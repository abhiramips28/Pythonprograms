"""Define a class, which have a class parameter and have a same instance parameter.
  Hints : Define a instance parameter, need add it in __init__ method.
          you can init a object with construct parameter or set the value later.
"""
class Person:
    #class parameter
    name = "Person"

    def __init__(self,name):
        #instance parameter
        self.name = name

obj = Person("Priya")
print("%s name is %s"%(Person.name,obj.name))

obj2 = Person("shiva")
print("%s name is %s"%(Person.name,obj2.name))
