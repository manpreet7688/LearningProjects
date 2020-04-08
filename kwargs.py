# Only difference is it returns in dictionary

def kwargs1(**kwargs):
    if 'Fruit' in kwargs:
        print("My favourite friut is {}".format(kwargs['Fruit']))

        print("\nLets see whats kwargs holds")
        print(kwargs)
        print("\nYes, It returns a dictionary")
    else:
        print("I dont like anything except fruit :(")


print("And the result is:")
kwargs1(Fruit = 'apple', Veggie = 'cauliflower')

# If we use both *args and **kwargs in a function that the order in which we pass args and kwargs should be same

def args_kwargs(*args, **kwargs):
    print("I would like to order {} {} for {} number of people".format(args[0],kwargs['desert'],args[2]))

args_kwargs(10,20,5,food='chinese',desert='gulab jamun',beverage = 'lime soda') # in the same order args first then kwargs
