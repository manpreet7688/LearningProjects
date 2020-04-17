'''Handle the exception thrown by the code below by using try and except blocks.'''
def exercise1():
    try:
        for i in ['a', 'b', 'c']:
            print(i ** 2)
    except TypeError:
        print("Please make sure that you are performing arithematic ex with int")

exercise1()