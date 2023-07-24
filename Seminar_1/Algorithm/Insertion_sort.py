""" Insertion Sort"""

def insertionsort(my_list):
    for i in range (1,len(my_list)):
        current_element = my_list[i]
        pos = i
        while current_element < my_list[pos-1] and pos > 0:
            my_list[pos] = my_list[pos-1]
            pos = pos - 1
        my_list[pos] = current_element
my_list = [2,4,3,5,1]
print("Unsorted list : ",my_list)
insertionsort(my_list)
print("Sorted list : ",my_list)
















# #insertion sort
#
# def insertion_Sort(array):
#     # pass through through 1 to len(array)
#     for temp_element1 in range(1, len(array)):
#
#         key = array[temp_element1]
#
#         # Move elements of array[0..i-1], that are
#         # greater than key, to one position ahead
#         # of their current position
#         temp_element2 = temp_element1 - 1
#         while temp_element2 >= 0 and key < array[temp_element2]:
#             array[temp_element2 + 1] = array[temp_element2]
#             temp_element2 -= 1
#         array[temp_element2 + 1] = key
#
#     # Driver code to test above
#
#
# array = [75, 34, 54, 56, 78, 1]
# insertion_Sort(array)
# for i in range(len(array)):
#     print("% d" % array[i],end= " ")