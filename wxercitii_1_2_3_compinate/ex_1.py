# Exercițiul 1: Analiză completă săptămânală

# Citește temperaturile și vânzările pentru fiecare zi a săptămânii.

# Calculează:

# temperatura maximă, minimă și medie;

# totalul vânzărilor și media zilnică;

# dacă weekend-ul a fost mai cald decât zilele lucrătoare;

# dacă vânzările de weekend au depășit vânzările din zilele lucrătoare;

# numărul de zile cu temperaturi peste 30°C și zile cu vânzări peste 500.

# Afișează un raport săptămânal care include toate informațiile de mai sus.

# Exercițiul 2: Recomandări pe baza temperaturii și vânzărilor

# Folosește datele de la exercițiul 1.

# Pentru fiecare zi:

# Dacă temperatura > 30°C și vânzările > 500, print: "Zi fierbinte și profitabilă: {zi}";

# Dacă temperatura < 20°C și vânzările < 200, print: "Zi rece și slabă vânzare: {zi}";

# În rest, print: "Zi normală: {zi}".

# Exercițiul 3: Rezervări hotel + analiza săptămânii

# Citește datele pentru o rezervare (nopți, preț/noapte, status).

# Normalizează statusul rezervării folosind funcția normalizare().

# Dacă rezervarea este confirmată:

# Calculează costul total (nopti * pret).

# Verifică dacă există o zi cu vânzări mai mari decât această sumă și print zilele respective.

# Dacă rezervarea nu e confirmată, print un mesaj corespunzător și cere datele din nou.

# Exercițiul 4: Clasificare combinată

# Folosește toate datele: temperaturi, vânzări și rezervări.

# Creează o listă cu zilele care îndeplinesc cel puțin două din următoarele condiții:

# temperatura > 30°C

# vânzări > 500

# există o rezervare confirmată care include acea zi

# Afișează zilele respective și motivele pentru care au fost selectate.


import unicodedata
def normalizare(text):
    text = text.lower()
    text = unicodedata.normalize("NFD", text)
    text = "".join( ch for ch in text if unicodedata.category(ch) != "Mn")
    return(text)


temperatura = []
zile = ["luni", "marti", "miercuri", "joi", "vineri", "sambata", "duminica"]

for zi in zile:
    while True:
        try:
            temp = int(input(f"temperatura pentru {zi}: "))
            temperatura.append(temp)
            break
        except ValueError:
            print("introdu o cifra")

vanzari = []
zile = ["luni", "marti", "miercuri", "joi", "vineri", "sambata", "duminica"]

for zi in zile:
    while True:
        try:
            van = float(input(f"vanzarile de {zi}: "))
            vanzari.append(van)
            break
        except ValueError:
            print("adauga o cifra")


# temperatura maximă, minimă și medie;
# # totalul vânzărilor și media zilnică;
# dacă weekend-ul a fost mai cald decât zilele lucrătoare;
# numărul de zile cu temperaturi peste 30°C și zile cu vânzări peste 500.
# dacă vânzările de weekend au depășit vânzările din zilele lucrătoare;



temperatura_max = max(temperatura)
tem_min = min(temperatura)
media_tem = sum(temperatura) / 7
tem_peste_30 = sum(t > 30 for t in temperatura)
wek_mai_mult_temp = sum(temperatura[5:]) > sum(temperatura[:5])

total_vanzari = sum(vanzari)
med_zilnic_van = sum(vanzari) / 7
van_peste_300 = sum( v > 500 for v in vanzari )
wek_mai_mult_vanz = sum(temperatura[5:]) > sum(temperatura[:5])

print("\n--- raport saptamanal---")
print(f"temperatura maxima: {temperatura_max}")
print(f"temperatura minima: {tem_min}")
print(f"media temperatura: {media_tem}")
print(f"temperatura peste 30: {tem_peste_30}")
print(f"in weekend a avut mai mult: {wek_mai_mult_temp}")

print(f"totalul vanzarilor: {total_vanzari}")
print(f"media zilnica vanzari: {med_zilnic_van}")
print(f"vanzari peste 500: {van_peste_300}")
print(f"weekend mai mult: {wek_mai_mult_vanz}")

# Exercițiul 2: Recomandări pe baza temperaturii și vânzărilor

# Folosește datele de la exercițiul 1.

# Pentru fiecare zi:

# Dacă temperatura > 30°C și vânzările > 500, print: "Zi fierbinte și profitabilă: {zi}";

# Dacă temperatura < 20°C și vânzările < 200, print: "Zi rece și slabă vânzare: {zi}";

# În rest, print: "Zi normală: {zi}".
print("\n--- raportari zilnice ---")

for i,zi in enumerate(zile):
    if temperatura[i] > 30 and vanzari[i] > 500:
        print(f"Zi fierbinte si profitabila: {zi}")
    elif temperatura[i] < 20 and vanzari[i] < 200:
        print(f"zi rece si slaba vanzare: {zi}")
    else:
        print(f"Zi normala: {zi}")

# Exercițiul 3: Rezervări hotel + analiza săptămânii

# Citește datele pentru o rezervare (nopți, preț/noapte, status).

# Normalizează statusul rezervării folosind funcția normalizare().

# Dacă rezervarea este confirmată:

# Calculează costul total (nopti * pret).

# Verifică dacă există o zi cu vânzări mai mari decât această sumă și print zilele respective.

# Dacă rezervarea nu e confirmată, print un mesaj corespunzător și cere datele din nou.

while True:
    try:
       nopti = int(input("introdu numarul de nopti: "))
       if not ( 1 <= nopti <= 15):
           print("poti introduce doar pana la 15 nopti")
           continue
    except ValueError:
        print("introdu din nou")

    try:
        pret = float(input("introdu pretul: "))
        if pret <= 0 :
            print("numarul este prea mic")
            continue
    except ValueError:
        print("nu te pricepi")
        continue
    
    status = input("status rezervare confirmata, neconfirmata, in asteptare: ")
    status_normalizare = normalizare(status)
    if status_normalizare == "confirmata":
        cons_total = nopti * pret 
        print(f"\nrezervare noprti:{nopti}, Pret:{pret}, Status:{status}")
        zile_mai_mari = [zile[i] for i,v in enumerate(vanzari) if v > cons_total ]
        if zile_mai_mari:
            print(f"zile cu vanzari mai mari:{', '.join(zile_mai_mari)}")
        else:
            print("nu exista zile cu vanzari mai mari")
        break
    elif status_normalizare in ["confirmata", "neconfirmata", "in asteptare"]:
        print("comanda nu este platita,incercati din nou")
        continue
    else:
        print("status necunoscut")
    

# Exercițiul 4: Clasificare combinată

# Folosește toate datele: temperaturi, vânzări și rezervări.

# Creează o listă cu zilele care îndeplinesc cel puțin două din următoarele condiții:

# temperatura > 30°C

# vânzări > 500

# există o rezervare confirmată care include acea zi

# Afișează zilele respective și motivele pentru care au fost selectate.

print("\n--- Clasificare combinata ---")

for i,zi in enumerate(zile):
    motive = []
    if temperatura[i] > 30:
        motive.append("fierbinte")
    if vanzari[i] > 500:
        motive.append("Profitabil")
    if i < nopti:
        motive.append("rezervare confirmata")
    if len(motive) >= 2:
        print(f"{zi.capitalize()}: {', '.join(motive)}")




