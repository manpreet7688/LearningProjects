'''Write a function that asks for an integer and prints the square of it. Use a while loop with a try, except, else block to account for incorrect inputs.'''
def exercise_3():
    while True:
        try:
            result = int(input("Enter a number"))
            print(result ** 2)
        except:
            print("Please enter a valid number")
            continue
        else:
            print("Thanks for providng a number ")
            break
        finally:
            print("We admire our customers")

exercise_3()