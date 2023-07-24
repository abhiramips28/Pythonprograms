''' Bubble sort '''

list1 = []
num = int(input("How many number you want to enter : "))
print("enter values: ")
for k in range(num):
    list1.append(int(input()))

print("unsorted list: ",list1)
for j in range(len(list1)-1,0,-1):
    for i in range(j):
        if list1[i] > list1[i+1]:
            list1[i] , list1[i+1] = list1[i+1],list1[i]
    #         print(list1)
    #     else:
    #         print(list1)
    # print()

print("sorted list : ",list1)










































# def bubble_Sort(array):
#     length = len(array)
#     # loop through each and every element which are keyed
#     # loop through each and every element which are keyed
#     for iterator_1 in range(length):
#         # loop through next element
#         for iterator_2 in range(0, length - iterator_1 - 1):
#
#             # From 0 to n-i-1 the array value needs to be looped upon
#             # when a element greater than the next element then the collected element needs to be swapped.
#             if array[iterator_2] > array[iterator_2 + 1]:
#                 array[iterator_2], array[iterator_2 + 1] = array[iterator_2 + 1], array[iterator_2]
#
#             # Driver code to test above
#
#
# array = [75, 34, 54, 56, 78, 1]
#
# bubble_Sort(array)
#
# print("Array values after sorting:")
# for i in range(len(array)):
#     print("%d" % array[i],end = " ")