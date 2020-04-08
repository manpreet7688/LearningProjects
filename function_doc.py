# Creating clean repeatable code is a key part of becoming an effective programmer
# Functions allow us to create blocks of code that can be easily executed many times, without needing to constantly rewrite the entire block of code.
# PIG LATIN problem
# If word starts with a vowel , add 'ay' to end
# If word does not start with a vowel , put first letter at the end , then add 'ay'

def pig_latin(word):
    first_letter = word[0]
    if first_letter in 'aeiou':
        pig_word = word + 'ay'
    else:
        pig_word = word[1:] + first_letter + 'ay'
    return pig_word

result = pig_latin('apple')
print(result)