"""
#Q. Extend nested list by adding the sub list.

       list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]
     #sub list to add
    sub_list = ["h","i","j"]
     Expected o/p - ['a', 'b', ['c', ['d', 'e', ['f', 'g', 'h', 'i', 'j'], 'k'], 'l'], 'm', 'n']
"""
list1 = ["a","b",["c",["d","e",["f","g"],"k"],"l"],"m","n"]
sub_list = ["h","i","j"]
list1[2][1][2].extend(sub_list)
print(list1)

#using insert

list1 = ["a","b",["c",["d","e",["f","g"],"k"],"l"],"m","n"]
sub_list = ["h","i","j"]
list1[2][1][2].insert(2,sub_list)
print(list1)

"""
#Q. WAP to find the sum of all numbers in a list.
    list_of_sum = [1,2,3,4,5]
"""
list_of_sum = [1,2,3,4,5]
i = 0
for i in list_of_sum:
    i += i
print(i)








"""
Q.	Remove empty strings from a list of strings
Str1 = [“John”, “ ”,“Jack”,”Emma”,” ”,”Jins”,”Lina”]
o/p: Str1 = [“John”,“Jack”,”Emma”,”Jins”,”Lina”]
"""
str1 = ["john"," ","jack","emma"," ", "jins","lina"]
i = ""
for i in str1:
    if i.isspace():
        list1.remove(i)
print(list1)





"""

#Q. Write a python program to remove repeated elements from a given list without using built-in methods.

"""

list1 = ["Let's", "google", "the", "pineapple","photo","google","photo"]
