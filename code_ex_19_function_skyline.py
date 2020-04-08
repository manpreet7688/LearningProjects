'''Define a function called myfunc that takes in a string and returns a matching string where every even letter is uppercase and every odd letter is lowercase.
Assume that the incoming string only contains letters and dont worry about numbers, spaces or punctuation.'''

def myfunc(string_letter):
    index = 1
    new_string = ''
    for every_letter in string_letter:
        if index%2==0:
            new_string = new_string + every_letter.capitalize()
        else:
            new_string = new_string + every_letter
        index +=1
    return new_string

result = myfunc('abcdefghijklmnop')
print(result)

