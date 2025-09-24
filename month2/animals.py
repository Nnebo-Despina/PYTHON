"""
Create a class called "Dog"
Create a constructor that will create properties called name & breed
Create a method called "Bark" that prints "woof woof"
"""

#Dog
class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        print("woof woof")

#Cat
class Cat:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def meow(self):
        print("meow meow")

    def printName(self):
        print(self.name)

    def __str__(self):
        return "This class requires a name and breed \n~ Despina"

myDog = Dog("Laura", "Pomerian")
# myDog.bark()

myCat = Cat("Mr. Meows", "Sphinx")
# myCat.meow()
# print(myCat)
myCat.name = "Pew Pew"
myCat.printName()
del myCat.breed
