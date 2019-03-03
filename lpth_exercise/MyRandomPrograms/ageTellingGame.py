age = float(input(">"))
if 60 >= age >= 18:
    print("Congratulations!! You can Join Our Program!")
    print("\t\tWELCOME TO GAME OF GUTS")
    
elif 0 < age < 18:
    print("Sorry!! You cannot Join Our Program!")
elif age > 60:
    print("Sorry Grandpa!! You are Too Old to join this Program!!")
else:
    print("Incorrect Input!!")