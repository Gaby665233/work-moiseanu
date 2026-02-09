# Alex dorește acum să monitorizeze și să actualizeze numărul de clienți în diferite zile ale săptămânii. Să creăm un set de variabile /
# care să stocheze numărul de clienți pentru fiecare zi, apoi să actualizăm variabila totală care conține numărul total de clienți.

# Să creăm următoarele variabile:

# total_clienti = 150
# clienti_luni = 50
# clienti_marti = 75
# clienti_miercuri = 60
# Actualizăm conținutul variabilei total_clienti și afișăm valoarea pe ecran.

clienti_luni = 50
clienti_marti = 75
clienti_miercuri = 60

total_clienti = clienti_luni + clienti_marti + clienti_miercuri
print(total_clienti)


# Mini proiect: Analiza datelor despre clienți

# Alex trebuie să analizeze datele despre numărul de clienți și valoarea medie a achizițiilor din magazinul său. Tabelul lui conține următoarele informații:

# număr_clienţi_ianuarie: 1200 de clienţi
# număr_clienţi_februarie: 950 de clienţi
# valoare_medie_ianuarie: 50.75 lei
# valoare_medie_februarie: 45.90 lei
# Sarcina noastră:

# Să creăm variabilele corespunzătoare în Python pentru a înregistra aceste date.
# Să calculăm numărul total de clienți pentru lunile ianuarie și februarie împreună.
# Să găsim valoarea medie a achizițiilor pentru ambele luni împreună.
# Să afișăm pe ecran valorile obținute.
# La final, să verificăm tipurile tuturor variabilelor pentru a ne asigura că datele au fost atribuite corect.
# Hint: Folosim funcția type() pentru a verifica tipul de date pentru fiecare variabilă.

număr_clienţi_ianuarie = 1200
număr_clienţi_februarie = 950 
valoare_medie_ianuarie = 50.75 
valoare_medie_februarie = 45.90

nr_total = număr_clienţi_ianuarie + număr_clienţi_februarie
med =  (valoare_medie_ianuarie + valoare_medie_februarie) / 7
print(f"totalul este: {nr_total}")
print(f"media este: {med}")


print(type(număr_clienţi_februarie))
print(type(număr_clienţi_februarie))
print(type(valoare_medie_februarie))
print(type(valoare_medie_ianuarie))
