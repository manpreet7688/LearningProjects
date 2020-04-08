def list_of_even_number(*args):
    my_list = []
    for num in args:
        if num%2==0:
            my_list.append(num)
    return my_list


lis_of_even_num = list_of_even_number(2,3,4,5,6,7,8,9,1)
print(lis_of_even_num)
