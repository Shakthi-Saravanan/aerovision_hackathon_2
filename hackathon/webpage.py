import tkinter as tk

# Define a dictionary to store customer information
customers = {}

# Function to add a new customer
def add_customer():
    name = name_entry.get()
    contact = contact_entry.get()
    if name and contact:
        customers[name] = {'Contact': contact, 'Flight History': []}
        status_label.config(text=f"Customer {name} added successfully.")
    else:
        status_label.config(text="Please enter both name and contact data.")

# Function to display customer information
def display_customer():
    name = name_entry.get()
    if name in customers:
        customer_info = customers[name]
        info_text.config(text=f"Name: {name}\nContact: {customer_info['Contact']}\nFlight History: {', '.join(customer_info['Flight History'])}")
    else:
        info_text.config(text=f"Customer {name} not found.")

# Function to add flight history for a customer
def add_flight_history():
    name = name_entry.get()
    flight = flight_entry.get()
    if name in customers:
        if flight:
            customers[name]['Flight History'].append(flight)
            status_label.config(text=f"Flight history added for {name}.")
        else:
            status_label.config(text="Please enter flight history.")
    else:
        status_label.config(text=f"Customer {name} not found.")

# Create the main application window
app = tk.Tk()
app.title("Customer Information Management System")

# Create and arrange GUI elements
name_label = tk.Label(app, text="Name:")
name_label.grid(row=0, column=0, padx=10, pady=5)

name_entry = tk.Entry(app)
name_entry.grid(row=0, column=1, padx=10, pady=5)

contact_label = tk.Label(app, text="Contact:")
contact_label.grid(row=1, column=0, padx=10, pady=5)

contact_entry = tk.Entry(app)
contact_entry.grid(row=1, column=1, padx=10, pady=5)

flight_label = tk.Label(app, text="Flight History:")
flight_label.grid(row=2, column=0, padx=10, pady=5)

flight_entry = tk.Entry(app)
flight_entry.grid(row=2, column=1, padx=10, pady=5)

add_button = tk.Button(app, text="Add Customer", command=add_customer)
add_button.grid(row=3, column=0, columnspan=2, padx=10, pady=5)

display_button = tk.Button(app, text="Display Customer", command=display_customer)
display_button.grid(row=4, column=0, columnspan=2, padx=10, pady=5)

add_flight_button = tk.Button(app, text="Add Flight History", command=add_flight_history)
add_flight_button.grid(row=5, column=0, columnspan=2, padx=10, pady=5)

status_label = tk.Label(app, text="", fg="green")
status_label.grid(row=6, column=0, columnspan=2, padx=10, pady=5)

info_text = tk.Label(app, text="")
info_text.grid(row=7, column=0, columnspan=2, padx=10, pady=5)

app.mainloop()
4