'''defaultdict is a dictionary -like object which provides all methods provided by a dictionary
but takes a first argument (default_factory) as a default data type for the dictionary.
Using defaultdict is faster than doing the same using dict.set_default method.
Note: A defaultdict will never raise a keyError. Any key that does not exist gets the value returned by the
default factory.'''

from collections import defaultdict
d = {}

#print(d['one']): Throws a keyError

d = defaultdict(lambda:0)
print(d['one'])
d['two'] = 2
print(d)