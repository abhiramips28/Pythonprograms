"""
os module:-
This module has functions to perform many tasks of operating system.
-- file-handling purpose
"""
import os
print(dir(os))
"""
mkdir() - create
We can create a new directory using mkdir() function from os module.
"""

# import os
# print(os.mkdir(r"C:\Users\LENOVO\PycharmProjects\NewProject\Modules\mod"))

import os
os.mkdir('F:\ anvitha')

"""
chdir() - change
To change current working directory to use chdir() function.
"""
import os
print(os.chdir())


"""
getcwd()
This function in returns name off current working directory.
"""




""" 
rmdir() - remove
The rmdir() function in os module removes a specified directory either with absolute or relative path. 
However it should not be the current working directory and it should be empty."""

import os

print(os.chdir(r"C:\Users\LENOVO\PycharmProjects\NewProject\Modules\mod"))






"""
listdir():
The os module has listdir() function which returns list of all files in specified directory.
"""





import os
print(os.name)