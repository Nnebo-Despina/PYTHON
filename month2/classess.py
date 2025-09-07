class User:
    firstName = "Despina"
    lastName = "Nnebo"
    age = 209
    gender = "Female"
    nationality = "Nigerian"
    email = "despina@gmail.com"
    phoneNo = "+234 808 8888 888"

p1 = User()

p1.lastName = "okoro"
print(p1.lastName)

class Person:
  def _init_(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)

print(p1.name)
print(p1.age)

# print(p1.firstName)
# print(p1.lastName)
# print(p1.age)
# print(p1.gender)
# print(p1.nationality)
# print(p1.email)
# print(p1.phoneNo)
