# Alex dorește să scrie un program care verifică dacă, în funcție de cantitatea introdusă, produsul este disponibil sau nu pentru vânzare.

# Creăm o variabilă status.
# Introducem statusul prin intermediul funcției input().
# Dacă statusul este un număr pozitiv, afișăm mesajul „Produsul este disponibil”.
# Dacă statusul nu este un număr pozitiv, afișăm mesajul „Produsul nu este disponibil”.

status = int(input("introdu un numar: "))

if status > 0:
    print("Produsul este disponibil")
else:
    print("Produsul nu este disponibil")

tranzactii = int(input("Introduceti numarul de tranzactii: "))

# Verificam daca numarul de tranzactii este impar

# != este impar

if tranzactii % 2 != 0:
    print("Numarul de tranzactii este impar.")
else:
    print("par")




# == este par
if tranzactii % 2 == 0:
    print("Numarul de tranzactii este par.")
else:
    print("impar")