'''PAPER DOLL: Given a string, return a string where for every character in the original there are three characters
paper_doll('Hello') --> 'HHHeeellllllooo'
paper_doll('Mississippi') --> 'MMMiiissssssiiippppppiii'''

def paper_doll(text):
    new_text = []
    new_text = text[0:]
    final_word = ''
    for letter in new_text:
        word = letter * 3
        final_word = final_word + word
    return final_word

result = paper_doll('Hello')
print(result)

result = paper_doll('Mississippi')
print(result)