#Q. to reverse a given number.

# num = 1234
# reversed_num = 0
# while num != 0:
#     digit = num % 10
#     reversed_num = reversed_num * 10 + digit
#     num //= 10
# print("Reversed number : "+str(reversed_num))

#another method

n = int(input("Enter the number : "))
rev = 0
while n > 0 :
    a = n % 10
    rev = rev * 10 + a
    n = n // 10
print("Reverse number : ",rev)