
cars = ["ford","volvo","BMW"]    #arrays are used to store multiple values in one single variable.
print(cars)

#Accessing the elements

cars = ["ford","volvo","BMW"]
x = cars[1]
print(x)

#modify the value

cars = ["ford","volvo","BMW"]
cars[1] = "abc"
print(cars)

#length

cars = ["ford","volvo","BMW"]
x = len(cars)
print(x)

#deleting

cars = ["ford","volvo","BMW"]
cars.remove(cars[1])
print(cars)

#search

cars = ["ford","volvo","BMW"]
x = cars.index("ford")
print(x)


#traverse

cars = ["ford","volvo","BMW"]
x = cars.index("ford")
print(x)



#insert

arr = [1,2,3,11,22]
arr.insert(3,4)
for x in arr:
    print(x,end = ',')

