cod = "12345"
print(cod.isdigit())  # Afiseaza: True

nume ="Marko"
print(nume.isalpha())  # Afiseaza: True

 


# Mini activitate

# Sarcină: Verificați dacă șirul „Marko2023” conține doar litere folosind metodele corespunzătoare.


nume = "Marko2023"
print(nume.isdigit())

text = "Bun venit la curs"
print(text.startswith("Bun"))  # Afiseaza: True
print(text.endswith("curs"))     # Afiseaza: True


# Mini activitate

# Sarcină: Verificați dacă propoziția „Python este distractiv” începe cu „Python” și se termină cu „distractiv”.

prop = "Python este distractiv"
print(prop.startswith("Python"))
print(prop.endswith("distractiv"))


nume = "Marko"
mesaj = "Bun venit, {}!".format(nume)
print(mesaj)  # Afiseaza: 'Bun venit, Marko!'

# Mini activitate

# Sarcină: Creați un mesaj „Comanda dvs. cu numărul 12345 a fost primită cu succes” folosind metoda format().

nummar = 12345
mesaj = "Comanda dvs. cu numărul {} a fost primită cu succes".format(nummar)
print(mesaj)



# Implementarea funcției clasice

# Definim o funcție filter_func(x) care returnează True dacă numărul este impar x % 2 != 0).
# filter(filter_func, numbers) folosește această funcție pentru a păstra doar numerele impare în lista numbers.
def filter_func(x):
    return x % 2 != 0

numbers = list(range(0, 10))
print(list(filter(filter_func, numbers)))  # Output: [1, 3, 5, 7, 9]



print("----ALT EXERCITIU-----")
# Alex are o listă de clienți cu cheltuielile lor totale și dorește să selecteze clienți VIP care au cheltuit mai mult de 100.000 de dinari.
customers = [
    {'name': 'Mark', 'spending': 75000},
    {'name': 'Anna', 'spending': 120000},
    {'name': 'John', 'spending': 50000},
    {'name': 'Eve', 'spending': 130000}
]

vip_customers = list(filter(lambda x: x['spending'] > 100000, customers))
for c in vip_customers:

    print(f"{c['name']} is a VIP customer with a spending of {c['spending']}.")