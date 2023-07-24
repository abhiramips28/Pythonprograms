# with open("samplenote.py","r") as file:
#     # f3 = open("samplenote.py","w")
#     for i in file:
#         print(i)
#

f = open("sample.py","x")   #create a file - 'x'
print(f)
f = open("sample.py","w")    #write
f.write("Hi dears, how are you? ")
f.close()



