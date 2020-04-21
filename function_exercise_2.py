'''Write a Python function that accepts a string and calculates the number of upper case letters and lower case letters.'''

def up_low(string):
    up = 0
    low = 0
    rest = 0
    for i in string:
        if i.isupper():
            up+=1
        elif i.islower():
            low+=1
        else:
            rest+=1

    print("No. of Upper case characters : " + str(up))
    print("No. of Lower case characters : " + str(low))

up_low('Hello, How are you?')



