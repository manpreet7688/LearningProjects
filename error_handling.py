'''Currently if there is any type of error in your code, the entire script will stop.
We can use error handling to let the script continue with other code, even if there is an error.
We use three keywords for this:
try: This is the block of code to be attempted (may lead to an error)
except: Block of code will execute in case there is an error in try block
finally: A final block of code to be executed , regardless of an error'''


def example_of_try_except():

    while True:
        try:
            result = int(input("Enter a number Please"))
        except:
            print("Please enter a valid number")
            continue
        else:
            print("Thank you for providing a valid number")
            break
        finally:
            print("Please also visit our site on 'www.test.com'")


example_of_try_except()
