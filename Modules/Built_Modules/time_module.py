"""
time() module
This function returns current system time in ticks """

import time
print(time.ctime())


import time
for i in range(5):
    time.sleep(2) #printed after 2min
    print(i)

import time
print(time.localtime())

import time
print(time.asctime())