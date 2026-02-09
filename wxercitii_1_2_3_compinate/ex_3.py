
# Citește pentru fiecare zi a săptămânii:

# Temperatura (float)

# Vânzările (float)

# Statusul rezervării (confirmata, anulat, in asteptare)

# Numărul de mese rezervate (număr întreg)

# Calculează și afișează:

# Temperatura maximă, minimă și media săptămânii

# Totalul vânzărilor și media zilnică

# Totalul rezervărilor confirmate (mese × 50 lei)

# Zilele în care vânzările au depășit totalul rezervărilor confirmate

# Analiză zilnică:

# Pentru fiecare zi:

# Dacă temperatura > 30°C și vânzările > 500 → "Zi fierbinte și profitabilă"

# Dacă temperatura < 20°C și vânzările < 200 → "Zi rece și slabă vânzare"

# Dacă rezervarea este confirmată și temperatura > 25 → "Zi bună pentru rezervare"

# În rest → "Zi normală"

# Clasificare combinată:

# Creează o listă cu zilele care îndeplinesc cel puțin două dintre următoarele:

# Temperatura > 30°C

# Vânzări > 500

# Rezervare confirmată

# Afișează zilele și motivele pentru care au fost selectate.





# Citește pentru fiecare zi a săptămânii:

# Temperatura (float)

# Vânzările (float)

# Statusul rezervării (confirmata, anulat, in asteptare)

# Numărul de mese rezervate (număr întreg)


import unicodedata
def normalizare(text):
    text = text.lower()
    text = unicodedata.normalize("NFD",text)
    text = ''.join( ch for ch in text if unicodedata.category(ch) != "Mn")
    return(text)

zile = ["luni", "marti", "miercuri", "joi", "vineri", "sambata", "duminica"]

temperatura = []
for zi in zile:
    while True:
        try:
            temp = (float(input(f"Temperatura {zi}: ")))
            temperatura.append(temp)
            break
        except ValueError:
            print("introdu din nou")

vanzari = []
for zi in zile:
    while True:
        try:
            van = float(input(f"Vanzarile {zi}: "))
            vanzari.append(van)
            break
        except ValueError:
            print("incearca iar")

status_rezervare = []
for zi in zile:
    while True:
        status = input(f"Introdu starusul rezervarii {zi}: confirmata, anulata, in asteptare")
        status_normalizare = normalizare(status)
        if status_normalizare in ["confirmata", "anulata", "in asteptare"]:
            status_rezervare.append(status_normalizare)
            break
        else:
            print("Status necunoscut")


mese = []
for zi in zile:
    while True:
        try:
            m = int(input(f"Masa {zi}: "))
            mese.append(m)
            break
        except ValueError:
            print("introdu ba numarul de mese")


# Calculează și afișează:

# Temperatura maximă, minimă și media săptămânii

# Totalul vânzărilor și media zilnică

# Totalul rezervărilor confirmate (mese × 50 lei)

# Zilele în care vânzările au depășit totalul rezervărilor confirmate
        
tem_max = max(temperatura)
tem_min = min(temperatura)
tem_med = sum(temperatura) / 7
total_vanzari = sum(temperatura)
vanzari_med = sum(temperatura) / 7

print("\n---Raport saptamana---")
print(f"Temperatura maxima: {tem_max}")
print(f"Temperatua minica: {tem_min}")
print(f"Temperatura medie: {tem_med}")
print(f"total vanzari: {total_vanzari}")
print(f"media zilnica vanzari: {vanzari_med}")


total_rezervari = 0

for i,status_normalizare in enumerate(status_rezervare):
    if status_normalizare =="confimare":
        total_rezervari += mese[i] * 50
        print(f"Total rezervari confirmate {total_rezervari}: ")

zile_mai_multe_vanzari = [zile[i] for i,v in enumerate(vanzari) if v > total_vanzari ]
if zile_mai_multe_vanzari:
    print(f"zile de vanzari care au depasit totalul rezervarilor: {', '.join(zile_mai_multe_vanzari)}")
else:
    print("nu au fost vanzari")

# Pentru fiecare zi:

# Dacă temperatura > 30°C și vânzările > 500 → "Zi fierbinte și profitabilă"

# Dacă temperatura < 20°C și vânzările < 200 → "Zi rece și slabă vânzare"

# Dacă rezervarea este confirmată și temperatura > 25 → "Zi bună pentru rezervare"

# În rest → "Zi normală"
print("\n---Raport zilnic---")
for i, zi in enumerate(zile):
    if temperatura[i] > 30 and vanzari[i] >500:
        print(f"{zi.capitalize()}: Zi fierbinte și profitabilă")
    elif temperatura[i] < 20 and vanzari < 200:
        print(f"{zi.capitalize()}: Zi rece și slabă vânzare")
    elif status_rezervare =="confirmata" and temperatura[i] > 25:
        print(f"{zi.capitalize()}: Zi bună pentru rezervare")
    else:
        print(f"{zi.capitalize()}: Zi normala")


# Creează o listă cu zilele care îndeplinesc cel puțin două dintre următoarele:

# Temperatura > 30°C

# Vânzări > 500

# Rezervare confirmată

# Afișează zilele și motivele pentru care au fost selectate.

for i,zi in enumerate(zile):
    motive = []
    if temperatura[i] > 30:
        motive.append("fierbinti")
    if vanzari[i] > 500:
        motive.append("Profitabil")
    if status_rezervare[i] =="confirmare":
        motive.append("rezervare confirmate")
    if len(motive) >= 2:
        print(f"{zi.capitalize()}: {', '.join(motive)}")