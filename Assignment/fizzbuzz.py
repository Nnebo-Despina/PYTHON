"""
You are to build a program that will print out from numbers 1 to 30.
It should print "fizz" if it gets to the number 3 or any number divisible by 3. 
It should print "buzz" if it gets to the number 5 or any number divisible by 5. 
"""

begin = 1

while (begin <= 30):
    if(begin % 3 == 0):
        print("fizz")
    elif(begin % 5 == 0):
        print("buzz")
    else:
        print(begin)
    begin += 1