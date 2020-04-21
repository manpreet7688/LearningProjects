'''Sometimes it's important to know how long your code is taking to run, or at least know if a particular
line of code is slowing down your entire project. Python has a built-in timing module to do this.

This module provides a simple way to time small bits of Python code. It has both a Command-Line Interface as
well as a callable one. It avoids a number of common traps for measuring execution times.'''

import timeit

'''Let's use timeit to time various methods of creating the string '0-1-2-3-.....-99'

We'll pass two arguments: the actual line we want to test encapsulated as a string and the number of times we 
wish to run it. Here we'll choose 10,000 runs to get some high enough numbers to compare various methods.'''

'0-1-2-3-...-99'

# For loop
timeit.timeit('"-".join(str(n) for n in range(100))', number=10000)
# List comprehension
timeit.timeit('"-".join([str(n) for n in range(100)])', number=10000)
# Map()
timeit.timeit('"-".join(map(str, range(100)))', number=10000)

'''iPython's %timeit will perform the same lines of code a certain number of times (loops) and will give you the fastest performance time (best of 3).'''

#%timeit "-".join(str(n) for n in range(100))
#%timeit "-".join([str(n) for n in range(100)])