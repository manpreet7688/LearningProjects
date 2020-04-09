'''OLD MACDONALD: Write a function that capitalizes the first and fourth letters of a name
old_macdonald('macdonald') --> MacDonald'''

def old_macdonald(name):
    first_letter = name[0]
    inbetween = name[1:3]
    fourth_letter = name[3]
    rest = name[4:]
    return first_letter.upper() + inbetween +fourth_letter.upper()+rest

result = old_macdonald('macdonald')
print(result)

# With capitalize method

def old_macdonald_with_capitalize(name):
    first_half = name[:3]
    second_half = name[3:]

    return first_half.capitalize() + second_half.capitalize()

result = old_macdonald_with_capitalize('macdonald')
print(result)



