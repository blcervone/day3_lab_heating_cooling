# Define first function using parameters in if/else statements
def heating_cooling(actual_temp, desired_temp):
    if actual_temp == desired_temp:
        print("Standby")
    elif actual_temp > desired_temp:
        print("Run A/C")
    elif actual_temp < desired_temp:
        print("Run heat")

# Define second function using parameters in if/else statements
def convert_temp(temp_celsius, target_unit):
    if target_unit.upper() == 'C':
        print(f"{temp_celsius} degrees Celsius")
    elif target_unit.upper() == 'K':
        temp = temp_celsius + 273.15
        print(f"{temp} degrees Kelvin")
    elif target_unit.upper() == 'F':
        temp = (temp_celsius * (9/5)) + 32
        print(f"{temp} degrees Fahrenheit")

# Initialize flag variable for while loop signal
keep_going = 'y'

# Start while loop to ask user for function parameter input and output defined functions with input parameters
while keep_going == 'y':
    # Ask for values from user
    actual_temp = int(input("What is the current temperature? (in degrees Celsius) "))
    print()
    desired_temp = int(input("What is your desired temperature? (in degrees Celsius) "))
    print()
    temp_celsius = actual_temp
    target_unit = input("What unit would you like to convert to? (C, F, or K) ")
    print()

    # Instantiate defined functions with input parameters given by user
    heating_cooling(actual_temp,desired_temp)
    print()

    convert_temp(temp_celsius, target_unit)
    print()

    # Ask if user would like to continue
    keep_going = input("Continue? (y/n) ")
    print()