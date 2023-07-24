"""Q. Define a function which count vowels and consonant in a vowels."""

def count(val):
    vov = 0
    con = 0
    for i in range (len(val)):
        if val[i] in ['a','e','i','o','u','A']:
           vov = vov + 1
        else:
            con = con + 1
    print("the count of vowels is ",vov)
    print("the count of consonant is ",con)

x = input("enter the value: ")
count(x)
