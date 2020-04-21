'''We have learned how to create functions with def and return statements.
Generator function allows us to write a function that can send back a value and then later resume to pick up
where it left off.
This type of function is a generator in python, allowing us to generate a sequence of values over time.
The main difference in syntax will be the use of a yield statement
When a generator function is compiled they become an object that supports an iteration protocol.
That means when they are called in your code they dont actually return a value and then exit.
Generator functions will automatically suspend and resume their execution and state around the last point of
value generation.
The advantage is that instead of having to compute an entire series of values up front, the generator computes
one value waits until the next value is called for.
For example, the range() function does not produce an list in memory for all the values from start to top.
Instead it just keeps track of the last number and the step size , to provide a flow of number.
If a user did need the list, they have to transform the generator to a list with list(range(0,10)).
Lets explore how to create our own generators!'''

def cube_square(n):
    result = []
    for i in range(n):
        result.append(i**3)
    return result

result = cube_square(7)
print(result)

# Above example is storing the entire list in memory, for the efficient use of the memory, we use generator

def cube1(n):
    for i in range(n):
        yield i**3

for x in cube1(7):
    print(x)

# Another example of next function in generator
print("*"*14)

def simple_gen(n):
    for i in range(n):
        yield i

g = simple_gen(8)
print(next(g))
print(next(g))
print(next(g))


# Iteration of string using iter function as next throws an error in case of string
print("*"*14)

def string_fun():
    s = 'Hello'
    for i in s:
        yield i

for x in string_fun():
    print(x)

print("\n using iter function")

g_string = iter(string_fun())
print(next(g_string))
print(next(g_string))
print(next(g_string))
