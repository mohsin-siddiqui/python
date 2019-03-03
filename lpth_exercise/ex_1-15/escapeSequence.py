# let 'esc' = escape sequence, then:

esc1 = "This is for \\ Backslash."
esc2 = "This is for \'Single-quote\'."
esc3 = "This is for \"Double-quote\""
esc4 = "This is for ASCII bell \a"
esc5 = "This is for ASCII backspace \b"
esc6 = "This is for ASCII formfeed \f"
esc7 = "This is for ASCII linefeed \n"
#esc8 = "This is for character named name in the Unicode database(Unicode only) \N{name}"
esc9 = "This is for Carriage Return \r"
esc10 = "This is for Horizontal Tab \t."
#esc11 = "This is for character with 16-bit hex value xxxx(u\" string only) \uxxxx"
#esc12 = "This is for character with 32-bit hex value xxxx(u\" string only) \Uxxxxxxxx"
esc13 = "This is for ASCII vertical tab \v"
#esc14 = "This is for character with octal value ooo, \ooo"
#esc15 = "This is for character with hex value hh, \xhh"


print(esc1)
print(esc2)
print(esc3)

print(esc4) # can't understand what it does
print(esc5) # can't understand what it does
print(esc6)
print("This is ascii formfeed.\flet's find what it does.\fEven now it's not so clear.\fLet's try it once more.\fNow it's more clear.")
print(esc7)
print("\\n is for linefeed or newline\nthis new line is created by it.")
#print(esc8)
print(u"\N{DAGGER}" * 30)
#print(esc9)
#print("checking \rwhich is used for carriage return.")

print(esc10)
print("Hi I'm \tHorizontal Tab.")

print(esc13)
print("Hi I'm\vVertical Tab.")

#print(esc14)
