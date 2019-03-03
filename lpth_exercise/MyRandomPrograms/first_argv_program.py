from sys import argv

script,first_name,last_name,age = argv
nationality = input("What is your Nationality? ")
profession = input("What is your Profession? ")

print(u"\N{heavy asterisk} " * 25)
print("\tYour first_name is:", first_name)
print("\tYour last_name is:", last_name)
print("\tYour age is:", age)

# yob = year of birth:
yob = 2018 - int(age)
print(f"\t   So, You were born in year {yob}.")

print(f"\tYou are a {nationality}.")
print(f"\tYou are a {profession} by profession.")
