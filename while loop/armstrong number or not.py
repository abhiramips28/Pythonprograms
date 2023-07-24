#Q. python prgm to check if the number is an armstrong number or not.

n = int(input("Enter the number : "))
num = n
l = len(str(n))
c = 0
i = 1
while i <= l:
    r = n % 10
    c += r ** l
    n //= 10
    i += 1
if c == num:
    print(num,"is an armstrong number.")
else:
    print(num,"is not an armstrong number.")


#another method

n = int(input("Enter the number : "))
x = n
a = 0
while n > 0:
    r = n % 10
    a = a + r * r * r
    n = n // 10
if a == x:
    print(x,"is an armstrong number.")
else:
    print(x,"is not an armstrong number.")
