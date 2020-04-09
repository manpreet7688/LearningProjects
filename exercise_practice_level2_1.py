'''Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.

has_33([1, 3, 3]) True
has_33([1, 3, 1, 3]) False
has_33([3, 1, 3])  False'''

def has_33(list_of_numbers):
    counter = 0
    for num in list_of_numbers:
        if num == 3:
            if num == list_of_numbers[counter+1]:
                return True
            else:
                return False
        counter+=1

result = has_33([1,3,3])
print(result)

result = has_33([1,3,1,3])
print(result)

result = has_33([3,1,3])
print(result)

print("\nResult from another way\n ")
# another way
def has_33_1(num):
    for i in range(0,len(num)-1):
        if num[i] == num[i+1]:
            return True
    return False

result = has_33_1([1,3,3])
print(result)

result = has_33_1([1,3,1,3])
print(result)

result = has_33_1([3,1,3])
print(result)