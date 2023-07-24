"""
  Dictionary - used to store data values in key : value pairs.
            > Ordered
            > Mutable
            > Indexed
            > Do not allow duplicates
"""
dict1 = {"name":"Anvi","age":3}
print(dict1)

print(dict1["name"])

print(type(dict1))  #type

print(len(dict1))   #length

dict2 = {"Name":"Anvi","Age":3,"class":"playclass"}
print(dict2)

# get() method
dict2 = {"Name":"Anvi","Age":3,"class":"playclass"}
x = dict2.get("Name")
print(x)

#keys() method & values() method
dict2 = {"Name":"Anvi","Age":3,"class":"playclass"}
print(dict2.keys())
print(dict2.values())

#copy() method
dict2 = {"Name":"Anvi","Age":3,"class":"playclass"}
x = dict2.copy()
print(x)

#items() method
dict2 = {"Name":"Anvi","Age":3,"class":"playclass"}
x = dict2.items()
print(x)

#pop() method
dict2 = {"Name":"Anvi","Age":3,"class":"playclass"}
x = dict2.pop("class")
print(x)

dict2 = {"Name":"Anvi","Age":3,"class":"playclass"}
dict2.pop("class")
print(dict2)

#popitems() method
dict2 = {"Name":"Anvi","Age":3,"class":"playclass","city":"Kottayam"}
dict2.popitem()
print(dict2)

dict2 = {"Name":"Anvi","Age":3,"class":"playclass","place":"Kottayam"}
x = dict2.popitem()
print(x)

#update() method
dict2 = {"Name":"Anvi","Age":3,"class":"playclass"}
x = dict2.update({"School":"Marian kids"})
print(dict2)

#fromkey() method
x = ("key1","key2")
y = 0
dict3 = dict.fromkeys(x,y)
print(dict3)


#setdault() method
dict2 = {"Name":"Anvi","Age":3,"class":"playclass"}
print(dict2.setdefault("age",3))
print(dict2)

#del

dict2 = {"Name":"Anvi","Age":3,"class":"playclass"}
del dict2["Age"]
print(dict2)










