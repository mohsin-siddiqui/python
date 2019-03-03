import sys
script, encoding, error, = sys.argv     # is it another way to say: from sys import argv

def main(language_file, encoding, errors) :     # here we are passing three parameters or arguments to the function named main
    line = language_file.readline()             # assigning the value or line that readline function reads from language_file and assign it to the varible named line

    if line:                                    # no idea what it does since here isn't any boolean or any other check to the line variable 
        print(line, encoding, errors)
        return main(language_file, encoding, errors)    # don't even know what it does


def print_line(line, encoding, errors) :
    next_lang = line.strip()                    # strip prints some part or piece of a string so this statement will only cut some part of the value of line variable and assigns this new value to a new variable called next_lang
    raw_bytes = next_lang.encode(encoding, errors = errors)             # I think it will encode the parameter
    cooked_string = raw_bytes.decode(encoding, errors = errors)         # and it will decode the parameter

    print(raw_bytes, "<===>", cooked_string)


languages = open("languages.txt", encoding = "utf-8")    # making a file object
main(languages, encoding, error)                # calling the above main function