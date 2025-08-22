"""
Print number between 13 - 35 jand show if they are odd or even
"""

begin = 13
end = 35

while(begin <= end):
    print(f"this is the value of begin: {begin}")

    if (begin % 2 == 0):
        print("It's an even number!")
    elif (begin % 2 != 0):
        print("It's an odd number!")
        
    begin += 1
    # begin = begin + 1

