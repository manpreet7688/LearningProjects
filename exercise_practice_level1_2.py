'''ANIMAL CRACKERS: Write a function takes a two-word string and returns True if both words begin with same letter
animal_crackers('Levelheaded Llama') --> True
animal_crackers('Crazy Kangaroo') --> False'''

def animal_crackers(two_word_string):
    splitted_string = two_word_string.split(' ')
    print(splitted_string)
    first_word = splitted_string[0]
    second_word = splitted_string[1]
    if first_word[0] == second_word[0]:
        return True
    else:
        return False



result = animal_crackers('mann latter')
print(result)

result = animal_crackers('Crazy Cangaroo')
print(result)

# Problem with previous code is that it fails if any of the letter is in lower case for ex: Cat cattle

def animal_crackers1(string):
    splitted_string = string.lower().split()
    print(splitted_string)
    return splitted_string[0][0] == splitted_string[1][0]



result = animal_crackers1('mann latter')
print(result)

result = animal_crackers1('Crazy cangaroo')
print(result)
