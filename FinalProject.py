########################################################################################
# Program Filename: FinalProject.py
# Author: Daniel Juliano, Tycho Butler, Kyle Wern, Sam Harker, Austin Gugenheim
# Date: 2023-06-4
# Description: Calculates heating and cooling loads on HVAC units and plots data
# Input: target_temp, surface_area,, ceiling height, number_occupants, number_doors,
# number_windows, number_machines,
# Output: cooling_btu, heating_btu, matplotlib
########################################################################################
import matplotlib.pyplot as plt


# sets up code to run and shows it hasn’t been run before
run = True
month_temp = []
heating_coefficient = []
cooling_coefficient = []
calculated = False


# base variable inputs
target_temp = 0.0
surface_area = 0.0
ceiling_height = 0.0
number_occupants = 0.0
number_doors = 0.0
number_windows = 0.0
number_machines = 0.0


########################################################################################
# Function name: collect_user_inputs
# Description: Collects user inputs for building information.
# Parameters: None
# Return Values: None
# Pre-Conditions: None
# Post-Conditions: The global variables for building info are updated with user inputs.
########################################################################################
def collect_user_inputs():
    global target_temp, surface_area, ceiling_height, number_occupants, number_doors, number_windows, number_machines
    while True:
        try:
            target_temp = float(
                input("What is the target temperature for the building: ")
            )
            surface_area = float(input("Surface Area: "))
            ceiling_height = float(input("What is the ceiling height: "))
            number_occupants = float(input("What is the number of occupants: "))
            number_doors = float(input("How many exterior doors are on the building: "))
            number_windows = float(input("How many windows are on the building: "))
            number_machines = float(input("How many machines are in the building: "))
            break
        except ValueError:
            print("bad input")
            pass


########################################################################################
# Function name: get_inputs
# Description: Prints the current building info and prompts the user to enter values.
# Parameters: None
# Return Values: None
# Pre-Conditions: None
# Post-Conditions: The global variables for building info are updated with user inputs.
########################################################################################
def get_inputs():
    global target_temp, surface_area, ceiling_height, number_occupants, number_doors, number_windows, number_machines
    print("--- Current Building Information ---")
    print(f"Target Temperature: {target_temp}")
    print(f"Surface Area: {surface_area}")
    print(f"Ceiling Height: {ceiling_height}")
    print(f"Number of Occupants: {number_occupants}")
    print(f"Number of Exterior Doors: {number_doors}")
    print(f"Number of Windows: {number_windows}")
    print(f"Number of Machines: {number_machines}")
    print("----------------------------------")
    print("Enter the new values:")

    while True:
        try:
            target_temp = float(
                input("What is the target temperature for the building: ")
            )
            surface_area = float(input("Surface Area: "))
            ceiling_height = float(input("What is the ceiling height: "))
            number_occupants = float(input("What is the number of occupants: "))
            number_doors = float(input("How many exterior doors are on the building: "))
            number_windows = float(input("How many windows are on the building: "))
            number_machines = float(input("How many machines are in the building: "))
            break
        except ValueError:
            print("bad input")
            pass


month_names = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
]


########################################################################################
# Function name: average_month_temp
# Description: Collects average temperature inputs for each month.
# Parameters: month_names - a list of month names
# Return Values: None
# Pre-Conditions: None
# Post-Conditions: The month_temp list is updated with avg temps for each month.
########################################################################################
def average_month_temp(month_names):
    global month_temp
    for month in month_names:
        while True:
            try:
                temp = float(input(f"Enter the average temperature for {month}: "))
                month_temp.append(temp)
                break
            except ValueError:
                print("Invalid input. Please enter a valid floating-point number.")
                pass


########################################################################################
# Function name: calculate_coefficients
# Description: Calculates the heating and cooling coefficients for each month.
# Parameters: None
# Return Values: None
# Pre-Conditions: The month_temp list should be populated with average temperatures for each month.
# Post-Conditions: The heating_coefficient and cooling_coefficient lists are populated with calculated coefficients.
########################################################################################
def calculate_coefficients():
    global heating_coefficient, cooling_coefficient
    for i in range(12):
        a = target_temp / month_temp[i]
        a = round(a, 1)
        heating_coefficient.append(a)

        b = month_temp[i] / target_temp
        b = round(b, 1)
        cooling_coefficient.append(b)


########################################################################################
# Function name: calculate_HVAC_load
# Description: Calculates the HVAC load.
# Parameters: None
# Return Values: HVAC_load - the calculated HVAC load
# Pre-Conditions: The global variables for building information should be properly set.
# Post-Conditions: None
########################################################################################
def calculate_HVAC_load():
    HVAC_load = (
        (surface_area * ceiling_height)
        + (number_occupants * 100)
        + (number_doors * 1000)
        + (number_windows * 1000)
        + (number_machines * 250)
    )
    return HVAC_load


########################################################################################
# Function name: calculate_cooling
# Description: Calculates the cooling BTU for each month.
# Parameters: None
# Return Values: cooling_btu - a list of calculated cooling BTU values
# Pre-Conditions: The heating_coefficient and cooling_coefficient are populated.
# Post-Conditions: None
########################################################################################
def calculate_cooling():
    cooling_btu = []
    HVAC_load = calculate_HVAC_load()
    for i in range(12):
        c = cooling_coefficient[i] * HVAC_load
        c = round(c, 1)
        cooling_btu.append(c)
    return cooling_btu


