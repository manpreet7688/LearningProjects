'''Handle the exception thrown by the code below by using try and except blocks. Then use a finally block to print 'All Done.'''
def exercise_2():
    x = 5
    y = 0

    try:
        z = x / y

    except ZeroDivisionError:
        print("Please make sure the value of y is not 0")

    finally:
        print("All Done")

exercise_2()