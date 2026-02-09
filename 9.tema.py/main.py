from product import Product
from employee import Employee
from user import User

# Creare produse
products = [
    Product("Laptop", 1200, 15, "Laptop performant pentru muncă și gaming."),
    Product("Mouse", 25, 50, "Mouse ergonomic cu DPI ajustabil."),
    Product("Keyboard", 80, 30, "Tastatură mecanică cu iluminare RGB."),
    Product("Monitor", 300, 20, "Monitor 27 inch Full HD."),
    Product("Headphones", 150, 8, "Căști wireless cu anulare a zgomotului.")
]

# Creare angajați
employees = [
    Employee("John Doe", "john@example.com", 3500, "123 Elm Street"),
    Employee("Jane Smith", "jane@example.com", 4200, "456 Oak Avenue")
]

# Creare utilizatori
users = [
    User("Alice Johnson", "alice@example.com", "0712345678", "12 Main Street"),
    User("Bob Brown", "bob@example.com", "0723456789", "34 Second Street"),
    User("Charlie Davis", "charlie@example.com", "0734567890", "56 Third Street")
]

# Adăugare produse în istoricul utilizatorilor
users[0].add_product(products[0])
users[0].add_product(products[1])

users[1].add_product(products[2])
users[1].add_product(products[3])
users[1].add_product(products[4])

users[2].add_product(products[1])
users[2].add_product(products[3])

# Afișare suma totală cheltuită de fiecare utilizator
for user in users:
    print(f"{user.name} has spent: ${user.total_spent():.2f}\n")

# Afișare informații utilizatori și angajați (polimorfism)
print("=== Users Info ===")
for user in users:
    print(user.display_info())
    print("-" * 40)

print("=== Employees Info ===")
for emp in employees:
    print(emp.display_info())
    print("-" * 40)

input("Enter pentru a inchide")