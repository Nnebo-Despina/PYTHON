"""
Create a class called "Human"
Create a constructor that will create properties namely;
name
eye 
nose 
skin 
ear 
toungue 
limb 
skincolor
height

Create a method called "walking" that prints "I am walking"
Create a method called "talking" that prints "I am talking"
"""

class Human:
    def __init__(self, name, eye, nose, ear, tongue, limb, skinColor, height):
        self.name = name
        self.eye = eye
        self.nose = nose
        self.ear = ear
        self.tongue = tongue
        self.limb = limb
        self.skinColor = skinColor
        self.height = height

    def walking(self):
        print(f"{self.name.capitalize()} is walking")

    def talking(self):
        print(f"{self.name.capitalize()} is talking")

despina = Human("despina", 2, 1, 2, 1, 4, "fair", "5.4")
despina.walking()
despina.talking()

