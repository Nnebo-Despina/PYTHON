"""
Create a funtion that;
sum of two numbers
says im in class
"""
# print("Enter first number")
# num1 = int(input("Number 1: "))

# print("Enter second number")
# num2 = int(input("Number 2: "))

# def sum():
#     sum = num1 + num2
#     print(f"The sum of {num1} and {num2} is {sum}")
    
# def add(a, b):
#     print(f"The sum of {a} and {b} is {a + b}")

# add(num1, num2)
# myName = input("Enter your name: ")

# def greet(name):
#     print(f"Hello user {name}")

# greet(myName)

# classList = ["nenye", "actress", "despina", "kamsy", "somto", "sanctus", " chisom", "irene", "pascal", "jude", "daniel", "chiemerie", "kosi"]

# def nameCheck(list):
#     for name in list:
#         if name.capitalize() == "Despina":
#             print(f"That's me, {name.capitalize()}!")
#         else:
#             print("That's not me.")

# nameCheck(classList)

def tri_recursion(k):
    if k > 0:
        result = k + tri_recursion(k - 1)
        print(result)
    else:
        result = 0
    return result

print("Recurssion Example Result")
tri_recursion(6)