# Dictionaries are unordered mappings for storing objects. Previously we saw how lists store objects in an ordered sequence
# -  dictionaries use a key-value pairing instead
# This key-value pair allows users to quickly grab objects without needing to know an index location
# Dictionaries use curly braces and colons to signify the keys and their associated values.
# {'key1':'value1','key2':'value2'}
# Question: When to choose a list and when to choose a dictionary?
# Ans:
# Dic: Objects retreieved by key name , unordered and can not be sorted
# Lists: Objects retrieved by location , Ordered sequesnce can be indxed or sliced

dic = {'key1':'value1','key2':'value2'}
print(dic)

#use case
price_lookup = {'dept':['food','beverage','clothes'],'priceOfFoodItems':{'apple':100,'grapes':150}}
print(price_lookup)
print(price_lookup['dept'])
print(price_lookup['priceOfFoodItems']['apple'])

#add new dic
dic_new = {'k1':'v1','k2':'v2'}
dic_new['k3'] = 'v3'
print(dic_new)

#replace
dic_new['k1'] = "New Value"
print(dic_new)

#Keys, items and value retrieve
print(dic_new.keys())
print(dic_new.values())
print(dic_new.items())