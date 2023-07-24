






# try:
#     a = int(input("Enter value of a: "))
#     b = int(input("Enter value of b: "))
#     c=a/b
#     print("The answer of a divide by b: ",c)
#
# except ZeroDivisionError:
#     print("Can't divide with zero")
# finally:
#     print("Inside a finally block")





try:
    num = int(input("Enter the num: "))
    assert num % 2 == 0
except:
    print("not an even num")

else:
    reciprocal = 1/num
    print(reciprocal)