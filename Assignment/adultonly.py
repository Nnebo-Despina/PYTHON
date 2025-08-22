"""
Make a program that will keep running until the user gives an age that is above 18.
"""

print("How old are you?")
age = int(input("Age: "))

while(age < 18):
    print("Too young. Want to try again?")
    age = int(input("Age: "))

print("Welcome adult!")
