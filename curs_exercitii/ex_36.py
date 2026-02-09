products_in_stock = {"Laptop", "Phone", "TV", "Laptop"}

print(products_in_stock)  # Outputs: {"Laptop", "Phone", "TV"}


 
# Adăugarea de elemente


products_in_stock = {"Laptop", "Phone", "TV"}
products_in_stock.add("Headphones")
print(products_in_stock)  # {"Laptop", "Phone", "TV", "Headphones"}


# Eliminarea elementelor

products_in_stock = {"Laptop", "Phone", "TV", "Headphones"}
products_in_stock.remove("TV")
print(products_in_stock)  # {"Laptop", "Phone", "Headphones"}


# Mini activitate: Eliminarea unui element care nu există în set

# Sarcină: Să scriem un program în care se elimină un element care nu există în set.

# products_in_stock = {"Laptop", "Phone", "TV", "Laptop"}

# Să încercăm să eliminăm elementul "Printer". Care este rezultatul când programul este rulat?


products_in_stock = {"Laptop", "Phone", "TV", "Laptop"}
products_in_stock.remove("Laptop")
print(products_in_stock)

# Metoda discard() ne permite să eliminăm în siguranță elemente dintr-un set fără a provoca o eroare/
# , chiar și atunci când elementul nu este prezent. Putem folosi această metodă atunci când nu suntem siguri dacă un anumit produs se află în set.

products_in_stock = {"Laptop", "Phone", "TV", "Headphones"}
products_in_stock.discard("Printer") # Does not raise an error even if "Printer" is not in the set
print(products_in_stock) # {"Laptop", "Phone", "TV", "Headphones"}


# Combinarea și compararea seturilor de date

products_on_sale = {"Phone", "Tablet", "Laptop"}
all_products = products_in_stock.union(products_on_sale)
print(all_products)

# Intersecția seturilor

common_products = products_in_stock.intersection(products_on_sale)
print(common_products)


# Diferența dintre seturi

# Diferența dintre două seturi arată elementele care se află doar într-unul dintre seturi. /
# Când Alex vrea să vadă doar produse disponibile în stoc și nu și la reducere, folosește diferența dintre seturi.

products_only_in_stock = products_in_stock.difference(products_on_sale)
print(products_only_in_stock) 

# Alex vrea să arate utilizatorilor o listă de produse. Lista numelor de produse se află în variabila /
# items, iar fiecare produs trebuie afișat individual, folosind indexuri.

# Sarcină:

# Să creăm două seturi de produse:
# primul set trebuie să conțină produse în stoc;
# al doilea set trebuie să conțină produse la reducere.
# Unirea: Să combinăm ambele seturi și să afișăm rezultatul.
# Intersecția: Să găsim produsele care sunt în ambele seturi.
# Diferența: Să arătăm produsele care sunt doar în stoc, dar nu și la reducere.
# Hint: Folosim metodele .union(), .intersection() și .difference() pentru fiecare operație și testăm diferențele în rezultate.
print("______----------EXERCITIU----------________")
products_in_stock = {"Laptop", "Phone", "Headphones"}
products_on_sale = {"Phone", "Tablet", "Laptop"}

ambele_unite = products_in_stock.union(products_on_sale)
print(ambele_unite)

prodisele_in_ambele = products_in_stock.intersection(products_on_sale)
print(prodisele_in_ambele)

doar_in_stoc = products_in_stock.difference(products_on_sale)

print(doar_in_stoc)


# Seturi ca instrument pentru eliminarea duplicatelor


# În timp ce lucra cu datele clienților, Alex a observat că multe nume de clienți au apărut de mai multe ori pe lista sa./
#  Eliminarea manuală a duplicatelor ar dura mult timp și ar fi predispusă la erori. Seturile oferă o soluție simplă la/
#  această problemă deoarece elimină automat duplicatele și afișează doar valori unice. Să ne uităm la un exemplu:

