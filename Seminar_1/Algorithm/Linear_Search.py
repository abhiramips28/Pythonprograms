def linear_search(list1,key):
    for i in range(len(list1)):
        if key == list1[i]:
            print("Key element is found at index : ",i)
            break
    else:
        print("element is not found")

list1 = [2,5,8,12,15,20]
print(list1)
key = int(input("Enter the key element : "))
linear_search(list1,key)




























#
# def linear_Search(list1, n, key):
#     # Searching list1 sequentially
#     for i in range(0, n):
#         if (list1[i] == key):
#             return i
#     return -1
#
#
# list1 = [1, 3, 5, 4, 7, 9]
# key = 7
#
# n = len(list1)
# res = linear_Search(list1, n, key)
# if (res == -1):
#     print("Element not found")
# else:
#     print("Element found at index: ", res)