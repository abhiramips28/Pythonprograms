'''Q. factorial of a number using recursion function.'''

def fact(n):
    if n == 1:
        return 1
    else:
        x = n * fact(n-1) # 2*1=2 , 3*2*1=6 , 4*3*2*1=24 , 5*4*3*2*1=120
        # print(x)
        return x

print(fact(5))