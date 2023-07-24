'''Find the sum of n natural numbers.'''

def sum_natural(n):
    sum = 0
    for i in range(1,n+1):
        print(i)
        sum = sum + i
    return sum
n = int(input("enter the range : "))
print(sum_natural(n))

'''Q. Write a python program function to sum all the numbers in a list.'''
#
# def sum_all_numbers(num):
#     sum = 0
#     for i in range (1,num+1):
#         sum = i + sum
#     return sum
# num = int(input("enter the numbers : "))
# print(sum_all_numbers(num))
#
