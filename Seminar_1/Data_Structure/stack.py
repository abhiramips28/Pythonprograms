#
# stackcontainer = [ ]
# stackcontainer.append("x")
# stackcontainer.append("y")
# stackcontainer.append("z")
#
# print("Stack Elements : ")
# print(stackcontainer)
#
# stackcontainer.pop()
# stackcontainer.pop()
# print("Elements after pop : ")
# print(stackcontainer)







stack = [ ]
def push():
    element = input("Enter the element : ")
    stack.append(element)
    print(stack)

def display():
    print(stack)

def pop_element():
    if not stack:
        print("Stack is empty!")
    else:
        e = stack.pop()
        print("Removed element: ",e)
        print(stack)

while True:
    print("Select the operation 1.Add 2.Remove 3.Show 4.Quit")
    choice = int(input("Choice : "))
    if choice == 1:
        push()
    elif choice == 2:
        pop_element()
    elif choice ==3:
        display()
    elif choice == 4:
        break
    else:
        print("Enter the correct operation!")















#
# # Program 1 - Python program to demonstrate stack implementation using the list
#
# stack_example = []
#
# # append() function to push element in the stack
# stack_example.append('one')
# stack_example.append('two')
# stack_example.append('three')
# stack_example.append('four')
#
# print('Initial stack with 4 elements one, two, three, four loaded in sequence')
# print(stack_example)
#
# # pop() function to pop element from stack in LIFO order
# print('3 Elements popped from stack in LIFO order:')
# print(stack_example.pop())
# print(stack_example.pop())
# print(stack_example.pop())
#
# print('Stack after 3 elements are popped:')
# print(stack_example)
# # stack is left with one element only
#
# print('Stack is left with one element only')
# print(stack_example.pop())
