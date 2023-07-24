"""
    Functions :- It is a block of codes,it executed whenever the functions is called.
                 keyword - def
                 >user-defined function
                 >built-in function
                 >lambda

"""
# def test_fun():
#     print("hi")
# test_fun()
#
# def sum():
#     a = 10
#     b = 20
#     c = a + b
#     print(c)
# sum()
#
#
# a = 20
# b = 20
# def sum1():
#     c = a + b
#     print(c)
# sum1()
#
# def sum():
#     a = int(input("enter the numbers : "))
#     b = 10
#     c = a + b
#     print(c)
# sum()
#
# def sum(a,b):
#     c = a + b
#     print(c)
# sum(1,2)
#
# def sum(a,b):
#     c = a + b
#     return c
# print(sum(2,2))
#
# def sum(a,b,d,g):
#     c = a + b
#     v = d + g
#     res = a * b
#     return c,v,res
# print(sum(6,6,5,4))

# Arguments(args)/positional args
# def my_function(msg1,msg2):
#     print(msg1 + msg2)
# my_function(("How","are", "you?"),("python","django","abc"))
# my_function("how are you"," hi dears")

# def my_function(fname, lname):
#   print(fname + " " + lname)
#
# my_function("Emil", "Refsnes")


# Arbitary arguments,(*args)
# def my_function(*kids):
#   print("The youngest child is " + kids[2])
#
# my_function("Emil", "Tobias", "Linus")
#
# def my_fun(*names):
#     print("Hi",names,"How are you?")
# my_fun("jain")
# my_fun("jerin")


# # Keyword arguments
'''You can also send arguments with the key = value syntax.'''

# def my_funct(Name1,Name2,Name3):
#     print("last name is "+Name3)
# my_funct(Name1="jain",Name2="jack",Name3="jerin")



# Arbitary keyword arguments(** )
''' many keyword arguments that will be passed into your function, 
 add two asterisk: ** before the parameter name in the function definition.'''
def my_function(**kid):
  print("last name is " + kid["lname"])

my_function(fname = "Anvitha", lname = "V")



# Default parameter value
def my_function(country = "Norway"):
  print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")



# passing a list of arguments
# def my_function(food):
#   for x in food:
#     print(x)
#
# fruits = ["apple", "banana", "cherry"]
#
# my_function(fruits)
#



# Return values
# def my_function(x):
#   return 5 * x
#
# print(my_function(3))
# print(my_function(5))
# print(my_function(9))