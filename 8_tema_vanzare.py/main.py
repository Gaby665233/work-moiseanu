from product import Product
from employee import Employee
from user import User

# Lista de produse
products = [
    Product("Laptop", 3500.0, 15, "Laptop performant"),
    Product("Telefon", 2500.0, 8, "Smartphone modern"),
    Product("Casti", 300.0, 20, "Casti wireless"),
    Product("Mouse", 150.0, 50, "Mouse optic"),
    Product("Tastatura", 200.0, 5, "Tastatura mecanica")
]

# Lista de angajati
employees = [
    Employee("Ana Popescu", "ana@company.com", 4500.0, "Bucuresti"),
    Employee("Ion Ionescu", "ion.company.com", 4000.0, "Cluj")
]

# Lista de utilizatori
users = [
    User("Maria", "maria@email.com", "0712345678", "Iasi"),
    User("Andrei", "andrei@email.com", "0723456789", "Timisoara"),
    User("Elena", "elena@email.com", "0734567890", "Brasov")
]

# Demonstratie Product
print("=== Verificare stoc produse ===")
for product in products:
    print(product.name, "stoc suficient:", product.check_quantity())

# Demonstratie Employee
print("\n=== Verificare email angajati ===")
for emp in employees:
    print(emp.name, "email valid:", emp.check_email())

employees[0].increase_salary(10)
print("\nSalariu dupa marire:", employees[0].salary)

# Demonstratie User
print("\n=== Achizitii utilizatori ===")
users[0].add_product(products[0])
users[0].add_product(products[2])

print("Total cheltuit de", users[0].name, ":", users[0].total_spent())
print("Email valid user:", users[0].check_email())

input("Apasă Enter pentru a închide programul...")