# Original customer list with duplicates
customers = ["Emma", "John", "Emma", "Sophia", "John"]

# Creating a set to keep only unique customers
unique_customers = set(customers)

print(unique_customers)  # Output: {"Emma", "John", "Sophia"}
# Seturile sunt o alegere ideală atunci când avem nevoie de o colecție de elemente unice sau/
#  când vrem să folosim operații matematice cu seturi în Python.


# Mini proiect: Descoperirea de produse populare noi

# Alex vrea să identifice produsele care au devenit populare în luna curentă, dar nu au fost/
#  printre cele mai bine vândute produse în luna precedentă.

#  Sarcină:

# Să creăm două seturi de produse:
# luna_precedentă: produse care au fost populare în luna precedentă ("TV", "Printer", "Tablet").
# luna_curentă: produse care sunt populare în prezent ("Printer", "Tablet", "Monitor", "Laptop").
# Evidențierea noilor produse: Alex vrea să listeze toate produsele care au devenit populare în luna curentă și nu erau populare înainte.
# Hint: Operația de diferență (difference()) între două seturi returnează elementele care sunt prezente doar în primul set.

# Întrebare pentru reflecție: Ce operație pentru lucrul cu seturi este folosită în acest exemplu /
# și de ce? Ar fi o diferență dacă am folosi această operație în ordine inversă, adică luna_precedentă.difference (luna_curentă)

print("ALT EXERCITIU")
luna_precedenta = {"TV", "Printer", "Tablet"}
luna_curenta = {"Printer", "Tablet", "Monitor", "Laptop"}

populare_acum = luna_curenta.difference(luna_precedenta)
print(populare_acum)



print("EXERCITIU ULTIMUL------")

# Context

# Alex, care lucrează într-un magazin online, vrea să analizeze schimbările din baza sa de clienți între 2023 și 2024. /
# Are date despre clienți pentru fiecare dintre acești ani, cu numele clienților reprezentate ca seturi:

# customers_2023: conține numele clienților care au făcut achiziții în 2023;
# customers_2024: conține numele clienților care au făcut achiziții în 2024.
# Scopul analizei

# Alex vrea:

# să găsească clienți noi în 2024, care nu au cumpărat în 2023;
# să găsească clienți pierduți – cei care au cumpărat în 2023, dar nu mai cumpără în 2024.
# Instrucțiuni

# Cum rezolvăm această provocare?

# Definim seturile customers_2023 și customers_2024 folosind exemple de nume.
# Aplicăm operații pe seturi pentru a găsi grupurile de clienți necesare.
# Afișăm rezultatele într-un format care îi va permite lui Alex să înțeleagă mai bine schimbările în rândul clienților.

customers_2023 = {"Alice", "Bob", "Charlie", "David", "Eva", "Frank"}
customers_2024 = {"George", "Hannah", "Ivan", "Bob", "Eva", "Jack"}

clienti_noi = customers_2024.difference(customers_2023)
print("Cienti noi 2024\n")
print(clienti_noi)

clieti_pierduti = customers_2023.difference(customers_2024)
print("clieti ce nu mai cumpara in prezent\n")
print(clieti_pierduti)

print("______-------alta varianta--------______")
customers_2023 = {"Alice", "Bob", "Charlie", "David", "Eva", "Frank"}
customers_2024 = {"George", "Hannah", "Ivan", "Bob", "Eva", "Jack"}

# Find new customers in 2024 who didn't buy in 2023
new_customers_2024 = customers_2024.difference(customers_2023)
print("New customers in 2024 who didn't buy in 2023:")
for customer in new_customers_2024:
     print("-",customer)  
    #  or print(f"- {customer})

# Find customers who bought in 2023 but not in 2024
lost_customers = customers_2023.difference(customers_2024)
print("\nCustomers who bought in 2023 but not in 2024:")
for customer in lost_customers:
    print(f"- {customer}")
    # or print ("-",customer)  
