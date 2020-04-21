'''Collection Module:
The collections module is a built-in module that implements specialized container data types providing alternatives
to python's general purpose containers. basics: dict, set, list, tuple.
Counter:
Counter is a dict subclass which helps count hashable objects. Inside of it elements are stored as dictionary
keys and the counts of the objects are stored as the value'''

from collections import Counter

list_name = [1,1,1,2,2,2,2,2,2,3,3,3,4,4,4,4,4,5,5,5,5,6,6,6]
print(Counter(list_name))


string_name = 'aaaaabbbbudjjjjidiiiii'
print(Counter(string_name))

# Counter with word in a sentence
s = 'How many times does each word show up in this sentence word times each each word'

words = s.split()
print(Counter(words))

#Methods with counter like most_common, sum, items etc

c = Counter(words)
print(c.most_common(2))
