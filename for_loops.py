# Many objects in Python are "Iterable", meaning we can iterate over every element in the object
# Such as every element in a list or every character in a string
# We can use for loops to execute a block of code for every iteration
# The term iterable means you can "iterate" over the objct
# For example you can iterate over every character in a string , iterate over every item in a alist, iterate over every key in a dictionary
# Syntax
#my_iterable = [1,2,3]
#for item_name in my_iterable:
#    print(item_name)

my_list = [1,2,3,4,5,6,7,8]
for item in my_list:
    print(item)

# check even and odd numbers in the list
for num in my_list:
    if num % 2:
        print("The number is even", num)
    else:
        print("The number is Odd", num)

print("*"*8)

# Sum of all the  numbers
sum_list = 0
for num in my_list:
    sum_list = sum_list + num
print(sum_list)

print("*"*8)

# with string
for letter in "Hello World":
    print(letter)

print("*"*8)

# unboxing tuple
tup = (1,2,3)
for t in tup:
    print(t)

print("unboxing Tuple example")

my_list1 = [(1,2),(3,4),(5,6)]
for a,b in my_list1:
    print(a)
    print(b)

print("Example of unboxing dictionaries")

# unboxing dictionaries
dic = {'k1':'v1','k2':'v2'}
for d in dic:
    print(d) # only print keys

print("Next ")
for k,v in dic.items():  # but it will be unordered
    print(k)
    print(v)
