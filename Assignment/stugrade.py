"""
A Very Simple Student Grade Tracker

Create a dictionary where keys are student names and values are lists of their test scores
Add functions to:

Add a new student
Add a grade for existing student
Calculate average grade for each student
Find the student with highest average
Display all students and their grades in a formatted table
"""

studentDict = {"James": [90, 70, 98], "Mary": [60, 75, 85], "Tiffany": [96, 93, 43]} 

def newStudent():
    
    print("Input new student's name: ")
    newName = input("Name: ").capitalize()

    if newName in studentDict:
        studentDict[newName] = []
    else:
        print("Student is not found. Try again.")


def newGrade():
    print("Input new grade: ")
    newGrade = int(input("Grade: "))
    studentDict["James"].append(newGrade)

def avgGrade():
    print("Input name of student for average: ")
    nameStudent = input("Name: ").capitalize()

    if nameStudent in studentDict:
        avgSum = sum(studentDict[nameStudent])
        avgLen = len(studentDict[nameStudent])
        average = avgSum / avgLen
        print(f"The average score of {nameStudent} = {average}")

    else:
        print("Student is not found. Try again.")

def highestAvgGrade():
    avgSum1 = sum(studentDict["James"])
    avgLen1 = len(studentDict["James"])
    average1 = avgSum1 / avgLen1
    
    avgSum2 = sum(studentDict["Mary"])
    avgLen2 = len(studentDict["Mary"])
    average2 = avgSum2 / avgLen2

    avgSum3 = sum(studentDict["Tiffany"])
    avgLen3 = len(studentDict["Tiffany"])
    average3 = avgSum3 / avgLen3

    if average1 > average2 and average3:
        print("The student with the hights average is James.")

    elif average2 > average1 and average3:
        print("The student with the hights average is Mary.")

    elif average3 > average1 and average2:
        print("The student with the hights average is Tiffany.")

    else:
        print("Unknown error has occured.")
    
def displayStudents():
    print("Student Grades:")
    print("Name  \t  Grades")

    for name, grades in studentDict.items():
        print(name, grades)

newStudent()
