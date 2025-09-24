def greeting():
    print("Hello World")

human = {
    "name" : "Despina",
    "age" : 15
}

def countup():
    isTrue = True
    count = 0
    while isTrue:
        print(count)
        count = count + 1
        if count >= 10:
            isTrue = False
            break
            