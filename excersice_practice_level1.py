'''LESSER OF TWO EVENS: Write a function that returns the lesser of two given numbers if both numbers are even,
but returns the greater if one or both numbers are odd
lesser_of_two_evens(2,4) --> 2
lesser_of_two_evens(2,5) --> 5'''

def lesser_of_two_events(a,b):
    if a%2==0 and b%2==0:
        if a<b:
            return a
        else:
           return b
    else:
        if a%2!=0 or b%2!=0:
            if a>b:
                return a
            else:
                return b

# When one of them is odd
result = lesser_of_two_events(2,5)
print(result)

# When both are even
result = lesser_of_two_events(2,4)
print(result)

# Reduce the code

def lesser_of_two_events1(a,b):
    if a%2==0 and b%2==0:
        return min(a,b)
    else:
        return max(a,b)

print("After reducing the code\n")
# When one of them is odd
result = lesser_of_two_events1(2,5)
print(result)

# When both are even
result = lesser_of_two_events1(2,4)
print(result)