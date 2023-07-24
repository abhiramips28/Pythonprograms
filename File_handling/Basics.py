"""
  File Handling
  """

f = open("samplenote.py","x")   #create a file - 'x'
print(f)


f = open("samplenote.py","w")    #write
f.write("Hi dears")
f.close()



f = open("samplenote.py",'r') #create a file - 'x'
print(f.read())

f = open("samplenote.py",'a')
f.write("Welcome to python course")

f = open("samplenote.py",'r')
lines = f.readline()
print(lines)