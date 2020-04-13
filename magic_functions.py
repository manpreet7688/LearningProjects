'''If there is an instance say my_dog = Dog()
and you print (my_dog) or print(len(my_dog)), it will throw an error as print functions provide string and it will show
the memory in which the object is stores as this is the only string value in case of an object , a print
functions finds out
So if you define __str__ in your code , then print(my_dog), print function asks you if you have any string
representation of this object
Lets see an example'''

class Books():
    def __init__(self, name, author , page):
        self.name = name
        self.author = author
        self.page = page

    def __str__(self):
        return "The name of the book is {} and author of the book is {}".format(self.name,self.author)

    def __len__(self): # Asking for the number of pages
        return self.page

my_book = Books("Meditation","Marcus",200)
print(my_book)
print(len(my_book))

# You can also delete the instance and free up the memory
class test():
    def __init__(self):
        print("testing")

    def __str__(self):
        return "Pupose of this class to show how to delete an object/instance"

test = test()
print(test)
del test