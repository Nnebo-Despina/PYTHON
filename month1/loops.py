# begin = 1
# end = 10

# while(begin <= end):
#     print(begin)
#     begin += 1
#     # begin = begin + 1

myList = ["football", "basketball", "tennis", "golf", "swimming", "racing"]

counter = 1
for item in myList:
    print(item)
    if (item == "golf"):
        print(f"This is {item}")
        print(counter)
        break
    else:
        counter += 1
        continue

    

# name = "despina"
# for letter in name:
#     print(letter)
