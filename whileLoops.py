# While loops will continue to execute a block of code while some condition remains True.
# For example while my pool is not full, keep filling my pool with water.
# Or while my dogs are still hungary, keep feeding my dogs.
# Syntax : while some_boolean_condition:
             #  Do something
        # else:
            # Do something else

x = 0
while x < 5:
    print("Current value of x is: ", str(x))
    x = x+1
else:
    print("The value of x is greater than 5 already")


# You can use break, continue and pass statements in our loops to add additional functionality for various casesa.
# Break: breaks out of the current closest enclosing loop
# Continue: goes to the top of the closest enclosing loop
# Pass: does nothing at all

# Continue
name = "sam"
for letter in name:
    if letter == "a":
        continue  # Go back to the closest enclosing loop
    print(letter)

print("*"*8)
# Break
name = "manpreet"
for letter in name:
    if letter == 'p':
        break # Comes out of the loop
    print(letter)

