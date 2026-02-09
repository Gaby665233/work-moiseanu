products = ["Laptop", "Phone", "TV", "Headphones", "Camera"]
print("List before modification:")
print(products)

# Removing the product "TV"
products.remove("TV")
print("List after modification:")
print(products)



# Mini activitate: Eliminarea mai multor elemente după valoare

# Alex vrea să scrie un program care să șteargă din listă toate elementele, nu doar primul, care au o valoare dată. Folosim lista:

# products = ["Phone", "Laptop", "Phone", "TV", "Headphones", "Camera", "Phone"]

# Sarcina: Să scriem un program care va șterge toate elementele listei care au valoarea "Phone".

# Hint: Combinăm bucla while și operatorul in pentru a verifica dacă mai există elemente cu o anumită valoare în listă.

product = ["Phone", "Laptop", "Phone", "TV", "Headphones", "Camera", "Phone"]


while "Phone" in product:
    product.remove("Phone")
print(product)
# or
product = ["Phone", "Laptop", "Phone", "TV", "Headphones", "Camera", "Phone"]

product = [item for item in product if item != "Phone"]

print(product)


# De exemplu, dacă dorește să elimine produsul de pe poziția 3:

# Product list
products = ["Laptop", "Phone", "TV", "Headphones", "Camera"]
print("List before modification:")
print(products)

# Removing the product at position 3
removed_item = products.pop(3)
print("List after modification:")
print(products)
print("The product at position 3 was:", removed_item)


print("___________---------------_________________")


products = ["Laptop", "Phone", "TV", "Headphones", "Camera"]
print("List before modification:")
print(products)

# Deleting the product at position 3
del products[3]
print("List after modification:")
print(products)

# remove(): Șterge primul element cu valoarea dată.
# pop(): Șterge elementul pe indexul dat și returnează valoarea lui.
# del: Șterge elementul pe indexul dat fără a returna valoare.

list1 = ["Laptop", "Phone", "TV", "Headphones", "Camera"]
list2 = ["Laptop Stand", "Mouse", "Keyboard"]

# Combining the lists into a new list using the + operator
combined_list = list1 + list2
print("Combined List:", combined_list)


# cu extend ,acelasi lucru

list1 = ["Laptop", "Phone", "TV", "Headphones", "Camera"]
list2 = ["Laptop Stand", "Mouse", "Keyboard"]

# Extending list1 by adding elements from list2 using extend()
list1.extend(list2)
print("Extended List1:", list1)


# Exemplu: Setarea elementelor listei în ordine alfabetică

# Product list
products = ["Laptop", "Phone", "TV", "Headphones", "Camera"]
print("List before sorting:")
print(products)

# Sorting the list in ascending order
products.sort()
print("List after sorting:")
print(products)


# Alex vrea să vadă lista de produse în ordine alfabetică inversă, cu cele mai recente produse la/
#  început; așadar, conținutul listei este cam așa: ['Laptop', 'Tv', 'Camera', 'Phone', 'Printer']

# Sarcină:

# să creăm o listă de produse numită products;
# să sortăm produsele în ordine alfabetică inversă;
# să afișăm conținutul listei după sortare.
# Hint: Funcția sort() poate avea un parametru de intrare reversed, care este de tip bool.

lucruri = ['Laptop', 'Tv', 'Camera', 'Phone', 'Printer']
lucruri.sort(reverse=True)

print(lucruri)


# Mini activitate: Să creăm o listă de produse sub 50 de euro

# Sarcină: Folosind funcțiile anterioare și tot ce am discutat până acum despre lucrul cu liste, să creăm un program care,/
#  din lista de produse pe care o are Alex, să creeze o nouă listă adăugând în ea element cu element, dar doar acele/
#  elemente care îndeplinesc criteriul specificat (prețul mai mic de 50 de euro). Lista de prețuri a lui Alex:/
#  [23.99, 19.50, 55.00, 48.75, 102.00, 33.40, 12.30]

# Hint: Folosim bucla for și condiția if pentru a parcurge lista și a adăuga doar acele prețuri care sunt mai mici de 50.

lista = [23.99, 19.50, 55.00, 48.75, 102.00, 33.40, 12.30]
pret = []
for i in lista:
    if i < 50:
        pret.append(i)
print(pret)



# Când și-a dat seama că ar putea grăbi și mai mult procesul, Alex a apelat list comprehension, o modalitate /
# simplă și puternică de a crea liste bazate pe o anumită condiție. Cu list comprehension, întregul proces de filtrare devine o singură linie de cod!

# Mai întâi, Alex și-a deschis mediul de dezvoltare și a scris următoarea linie:

# Când a rulat codul, rezultatul a fost exact ce se aștepta:
print("ALTCEVA______________")
# # Define the initial list of prices
prices = [23.99, 19.50, 55.00, 48.75, 102.00, 33.40, 12.30]

# # Create an empty list to store prices below 50
prices_below_50 = []
prices_below_50 = [c for c in prices if c < 50]

# Print the list of prices below 50
print(prices_below_50)

