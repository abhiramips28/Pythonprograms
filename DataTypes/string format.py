# String formatting
"""
Python f-string

     Python f-string is the newest python syntax to do string formatting.
     It is available since python 3.6.
     Python f-strings prpvide a faster, more readable, more concise, & less error prone way of
     formatting string in python.

     The f-string have the f prefix &  use {} brackets to evaluate values.

"""

name = 'anvitha'
age = '5'

# print('%s is %d years old' % (name,age))
print('{} is {} years old'.format(name,age))
print(f'{name} is {age} years old')


bags = 3
apples_in_bag = 12

print(f'There are total of {bags * apples_in_bag} apples')