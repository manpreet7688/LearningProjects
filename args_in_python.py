# *args allows user to paas as many arguments as he wants
# It returns back tuple

# Example without args

def without_args(a,b,c=0,d=0):
    total_sum = sum((a,b,c,d))
    print(total_sum)

without_args(1,2)
without_args(3,4,5,6)
# without_args(2,3,4,5,6) throws an error

# with args
print("*"*8)

def with_args(*args):
    print("Whats is args , Lets see")
    print(args)
    print("Oh! its a tuple")
    total_sum = sum((args))
    print(total_sum)

with_args(2,3,4)
with_args(2,3,4,5,6,7)
with_args(2,3,4,6,7,8,99,12,45,9)

print("\nSecond Example**********\n")

def with_args1(*args):
    for items in args:
        print(items)

with_args1("hello",'hi','how are you')
