# Lists are order sequences that can hold a variety of object types
# They use [] and commas to separate objects in it [1,2,3]
# Lists support indexing and slicing. List can be nested and also have a variety of useful methods that can be called off of them

# indexing in list

my_list = ['one','two',3,4.5]
print(my_list[0])

#slicing
print(my_list[1:])

#replace index with new value
my_list[0] = "Inserted"
print(my_list)

# append new value
my_list = ["One","two"]
my_list.append("Three")
my_list.append("Four")
print(my_list)

# Delete a value from the end-pop(): Always return a value
print(my_list.pop())

# Delete a value in any place
print(my_list.pop(1))
print(my_list)

my_list.append("Four")
popped_item = my_list.pop()
print(popped_item)

# Sort a list - does not return a value
my_newList = ['a','x','h','b']
my_newList.sort()
print(my_newList)

sorted_list = my_newList.sort()
#Does not return anything
print(sorted_list)
print(type(sorted_list))

my_newList.reverse()
print(my_newList)


