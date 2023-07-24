"""
 List
    > Lists are used to store multiple items in a single variable.
    > List is mutable,ordered, indexed, allows duplicates.
    > items = ["apple",123,"orange",9.0]
"""
"""
List Methods:-
"""
# append() method

items = ["apple",123,"orange",9.0,"kiwi"]

items.append("grapes")
items.append(["grapes","banana",2345])
print(items)

# clear() method

items = ["apple",123,"orange",9.0,"kiwi"]
items.clear()
print(items)


# copy() method

items = ["apple",123,"orange",9.0,"kiwi"]
x = items.copy()
print(x)

# count() method

fruits = ["apple", "banana", "cherry"]
x = fruits.count("banana")
print(x)


# extend() method

items = ["apple",123,"orange",9.0,"kiwi"]
l2 = ["ford","vento","volvo"]
items.extend(l2)
print(items)

# index() method

fruits = ['apple', 'banana', 'cherry']
x = fruits.index("cherry")
print(x)

# insert() method

items = ["apple",123,"orange",9.0,"kiwi"]
items.insert(1,"Grape")
print(items)

# pop() method

fruits = ['apple', 'banana', 'cherry']
fruits.pop(1)
print(fruits)

# remove() method

fruits = ['apple', 'banana', 'cherry']
fruits.remove('apple')
print(fruits)

# reverse() method

fruits = ['apple', 'banana', 'cherry']
fruits.reverse()
print(fruits)

# sort() method

cars = ['Ford', 'BMW', 'Volvo']
cars.sort()
print(cars)





# list - while loop -

# mark = [0, 0, 0, 0, 0]
# i = 0
# while i <= 4:
#     mark[i] = int(input("Enter the value : "))
#     i += 1
# print(mark)

#
# mark1 = [0, 0, 0, 0, 0]
# i = 0
# while i <= 4:
#     mark1[i] = int(input("Enter the value : "))
#     i += 1
# print(mark1)
#
# i = 0
# while (i<=4):
#     print(mark1[i])
#     i += 1

# while loop - find 23 in list

# mark2 = [12,23,45,34]
# i=0
# while i<=4:
#     if mark2[i] == 23:
#         print("The element is found in index - ",i)
#     i = i+1


# while loop - find how many 23 in list

mark = [12, 23, 45, 34, 23]
count = 0
i = 0
while i < 5:
    if mark[i] == 23 :
        count = count + 1
    i = i + 1
print("Count - ",count)
