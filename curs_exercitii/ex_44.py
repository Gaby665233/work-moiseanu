# Mini activitate: Reamintirea cunoştinţelor anterioare

#  Sarcină: Să îl ajutăm pe Alex să scrie un program care:

# creează două dicţionare customer1 şi customer2 şi le stochează în lista customers;
# creează funcţia cu care Alex poate itera prin lista customers şi poate lista informaţiile despre fiecare client folosind cheile în dicţionare.
# permite adăugarea unui nou client prin crearea unui nou dicționar și adăugarea acestuia în lista customers;
# actualizează datele despre client, de exemplu, adresa de e-mail a clientului.

# Creating dictionaries for customers
customer1 = {
    "name": "John Doe",
    "email": "john.doe@example.com",
    "phone": "123-456-7890",
    "address": "123 Elm Street"
}

customer2 = {
    "name": "Jane Smith",
    "email": "jane.smith@example.com",
    "phone": "987-654-3210",
    "address": "456 Oak Avenue"
}

# List to store customers
customers = [customer1, customer2]

# Function to display all customers
def display_customers(customers_list):
    for i, customer in enumerate(customers_list, 1):
        print(f"Customer {i}:")
        for key, value in customer.items():
            print(f"  {key.capitalize()}: {value}")
        print()  # Empty line for spacing

# Function to add a new customer
def add_customer(customers_list, name, email, phone, address):
    new_customer = {
        "name": name,
        "email": email,
        "phone": phone,
        "address": address
    }
    customers_list.append(new_customer)
    print(f"Customer {name} has been added.\n")

# Function to update a customer's email
def update_customer_email(customers_list, name, new_email):
    for customer in customers_list:
        if customer["name"] == name:
            customer["email"] = new_email
            print(f"Email for {name} has been updated to {new_email}.\n")
            return
    print(f"Customer {name} not found.\n")

# Testing the functions
print("Initial customer list:")
display_customers(customers)

# Adding a new customer
add_customer(customers, "Alex Johnson", "alex.johnson@example.com", "555-555-5555", "789 Pine Road")

print("Customer list after adding a new customer:")
display_customers(customers)

# Updating the email address of an existing customer
update_customer_email(customers, "Jane Smith", "jane.newemail@example.com")

print("Customer list after updating email:")
display_customers(customers)