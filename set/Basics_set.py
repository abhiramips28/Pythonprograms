"""
Set - to store multiple items in a single variables.
       > curly brackets.

     1.Immutable
     2.Unordered
     3.Unindexed
     4.No duplicate


"""

set1 = {1,2,3,"anvi"}
print(type(set1))

print(3 in set1)

for i in set1:
    print(i)

# add() method
set1.add("apple")
print(set1)

# update() method
set2 = {"orange","apple","pineapple"}
set1.update(set2)
print(set1)

# remove()
set1.remove("anvi")
print(set1)

# discard()

set1.discard("python")
print(set1)

# pop()
x = set1.pop()
print(x)
print(set1)

# clear()
set1.clear()
print(set1)

#del()
# del set1
# print(set1)

#union()
set1 = {"a","b","c",1,5}
set4 = {1,5,9,7,"a","b"}
set3 = set1.union(set4)
print(set3)


#intersection_update()
z = set1.intersection(set4)
print(z)

#difference()
z = set1.difference(set4)
print(z)

#symmetric_difference
z = set1.symmetric_difference(set4)
print(z)


# # update |=

#
set1 = {"a","b","c",1,5,"anvi"}
set4 = {1,5,9,7,"a","b",10,22}
set3 = set1.union(set4)
print(set3)

# #intersection_update()

set1.intersection_update(set4)
print(set1)

# #difference_update()
#
# set1.difference_update(set4)
# print(set1)
#
# #symmetric_difference_update()
#
# set1.symmetric_difference_update(set4)
# print(set1)
#
#
# # isdisjoint()
# x = {"apple", "banana", "cherry"}
# y = {"google", "microsoft", "facebook"}
# z = x.isdisjoint(y)
# print(z)
#
# # issubset()
# x = {"a", "b", "c"}
# y = {"f", "e", "d", "c", "b", "a"}
# z = x.issubset(y)
# print(z)
#
# # issuperset()
#
# x = {"f", "e", "d", "c", "b", "a"}
# y = {"a", "b", "c"}
# z = x.issuperset(y)
# print(z)