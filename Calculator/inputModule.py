"""
inputModule.py => gets all the input (num1, num2, op)

def getnum1()
def getnum2()
def getOperation()
"""

def getnum1():
    print("What is your first number?")
    while True:
        try:
            num1 = int(input("Number 1: "))
            return num1
        except ValueError:
            print("This is not a number! Input number: ")
            continue
        break

def getnum2():
    print("What is your second number?")
    while True:
        try:
            num2 = int(input("Number 2: "))
            return num2
        except ValueError:
            print("This is not a number! Input number: ")
            continue
        break

def getOperation():
    print("What operation do you want to perform on the numbers? (Add, Sub, Div or Mult)")
    op = input("Operation: ").lower()
    return op