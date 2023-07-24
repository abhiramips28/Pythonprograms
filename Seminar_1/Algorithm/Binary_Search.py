def binary_search(list1,key):
    low = 0
    high = len(list1)-1
    found = False
    while low <= high and not found:
        mid = (low+high)//2
        if key == list1[mid]:
            found = True
        elif key > list1[mid]:
            low = mid + 1
        else:
            high = mid - 1
    if found == True:
        print("Key is found")
    else:
        print("Key is not found")

list1 = [23,20,15,2,10,6,8,4]
print(list1)
list1.sort()
print(list1)
key = int(input("Enter the key : "))
binary_search(list1,key)









































# # Iterative Binary Search Function method Python Implementation
# # It returns index of n in given list1 if present,
# # else returns -1
# def binary_search(list1, n):
#     low = 0
#     high = len(list1) - 1
#     mid = 0
#
#     while low <= high:
#         # for get integer result
#         mid = (high + low) // 2
#
#         # Check if n is present at mid
#         if list1[mid] < n:
#             low = mid + 1
#
#             # If n is greater, compare to the right of mid
#         elif list1[mid] > n:
#             high = mid - 1
#
#             # If n is smaller, compared to the left of mid
#         else:
#             return mid
#
#             # element was not present in the list, return -1
#     return -1
#
#
# # Initial list1
# list1 = [12, 24, 32, 39, 45, 50, 54]
# n = 45
#
# # Function call
# result = binary_search(list1, n)
#
# if result != -1:
#     print("Element is present at index", str(result))
# else:
#     print("Element is not present in list1")