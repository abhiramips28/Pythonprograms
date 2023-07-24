#Q1. Write a python program to convert json data to python object.

# import json
# a = {"name":"anvi","place":"chry"}
# y = json.dumps(a)
# print(y)
# print(type(y))


#Q2. Write a python program to convert python object to json data.
# import json
# a = '{"name":"anvi","place":"chry"}'
# y = json.loads(a)
# print(y)
# print(type(y))

#Q3. Write python program to convert python object into json strings. print all the values.

# import json
#
# dict1 = {"name":"anvi","age":3}
# list1 = ["Red","pink",1,2]
#
# a = json.dumps(dict1)
# b = json.dumps(list1)
#
# print(a)
# print(b)
#
# print(type(a))
# print(type(b))


#Q4.  Write a python program to convert python dictionary object(sort by key) to json data. print the object members
#       with indent level 4.








#Q4.
#
# import json
#
# dict1 = '{"name":"anvi","age":3,"place":"chry"}'
# list1 = '["pink",5,3]'
# x = json.loads(dict1)
# y = json.loads(list1)
# print(x)
# print(type(x))
# print(y)
# print(type(y))


"""
Write a python program to generate a random color hex, a random alphabetical string random value between two integers
and a random multiple of 7 between 0 and 70.
"""

import random
random_numb = random.randint(0,16777215)
hex_num = str(hex(random_numb))
print(hex_num)
hex_num = '#' + hex_num[2:]
print("hex color code is",hex_num)


import random

print(random.choice())

import random
print("Generate a random value between two integers : ")
print(random.randint(1,10))
print(random.randint(-5,5))

print("Generate a random multiple of 7 between 0 and 70:")
print(random.randint(0, 10) * 7)