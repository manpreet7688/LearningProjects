class Dog():
    def __init__(self,name):
        self.name = name

    def speak(self):
        return self.name + " says woof!"

class Cat():
    def __init__(self,name):
        self.name = name

    def speak(self):
        return self.name + " says meow!"


niko_dog = Dog("Niko")
stacy_cat = Cat("Stacy")

print(niko_dog.speak())
print(stacy_cat.speak())

for pet in [niko_dog,stacy_cat]:
    print(type(pet))
    print(pet.speak())

def pet_speak(pet):
    print(pet.speak())

pet_speak(niko_dog)
pet_speak(stacy_cat)
