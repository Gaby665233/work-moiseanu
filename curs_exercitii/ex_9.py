# Să ne imaginăm că Alex vrea să verifice datele despre clienți și vânzări după a treia lună (martie) și să actualizeze valorile pentru a avea un/
#  raport total pentru trimestru.

# Date pentru martie:

# Numărul de clienți: 140
# Vânzarea medie: 48.25 lei
# Cheltuieli pentru promovare: 4.000 lei
# Sarcina:

# Să creăm variabile pentru numărul de clienți și vânzările din ianuarie, februarie și martie.
# Să folosim operatori aritmetici combinați cu operatorul de atribuire pentru:
# a aduna numărul de clienți din martie cu numărul existent de clienți pentru ianuarie și februarie;
# a adăuga vânzarea medie din martie la vânzările din ianuarie și februarie;
# a scădea cheltuielile de promovare din vânzarea totală.
# Să afișăm rezultatele finale pentru numărul de clienți și vânzările totale după cheltuielile de promovare.
#  Hint: Utilizați operatorii += și -= pentru a actualiza datele.

umărul_de_clienți = 140
vânzarea_medie = 48.25 
cheltuieli_promovare = 4.000 
clienţi_ianuarie = 135
clienţi_februarie = 120
valoarea_medie_ianuarie = 52.75 
valoarea_medie_februarie = 47.50 

umărul_de_clienți += clienţi_ianuarie + clienţi_februarie
print(umărul_de_clienți)

total_vanzari = valoarea_medie_ianuarie + valoarea_medie_februarie
total_vanzari += vânzarea_medie

total_vanzari -= cheltuieli_promovare
print(total_vanzari)

