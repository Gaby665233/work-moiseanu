# Un magazin înregistrează vânzările zilnice într-o săptămână.

# 🔹 Programul trebuie să:

# citească vânzările pentru fiecare zi

# calculeze:

# totalul săptămânal

# totalul zilelor lucrătoare

# totalul weekendului

# verifice dacă duminica > sâmbăta (if pe o linie)

# verifice dacă lucrătoarele > weekend (if-else)

# verifice dacă ambele zile de weekend au peste 500 lei vânzări:

# mesaj pentru ambele

# mesaj pentru una singură

# mesaj pentru niciuna

vanzari = []
zile = ["luni", "marti", "miercuri", "joi", "vineri", "sambata", "duminica"]
for i in zile:
    while True:
        try:
            van = int(input(f" inregistrari vanzari {i}: "))
            vanzari.append(van)
            break
        except ValueError:
            print("introdu un numar, incercati din nou")


total_sap = sum(vanzari)
zile_lucratoare = sum(vanzari[:5])
weekend = sum(vanzari[5:])

print(f"totalul saptamana:{total_sap}")
print(f"total zile lucratoare: {zile_lucratoare}")
print(f" total weekend: {weekend}")
# if pe o linie
print("duminica au fost mai multe vanzari" if vanzari[6] > vanzari[5] else "sambata au fost mai multe vanzari")
# if-else
if zile_lucratoare > weekend:
    print("zilele lucratoare au fost mai profitabile")
else:
    print("weekend-ul a fost mai profitabil")

if vanzari[5] > 500 and  vanzari[6] > 500:
    print("ambele zile de weekend au vanzari peste 500")
elif vanzari[5] > 500 or  vanzari[6] > 500:
    print(f"daor o zi de weekend a avut vanzari peste 500: {"sambata" if vanzari[5] > vanzari[6] else "duminica"}")
else:
    print("nu a fost nicio zi peste 500")





    # varianta sa o ia de la capat v1
vanzari = []
zile = ["luni", "marti", "miercuri", "joi", "vineri", "sambata", "duminica"]

while True:
        try:
            vanzari.clear()
            for i in zile:
                van = int(input(f" inregistrari vanzari {i}: "))
                vanzari.append(van)
            break
        except ValueError:
            print("introdu un numar, incercati din nou")


total_sap = sum(vanzari)
zile_lucratoare = sum(vanzari[:5])
weekend = sum(vanzari[5:])

print(f"totalul saptamana:{total_sap}")
print(f"total zile lucratoare: {zile_lucratoare}")
print(f" total weekend: {weekend}")
# if pe o linie
print("duminica au fost mai multe vanzari" if vanzari[6] > vanzari[5] else "sambata au fost mai multe vanzari")
# if-else
if zile_lucratoare > weekend:
    print("zilele lucratoare au fost mai profitabile")
else:
    print("weekend-ul a fost mai profitabil")

if vanzari[5] > 500 and  vanzari[6] > 500:
    print("ambele zile de weekend au vanzari peste 500")
elif vanzari[5] > 500 or  vanzari[6] > 500:
    print(f"daor o zi de weekend a avut vanzari peste 500: {"sambata" if vanzari[5] > vanzari[6] else "duminica"}")
else:
    print("nu a fost nicio zi peste 500")


# varianta sa o ia de la capat v2


zile = ["luni", "marti", "miercuri", "joi", "vineri", "sambata", "duminica"]

while True:
        vanzari = []
        try:
            for i in zile:
                van = int(input(f" inregistrari vanzari {i}: "))
                vanzari.append(van)
            break
        except ValueError:
            print("introdu un numar, incercati din nou")


total_sap = sum(vanzari)
zile_lucratoare = sum(vanzari[:5])
weekend = sum(vanzari[5:])

print(f"totalul saptamana:{total_sap}")
print(f"total zile lucratoare: {zile_lucratoare}")
print(f" total weekend: {weekend}")
# if pe o linie
print("duminica au fost mai multe vanzari" if vanzari[6] > vanzari[5] else "sambata au fost mai multe vanzari")
# if-else
if zile_lucratoare > weekend:
    print("zilele lucratoare au fost mai profitabile")
else:
    print("weekend-ul a fost mai profitabil")

if vanzari[5] > 500 and  vanzari[6] > 500:
    print("ambele zile de weekend au vanzari peste 500")
elif vanzari[5] > 500 or  vanzari[6] > 500:
    print(f"daor o zi de weekend a avut vanzari peste 500: {"sambata" if vanzari[5] > vanzari[6] else "duminica"}")
else:
    print("nu a fost nicio zi peste 500")
   

   
