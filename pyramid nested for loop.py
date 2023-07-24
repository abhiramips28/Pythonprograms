#Nested for loop

#full pyramid

rows = int(input("Enter the rows : "))
for i in range(0, rows):
    for s in range(0,rows-i-1):
        print(" ",end = " ")
    for j in range(0,i+1):
        print("*  ",end=" ")
    print()


#another method - full pyramid
#
# rows = int(input("Enter a number : "))
# for i in range(rows+1):
#     for space in range(rows-i):
#         print("_",end=" ")
#     for star in range(i):
#         print("*  ",end=" ")
#     print( )
#
#
#half pyramid

# rows = int(input("Enter a number : "))
# for i in range(rows):
#     for star in range(i+1):
#         print("*  ",end=" ")
#     print( )

#inverted half pyramid

# rows = int(input("Enter a number : "))
# for i in range(rows,0,-1):
#     for star in range(i):
#        print("*  ",end=" ")
#     print()


#inverted full pyramid
#
# rows = int(input("enter a number : "))
# for i in range(rows,0,-1):
#     for space in range(rows-i):
#         print(" ",end=" ")
#     for star in range(i):
#         print("*  ",end=" ")
#     print()


#Number pattern

# rows = int(input("Enter a number: "))
# for i in range(rows):
#     for j in range(i+1):
#         print(j+1,end=" ")
#     print()
#
#