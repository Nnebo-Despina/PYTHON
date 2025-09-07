"""
Create a multiplications table
"""

#while loop
# num1 = int(input("What number do you want to multiply? "))
# multipler = 1
# while (multipler <= 12):
#     product = num1 * multipler
#     print(f"{num1} x {multipler} = {product}")
#     multipler += 1

# for loop
# multiplyTable = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

number = int(input("What number do you want to multiply? "))
for multiple in range(1, 13):
    product = number * multiple
    print(f"{number} x {multiple} = {product}")