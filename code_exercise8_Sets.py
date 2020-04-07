# Sets are unordered collections of unique elements
# meaning there can only be one representative of the same object
# Example:
my_set = set()
print(my_set)

my_set.add(1)
print(my_set)

my_set.add(2)
print(my_set)

# If we add 2 again in set it wont add it again thats what set is unique list of values
my_set.add(2)
print(my_set)

#More Example
my_list =  [1,1,1,1,2,2,2,3,3,3,3]
print(set(my_list))