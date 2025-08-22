"""
Make a program that will collect an int input from the user and keeps running until the user gives you a negative number.
"""

print("Input a positive only number (or else...)")
positive = int(input("Positive Number: "))

while(positive >= 0):
    print("Good, now keep input a positive only number (or else...)")
    positive = int(input("Positive Number: "))

print("Why did you do that? :(")
