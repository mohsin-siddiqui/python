print("Mary had a little lamb.") # printing this string

# IMPORTANT:

print("Its fleece was white as {}.".format('snow')) # printing this format string and inserting the string snow in it with the help of .format() method
                                                    # inserting a string into a string

print("And everywhere that Mary went.") # printing this string
print("." * 10) # what'd that do?        # this will print 10 dots

end1 = "C"       # assingning C to the variable end1 and so on
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"

# watch that comma at the end. try removing it to see what happens.
print(end1 + end2 + end3 + end4 + end5 + end6 , end=' ')    # concatenating end1:end6 and adding spcace at the end of the string
                                                        # this adds the space but prints the upcoming string in the same line
print(end7 + end8 + end9 + end10 + end11 + end12) # concatenating end7:end12

print('check', end=' * ')
print('test')


# hence it is concluded that the keyword end is used to end the line with some thing and print the next line just after that!

# see ex11.py for more details on end