"""
Make a human class that should have properties, namely;
No of eyes
Hair color
No of legs
Gender
Height

It should also include three methods;
Walking, which would print out I am walking
Speaking, which would print out I am talking
Breathing, which would print out I am breathing
"""

class Human:
    # noOfEyes = 2
    # hairColor = "Black"
    # noOfLegs = 2
    # gender = "Female"
    # height = "6'1"

    
    def __init__(self, noOfEyes, hairColor, noOfLegs, gender, height):
        self.noOfEyes = noOfEyes
        self.hairColor = hairColor
        self.noOfLegs = noOfLegs
        self.gender = gender
        self.height = height

    def walking():
        print("I am walking")

    def speaking():
        print("I am speaking")

    def breathing():
        print("I am breathing")

humanOne = Human(2,"Black", 2, "Female", 6.1)
print(humanOne.noOfEyes) 