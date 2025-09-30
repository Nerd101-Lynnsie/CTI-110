###Zaria Hill - Sept. 25,2025 - P2LAB2 - Create a dictionary used to calculate gas


###Create the dictionary
cars_to_gas = {"Camraro":18.21, "Prius":52.36, "Model S":110, "Silverado":26}

##Display all keys to the user
print()
print(cars_to_gas.keys())

###Get input from user
car_name = input("Enter a vehicle to see it's mpg: ")
print()


##Create a variable to hold the mpg of the given car
car_mpg = cars_to_gas[car_name]

##Display info to user
print(f"The {car_name} gets {car_mpg} mpg.")

#Ask the user how many miles they will drive the car
print()
miles = int(input(f"How many miles will you drive the {car_name}? "))
print()

#Create a variable to hold the gallons of gas needed
gas_gallons = miles / car_mpg
print()

#Display info to user
print(f"{gas_gallons:.2f} gallon(s) of gas are needed to drive the {car_name} {miles} miles.")