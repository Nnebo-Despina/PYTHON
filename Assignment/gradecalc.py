"""
Grade Calculator

Ask user for their score (0-100)
Assign letter grades: A (90+), B (80-89), C (70-79), D (60-69), F (<60)
Provide encouraging messages based on the grade
Handle invalid input (scores outside 0-100 range)
"""
while True:
    print("What is your score?")
    score = int(input("Score: "))

    if score >= 90 and score <= 100:
        print("A \nAmazing job! Keep up the good work")

    elif score >= 80 and score <= 89:
        print("B \nGreat job! Keep working hard!")

    elif score >= 70 and score <= 79:
        print("C \nKeep striving, you can do better!")

    elif score >= 60 and score <= 69:
        print("D \nDon't be discouraged! You can do better!")

    elif score < 60:
        print("F \nDon't be discouraged! You can do better!")

    else:
        print("Invalid input.")