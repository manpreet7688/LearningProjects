'''Write a function that checks whether a number is in a given range (inclusive of high and low)'''

def ran_check(num, high, low):
    if num >= low and num <= high:
        return True
    else:
        return False

result = ran_check(20,10,0)
print(result)