########################################################################################
# Function name: calculate_heating
# Description: Calculates the heating BTU for each month.
# Parameters: None
# Return Values: heating_btu - a list of calculated heating BTU values
# Pre-Conditions: The heating_coefficient and cooling_coefficient lists are populated.
# Post-Conditions: None
########################################################################################
def calculate_heating():
    heating_btu = []
    HVAC_load = calculate_HVAC_load()
    for i in range(12):
        h = heating_coefficient[i] * HVAC_load
        h = round(h, 1)
        heating_btu.append(h)
    return heating_btu


########################################################################################
# Function name: calculate_energy_draw
# Description: Calculates the energy draw for different components.
# Parameters: None
# Return Values: The energy draw values for doors, occupants, windows, and machines.
# Pre-Conditions: The global variables for building information should be properly set.
# Post-Conditions: None
########################################################################################
def calculate_energy_draw():
    number_occupants_energy = number_occupants * 100
    number_doors_energy = number_doors * 1000
    number_windows_energy = number_windows * 1000
    number_machines_energy = number_machines * 250
    return (
        number_doors_energy,
        number_occupants_energy,
        number_windows_energy,
        number_machines_energy,
    )


########################################################################################
# Function name: compare_energy_draw
# Description: Compares energy draw values and provides recommendations.
# Parameters:
#   - number_doors_energy: Energy draw from doors
#   - number_occupants_energy: Energy draw from occupants
#   - number_windows_energy: Energy draw from windows
#   - number_machines_energy: Energy draw from machines
# Return Values: None
# Pre-Conditions: None
# Post-Conditions: None
########################################################################################
def compare_energy_draw(
    number_doors_energy,
    number_occupants_energy,
    number_windows_energy,
    number_machines_energy,
):
    max_energy_draw = max(
        number_doors_energy,
        number_occupants_energy,
        number_windows_energy,
        number_machines_energy,
    )

    categories = []
    if number_doors_energy == max_energy_draw:
        categories.append("The number and quality of doors you have")
    if number_occupants_energy == max_energy_draw:
        categories.append("The number of occupants in your building")
    if number_windows_energy == max_energy_draw:
        categories.append("The number and quality of windows you have")
    if number_machines_energy == max_energy_draw:
        categories.append("The number of machines you have")

    print("The largest HVAC energy draw(s) on your building is/are:")
    print(", ".join(categories))
    print("Tips to reduce energy usage:")
    if "The number and quality of doors you have" in categories:
        print("- Optimize door usage, check for drafts, and ensure proper sealing.")
    if "The number of occupants in your building" in categories:
        print(
            "- Promote energy-saving behaviors among occupants, such as turning off lights when not needed."
        )
    if "The number and quality of windows you have" in categories:
        print(
            "- Upgrade windows to energy-efficient models, consider window films or shades for insulation."
        )
    if "The number of machines you have" in categories:
        print(
            "- Optimize machine usage, implement energy-saving settings, and explore energy-efficient alternatives."
        )


########################################################################################
# Function name: go
# Description: Perform calculations and plot energy usage graphs.
# Parameters: None
# Return Values: None
# Pre-Conditions: The heating_coefficient and cooling_coefficient lists are populated.
# Post-Conditions: None
########################################################################################
def go():
    calculate_coefficients()
    heating_btu = calculate_heating()
    cooling_btu = calculate_cooling()
    plt.bar(month_names, heating_btu, color="orange")
    plt.title("Heating Energy")
    plt.xlabel("Months")
    plt.ylabel("Average energy used per day for each month")
    plt.xticks(rotation=45)
    plt.show()
    plt.bar(month_names, cooling_btu)
    plt.title("Cooling Energy")
    plt.xlabel("Months")
    plt.ylabel("Average energy used per day for each month")
    plt.xticks(rotation=45)
    plt.show()


########################################################################################
# Function name: menu
# Description: Displays the menu options for the program to a user.
# Parameters: None
# Return Values: None
# Pre-Conditions: None
# Post-Conditions: None
########################################################################################
def menu():
    global menu_input
    print("0----------------------------------------------------0")
    print("Menu:")
    print("Quit - Exit the program")
    print("Start - Calculate the HVAC load and energy usage")
    print("Show - Display the energy usage graphs")
    print("Edit - Edit the building information")
    print("0----------------------------------------------------0")

    menu_input = input("what would you like to do? ")


########################################################################################
# Function name: main
# Description: Acts as the brain of the code choosing which processes run
# Parameters: None
# Return values: None
# Pre-Conditions: run = True
# Post-Conditions: None
########################################################################################
def main():
    global run, calculated, menu_input

    while run:  # Add a while loop to keep the program running until 'run' is False
        menu()

        if menu_input == "Quit":
            print("Goodbye, thank you")
            run = False
            break
        elif menu_input == "Start":
            if not calculated:
                collect_user_inputs()
                average_month_temp(month_names)
                calculated = True
            calculate_energy_draw()
            go()
            compare_energy_draw(*calculate_energy_draw())
            break
        elif menu_input == "Show":
            if not calculated:
                print("Please calculate the HVAC load and energy usage first.")
                print()
            else:
                go()
                compare_energy_draw(*calculate_energy_draw())
                break
        elif menu_input == "Edit":
            if not calculated:
                print("Please run the initial calculation before making edits")
            else:
                global heating_btu, cooling_btu
                get_inputs()
                print("Building information updated.")
                print()
                calculate_energy_draw()
                calculate_coefficients()
                heating_btu = calculate_heating()
                cooling_btu = calculate_cooling()
                break
        else:
            print("That is an invalid input, please try again.")
            print()
            menu_input = input("what would you like to do? ")


while run:
    main()

if __name__ == "__main__":
    main()
