from sys import argv

script, input_file = argv

    # defing 3 different functions:

def print_all(f) :
    print(f.read())

def rewind(f) :
    f.seek(0)

def print_a_line(line_count, f) :
    print(line_count, f.readline())


    # defining a variable:
current_file = open(input_file)

    # calling a function:
print("First let's print the whole file:\n")
print_all(current_file)

    # calling second function:
print("Now let's rewind, kind of like a tape:\n")
rewind(current_file)

    # Now let's print three lines:
print("Let's print three lines:\n")

current_line = 1                                            # here value is 1
print_a_line(current_line, current_file)

current_line += 1                             # here value is 1 + 1 = 2
print_a_line(current_line, current_file)

current_line += 1                             # here value is 2 + 1 = 3
print_a_line(current_line, current_file)

# working of the third function is creating confusions:

#print(current_file.readline())
#print(current_line, current_file.readline())
#print(current_file.readline())
#print(current_file.readline())

