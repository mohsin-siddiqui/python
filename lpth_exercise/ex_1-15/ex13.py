from sys import argv
# read the WYSS section for how to read this

#nameOfScript, first, second, third = argv

script, first, second, third = argv

#print("The script is called:", nameOfScript)
print("Your first variable is:", first)
print("Your second variable is:", second)
print("Your third variable is:", third)

print(third * 2)
print(int(third) * 2)
newInput = input("Your name?")
newInputB = int(input("Your Age?"))

print(f"So, your Age is {newInputB} and your name is {newInput}")