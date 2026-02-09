# Mini activitate: Corectarea codului cu operatori logici

# Alex lucrează acum la o sarcină pentru echipa de marketing. Este necesar să analizeze reducerile care se aplică clienților, /
# în funcție de statutul lor și de suma achiziției. Echipa folosește două tipuri de reduceri – pentru clienți obișnuiți și membri ai programului de loialitate. /
# Alex este responsabil să pregătească un program care calculează automat reducerea corectă pentru fiecare tip de client pe baza regulilor următoare.

# Reguli de reducere:

# Clienți obișnuiți:
# Suma mai mică de 100 de dolari: Fără reducere.
# Suma între 100 și 500 de dolari: 5% reducere.
# Suma mai mare de 500 de dolari: 10% reducere.
# Membri ai programului de loialitate:
# Suma mai mică de 100 de dolari: 5% reducere.
# Suma între 100 și 500 de dolari: 10% reducere.
# Suma mai mare de 500 de dolari: 15% reducere.
# Sarcina: Să scriem un program Python care folosește structuri if imbricate pentru ca Alex să analizeze datele clienților și să calculeze /
# reducerile pe baza statutului lor și a sumei achiziției.

# Instrucțiuni:

# Folosim input() pentru a introduce statutul clientului (obișnuit sau membru al programului de loialitate) și suma achiziției.
# Mai întâi, verificăm dacă clientul este obișnuit sau membru al programului de loialitate.
# În cadrul acelei verificări, folosim un bloc if imbricat pentru a aloca reducerea corespunzătoare pe baza sumei achiziție.
# Hint: Programul ar trebui să folosească structuri if imbricate – în cadrul primei decizii despre statutul clientului, adăugăm o a doua /
# verificare pentru suma achiziției și alocăm reducerea corespunzătoare.

# Să testăm codul nostru: După ce scriem codul, să-l testăm cu următoarele valori:

# Status: client obișnuit, Sumă: 75 de dolari (rezultatul așteptat: Fără reducere)
# Status: membru al programului de loialitate, Sumă: 200 de dolari (rezultatul așteptat: 10% reducere)
# Status: client obișnuit, Sumă: 600 de dolari (rezultatul așteptat: 10% reducere)
# Status: membru al programului de loialitate, Sumă: 1050 de dolari (rezultatul așteptat: 15% reducere)
#  Notă despre erori:

# Să fim atenți la indentarea corectă a codului pentru ca Python să interpreteze corect structurile imbricate.
# Să verificăm logica condițiilor – să ne asigurăm că folosim intervalul de valori corespunzător (de exemplu, >= sau <=).

clienti = input("Status: obisnuit/premium: ").lower()
suma = int(input("introdu suma: "))
print(f"Status: Client {clienti},Suma: {suma} de dolari")
if clienti == "obisnuit":
    if suma <= 100:
        print("fara reducere")
    elif 100 <= suma <= 500:
        print("5%")
    else:
        print("10%")


elif clienti == "premium":
    if suma <= 100:
        print("5%")
    elif 100 <= suma >= 500:
        print("10%")
    else:
        print("15%") 
else:
    print("nu se cunoaste")

# v2
clienti = input("Status: obisnuit/premium: ").lower()
suma = float(input("Introduce suma: "))
print(f"Status: Client {clienti}, Suma: {suma} de dolari")

# inițializare reducere
reducere = 0

if clienti == "obisnuit":
    if suma < 100:
        reducere = 0
    elif suma <= 500:
        reducere = 0.05
    else:
        reducere = 0.10

elif clienti == "premium":
    if suma < 100:
        reducere = 0.05
    elif suma <= 500:
        reducere = 0.10
    else:
        reducere = 0.15

else:
    print("Statut necunoscut")
    reducere = 0

# afișăm reducerea obținută
print(f"Reducerea aplicată este: {reducere*100}%")