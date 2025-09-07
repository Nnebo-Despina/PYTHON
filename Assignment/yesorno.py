"""
Keep asking the user if he wants to continue
They should choose between y or n
If y. Then keep running he program 
If n then break and end the program
"""

print("Do you want to continue?")
choice = input("Choice: ")

while(choice == "y"):
    print("Do you want to continue?")
    choice = input("Choice: ")
    if(choice == "y"):
        continue
    elif(choice == "n"):
        break
    else:
        print("invalid input.")