cars = 100 # assigning the value 100 to the variable cars
space_in_a_car = 4.0 # assigning the value 4.0 to the variable space_in_a_car,this value is a floating point number and different of 4 which is an integer
drivers = 30 # assigning the value 30 to the drivers variable
passengers = 90 # assigning the value 90 to the passengers variable
cars_not_driven = cars - drivers # assignig the value of the difference of cars and drivers to the variable cars_not_driven
cars_driven = drivers # assigning the value to drivers to the variable cars_driven
carpool_capacity = cars_driven * space_in_a_car # assignig the value of the product of cars_driven and space_in_a_car to the variable carpool_capacity
average_passengers_per_car = passengers / cars_driven # assigning the value of the quotient of passengers divided by cars_driven to the variable average_passengers_per_car


print("There are",cars,"cars available.")
print("There are only",drivers,"drivers available.")
print("There will be",cars_not_driven,"empty cars today.")
print("We can transport",carpool_capacity,"people today.")
print("We have",passengers,"to carpool today.")
print("We need to put about",average_passengers_per_car,"in each car.")
