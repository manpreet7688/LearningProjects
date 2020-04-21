'''Use the iter() function to convert the string below into an iterator:'''
def string_func(s):
    for i in s:
        yield i


for string_v in string_func('manpreet'):
    print(string_v)

print("iter function for iteration")

iterate_string = iter(string_func('manpreet'))
print(next(iterate_string))
print(next(iterate_string))
print(next(iterate_string))