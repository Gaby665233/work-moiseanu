products = ["Laptop", "TV", "Monitor", "Keyboard", "Printer"]
# Looping through all products in the list and printing their names
for product in products:
    print(product)


# Mini activitate: Separarea produselor cu caracteristici specifice

# Alex vrea să scrie un program care listează doar produsele care conțin în numele lor cuvântul „Telefon”. În felul acesta, poate /
# separa rapid toate telefoanele din oferta companiei.

# Să creăm o listă de produse: ["Samsung Phone", "Laptop", "iPhone", "TV", "Headphones", "Camera", "Xiaomi Phone"]

# Sarcină: Folosim bucla for pentru a trece prin toate produsele din listă și le afișăm doar pe cele care conțin cuvântul "Phone".

# Hint: Folosim bucla for și operatorul in pentru a trece prin listă. Pentru mai multă flexibilitate, putem folosi și funcții pentru /
# lucru cu stringuri, precum find() sau startswith(), pentru a căuta cu precizie produse.

# Să vedem soluția
products = ["Samsung Phone", "Laptop", "iPhone", "TV", "Headphones", "Camera", "Xiaomi Phone"]
for product in products:
    if "Phone" in product:
        print(product)


# Întrebare pentru reflecție: Ce s-ar întâmpla dacă am dori să găsim produse care conțin un alt termen specific, cum ar fi "Laptop"?/
#  Cum am modifica codul pentru a face programul mai flexibil și pentru a permite utilizatorului să introducă termenul pe care vrea să-l găsească?

# Provocare pentru practică: Modificăm codul astfel încât utilizatorul să poată introduce orice termen pe care îl caută în numele produselor. /
# În felul acesta, programul va deveni mai dinamic și adaptat la diferite nevoi.

# Hint: Putem folosi funcția input() pentru a permite utilizatorului să introducă un termen care va fi apoi folosit în căutare.

produc = ["Samsung Phone", "Laptop", "iPhone", "TV", "Headphones", "Camera", "Xiaomi Phone"]

nume_prod = input("Ce alegi: ")
for i in produc:
    if nume_prod in i:
        print(i)


print("-------Au da ce avem domnule aici fac 15 min si secunde pana jos-----")
products = ["Samsung Phone", "Laptop", "iPhone", "TV", "Headphones", "Camera", "Xiaomi Phone"]

prod_lungime = len(products)
# prin len am facut lsita in cifre pentru ca range ia in calcul doar cifrele
for i in range(prod_lungime):
    if "Phone" in products[i]:
        print(f"Element {i}: {products[i]}")



products = ["Laptop", "Phone", "TV", "Headphones", "Camera"]
# Using len() to get the size of the list
total_products = len(products)
print(f"We have {total_products} products in our assortment.")


# Mini activitate: Listarea produselor dintr-o listă folosind len() și index

# Acum, Alex vrea să arate utilizatorilor lista de produse. Lista numelor de produse se află în variabila items, iar fiecare/
# produs trebuie afișat individual, folosind indexuri.

# Sarcină: Este necesar:

# să definim lista items cu cel puțin cinci nume de produse;
# să utilizăm bucla for cu range și funcția len() pentru a afișa fiecare produs din lista items, unul câte unul.
# Notă: În loc de iterarea directă prin listă (de exemplu, for item in items), folosim indexurile de listă.

# De ce folosim range și len()? Funcția len() returnează numărul de elemente în lista items, ceea ce ne permite să creăm cu range un/
# număr de index corespunzător. În felul acesta, folosim bucla for pentru a accesa fiecare index al listei în mod individual, ceea /
#     ce este util atunci când dorim un control complet asupra ordinii în care sunt afișate datele.


items = ["Laptop", "Smartphone", "Headphones", "Camera", "Smartwatch"]
lungimre = len(items)
for i in range(lungimre):
    print(items[i])


# Mini activitate: Verificarea disponibilității produsului

# Să ne imaginăm că Alex trebuie să verifice disponibilitatea anumitor produse înainte de a le comanda. Definim lista available_products cu câteva produse și apoi, folosind operatorul in, verificăm dacă anumite produse sunt prezente în acea listă.

# Sarcină:

# să creăm o listă available_products cu cel puțin cinci produse la alegere;
# să definim variabila product_to_check care conține numele produsului pe care dorim să-l verificăm;
# să folosim if și in pentru a verifica dacă product_to_check este prezent pe listă și tipărim mesajul corespunzător.
# Hint: Să modificăm valoarea product_to_check și să testăm codul pentru a vedea rezultate diferite.

# Să vedem o posibilă soluție

# List of available products
available_products = ["Laptop", "Phone", "TV", "Camera", "Headphones"]

# Product to check
product_to_check = "Tablet"

if product_to_check in available_products:
    print("se alfa")
else:
    print("niu")