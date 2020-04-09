'''MAKES TWENTY: Given two integers, return True if the sum of the integers is 20 or if one of the integers is 20.
If not, return False
makes_twenty(20,10) --> True
makes_twenty(12,8) --> True
makes_twenty(2,3) --> False'''

def makes_twenty(int1,int2):
    if int1 == 20 or int2 == 20 or sum((int1,int2)) == 20:
        return True
    else:
        return False

result = makes_twenty(20,10)
print(result)

result = makes_twenty(12,8)
print(result)

result = makes_twenty(2,3)
print(result)

# Reduce the code
def makes_twenty1(int1,int2):
    return int1 == 20 or int2 == 20 or sum((int1,int2)) == 20

result = makes_twenty1(20,10)
print(result)

result = makes_twenty1(12,8)
print(result)

result = makes_twenty1(2,3)
print(result)