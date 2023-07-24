#Q. To print alphabrts A-Z
#
# for i in range(65,91):
#     print(chr(i)," ",end = " ")

# for i in range(97,123):
#     print(chr(i),end= " ")

# import string
#
# for i in string.ascii_lowercase:
#     print(i,end=" ")
#
# for i in string.ascii_uppercase:
#     print(i,end=" ")

#CHARACTER PATTERN

rows=int(input("enter a number:"))
A=65
for i in range(rows):
    for j in range(i+1):
        print(chr(A)," ",end = " ")
        A=A+1
    print()


#character in pyramid shape
# #
# rows = int(input("Enter a number : "))
# A=65
# for i in range(rows+1):
#     for n in range(rows-i):
#         print(" ",end=" ")
#     for j in range(i+1):
#         print(chr(A)," ",end = " ")
#         A=A+1
#     print()
# #
#
#Q. try to print below pattern.

word = input("Enter the string : ")
char = len(word)
for i in range(char+1):
    for j in range(i):
        print(word[j],end=" ")
    print()
