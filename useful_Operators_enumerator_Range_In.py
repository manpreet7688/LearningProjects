# Range Operator - It's a generator, generator information instead of saving it in memory
my_list = [1,2,3,4]
for num in range(10):
    print(num)

print("Another Example")
for num in range(1,10):
    print(num)

print("Another Example 1")
for num in range(1,10,2):
    print(num)

# enumerate
print("Example withut enumerate")
index_count = 0
word = 'abcdef'
for letter in word:
    print("The {} of {} ".format(index_count,letter))
    index_count +=1

print("Example with enum")
word = 'abcdf'
for item in enumerate(word):  # It will return index and letter in tuple which can further be unboxed
    print(item)

print("After unboxing")
for index,letter in enumerate(word):
    print(index)
    print(letter)
    print("\n")

# Zip Operator- zip together two lists

print("Zip Example")

myList1 = [1,2,3]
myList2 = ['a','b','c']
myList3 = [100,200,300]
for items in zip(myList1,myList2,myList3):
    print(items)

# Example if lists are not having equal values
myList1 = [1,2,3,4,5,6,7,8]
myList2 = ['a','b','c']
myList3 = [100,200,300]
for items in zip(myList1,myList2,myList3):
    print(items)

# cast zip in list
print("list typecast while using zip")
print(list(zip(myList1,myList2)))

# In Operator
print("*"*8)
print('x' in ['x','y']) # returns false or true
print('l' in "Hello") # String
print('mykey' in {'mykey':'value'}) # dictionaries

d = {'mykey':395}
print(str(395) in d.keys())
print(395 in d.values())

# min and max
list_items = [10,20,30,40,50]
print(min(list_items))
print(max(list_items))

# Random
from random import shuffle

mylist_new = [1,2,3,4,5]
shuffle(mylist_new)
print(mylist_new)

# randint - generates random number
print("*"*8)
from random import randint
print(randint(0,99))

# Input Operator
input("Enter your name: ")
