'''Write a Python function to multiply all the numbers in a list.

Sample List : [1, 2, 3, -4]
Expected Output : -24'''

def multiply(numbers):
    multiplied_var = 1
    for i in numbers:
        multiplied_var = multiplied_var * i
    return multiplied_var

result = multiply([1, 2, 3, -4])
print(result)
