# first section:
# let's keep this all in a separate function called introduction():

def introduction() :
    print("How old are you?", end=' ')
    age = input()
    print("How tall are you?", end=' ')
    height = input()
    print("How much do you weigh?", end=' ')
    weight = input()
    print(f"So, you're {age} old, {height} tall and {weight} heavy.")



# second section:
# making another function called contentOutput(filename) and putting all this section in that function:
from sys import argv
script, filename = argv

def contentOutput(filename) :
    txt = open(filename)
    print(f"Here's your file {filename}:")
    print(txt.read())

    print("Type the filename again:")
    file_again = input("> ")
    txt_again = open(file_again)
    print(txt_again.read())


# third section:
def printSomeNonse() :
    """This function will just print some nonsense!!"""
    people = 20
    cats = 30
    dogs = 15


    if people < cats:
        print ("Too many cats! The world is doomed!")

    if people > cats:
        print("Not many cats! The world is saved!")

    if people < dogs:
        print("The world is drooled on!")

    if people > dogs:
        print("The world is dry!")


    dogs += 5

    if people >= dogs:
        print("People are greater than or equal to dogs.")

    if people <= dogs:
        print("People are less than or equal to dogs.")

    if people == dogs:
        print("People are dogs.")