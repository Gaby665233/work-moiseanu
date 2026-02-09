# Mini activitate: Să recunoaștem dicționarul

# Sarcină: Care dintre următoarele trei structuri reprezintă un dicționar?

# x = ('laptop', 'smartphone', 'tablet')  # Option 1
x = {'category': 'electronics', 'product_name': 'smartphone', 'price': 500, 'in_stock': True}  # Option 2
# x = ['laptop', 'mouse', 'keyboard']  # Option 3

# Întrebare pentru reflecție: Putem recunoaște și numi toate cele trei structuri? Ce le deosebește?

# Când Alex primește informații despre o modificare a statusului comenzii, /
# poate actualiza cu ușurință valoarea existentă folosind cheia "status":

order = {}
order["status"] = "in transit"
print(order["status"])  # Outputs: in transit 

# În mod similar, dacă dorește să adauge informații noi în dicționar, cum ar fi un curier,/
#  poate face acest lucru prin simpla atribuire a unei noi chei și valori:

order["delivery_service"] = "DHL"
print(order["delivery_service"])

# Mini activitate: Modificarea valorii pentru o cheie existentă

# Ce se întâmplă când încercăm să adăugăm un element nou la un dicționar folosind o cheie care există deja?

# Sarcină:

# Să definim un dicționar cu mai multe articole:
items = {1: "laptop", 2: "monitor", 3: "printer", 4: "mouse"}

    # 2. Să încercăm să schimbăm valoarea cu cheia 3 în "keyboard":

items[3] = "keyboard"

    # 3. Să verificăm rezultatul:

print(items)

# Întrebare pentru reflecție: Ce observăm? Cum tratează Python încercarea de a adăuga o valoare nouă la o cheie existentă?

# Alex poate examina toate cheile și valorile dintr-un dicționar folosind bucla for cu metoda .items(), care permite iterația prin fiecare pereche cheie-valoare:
print("NOU")
order = {
    "customer": "John Doe",
    "product": "Laptop",
    "price": 75000,
    "date": "2024-10-15",
    "status": "delivered"
}

for key, value in order.items():
    print(f"{key}: {value}") 



# 2 VARIANTE
key = items.keys()
for k in items:
    print(items[k])
    # ORi
for k,v in items.items():
    print( f"{k}:{v}" )






# Exemplu: Calcularea veniturilor din vânzări

# Alex are date despre comenzi dintr-un magazin online, unde fiecare comandă conține informații despre articol, cantitate și prețul pe unitate./
#  El trebuie să scrie un program care va calcula veniturile totale din vânzarea tuturor comenzilor.

# Informații despre comenzi:
print("---------------EXERCITIU NOU-------------")
cart = [
    {'item': 'Laptop', 'count': 5, 'price': 700},
    { 'item': 'Computer mouse', 'count': 10, 'price': 20},
    { 'item': 'Keyboard', 'count': 7, 'price': 30},
    { 'item': 'Мonitor', 'count': 3, 'price': 150},
    { 'item': 'Laptop', 'count': 2, 'price': 700},
    { 'item': 'Computer mouse', 'count': 5, 'price': 20},
]

# Putem calcula venitul total din vânzări în felul următor: vom parcurge fiecare comandă și vom înmulți cantitatea cu prețul, apoi vom aduna toate rezultatele.

total_income = 0
for item in cart:
    total_income += item['count'] * item['price']
  

print(f"Total income from sales: ${total_income}")

# Această abordare simplă adună valoarea fiecărei comenzi, înmulțind numărul de unități cu prețul, iar așa se calculează venitul total.


# Sarcină:

# Trebuie să scriem un program care:

# va crea și tipări un dicționar care să conțină numărul total de unități vândute pentru fiecare produs;

# va crea și tipări un dicționar care să conțină numărul total de unități vândute pentru fiecare lună.

# Datele de vânzări sunt date în următorul format:

# sales_data = [
#     {'product': 'Smartphone', 'month': 'January', 'quantity': 150},
#     {'product': 'Laptop', 'month': 'January', 'quantity': 80},
#     {'product': 'Tablet', 'month': 'January', 'quantity': 50},
#     {'product': 'Smartphone', 'month': 'February', 'quantity': 200},
#     {'product': 'Laptop', 'month': 'February', 'quantity': 90},
#     {'product': 'Tablet', 'month': 'February', 'quantity': 60},
#     {'product': 'Smartphone', 'month': 'March', 'quantity': 250},
#     {'product': 'Laptop', 'month': 'March', 'quantity': 100},
#     {'product': 'Tablet', 'month': 'March', 'quantity': 70},
# ] 

# Rezultatele așteptate ale programului:

# Total sales by product:
# - Smartphone: 600 units
# - Laptop: 270 units
# - Tablet: 180 units

# Total sales by month:
# - January: 280 units
# - February: 350 units
# - March: 420 units

# Hint:

# Folosim dicționare pentru a stoca valori cumulate pentru fiecare produs și pentru fiecare lună.
# Parcurgem lista sales_data, actualizând valorile din dicționare în funcție de product și month.
print("------------------------------------------------------exercitu--------------------------------------")
sales_data = [
     {'product': 'Smartphone', 'month': 'January', 'quantity': 150},
     {'product': 'Laptop', 'month': 'January', 'quantity': 80},
     {'product': 'Tablet', 'month': 'January', 'quantity': 50},
     {'product': 'Smartphone', 'month': 'February', 'quantity': 200},
     {'product': 'Laptop', 'month': 'February', 'quantity': 90},
     {'product': 'Tablet', 'month': 'February', 'quantity': 60},
     {'product': 'Smartphone', 'month': 'March', 'quantity': 250},
     {'product': 'Laptop', 'month': 'March', 'quantity': 100},
     {'product': 'Tablet', 'month': 'March', 'quantity': 70},
 ]

total_product = {}

total_luna = {}

for i in sales_data:
    product = i['product']
    month = i['month']
    quantity = i['quantity']

    if product in total_product:
        total_product[product] += quantity
    else:
        total_product[product] = quantity

    if month in total_luna:
        total_luna[month] += quantity
    else:
        total_luna[month] = quantity

print(" unități vândute pentru fiecare produs")
for product, total in total_product.items():
    print(f"- {product}: {total} unitati")

print("unități vândute pentru fiecare lună")
for month,total in total_luna.items():
    print(f"- {month}: {total} unitati")

january_sales = filter(lambda x: x['month'] == 'January', sales_data)

print(list(january_sales))

