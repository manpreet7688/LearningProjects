'''An OrderedDict is a dictionary subclass that remembers the order in which its contents are added.'''

d = {}
d['a'] = 1
d['b'] = 2
d['c'] = 3
d['d'] = 4
d['e'] = 5

for k,v in d.items():
    print k,v   # Will not print dictionary in ordered in which it is stored

from collections import OrderedDict
d = OrderedDict()

print("\n after using OrderedDict")
d['a'] = 1
d['b'] = 2
d['c'] = 3
d['d'] = 4
d['e'] = 5

for k,v in d.items():
    print k,v


# another example
d1 = {}
d1['a'] = 1
d1['b'] = 2

d2 = {}
d2['b'] = 2
d2['a'] = 1

# Equality with an Ordered Dictionary
# Technically the aforementioned dictionaries are not in same order despite having the same values
# So when we compare

if d1 == d2:
    print True
else:
    print False

# True result is wrong so now,

d1 = OrderedDict()
d1['a'] = 1
d1['b'] = 2

d2 = OrderedDict()
d2['b'] = 2
d2['a'] = 1

if d1 == d2:
    print True
else:
    print False

