"""
functionModule.py => add, sub, div and mult functions

def add()
def sub()
def div()
def mult()
"""
from inputModule import getnum1 as g1
from inputModule import getnum2 as g2

def add(num1, num2):
    add = num1 + num2 
    print(f"This is the sum of the two numbers; {add}") #addition

def sub(num1, num2):
    sub = num1 - num2
    print(f"This is the difference of the two numbers; {sub}") #subtraction

def div(num1, num2):
    if num2 == 0:
        print("Division by zero(0) is not possible.")
    
    else:
        div = num1 / num2
        print(f"This is the quotient of the two numbers; {div}") #division
        
def mult(num1, num2):
    mult = num1 * num2
    print(f"This is the product of the two numbers; {mult}") #multiplication 

