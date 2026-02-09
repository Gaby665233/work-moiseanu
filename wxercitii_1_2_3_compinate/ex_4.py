# EXERCIȚIU NOU – „Cafenea: trafic, vânzări și rezervări mese”
# 📌 Context

# O cafenea monitorizează timp de 7 zile:

# numărul de clienți pe zi

# vânzările zilnice

# rezervările de mese

# 🟩 EXERCIȚIUL 1 – Analiză săptămânală

# Citește pentru fiecare zi a săptămânii:

# numărul de clienți

# valoarea vânzărilor

# Calculează și afișează:

# numărul maxim și minim de clienți

# media clienților pe zi

# totalul vânzărilor și media zilnică

# dacă weekendul a avut mai mulți clienți decât zilele lucrătoare

# câte zile au avut peste 100 de clienți și câte zile peste 1000 lei vânzări

# 🟨 EXERCIȚIUL 2 – Clasificare zilnică

# Pentru fiecare zi:

# dacă clienți > 120 și vânzări > 1500 →
# 👉 Zi aglomerată și foarte profitabilă: {zi}

# dacă clienți < 60 și vânzări < 500 →
# 👉 Zi slabă: {zi}

# altfel →
# 👉 Zi normală: {zi}

# 🟦 EXERCIȚIUL 3 – Rezervări mese + analiză

# Pentru fiecare zi:

# citește numărul de mese rezervate

# citește statusul rezervării (confirmata / anulata / in asteptare)

# normalizează statusul

# Calculează:

# suma totală obținută din rezervări confirmate
# (o masă = 40 lei)

# 🟥 EXERCIȚIUL 4 – Clasificare combinată

# Afișează zilele care îndeplinesc cel puțin 2 din următoarele condiții:

# peste 120 clienți

# vânzări peste 1500 lei

# rezervare confirmată

# Pentru fiecare zi afișează motivele.




#  EXERCIȚIUL 1 – Analiză săptămânală

# Citește pentru fiecare zi a săptămânii:

# numărul de clienți

# valoarea vânzărilor

# Calculează și afișează:

# numărul maxim și minim de clienți

# media clienților pe zi

# totalul vânzărilor și media zilnică

# dacă weekendul a avut mai mulți clienți decât zilele lucrătoare

# câte zile au avut peste 100 de clienți și câte zile peste 1000 lei vânzări

import unicodedata
def normalize(text):
    text = text.lower()
    text = unicodedata.normalize("NFD",text)
    text = ''.join( ch for ch in text if unicodedata.category(ch) != "Mn")
    return(text)


zile = ["luni", "marti", "miercuri", "joi", "vineri", "sambata", "duminica"]

clienti = []
for zi in zile:
    while True:
        try:
            cli = int(input(f"Clienti {zi}: "))
            clienti.append(cli)
            break
        except ValueError:
            print("incerca din nou")

vanzari = []
for zi in zile:
    while True:
        try:
            van = int(input(f"vanzarile {zi}: "))
            vanzari.append(van)
            break
        except ValueError:
            print("incearca iar")


clienti_max = max(clienti)
clienti_min = min(clienti)
clienti_med = sum(clienti) / 7
vanzari_total = sum(vanzari)
vanzari_med = sum(vanzari)
wek_maimare_lucaratoare = sum(clienti[5:]) > sum(clienti[:5])
zlie_clienti_100 = sum( c > 100 for c in clienti )
zile_vanzari_100 = sum( v > 100 for v in clienti )



    



#  EXERCIȚIUL 2 – Clasificare zilnică

# Pentru fiecare zi:

# dacă clienți > 120 și vânzări > 1500 →
# 👉 Zi aglomerată și foarte profitabilă: {zi}

# dacă clienți < 60 și vânzări < 500 →
# 👉 Zi slabă: {zi}

# altfel →
# 👉 Zi normală: {zi}


print("\n--- CLASIFICARE ZILNICA ---")
for i,zi in enumerate(zile):
    if clienti[i] > 120 and vanzari[i] > 1500:
        print(f"Zi aglomerată și foarte profitabilă: {zi} ")
    elif clienti[i] < 60 and vanzari[i] < 500:
        print(f"Zi slabă: {zi}")
    else:
        print(f"Zi normala: {zi}")



#  EXERCIȚIUL 3 – Rezervări mese + analiză

# Pentru fiecare zi:

# citește numărul de mese rezervate

# citește statusul rezervării (confirmata / anulata / in asteptare)

# normalizează statusul
# Calculează:

# suma totală obținută din rezervări confirmate
# (o masă = 40 lei)


mese = []

for zi in zile:
    while True:
        try:
            m = int(input(f"masa {zi}: "))
            if mese < 0:
                print("numarul este negativ")
                continue
            mese.append(m)
            break
        except ValueError:
            print("lasa te")

status_rezervare = []
while True:
    status = input(f"Status rezervare {zi}: confirmata / anulata / in asteptare ")
    status_norm = normalize(status)
    if status_norm in ["confirmata" / "anulata" / "in asteptare"]:
        status_rezervare.append(status_norm)
        break
    else:
        print("nimic")

total_rezervari = 0
for i,status_norm in enumerate(zile):
    if status_norm == "confirmata":
        total_rezervari =+ mese[i] * 40
        print(f"\nSuma obtinuta din rezervari {total_rezervari}")



#  EXERCIȚIUL 4 – Clasificare combinată

# Afișează zilele care îndeplinesc cel puțin 2 din următoarele condiții:

# peste 120 clienți

# vânzări peste 1500 lei

# rezervare confirmată

# Pentru fiecare zi afișează motivele.

for i,zi in enumerate(zile):
    motive = []
if clienti[i] >120:
    motive.append("Multi clienti")
if vanzari[i] > 1500:
    motive.append("s au facut bani azi")
if status_rezervare[i] == "confirmata":
    motive.append("merge treaba")
if len(motive) >= 2:
    print(f"{zi.capitalize()}: {', '.join(motive)}")