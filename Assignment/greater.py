"""
This program takes two inputed numbers and shows whether one is greater than the other.
"""

print("What is your first number?")
num1 = int(input("Number 1: "))

print("What is your second number?")
num2 = int(input("Number 2: "))

if (num1 > num2):
    print("Number 1 is greater than number 2.")

elif (num1 < num2):
    print("Number 2 is greater than number 1.")

elif (num1 == num2):
    print("They are the same numbers.")

else:
    print("Error")