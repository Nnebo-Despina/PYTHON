# name = "Antelopes"
# verb = "have"
# very = "very"
# long = "long"
# legs = "legs."
# fate = "Unfortunately,"
# they = "they"
# are = "are"
# time = "often"
# prey = "prey"
# fo = "for"
# animal = "lions."

# print(name, verb, very, long, legs, fate, they, are, time, prey, fo, animal)

"""
Obi is a boy, who loves football.
He's a student of Aptech

Obi = name
boy = gender
football = sport
he = heHer
aptech = school
"""
print("What is your name?")
name = input("Name: ")

print("Are you a boy or a girl?")
gender = input("Gender: ")

print("What sport are you interested in?")
sport = input("Sport: ")

print("Are you a he or a she?")
heShe = input("Pronoun: ")

print("What is the name of your school?")
school = input("School: ")

print(f"{name.capitalize()} is a {gender.lower()}, who loves {sport.lower()}. \n{heShe.capitalize()}'s a student of {school}.")
