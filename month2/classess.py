# class User:
#     firstName = "Despina"
#     lastName = "Nnebo"
#     age = 209
#     gender = "Female"
#     nationality = "Nigerian"
#     email = "despina@gmail.com"
#     phoneNo = "+234 808 8888 888"

# p1 = User()

# p1.lastName = "okoro"

# class Person:
# 	#a constructor to get user data
# 	def _init_(self, name, age):
# 		self.name = name
# 		self.age = age

# 	#a method to return firstname
# # 	def printFirstName(self):
# # 		print(self.name)

# # userOne = Person("Daniel")
# # userOne.printFirstName()


# # print(p1.firstName)
# # print(p1.lastName)
# # print(p1.age)
# # print(p1.gender)
# # print(p1.nationality)
# # print(p1.email)
# # print(p1.phoneNo)


class User:
    # a constructor to get data
    def __init__(self, firstname, lastname, age, gender, nationality, email, phone):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.gender = gender
        self.nationality = nationality
        self.email = email
        self.phone = phone

    def printFirstName(self):
        print(self.firstname)

    def printLastName(self):
        print(self.lastname)

    def printAge(self):
        print(self.age)

    def printGender(self):
        print(self.gender)
        
    def printNationality(self):
        print(self.nationality)

# object of the class User
user1 = User("Despina", "Nnebo", 19, "Female", "Nigerian", "fake@gmail.com", "09060495111")
user1.printFirstName()


# user1.Lastname = "Okafor"
# print(user1.Lastname)
# print(user1.Firstname)
# print(user1.Lastname)
# print(user1.age)
# print(user1.Gender)
# print(user1.Nationality)
# print(user1.Email)
# print(user1.Phone)