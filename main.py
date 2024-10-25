# Define the list of allowed vehicles
AllowedVehiclesList = ['Ford F-150', 'Chevrolet Silverado', 'Tesla CyberTruck', 'Toyota Tundra', 'Nissan Titan']

# Function to print all allowed vehicles
def print_allowed_vehicles():
    print(" ")
    print("The AutoCountry sales manager has authorized the purchase and selling of the following vehicles:")
    for vehicle in AllowedVehiclesList:
        print(f"- {vehicle}")
        print(" ")

# Main menu function
def menu():
    while True:
        print("********************************")
        print("AutoCountry Vehicle Finder v0.1")
        print("********************************")
        print(" ")
        print("Please Enter the following number below from the following menu:")
        print("1. Print all Authorized Vehicles")
        print("2. Exit")

        choice = input("           ")

        if choice == '1':
            print_allowed_vehicles()
        elif choice == '2':
            print("Thank you for using the AutoCountry Vehicle Finder, good-bye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the program
menu()
