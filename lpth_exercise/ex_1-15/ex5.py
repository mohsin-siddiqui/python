


# This part is about Format String or f-string



name_of_person = 'Zed A. Shaw'
age_of_person = 35 # not a lie
height_of_person = 74 # inches
weight_of_person = 180 # lbs
color_of_eyes = 'Blue'
color_of_teeth = 'White'
color_of_hair = 'Brown'

# converting inches to centimeters:
height_in_cm = height_of_person * 2.54

# converting pounds into kilograms:
weight_in_kg = weight_of_person * 0.453592


print(f"Let's talk about {name_of_person}.")
print(f"He's {height_of_person} inches tall.")
print(f"i.e. He's {height_in_cm} centimeters tall.")
print(f"He's {weight_of_person} pounds heavy.")
print(f"i.e. He's {weight_in_kg} kilograms heavy.")
print("Aprroximately, He's ",round(weight_in_kg),"kilograms heavy.")
print("Actually that's not too heavy.")
print(f"He's got {color_of_eyes} eyes and {color_of_hair} hair.")
print(f"His teeth are usually {color_of_teeth} depending on the coffee.")

# this line is tricky, try to get it exactly right
total1 = age_of_person + height_of_person + weight_of_person

print(f"If I add {age_of_person}, {height_of_person}, and {weight_of_person} I get",str(total1) + ".")

total2 = age_of_person + height_in_cm + weight_in_kg
print(f"If I add {age_of_person}, {height_in_cm}, and {weight_in_kg} I get",str(total2) + ".")
