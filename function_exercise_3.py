'''
Write a Python function that takes a list and returns a new list with unique elements of the first list.

Sample List : [1,1,1,1,2,2,3,3,3,3,4,5]
Unique List : [1, 2, 3, 4, 5]'''

def unique_list(lst):
    unique_list = []
    for i in lst:
        if i not in unique_list:
            unique_list.append(i)
        else:
            pass
    return unique_list

new_list = unique_list([1,1,1,1,2,2,3,3,3,3,4,5])
print(new_list)
