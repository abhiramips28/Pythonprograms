"""
Random module:-
  Python’s standard library contains random module which defines various functions for handling randomization.
"""
"""
random.random()
 Returns a random float number between 0.0 to 1.0. The function doesn’t need any arguments
"""
import random
print(random.random())

print(dir(random))

"""
random.randint() 
Returns a random integer between the specified integers.
"""

import random
print(random.randint(1,100))

"""
random.randrange()
 Returns a random element from the range created by start, stop and step arguments. 
The start , stop and step parameters behave similar to range() function.
"""

import random
print(random.randrange(1,10,2)) #2 vecha ulla numbers increment cheyum

"""
random.choice() 
Returns a randomly selected element from a sequence object such as string, list or tuple.
 An empty sequence as argument raises IndexError
"""
import random
print(random.choice('computer'))

"""
random.shuffle()
 This functions randomly reorders elements in a list.
"""
import random
numbers = [1,2,3,4,5,6]
random.shuffle(numbers)
print(numbers)