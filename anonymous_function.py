


""" Map """







#add two list
def func(a,b):
    return (a+b)
a = [2,5,6,3,8,2]
b = [5,1,8,3,1,1]

x = map(func,a,b)

print(list(x))

#length of string
def func(x):
    return len(x)

x = ("Apple","kiwi","orange")
y = map(func,x)
print(list(y))



fruits = ['apple','orange','kiwi']
length = list(map(lambda x: len(x),fruits))
print(length)



my_pets = ['alfred','tabitha','william','arla']
upper_pets = []
for elem in my_pets:
    u_pets = elem.upper()
    upper_pets.append(u_pets)

print(upper_pets)

#using map() function
upper_p = list(map(str.upper,my_pets))
print(upper_p)


""" Filter """

def fun(val):
    letters = ['a','e','i','o','u']
    if val in letters:
        return True
    else:
        return False

str1 = 'apple'
filtered = filter(fun,str1)
print(list(filtered))

""" Reduce """























#factorial of a number using reduce()

def func(fac,i):
    return int(fac*i)
fac = 5
i = 0
y = reduce(func,fac,i)
print(y)

