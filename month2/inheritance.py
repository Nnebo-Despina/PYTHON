class Person:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def printFullName(self):
        print(self.fname, self.lname)

name = Person("Despina", "Nnebo")
name.printFullName()

class Student(Person):
    def printLastName(self):
        print(self.lname)

sanctus = Student("Sanctus", "Onah")
sanctus.printFullName()
sanctus.printLastName()

#NB: Study how to make child class have init. Learn how to loop through an iterator
