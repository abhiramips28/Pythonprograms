"""
print

0 b
1 a
2 n
3 a
4 n
5 a
"""

# str1 = 'banana'
# for i in range(len(str1)):
#     print(f'{i},{str1[i]}')
#

"""
Q1. Create a string made of the first, middle and last character.

str1 ='Anvitha'
o/p = aia

"""

# str1 = input("Enter the name : ")
# first = str1[0]
# print(first)
# l = len(str1)
# # print(l)
# mid = int(l/2)
# print(str1[mid])
# first = first + str1[mid]
# first = first + str1[l-1]
# print(str1[l-1])
# print("new string : ",first)


"""
Q2. To append the new string into the middle of 1st string. 
      s1 = 'hello'
      s2 = 'world'
      o/p = heworldllo

"""
#
# s1 = 'hello'
# s2 = 'world'
# l = len(s1)
# mid = int(l/2)
# x = s1[:mid]
# print(x)
# x = x + s2
# print(x)
# x = x + s1[mid:]
# print("After appending the string :",x)


"""
Q3. Arrange string characters such that lowercase letters should come first 
    str1 = "HeLLO World"
    o/p = eorldHLLOW

"""
# str1 = "HeLLO World"
# a = str1[1]
# b = str1[7:]
# c = a + b
# print(c)
# x = str1[0]
# y = str1[2:7]
# z = x + y
# print(z)
# print(c+z)

#correct method
#
# str1 = input("Enter the name : ")
# lower = ""
# upper = ""
# special = ""
# for char in str1:
#     if char.islower():
#         lower += char
#         print(lower)
#     elif char.isupper():
#         upper += char
#         print(upper)
#     else:
#         special += char
#         print(special)
# print('Result ',lower + upper + special)


"""
Q4. Count all letters,digits & special symbols from a given strings.
    eg - str1 = "p@#$yn26at^:5ve"
 """
# str1 = input("Enter the strings : ")
# l = d = sym = 0
# for i in str1:
#     if i.isalpha():
#         l = l + 1
#     elif i.isdigit():
#          d += 1
#     else:
#         sym += 1
# print("number of letters = ",l)
# print("number of digits = ",d)
# print("number of sym = ",sym)