"""
Tuple - to store multiple items in a single variables.

     > Immutable - unchangable
     > Ordered
     > Indexed
     > Allow duplicates

     - multiple datatypes accept in tuple

"""

this_tuple = ("cars","jeeps","lorry",1,6,4,9.0)
print(this_tuple)

this_tuple = ("cars","jeeps","lorry",1,6,4,9.0,[1,3,5],(1,4,5))
print(this_tuple)

print(this_tuple[0])

print(this_tuple[0:4])

print(this_tuple[-1])

print(this_tuple[:-1])

print(this_tuple[::-1])

print(len(this_tuple))

print(type(this_tuple))

"""
> remove jeep from tuple.
"""
tuple1 = ("cars","jeeps","lorry",1,6,4,9.0)
list1 = list(tuple1)
list1.remove("jeeps")
tuple1 = tuple(list1)
print(tuple1)

"""
> Replace
"""
tuple1 = ("cars","jeeps","lorry",1,6,4,9.0)
list1 = list(tuple1)
list1[2] = "car"
tuple1 = tuple(list1)
print(tuple1)

"""
> Reverse
"""
tuple1 = ("cars","jeeps","lorry",1,6,4,9.0)
x = list(tuple1)
x.reverse()
tuple1 = tuple(x)
print(tuple1)

"""
> Add
"""
tuple1 = ("cars","jeeps","lorry",1,6,4,9.0)
x = list(tuple1)
x.append([1,2,3])
tuple1 = tuple(x)
print(tuple1)


"""
  Unpack
"""

tuple1 = ("apple",[1,2,3],(5,12,22))
(x,y,z) = tuple1
print(x)
print(y)
print(z)

tuple1 = ("apple","orange",9,6,8,[1,2,3],(2,6,7))
(x, *y) = tuple1
# print(x)
print(tuple(y))


x = y = z = 3
print(x)
print(y)
print(z)


x,y,z = 3,5,8
print(x)
print(y)
print(z)

"""
built-in function
"""
#all()

# mylist = [5,0]
# x = all(mylist)
# print(x)


#any()

# mylist = [0,1,9]
# x = any(mylist)
# print(x)

#max()
# mylist = [0,1,9,10]
# x = max(mylist)
# print(x)
#
# mylist = ["apple","orange"]
# x = max(mylist)
# print(x)

#min()

# mylist = [1,9,10]
# x = min(mylist)
# print(x)
#
# mylist = ["banana","apple","orange","kiwi"]
# x = min(mylist)
# print(x)   #alphabet order print
