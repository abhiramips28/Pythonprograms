"""
Q. WAP  to check whether an element exist within a tuple.
"""
tuple1 = ("Apple",[10,20,30],(5,12,25),1,5,6,7)
print("Apple" in tuple1) #membership operator

tuple1 = ("Apple",[10,20,30],(5,12,25),1,5,6,7)
x = tuple1[1]
print(x)
print(x in tuple1)


"""
Q. to covert a tuple to a string
"""

tuple2 = ("s","t","r","i","n","g")
x = "".join(tuple2)
print(x)

"""
Q.index position 
"""

tuple2 = ("s","t","r","i","n","g")
y = enumerate(tuple2)
print(list(y))
