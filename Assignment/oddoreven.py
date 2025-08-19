"""
This displays if the number a user inputs is odd or even.
"""

print("Welcome to Odd Or Even! Please input your number.")
num = int(input("Number: "))

if (num % 2 == 0):
    print("It's an even number!")

elif (num % 2 != 0):
    print("It's an odd number!")

else:
    print("This is not a number :(")