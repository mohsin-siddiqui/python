# https://www.unicode.org/Public/UCD/latest/charts/CodeCharts.pdf
# https://en.wikipedia.org/wiki/List_of_Unicode_characters


# using ascii backspace(\b):
#print("1234\b5678")

# using characters from unicode character database(ucd)
# \N{nameOfTheCharacter}
#print(u"\N{DAGGER} ")
#print(u"\N{DAGGER} " * 30)
#print(u"\N{heavy asterisk} " * 20)
#print(u"\N{asterisk} " * 20)
#print(u"\N{arabic five pointed star} " * 20)

# PRINTING 16 BIT HEX VALUED UNICODE CHARACTERS:
print(u"\u2030 " * 15) # this is the 16 bit hex value for per mile sign, so it will print it
#print(u"\u00b5 " * 15) # should print mew sign

#print(u"\u00a9  " * 5) # will print copyright sign

# let's try some more 16 bit hex value unicode characters :

print(u"\u041b")

# don't know why the below symbol is not working:

#print(u"\u0098") # sos symbol

# now let's try some 32 bit hex value unicode characters:

print(u"\U000003b1") # greek alpha
print(u"\U0001f910") # this is for emoji

print(u"\U000001a9")  # this will print sigma notation


# let's print some characters based on their octal value:

print(u"\043") # prints pound sign


# prints character based on it's hex value:
print(u"\x23") # it also prints pound sign
