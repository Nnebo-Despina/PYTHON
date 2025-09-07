"""
Simple Password Strength Checker

Ask user for a password
Check if it meets criteria: at least 8 characters, has uppercase, lowercase, and numbers
Use loops to count each type of character
Keep asking until they provide a strong password
"""

while True:
    print("Input a strong password")
    password = input("Password: ")

    upperCase = 0
    lowerCase = 0
    includeNumber = 0

    for char in password:
        if char.isupper():
            upperCase += 1
        elif char.islower():
            lowerCase += 1
        elif char.isdigit():
            includeNumber += 1
        else:
            print

    if len(password) >= 8 and upperCase > 0 and lowerCase > 0 and includeNumber > 0:
        print("Password accepted!")
        break
    else:
        print("Weak password! \nMust have at least; \n8 characters, \n1 uppercase, \n1 lowercase, \nand 1 number.\nTry again.\n")
