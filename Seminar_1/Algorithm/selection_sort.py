''' selection sort '''

list1 =[ ]
num = int(input("How many numbers you want to enter : "))
print("Enter number : ")
for x in range (num):
    list1.append(int(input()))
print("Unsorted list : ",list1)

for i in range (len(list1)-1):
    m = i
    for j in range (i+1 , len(list1)):
        if list1[j] < list1[m]:
            m = j

    if list1[i] != list1[m]:
        list1[i],list1[m] = list1[m],list1[i]

print("Sorted : ",list1)






















#Ascending order
#
# list1 = [56,3,2,78,6,0]
# print(list1)
#
# for i in range (len(list1)):
#     min_val = min(list1[i:])
#     mid_ind = list1.index(min_val)
#     list1[i],list1[mid_ind] = list1[mid_ind],list1[i]
#     print(list1)
#     print()
#
# print(list1)




#
# list1 = [56,3,2,78,6,0]
# print(list1)
#
# for i in range (len(list1)):
#     min_val = max(list1[i:])
#     mid_ind = list1.index(min_val)
#     list1[i],list1[mid_ind] = list1[mid_ind],list1[i]
#     print(list1)
#     print()
#






























# import sys
#
# Array = [63, 75, 13, 2, 441]
#
# # loop through each and every element in the array
# for element1 in range(len(Array)):
#
#     # To determine the least element in the remaining list
#     minimum_idx = element1
#     for element2 in range(element1 + 1, len(Array)):
#         if Array[minimum_idx] > Array[element2]:
#             min_idx = element2
#
#             # swap the determined least element with the  previous element in the list
#     Array[element1], Array[minimum_idx] = Array[minimum_idx], Array[element1]
#
# # main code
# print("Array after getting sorted by selection sort")
# for i in range(len(Array)):
#     print("%d" % Array[i],end= " ")