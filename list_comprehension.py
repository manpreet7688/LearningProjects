# List comprehensions are a unique way of quickly creating a list with python
# If you find yourself using a for loop along with .append() to create a list , List comprehensions are a good alternative
print("Normal Example")
myList = [1,2,3,4,5]
for l in myList:
    print(l)

print("Another way of doing this")
myList = [l for l in myList]
print(myList)

# can perform operation
myList = [l**2 for l in myList]
print(myList)

# or use if statemnet
myList = [l**2 for l in myList if l % 2 ==0]
print(myList)

print("Exercise")
st = "Print only the words that start with s in this sentence"
new_sen = st.split()
print(new_sen)
for every_word in new_sen:
    index = every_word
    if index[0] == "s":
        print(every_word)


