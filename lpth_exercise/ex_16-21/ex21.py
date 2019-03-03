def add(a, b) :
    print(f"ADDING {a} + {b}")
    return a + b

def subtract(a, b) :
    print(f"SUBTRACTING {a} - {b}")
    return a - b

def multiply(a, b) :
    print(f"MULTIPLYING {a} * {b}")
    return a * b

def divide(a, b) :
    print(f"DIVIDING {a} / {b}")
    return a / b

print("Let's do some math with just functions!")

age = add(int(input("valueForAge:> ")), 5)
height = subtract(float(input("valueForHeight:> ")), 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print(f"AGE: {age}, HEIGHT: {height}, WEIGHT: {weight}, IQ: {iq}")

# A puzzle for the extra credit, type it in anyway.

print("Here's is a puzzle.")

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))
whatB = subtract(age, multiply(height, add(weight, divide(iq, 2))))
whatC = divide(age, multiply(height, subtract(weight, add(iq, 2))))
whatD = multiply(age, subtract(divide(iq, 4), add(weight, height)))

# add(30, 5) + (subtract(74, multiply(180, divide(iq, 2))))
# 35+(74-(180*50/2))
# -4391

print("That becomes: ", what, "Can you do it by hand?")

print("I am whatB", whatB)
print("I am whatC", whatC)
print("I am whatD", whatD)

# The conclusion is the statements started to execute from the inner most part and expanded outside hence it is inside out!!


# exersise from drill:

# write formula for: 24 + 34 / 100 - 1023
# the Ans. is: -998.66
print("Time to print final result which should be:\n\n\n\n\n>>>>> -998.66\n\n")

finalResult = subtract(add(24, divide(34, 100)), 1023) 

print("And the calculated finalResult is: ", finalResult)

print("\t\tHENCE I NAILED THIS DRILL\t\t")