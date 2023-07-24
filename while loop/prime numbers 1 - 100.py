#print prime numbers in between 10 to 100 using while loop.

n = 2
i = 2
while n <= 100:
    while i < n:
        if n % i == 0:
            break
        i += 1
    else:
        print(n,end = " ")
    i = 2
    n += 1
