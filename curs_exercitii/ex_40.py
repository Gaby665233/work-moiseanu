addition = lambda x, y: x + y
print(addition(2, 6))
print("----------------------------------")
addition = lambda x , y: x * y
print(addition(6, 3))

print("exemple mai multe")

addition = lambda x , y : x + y
print(addition (5, 10))

print("---------------------------------")
# Sarcină: Alex vrea să scrie o funcție care înmulțește un număr cu 2.

# Folosirea funcției standard

# Mai întâi, putem face acest lucru folosind o funcție clasică Python:

def multiply_by_two(x):
    return x * 2

print(multiply_by_two(5))  # Result: 10


print("------------------------------------")


def inmultit_cu_4(x):
    return x * 4

print(inmultit_cu_4(10))

# Folosirea funcției lambda

# Acum, putem îndeplini aceeași sarcină folosind o expresie lambda:

multiply_by_tw = lambda x: x * 2
print(multiply_by_tw(5))  # Result: 10


# Funcția Filter()



# Aici am implementat două moduri diferite de a vedea diferența în abordarea utilizării unei funcții/
# lambda și definirea unei funcții separate. După cum puteți vedea, rezultatul ambelor funcții este același.


customers = [
    {'name': 'Mark', 'spending': 75000},
    {'name': 'Anna', 'spending': 120000},
    {'name': 'John', 'spending': 50000},
    {'name': 'Eve', 'spending': 130000}
]

vip_customers = list(filter(lambda x: x['spending'] > 100000, customers))
for i in vip_customers:

    print(f"{i['name']} is a VIP customer with a spending of {i['spending']}.")



# Alex vrea să crească salariile tuturor angajaților cu 5%.
print("-=-=-=-=-=-=-=-=")
employees = [
    {'name': 'Peter', 'salary': 50000},
    {'name': 'Mila', 'salary': 60000},
    {'name': 'Nemanja', 'salary': 55000}
]

employees_with_increased_salaries = list(map(lambda x: {'name': x['name'], 'salary': x['salary'] * 1.05}, employees))
for i in employees_with_increased_salaries:
    print(f"{i['name']} has a new salary: {i['salary']} dinars")


print("\nex nou\n")
prices = [100, 200, 300, 400, 500]

prices_above_250 = list(filter(lambda x: x > 250, prices))

print(prices_above_250)



# sarcină: Să-l ajutăm pe Alex să identifice produsele care sunt la reducere. Lista produselor,/
# cu prețurile acestora și informațiile despre dacă sunt sau nu la reducere, este stocată în felul următor:
products = [
    {'name': 'Laptop', 'price': 85000, 'discount': True},
    {'name': 'Phone', 'price': 50000, 'discount': False},
    {'name': 'TV', 'price': 60000, 'discount': True},
    {'name': 'Camera', 'price': 25000, 'discount': False}

]

reducere = list(filter(lambda x: x['discount'] == True , products))
for i in reducere:
    print(f"{i['name']} este la reducere cu pretul {i['price']}")


# Funcția sorted()

s = "String"
print(sorted(s, key=lambda x: x))

products = [
    {'name': 'Laptop', 'price': 85000, 'discount': True},
    {'name': 'Phone', 'price': 50000, 'discount': False},
    {'name': 'TV', 'price': 60000, 'discount': True},
    {'name': 'Camera', 'price': 25000, 'discount': False}
]

# Sorting products by price in ascending order
products.sort(key=lambda x: x['price'])

# Displaying sorted products
for product in products:
    print(f"{product['name']}: {product['price']} dinars")

cities =[("New York",10001),
       ("Paris",75000),
       ("Moscow", 101000),
       ("Tokyo",100000)]

cities.sort(key=lambda x : x[1])
print(cities)

# Funcția map()

prices_in_euros = [10, 20, 15, 30]
prices_in_dinars = list(map(lambda x: x * 117, prices_in_euros))

print(prices_in_dinars)

# Sarcină: Alex are o listă de produse cu prețuri fără taxe și dorește să adauge o taxă de 20% la fiecare preț. Folosim funcția map() pentru a actualiza prețurile rapid și eficient.

products = [
    {'name': 'Laptop', 'price': 50000},
    {'name': 'Phone', 'price': 30000},
    {'name': 'Tablet', 'price': 20000}
]

adauge_20 = list(map(lambda x : {'name': x['name'], 'price': x ['price'] * 1.2}, products)) 
for i in adauge_20:
    print(f"{i['name']}-{i['price']}")




status = lambda x: 'Positive number' if x > 0 else 'Negative number'
print(status(10))  # Output: 'Positive number'
print(status(-5))  # Output: 'Negative number'


complex_condition = lambda x: x**2 if x < 5 else (x**3 if x > 5 else x)
print(complex_condition(3))  # Output: 9
print(complex_condition(6))  # Output: 216
print(complex_condition(5))  # Output: 5
