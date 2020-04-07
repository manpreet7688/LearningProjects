# Often you will want to "inject" a variable into your string for printing Example:
# my_name = "manpreet"
#print("Hello" + my_name)
# There are multiple ways to format strings for printing variables in them
# This is know as String Interpolation
# Lets explore two methods for this
# .format() method
# f-strings (formatted string liberals

print("This is a string {}".format("INSERTED"))

print("The {} {} {}".format("brown","quick","fox"))

# Index wise
print("The {1} {0} {2}".format("brown","quick","fox"))

#Assign
print("The {a} {b} {c}".format(a="brown",b="quick",c="fox"))

#***** Float formatting follows "{value:width.precision f}
result = 100 / 777
print(result)

print("The result was {r}".format(r=result))

print("The result was {r:1.2f}".format(r=result))

# f-strings (formatted string liberals

name = "manpreet"
#print(f"The name is {name}") it is python 3 feature

name = "manpreet"
age = 27
#print(f"Her name is {name} and age is {age}")