"""
Set a secret number (e.g., 7) and Ask the user to guess the number.
Keep asking until they guess correctly
When guessed right, print "Correct! You win."
"""
print("Guess the number :)")
guess = int(input("Number: "))
secretNo = 7

while(guess != secretNo):
    print("Wrong! \nGuess the number :)")
    guess = int(input("Number: "))

print("Correct! You win!")