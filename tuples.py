# Tuples are very similar to list. Howevere they have one difference -immutability
# Once an element is inside a tuple , it can not be reassigned
# Tuples are parenthesis: (1,2,3)

t = (1,2,3)
my_list = [1,2,3]

print(type(t))
print(type(my_list))

#length function
print(len(t))

# Indexing just like list
print(t[0])
print(t[-1])
print("*"*8)
#Count and Index functions in tuple
t = ('a','a','b')
print(t.count('a'))

print(t.index('a')) # provides first index

#diff b/w tuple and list

my_list[0] = "New value"
print(my_list)

t[0]="new value"  # throws an error
print(t)