# Toate produsele al căror preț era sub 50 euro erau acum afișate. Într-o singură linie de cod, Alex/
#  a obținut același rezultat! „Ce se întâmplă cu adevărat aici?” Alex și-a dat seama: codul lui a /
# citit lista prices, a parcurs fiecare element individual (pe care l-a numit c) și a verificat dacă /
# acea valoare era mai mică de 50. Dacă condiția era adevărată, acel preț ar fi fost adăugat la lista nouă numită prices_below_50.

# Alex s-a gândit cu entuziasm: „Este mult mai eficient decât să o faci manual”, și trebuie să fim de acord /
# cu el. Următorul tutorial video prezintă tehnica list comprehension, care permite crearea elegantă a listelor după anumite criterii.

products_on_sale = ["Laptop", "Phone", "TV"]
products_on_sale[1] = "Tablet"
print(products_on_sale)
   

roducts_on_sale = ("Laptop", "Phone", "TV")
products_on_sale[1] = "Tablet"
print(products_on_sale)


# Concatenarea tuplurilor

products_on_sale = ("Laptop", "Phone", "TV")
new_category = ("Headphones", "Camera")

# Merging two tuples
all_products = products_on_sale + new_category
print(all_products) # Outputs ("Laptop", "Phone", "TV", "Headphones", "Camera")

# Mini activitate: Combinarea tuplurilor în ordine inversă

# Sarcină: Să creăm un program care combină new_category și products_on_sale, dar astfel încât să adăugăm mai întâi categoria nouă, apoi produsele existente.

products_on_sale = ("Laptop", "Phone", "TV")
new_category = ("Headphones", "Camera")
toate_produs = new_category + products_on_sale
print(toate_produs)


# count() – numără de câte ori apare un anumit element într-un tuplu.
all_products = ("Laptop", "Phone", "TV", "Phone", "Camera")
print(all_products.count("Phone"))  # Outputs 2

# index() – returnează indexul primei apariții a unui anumit element.
print(all_products.index("TV"))  # Outputs 2




# Exemplu: Urmărirea statusului comenzilor într-un magazin online

# Alex vrea să țină evidența comenzilor și a statusului lor. Fiecare comandă este reprezentată de un tuplu care conține următoarele informații:

# ID comandă – număr unic de comandă;
# numele clientului – numele persoanei care a făcut comanda;
# suma comenzii – valoarea comenzii în dolari;
# statusul comenzii – statusul curent, precum "Pending", "Shipped", "Delivered", "Cancelled".
# Deoarece stările sunt imuabile, Alex folosește tupluri pentru a păstra datele originale privind statusul comenzii fără posibilitatea /
# unor modificări accidentale.

# Cod: Definirea comenzii și analiza statusului

# Defining the list of orders, where each order is represented as a tuple
orders = [

    (101, "John Doe", 299.99, "Pending"),
    (102, "Jane Smith", 149.50, "Shipped"),
    (103, "Mike Johnson", 89.75, "Delivered"),
    (104, "Emily Davis", 249.99, "Pending"),
    (105, "Alice Brown", 120.00, "Cancelled")
]

# Displaying all orders with status "Pending"
print("Orders with status 'Pending':")
for order in orders:
    order_id = order[0]
    customer_name = order[1]
    amount = order[2]
    status = order[3]

    if status == "Pending":
        print(f"Order ID: {order_id}, Customer: {customer_name}, Amount: ${amount:.2f}, Status: {status}")

# Displaying the total amount of all successful orders ("Shipped" or "Delivered")
total_successful_orders = 0.0
for order in orders:
    amount = order[2]

    status = order[3]

    if status in ("Shipped", "Delivered"):
        total_successful_orders += amount

print(f"Total amount of successful orders: ${total_successful_orders:.2f}")



# Mini Proiect: Inventar – Calcularea valorilor de inventar folosind tupluri și liste

# Alex vrea să calculeze valoarea de inventar a tuturor produselor disponibile. Fiecare produs este reprezentat de un tuplu care conține:

# numele produsului;
# cantitatea pe stoc;
# prețul pe unitate.
#  Sarcină:

# să definim lista products cu mai multe produse (5-6);
# să trecem prin listă și să calculăm pentru fiecare produs valoarea de inventar (cantitate × preț);
# să calculăm valoarea totală a întregului inventar adăugând valoarea de inventar pentru fiecare produs;
# să listăm valoarea totală a stocului pe ecran.
#  Să vedem soluția.

# Define the list of products, each product is a tuple: (product name, quantity, price per unit)
products = [("Laptop", 10, 800.00),
            ("Smartphone", 25, 500.00),
            ("Headphones", 50, 30.00),
            ("Monitor", 15, 150.00),
            ("Keyboard", 40, 20.00),
            ("Mouse", 60, 15.00)]
valoare_total = 0

for i in products:
    order = i[0]
    cate_sunt = i[1]
    suma = i[2]
    valoare = cate_sunt * suma
    valoare_total += valoare
    print(f"{order}: Quantity = {cate_sunt}, Price = ${suma:.2f}, Inventory Value = ${valoare:.2f}")
print(f"valoarea totala este: {valoare_total}")