from sys import argv        # importing argv from sys module
script, filename = argv     # declaring two argument variables

txt = open(filename)        # opening file with name filename and storing it's value to txt

print(f"Here's your file {filename}:")      # printing a short format string with variable filename
print(txt.read())           # reading the value stored in txt variable and printing it on stdout

print("Type the filename again:")           # printing a short string(asking for the filename again)
file_again = input("> ")                    # taking file name as input and storing it to a new variable called file_again

txt_again = open(file_again)        # opening the above file and storing it to txt_again variable

print(f"Here's your file {file_again}:")       # a simple and short format string with variable file_again
print(txt_again.read())             # reading txt_again and printing it to stdout
