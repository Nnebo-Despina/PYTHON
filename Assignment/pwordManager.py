"""
Build a password manager where:
1. Users will save their passwords for a particular thing.
2. It will be saved in a list
3. It can be viewed later
"""

passwords = []

def newPassword():
    print("What is the name of your password? (You can use the app or website name that it'll be used)")
    passwordName = input("Name: ")

    print("Input your password")
    password = input("Password: ")

    newPasswordList = [("name", passwordName), ("password", password)]
    newPasswordDict = dict(newPasswordList)
    passwords.append(newPasswordDict)
    print("Added!")

def showAllPasswords():
    for pword in passwords:
        pwordIndex = passwords.index(pword) + 1
        print (
            f"{pwordIndex}. { pword["name"] }: ({ pword["password"] })"
        )

print("Welcome to Password List! \nSponsored by Mr. Majesty, the taecher that gives assignment on impulse😑")
print("Select Operation: \n1. Add New Password\n2. Show All Passwords")
while True:
    try:
        op = int(input("Operation: "))
    except ValueError:
        print("This is not a number! Input operation number: ")
        continue
    
    if op == 1:
        newPassword()

    elif op == 2:
        showAllPasswords()
    
    else:
        print("That number is not among operations. Please, try again.")
        continue
