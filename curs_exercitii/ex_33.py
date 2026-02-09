# De exemplu, Alex observă că "Camera" nu mai este la vânzare și vrea să o înlocuiască cu un produs nou, "Smart Watch", exact în același loc din listă.

# Product list
products = ["Laptop", "Phone", "TV", "Headphones", "Camera"]
print("List contents before modification:")
print(products)

# Replacing the last item in the list with "Smart Watch"
products[-1] = "Smart Watch"
print("List contents after modification:")
print(products)


# Să ne uităm la un exemplu simplu în care Alex adaugă "Tablet" la lista de produse:
print("___________---------------__________________")
# Product list before modification
products = ["Laptop", "Phone", "TV", "Headphones", "Camera"]
print("List contents before modification:")
print(products)

# Adding a new product to the end of the list
products.append("Tablet")
print("List contents after modification:")
print(products)

# Când Alex va rula acest cod, "Tablet" va apărea la sfârșitul listei, permițându-i să urmărească cu ușurință modificările din sortiment.



# Mini activitate: Urmărirea vânzărilor și actualizarea inventarului

# Alex stochează informații despre cantitatea totală de produse pe care le are în stoc în variabila total_stock. Pe parcursul unei /
# săptămâni (7 zile), se înregistrează numărul de articole vândute în fiecare zi. Prin această sarcină, vom aplica metodele de /
# lucru cu listele pe care le-am învățat în această lecție.

# Sarcină:

# Este necesar:

# să definim nivelul inițial al stocului – să setăm total_stock la 1000, care reprezintă cantitatea inițială de articole din stoc;
# să creăm o listă sales care va stoca numărul de articole vândute pentru fiecare zi a săptămânii (7 zile).
# să completăm lista sales cu intrarea utilizatorului folosind funcția input() din interiorul buclei; fiecare intrare reprezintă /
# numărul de articole vândute într-o zi;
# să calculăm vânzările totale pentru săptămână adunând toate valorile din lista sales.
# să actualizăm soldul stocului scăzând numărul total de articole vândute din valoarea inițială a total_stock.
# să imprimăm cantitatea rămasă de articole după o săptămână.

total_stock = 1000
sales = []
zile = ["luni", "marti", "miercuri", "joi", "vineri", "sambata", "duminica"]
while True:
    try:
        for i in zile:
            utilizator = int(input(f"introdu cate articole sunt vandute {i}: "))
            sales.append(utilizator)
        break
    except ValueError:
        print("ai gresit")



            
            
total = sum(sales)
soldul = total - total_stock
print(f"a mai ramams {soldul}")

# varinta 2
totala = 1000
sales = []
while True:
    try:
        for i in range(7):
            utilizatora = int(input(f"introdu cate articole sunt vandute {i + 1}: "))
            sales.append(utilizatora)
        break
    except ValueError:
        print("inncorect")

total = sum(sales)
soldul = total - total_stock
print(f"a mai ramams {soldul}")