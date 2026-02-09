# O sală de fitness urmărește numărul de clienți zilnic.

# 🔹 Programul trebuie să:

# citească clienții pentru fiecare zi

# calculeze:

# total săptămână

# total lucrătoare

# total weekend

# compare sâmbătă și duminică

# compare lucrătoare vs weekend

# verifice dacă ambele zile de weekend au avut peste 50 clienți

# varianta in care nu se repeta
clienti = []
zile = ["luni", "marti", "miercuri", "joi", "vineri", "sambata", "duminica"]
for i in zile:
    c = int(input(f" numarul de clienti {i}:"))
    clienti.append(c)

total = sum(clienti)
total_lucratoare = sum(clienti[:5])
total_wek = sum(clienti[5:])

print(f"total saptamana:{total}")
print(f"total zile lucra:{total_lucratoare}")
print(f"weekend:{total_wek}")

print("sambata au fost mai multi clienti" if clienti[5] > clienti[6] else "duminica au fost mai multi clienti")

if total_lucratoare > total_wek:
    print("zilele lucratoare au fost mai bune")
else:
    print("weekendul a fost mai profitabil")

if clienti[5] > clienti[6] and clienti[6] > clienti[5]:
    print("ambele weekend uri au avut succes")
elif clienti[5] > 50 or clienti[6] > 60:
    print(f"doar {"sambata" if clienti[5] > clienti[6] else "duminica"} a avut mai multi clienti: "
          f"{clienti[5] if clienti[5] > clienti[6] else clienti[6]}")
else:
    print("nimic")

# varianta in care se repeta
clienti = []
zile = ["luni", "marti", "miercuri", "joi", "vineri", "sambata", "duminica"]
while True:
    try:
        clienti.clear()
        for i in zile:
            c = int(input(f" numarul de clienti {i}:"))
            clienti.append(c)
        break
    except ValueError:
        print("incearca iar")


total = sum(clienti)
total_lucratoare = sum(clienti[:5])
total_wek = sum(clienti[5:])

print(f"total saptamana:{total}")
print(f"total zile lucra:{total_lucratoare}")
print(f"weekend:{total_wek}")

print("sambata au fost mai multi clienti" if clienti[5] > clienti[6] else "duminica au fost mai multi clienti")

if total_lucratoare > total_wek:
    print("zilele lucratoare au fost mai bune")
else:
    print("weekendul a fost mai profitabil")

if clienti[5] > clienti[6] and clienti[6] > clienti[5]:
    print("ambele weekend uri au avut succes")
elif clienti[5] > 50 or clienti[6] > 60:
    print(f"doar {"sambata" if clienti[5] > clienti[6] else "duminica"} a avut mai multi clienti:"
          f"{clienti[5] if clienti[5] > clienti[6] else clienti[6]}")
else:
    print("nimic")
