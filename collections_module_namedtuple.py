'''The standard tuple uses numerical indexes to access its members'''

t = (1,2,3)
print(t[0])

'''For simple use cases, this is usually enough. On the other hand, remembering which index should be used for 
each value can lead to errors, especially if the tuple has a lot of fields and is constructed far from where 
it is used. A namedtuple assigns names, as well as the numerical index, to each member.
Each kind of namedtuple is represented by its own class, created by using the namedtuple() factory function. 
The arguments are the name of the new class and a string containing the names of the elements.
You can basically think of namedtuples as a very quick way of creating a new object/class type with some 
attribute fields. For example:'''

from collections import namedtuple
Dog = namedtuple('Dog','name, age, breed')
sam = Dog(name = 'sammy', age = 2, breed='Lab')
frank = Dog(age=2,breed='Shepard',name="Frankie")

'''We construct the namedtuple by first passing the object type name (Dog) and then passing a string with 
the variety of fields as a string with spaces between the field names. We can then call on the various 
attributes:'''

print(sam)
print(sam.name)
print(sam[0])
