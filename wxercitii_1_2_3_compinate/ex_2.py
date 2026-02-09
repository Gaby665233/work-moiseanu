# Exercițiu nou: Analiza restaurantului

# Descriere:

# Ai un restaurant deschis 7 zile pe săptămână.

# Pentru fiecare zi, citește:

# temperatura exterioară (°C)

# vânzările în lei

# numărul de mese rezervate

# Normalizează statusul rezervării pentru mesele speciale (confirmata, anulat, in asteptare).

# Calculează și afișează:

# temperatura maximă, minimă și medie

# totalul vânzărilor și media zilnică

# numărul de zile fierbinți (temperatura > 30°C) și zile cu vânzări mari (> 1000 lei)

# dacă weekend-ul a fost mai profitabil decât zilele lucrătoare

# Pentru fiecare zi, print recomandări:

# Dacă temperatura > 30°C și vânzările > 1000 → „Zi fierbinte și profitabilă”

# Dacă temperatura < 20°C și vânzările < 300 → „Zi rece și slabă vânzare”

# În rest → „Zi normală”

# Pentru rezervările confirmate, calculează suma totală (mese * 50 lei pe masă) și afișează zilele în care vânzările depășesc această sumă.

# Creează o listă cu zile speciale, care îndeplinesc cel puțin două dintre condițiile:

# temperatura > 30°C

# vânzări > 1000

# rezervare confirmată




#  Ai un restaurant deschis 7 zile pe săptămână.

# Pentru fiecare zi, citește:

# temperatura exterioară (°C)

# vânzările în lei

# numărul de mese rezervate


import unicodedata
def normalizare(text):
    text = text.lower()
    text = unicodedata.normalize("NFD", text)
    text = ''.join(ch for ch in text if unicodedata.category(ch) != "Mn")
    return(text)


zile = ["luni", "marti", "miercuri", "joi", "vineri", "sambata", "duminica"]


temperatura = []
for zi in zile:
    while True:
        try:
            temp = int(input(f"Temperatura {zi}: "))
            temperatura.append(temp)
            break
        except ValueError:
            print("introdu un numar")


vazari = []
for zi in zile:
    while True:
        try:
            van = float(input(f"Vanzarile {zi}: "))
            vazari.append(van)
            break
        except ValueError:
            print("introdu un numar")

mese = []
for zi in zile:
    while True:
        try:
            mas = int(input(f"Mese {zi}: "))
            mese.append(mas)
            break
        except ValueError:
            print("introdu un numar de mere")


# Normalizează statusul rezervării pentru mesele speciale (confirmata, anulat, in asteptare).

# Calculează și afișează:

# temperatura maximă, minimă și medie

# totalul vânzărilor și media zilnică

# numărul de zile fierbinți (temperatura > 30°C) și zile cu vânzări mari (> 1000 lei)

# dacă weekend-ul a fost mai profitabil decât zilele lucrătoare

rezervare_status = []
for zi in zile:
    while True:
        status = input(f"Statud rezervare pentru {zi}: confirmata, neconfirmata, anulata: ")
        status_normalize = normalizare(status)
        if status_normalize in ["confirmata", "neconfirmata", "anulata"]:
            rezervare_status.append(status_normalize)
            break
        else:
            print("Status necumoscut")


temp_max = max(temperatura)
temp_min = min(temperatura)
media_temp = sum(temperatura) / 7
total_vanzari = sum(vazari)
med_zilnic = sum(vazari) / 7
zile_fiebinti = sum(t > 30 for t in temperatura)
vanzari_mari = sum( v > 1000 for v in vazari)
wek_mai_profitabil = sum(vazari[5:]) > sum(vazari[:5])

print("\n--- Raport saptamanal---")
print(f"Temperatura maxima {temp_max}: ")
print(f"Temperatura minima {temp_min}: ")
print(f"Media temperatura {media_temp}: ")
print(f"Total vanzari {total_vanzari}: ")
print(f"Media zilnica {med_zilnic}: ")
print(f"Zile fierbinti {zile_fiebinti}: ")
print(f"vanzari mari {vanzari_mari}: ")   
print(f"Weekend mai profitabil {wek_mai_profitabil}: ")


# Pentru fiecare zi, print recomandări:

# Dacă temperatura > 30°C și vânzările > 1000 → „Zi fierbinte și profitabilă”

# Dacă temperatura < 20°C și vânzările < 300 → „Zi rece și slabă vânzare”

# În rest → „Zi normală”

# Pentru rezervările confirmate, calculează suma totală (mese * 50 lei pe masă) și afișează zilele în care vânzările depășesc această sumă.
print("--- Raport zilnic---")

for i,zi in enumerate(zile):
    if temperatura[i] > 30 and vazari[i] > 1000:
        print("Zi fierbinte si profitabila")
    elif temperatura[i] < 20 and vazari[i]  < 300:
        print("zi rece si calda")
    else:
        print("zi normala")

#  Pentru rezervările confirmate, calculează suma totală (mese * 50 lei pe masă) și afișează zilele în care vânzările depășesc această sumă.
total_rezervari = 0
for i,status in enumerate(rezervare_status):
    if status == "confirmata":
        total_rezervari += mese[i] * 50
        print(f"\nSuma totala din rezervari {total_rezervari}")

zile_vanzari_mai_mari = [zile[i] for i,v in enumerate(vazari) if v > total_rezervari]
if zile_vanzari_mai_mari:
    print(f"zile cu vanzari mai mari decat totalul rezervarilor: {', '.join(zile_vanzari_mai_mari)}")
else:
    print("nu au fost vanzari mai mari")


# Creează o listă cu zile speciale, care îndeplinesc cel puțin două dintre condițiile:

# temperatura > 30°C

# vânzări > 1000

# rezervare confirmată

print("\n--- Zile speciale--- ")

Speciale = []

for i,zi in enumerate(zile):
    conditii = 0
    if temperatura[i] > 30:
        conditii += 1
        
    if vazari[i] > 1000:
        conditii += 1

    if rezervare_status[i] =="confirmata" and mese[i] > 0:
        conditii += 1
    
    if conditii >= 2:
        Speciale.append(zile)
    print("zile speciale:", Speciale)



