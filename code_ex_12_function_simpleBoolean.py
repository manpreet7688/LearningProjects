def myfunc(value):
    if value == True:
        return "Inside"
    elif value == False:
        return "Outside"
    else:
        return "Please enter the correct value"

result = myfunc('abc')
print(result)