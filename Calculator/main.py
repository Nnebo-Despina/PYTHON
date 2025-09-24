"""
main.py
inputModule.py => gets all the input (num1, num2, op)
functionModule.py => add, sub, div and mult functions
logicModule.py => Conditional if statements

==================================================
main.py

while:
    inputModule.getnum1()
    inputModule.getnum2()
    inputModule.getOperation()

    logicModule.checkOp(op)

==================================================
inputModule.py

def getnum1()
def getnum2()
def getOperation()

====================================================
functionModule.py

def add()
def sub()
def div()
def mult()

====================================================
LogicModule.py

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

import inputModule
import logicModule
import functionModule

while True:
    logicModule.checkOp()

