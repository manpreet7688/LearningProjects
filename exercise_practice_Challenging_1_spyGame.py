'''SPY GAME: Write a function that takes in a list of integers and returns True if it contains 007 in order
 spy_game([1,2,4,0,0,7,5]) --> True
 spy_game([1,0,2,4,0,5,7]) --> True
 spy_game([1,7,2,0,4,5,0]) --> False'''

def spy_game(list_of_num):
    for i in range(0, len(list_of_num)-1):
        while list_of_num[i] != 0:
            continue
        if list_of_num[i+1] == 0 and list_of_num[i+2]==7:
            return True

        else:
            return False

result = spy_game([1,2,4,0,0,7,5])
print(result)