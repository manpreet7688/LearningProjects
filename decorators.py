'''Decorators allow you to "decorate" a function
Python has decorators that allow tack on extra functionality to an already existing function.
They use the @ operator and are then placed on top of the original function.
Before using decorator, we will see what actually happenes behind the scene when we use decorator'''


# Example 1 return a function
def function(name='mann'):
    def hello():
        print('This is hello() inside a function')

    def greet():
        print('This is greet() inside a function')

    if name=='mann':
        return hello
    else:
        return greet

new_function = function('random')
print(new_function())


# Exmaple 2 pass a function
def name_of_a_person(function_to_be_executed):
    print("Name os the person is 'Manpreet'")

    function_to_be_executed()

def profession_fun():
    print("Profession of the person is Senior Software Engineer")

function = name_of_a_person(profession_fun)
print(function)



# Why use decorator
def new_decorator(original_fun):
    def wrap():
        print("Code to be executed before original_fun")

        original_fun()

        print("Code to be executed after original_fun")

    return wrap

def func_needs_decorator():
    print("I want to be decorate!")

decorated_fun = new_decorator(func_needs_decorator)
print(decorated_fun())

print("\n Example of decorator @ \n")

# Now to sort this out , we use @
@new_decorator
def func_needs_decorator_new():
    print("I want to be decorate! to clear the example of decorators")


func_needs_decorator_new()



