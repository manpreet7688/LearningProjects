# Instead of using polymorphism we can also use the same method having different values for different classes using abstarct

class Animal():
    def __init__(self,name):
        self.name = name

    def speak(self): # If this abstract function is not being defined in any class it will raise an error message as defined
        raise NotImplementedError ("This method has not been used in any subclass")

class Dog(Animal):
    def speak(self):
        return self.name + " says woof!"

class Cat(Animal):
    def speak(self):
        return self.name + " says meow!"


jacky = Dog("Jacky")
stacy = Cat("Stacy")
print(jacky.speak())
print(stacy.speak())