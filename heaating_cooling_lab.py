def heating_cooling(actual_temp, desired_temp):
    if actual_temp == desired_temp:
        print("Standby")
    elif actual_temp > desired_temp:
        print("Run A/C")
    elif actual_temp < desired_temp:
        print("Run heat")

def convert_temp(temp_celsius, target_unit):
    if target_unit.upper() == 'C':
        print(f"{temp_celsius} degrees Celsius")
    elif target_unit.upper() == 'K':
        temp = temp_celsius + 273.15
        print(f"{temp} degrees Kelvin")
    elif target_unit.upper() == 'F':
        temp = (temp_celsius * (9/5)) + 32
        print(f"{temp} degrees Fahrenheit")

keep_going = 'y'

while keep_going == 'y':
    actual_temp = int(input("What is the current temperature? (in degrees Celsius) "))
    desired_temp = int(input("What is your desired temperature? (in degrees Celsius) "))
    temp_celsius = actual_temp
    target_unit = input("What unit would you like to convert to? (C, F, or K) ")

    heating_cooling(actual_temp,desired_temp)

    convert_temp(temp_celsius, target_unit)

    keep_going = input("Continue? (y/n) ")