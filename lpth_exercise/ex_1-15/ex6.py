

# DIFFERENT TYPES OF VARIABLES:

types_of_people = 10 # declaring a variable
x = f"There are {types_of_people} types of people." # declaring a f-string variable

binary = "binary" # declaring a string variable
do_not = "don't" # declaring a string variable
y = f"Those who know {binary} and those who {do_not}." # declaring a f-string variable
                                                        # also here two strings r inserted in a string or f-string
print(x) # printing the variables x and y respectively
print(y)

print(f"I said: {x}") # printing f-string #also a string is put inside a string
print(f"I also said: '{y}'") # printing f-string #also a string is put inside a string

hilarious = False # assigning the boolean False to hilarious variable


# Use of .format() model of f-strings:


joke_evaluation = "Isn't that joke so funny?! {}" # assigning f-string in .format() model
print(joke_evaluation.format(hilarious)) # passing the value of variable hilarious to the above format string





w = "This is the left side of..." # assingning a string variable
e = "a string with a right side." # assingning another string varianble

print(w + e) # adding the above two variables and printing them to the stdout
                # hence adding two strings concatenates them together and makes a longer string
