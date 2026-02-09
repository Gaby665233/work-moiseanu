# Alex a primit sarcina de a ține evidența achizițiilor pe care până acum o făcea manual. În ultimul timp, volumul achizițiilor/
#  a crescut, iar urmărirea datelor despre clienți și achizițiile lor a devenit din ce în ce mai complexă și mai solicitantă. /
# Alex s-a confruntat cu o problemă: urmărirea manuală a cheltuielilor clienților și analizarea obiceiurilor lor necesită timp/
#  și este predispusă la erori. Pentru a rezolva această problemă, Alex sugerează crearea unui program în Python care va urmări/
#  automat datele. În felul acesta, va avea o perspectivă rapidă asupra informațiilor importante și va putea analiza datele mai /
# eficient, ceea ce va ajuta la îmbunătățirea afacerii.

# Să îl ajutăm pe Alex să creeze un program care stochează informații despre clienți și achizițiile lor. /
# Acesta va folosi structurile de date pe care le-am învățat până acum. Programul ar trebui să proceseze /
# date și să ofere analize, cum ar fi totalul banilor cheltuiți per client, listarea tuturor achizițiilor,/
#  cât și informații despre cele mai scumpe articole achiziționate de clienți.

# Crearea structurilor de date
# Vom defini o listă numită customers, care va conține date despre clienți și achizițiile lor. Fiecare client este reprezentat ca un dicționar cu următoarele date:

# "first_name": prenumele clientului (string);
# "last_name": numele clientului (string);
# "purchases": lista de tupluri, unde fiecare tuplu conține informații despre articolul achiziționat.
# Fiecare tuplu are

# numele articolului (string);
# prețul articolului (float).
customers = [
    {
        "first_name": "Emma",
        "last_name": "Smith",
        "purchases": [
            ("Laptop", 1200.0),
            ("Mouse", 50.0)
        ]
    }
]
# Procesarea datelor
# Să creăm funcții care vor analiza datele despre achiziție:

# calculate_total_spent(customers): O funcție care calculează și afișează suma totală cheltuită pentru fiecare client.
# total_items_purchased(customers): O funcție care calculează și afișează numărul total de articole achiziționate pentru fiecare client.
# Afișarea celei mai scumpe achiziții
# Să creăm funcția most_expensive_purchase(customers) care găsește și afișează cel mai scump articol achiziționat de fiecare client.

# Generarea unui raport cuprinzător
# La sfârșitul programului vom genera un raport cuprinzător pentru fiecare client, care să arate:

# prenumele și numele clientului;
# suma totală cheltuită;
# numărul de articole achiziționate;
# numele și prețul celui mai scump articol.
# Exemplu de raport generat:
# Exemplu de raport generat:

# Calculating total spent by each customer:
# Customer: Emma Smith
# Total spent: 1250.00 euros
# Customer: Jamie Lee
# Total spent: 900.00 euros

# Calculating total items purchased by each customer:
# Customer: Emma Smith
# Total items purchased: 2
# Customer: Jamie Lee
# Total items purchased: 2

# Finding the most expensive purchase for each customer:
# Customer: Emma Smith
# Most expensive item: Laptop - 1200.00 euros
# Customer: Jamie Lee
# Most expensive item: Smartphone - 800.00 euros

# Urmăm acești pași pentru a crea un program pe care Alex îl poate folosi pentru a urmări eficient achizițiile și a analiza comportamentul clienților.
# Sample customer data
customers = [
    {
        "first_name": "Emma",
        "last_name": "Smith",
        "purchases": [
            ("Laptop", 1200.0),
            ("Mouse", 50.0)
        ]
    },
    {
        "first_name": "Jamie",
        "last_name": "Lee",
        "purchases": [
            ("Smartphone", 800.0),
            ("Headphones", 100.0)
        ]
    },
    {
        "first_name": "Alex",
        "last_name": "Taylor",
        "purchases": [
            ("Tablet", 400.0),
            ("Keyboard", 60.0),
            ("Monitor", 300.0)
        ]
    }
]




def calculate_total_spent(customers):
    for customer in customers:
        total_spent = sum(item[1] for item in customer["purchases"])
        print(f"Customer: {customer['first_name']} {customer['last_name']}")
        print(f"Total spent: {total_spent:.2f} euros\n")

# Function to calculate total number of items purchased by each customer
def total_items_purchased(customers):
    for customer in customers:
        total_items = len(customer["purchases"])
        print(f"Customer: {customer['first_name']} {customer['last_name']}")
        print(f"Total items purchased: {total_items}\n")

# Function to find the most expensive purchase for each customer
def most_expensive_purchase(customers):
    for customer in customers:
        most_expensive = max(customer["purchases"], key=lambda x: x[1])
        print(f"Customer: {customer['first_name']} {customer['last_name']}")
        print(f"Most expensive item: {most_expensive[0]} - {most_expensive[1]:.2f} euros\n")
# Generate a comprehensive report
def generate_report(customers):
    print("Calculating total spent by each customer:")
    calculate_total_spent(customers)

    print("Calculating total items purchased by each customer:")
    total_items_purchased(customers)

    print("Finding the most expensive purchase for each customer:")
    most_expensive_purchase(customers)   

# Running the main function
generate_report(customers)

 