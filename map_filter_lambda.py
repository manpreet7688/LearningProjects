def sequare(n):
    return n**2

my_list = [1,2,3,4]

print(map(sequare, my_list))

def filter_ex(n):
    if n%2==0:
        return n


my_list_filter = [1,2,3,4,5,6,7,8,9]
print(filter(filter_ex, my_list_filter))


# Filter another example
def splicer(name):
    if len(name)%2==0:
        return 'Even'
    else:
        return name[0]

string_list = ["andy","liela", "rupalia"]
for n in map(splicer, string_list):
    print(n)


'''So while using lambda we do not need to use below mentioon function
def check_num(num):
    if num%2==0:
        return "Even"'''

'''Instaed write limbda directly'''

my_integer_list = [1,2,3,4,5,6,7]

print(filter(lambda num:num%2==0,my_integer_list))
