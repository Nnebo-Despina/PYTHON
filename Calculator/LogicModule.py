"""
logicModule.py => Conditional if statements

def checkOp()
    if(op == "add"):
        functionModule.add()
    
    if(op == "sub"):
        functionModule.sub()

    if(op == "div"):
        functionModule.div()

    if(op == "mult"):
        functionModule.mult()
"""

import functionModule
from inputModule import getnum1 as g1, getnum2 as g2, getOperation as go

def checkOp():
    while True:
        num1 = g1()
        num2 = g2()
        op = go()

        if op == "add":
            functionModule.add(num1, num2)
            break
        
        elif op == "sub":
            functionModule.sub(num1, num2)
            break

        elif op == "div":
            functionModule.div(num1, num2)
            break

        elif op == "mult":
            functionModule.mult(num1, num2)
            break

        else:
            print("This is not an operation")
            continue
