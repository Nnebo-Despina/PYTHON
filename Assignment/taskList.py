"""
Build a task list program in Python where the user can:
1. Add tasks
2. Update task names
3. Delete tasks
4. Mark tasks as completed
"""
tasks = []

def addTask():
    print("What is your task?")
    taskName = input("Task: ")
    newTask = [("task", taskName), ("completed", False), ("deleted", False)]
    newDict = dict(newTask)
    tasks.append(newDict)
    print("Added!")

def updateTaskName():
    print("What number is your designated task in?")
    while True:
        try:
            taskIndex = int(input("Task number: "))
            print("Input new task name:")
            newTaskName = input("Name: ")

            tasks[taskIndex - 1]["task"] = newTaskName
        except ValueError:
            print("This is not a number! Input task number: ")
            continue
        except IndexError:
            print("There is no task like that existing! Try again.")
            continue
        break

    print("Done!")

def markCompleted():
    print("What is the number of the task you completed?")
    while True:
        try:
            taskIndex = int(input("Task number: "))
            tasks[taskIndex - 1]["completed"] = True
        except ValueError:
            print("This is not a number! Input task number: ")
            continue
        except IndexError:
            print("There is no task like that existing! Try again.")
            continue
        break
    
    print("Done!")

def deleteCompleted():
    print("What is the number of the task you wish to delete?")
    while True:
        try:
            taskIndex = int(input("Task number: "))
            tasks[taskIndex - 1]["deleted"] = True
        except ValueError:
            print("This is not a number! Input task number: ")
            continue
        except IndexError:
            print("There is no task like that existing! Try again.")
            continue
        break

    print("Done!")

def showTask():
    for indiTask in tasks:
        if indiTask["deleted"] == False:
            taskIndex = tasks.index(indiTask) + 1
            print (f"{taskIndex}. { indiTask["task"] } - Completed({ indiTask["completed"] })")
        else:
            print

print("Welcome to Task List! \nSponsored by Mr. Majesty, the teacher that gives assignment on impulse😑")
print("Select Operation: \n1. Add Task\n2. Update Task Name\n3. Mark Task as Complete\n4. Delete Task\n5. View all Tasks (Bonus by me :)")
while True:
    try:
        op = int(input("Operation: "))
    except ValueError:
        print("This is not a number! Input operation number: ")
        continue
    
    if op == 1:
        addTask()

    elif op == 2:
        updateTaskName()
    
    elif op == 3:
        markCompleted()

    elif op == 4:
       deleteCompleted()

    elif op == 5:
        showTask()

    else:
        print("That number is not among operations. Please, try again.")
        continue
