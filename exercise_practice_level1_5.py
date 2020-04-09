'''MASTER YODA: Given a sentence, return a sentence with the words reversed
master_yoda('I am home') --> 'home am I'
master_yoda('We are ready') --> 'ready are We'''

def master_yoda(text):
    new_text = text.split()
    reversed_list = new_text[::-1]
    print(" \nbefore using join \n" + str(reversed_list) +'\n')
    print("after using join")
    return ' '.join(reversed_list)



result = master_yoda('home am I')
print(result)

result = master_yoda('ready are We')
print(result)
