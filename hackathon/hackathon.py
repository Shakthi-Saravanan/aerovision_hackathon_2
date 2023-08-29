# Define a dictionary to store customer information
customers = {}

# Function to add a new customer
def add_customer():
    print("Add a new customer:")
    name = input("Enter customer name: ")
    contact = input("Enter customer contact data: ")
    flight_history = []
    customers[name] = {'Contact': contact, 'Flight History': flight_history}
    print(f"Customer {name} added successfully.")

# Function to display customer information
def display_customer():
    name = input("Enter customer name: ")
    if name in customers:
        customer_info = customers[name]
        print(f"Name: {name}")
        print(f"Contact: {customer_info['Contact']}")
        print("Flight History:")
        for idx, flight in enumerate(customer_info['Flight History'], 1):
            print(f"{idx}. {flight}")
    else:
        print(f"Customer {name} not found.")

# Function to add flight history for a customer
def add_flight_history():
    name = input("Enter customer name: ")
    if name in customers:
        flight = input("Enter flight history: ")
        customers[name]['Flight History'].append(flight)
        print(f"Flight history added for {name}.")
    else:
        print(f"Customer {name} not found.")

# Main loop
while True:
    print("\nCustomer Information Management System")
    print("1. Add Customer")
    print("2. Display Customer Information")
    print("3. Add Flight History")
    print("4. Exit")
    choice = input("Select an option: ")

    if choice == '1':
        add_customer()
    elif choice == '2':
        display_customer()
    elif choice == '3':
        add_flight_history()
    elif choice == '4':
        break
    else:
        print("Invalid choice. Please try again.")
1