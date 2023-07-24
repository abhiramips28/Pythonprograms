"""
Q. To check if the file is exist or not.
"""

import os.path
file_path = r'C:\Users\LENOVO\PycharmProjects\NewProject\File_handling\samplenote.py'
flag = os.path.exists(file_path)
if flag:
    print(f'The file {file_path}exists')
else:
    print(f'The file {file_path}does not exists')


"""
Q. getsize
"""

import os.path
file_path = r'C:\Users\LENOVO\PycharmProjects\NewProject\File_handling\samplenote.py'
sz = os.path.getsize(file_path)
print(f'The {file_path} size is ',sz,'bytes')


"""
Q.Delete lines from a file.
"""

import os
