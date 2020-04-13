class Animal():
    def __init__(self):
        print("This is an animal catalog")

    def for_dog(self):
        print("Yes, ofcourse, i bark")

    def for_cat(self):
        print("Yes, ofcourse, i meow")

    def default_color(self):
        print("Black")

class Dog(Animal):
    def __init__(self):
        Animal.__init__(self)
        print("I am a dog")

    def default_color(self, color):
        print("Default color is {}".format(color))



class Cat(Dog):
    def __init__(self):
        Animal.__init__(self)






my_dog = Dog()
my_dog.for_dog()
my_dog.default_color("Brown")


print("\n Cat's detail\n")
my_cat = Cat()
my_cat.for_cat()
my_cat.default_color("White")