"""
  In Python, a decorator is a design pattern that allows you to modify the functionality of a function
  by wrapping it in another function.

   The outer function is called the decorator, which takes the original function as
    an argument and returns a modified version of it.


"""

# def make_pretty(func):
#     def inner():
#         print("I got decorated")
#         func()
#     return inner
#
#
# def ordinary():
#     print("I am ordinary")
#
# ordinary()

# def make_pretty(func):
#     # define the inner function
#     def inner():
#         # add some additional behavior to decorated function
#         print("I got decorated")
#
#         # call original function
#         func()
#
#     # return the inner function
#     return inner
#
#
# # define ordinary function
# def ordinary():
#     print("I am ordinary")
#
#
# # decorate the ordinary function
# decorated_func = make_pretty(ordinary)
#
# # call the decorated function
# decorated_func()



def make_pretty(func):

    def inner():
        print("I got decorated")
        func()
    return inner

@make_pretty
def ordinary():
    print("I am ordinary")

ordinary()


#another example


def upper_decor(fun):
    def wrapper(name):
        result = fun(name)
        return result.upper()
    return wrapper

@upper_decor
def hello_name(name):
    return "hello"+name

print(hello_name(" vishnu"))



def add(x,y):
    return x+y
def calculate(func , x,y):
    return func(x,y)
result = calculate(add,4,8)
print(result)