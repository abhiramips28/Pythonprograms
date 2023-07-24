"""Nested Function"""
def outer_func():
    def inner_func():
        print('Hi dears')
    inner_func()
outer_func()


def increment(number):
    def inner_increment():
        return number + 1
    return inner_increment()
print(increment(10))

