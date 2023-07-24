# list1 = [2,3,5,6,8,7,4,9]
# even = []
# odd = []
# for i in list1:
#     if i%2 == 0:
#         even.append(i)
#     else:
#         odd.append(i)
# print(even)
# print(odd)

# list_items =[2,3,4,5,6]
# obj = [(i,"even" if i%2==0 else "odd") for i in list_items]
# print(obj)




# fruits = ["apple","banana","orange","grapes","kiwi"]
# newlist = []
# for x in fruits:
#     if 'a' in x:
#         newlist.append(x)
# print(newlist)

# fruits = ["apple","banana","orange","grapes","kiwi"]
# newlist = [x for x in fruits if 'a' in x]
# print(newlist)





# print prime numbers

n = [1,2,3,4,5,6,7,8,9,10,11]
newlist1 = [(i,'prime' if n%i==0 else 'not prime')for i in n]
print(newlist1)