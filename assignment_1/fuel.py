"""
******************************
This file is used to calculate the total cost of tne selected fuel type
based on user input of type and amount. It validates the fuel type and litres entered, 
then prints the final cost formatted to two decimal places.
******************************
"""

# Fuel cost dictionary
FUEL_COSTS = {
    "regular": 1.42,
    "extra": 1.53,
    "premium": 1.60,
    "diesel": 1.75
}

# Prompt user for fuel type (case-insensitive)
fuel_type = input("Please enter fuel type (regular, extra, premium, diesel): ").strip().lower()

# Check if the Fuel type is valid by looking it up in the dictionary
if fuel_type not in FUEL_COSTS:
    print("Error: Invalid fuel type entered. Program ending.") 

else:
    # Set the cost per litre based on the fuel type
    cost_per_litre = FUEL_COSTS[fuel_type]

    # Prompt user for the amount of fuel needed in litres
    litres_input = input("Enter number of litres (There must be a decimal point): ").strip()

    # Check if the provided litres_input is valid and raise Exception if not valid
    try:
        # We will raise the Exception for any invalid input
        if "." not in litres_input:
            raise Exception("Error: Invalid number, No decimal point found") # Check for decimal point
        
        # Split into fractional and integer parts using the split() method around the decimal point and check if both parts are digits
        before, after = litres_input.split(".")

        if not (before.isdigit() and after.isdigit()): # Check if both parts are digits
            raise Exception("Error: Invalid number, The input is not a valid number")
        
        if before == "" or after == "": # Check if both parts are not empty
            raise Exception("Error: Invalid number, Missing digits before and/or after decimal point")
        
        # Convert the input to float
        litres = float(litres_input)

        # Check that the number is a valid positive (greater than 0) number
        if litres <= 0:
            raise Exception("Invalid number, Error: Number must be positive")

        # Calculate total cost 
        total_cost = litres * cost_per_litre

        # Print formatted cost
        print(f"Cost: ${total_cost:.2f}")

    # Print any exceptions raised during input validation, then exit
    except Exception as e:
        print(e)
        print("Program ending.")

