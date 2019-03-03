#i = 0   # initializing the value
#numbers = []    # daclaring an empty list

#while i < 6:    # condition check or boolean check
   # print(f"At the top i is {i}")
   # numbers.append(i)

   # i = i + 1   # updating the value
   # print("Numbers now: ", numbers)     # printing members of above list so far
   # print(f"At the bottom i is {i}")    # new updated value of i


#print("The numbers: ")

#for num in numbers:
    #print(num)





############################# Doing this with for loop ##############################################


numbers = []

for i in range(0, 6) :
    numbers.append(i)
    print("Numbers now: ", numbers)
    i += i  # hence incrementer shows no effect in a for loop
    print("New value of i is: ", i)

print("finally, Numbers are: ", numbers)