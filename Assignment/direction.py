"""
A program to direct a person going to abakpa or emene from aptech.
"""

print("Hi! Where do you want me to direct you to?")
place = input("Place: ").lower()

if (place == "abakpa"):
    print("Enter keke or bus from Aptech to Ogbete Motor Park. \nThen enter a Shuttle or public bus heading toward Abakpa Nike or via the Abakaliki Road. \nDrop at Abakpa Market or Iji-Nike area.")

elif (place == "emene"):
    print("Enter a keke or bus from Aptech heading to Ogbete Motor Park. \nEnter a bus heading toward Abakaliki Expressway, then ask to be dropped off at Emene junction (near the airport side of town).")

else:
    print("I don't really know that place :(")