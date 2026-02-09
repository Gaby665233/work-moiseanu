def calculate_discount(price, discount_percent):
    new_price = price - (price * discount_percent) / 100
    return new_price

# Apelarea functiei pentru exemplul cand pretul este 500, iar reducerea 10%
print(calculate_discount(500, 10))


# Mini activitate: Să calculăm prețul cu reducerea

# Acum este rândul nostru! Creați o funcție care să vă ajute să calculați noul preț al produsului cu reducere pentru diferite valori. /
# Încercați-o cu câteva introduceri diferite și verificați cum calculează corect prețul produsului.

#  Sarcină: Să scriem o funcție numită total_timp care:

# va defini funcția care primește prețul produsului și procentul de reducere;
# va face funcția să calculeze noul preț al produsului folosind aceiași pași ca Alex;
# va testa funcția cu mai multe prețuri și procente de reducere.
# Când terminăm, să ne gândim la următoarea întrebare:

# Întrebare pentru reflecție: Cum ar putea fi această funcție adaptată pentru situații în care există mai multe reduceri diferite, în funcție /
# de tipul produsului sau de statutul de membru al clientului? Cum ați adapta funcția pentru a lua în considerare diferite niveluri de reducere?

def reducere(pret, produs_reducere):
    nou_pret = pret - (pret * produs_reducere) / 100
    return nou_pret
print(reducere(400, 20))


# În echipa lui Alex, clienții cu o cheltuială lunară mai mare de 10.000 de lei obțin statut VIP. Pentru a automatiza această verificare, /
# Alex a definit o funcție vip_customer, care primește suma cheltuită ca argument și returnează True dacă clientul îndeplinește condiția pentru statut /
# VIP și False dacă nu o îndeplinește.

def vip_customer(amount):
    if amount > 10000:
        return True
    else:
        return False
# Apelarea functiei și afișarea rezultatelor
ans1 = vip_customer(1500)
print(f"Utilizatorul care a cheltuit 1500 lei este client VIP: {ans1}")
ans2 = vip_customer(20000)
print(f"Utilizatorul care a cheltuit 20000 lei este client VIP: {ans2}")




# Mini activitate: Verificarea statutului VIP

# Să exersăm împreună! Creați o funcție care verifică dacă un client cu cheltuieli săptămânale este calificat pentru statutul VIP,/
# dar să aibă un prag mai mic decât cel folosit de Alex pentru cheltuielile lunare.

#  Sarcină: Să scriem o funcție numită total_timp care:

# va defini funcția ce primește suma totală a cheltuielilor pentru o săptămână ca argument.
# va verifica dacă suma este mai mare de 2.500 de lei și va returna True dacă da, altfel returnează False.
# va testa funcția cu mai multe valori diferite ale cheltuielilor săptămânale și să vedem cum funcția ia decizii corecte.
#  Întrebare pentru reflecție: Cum ar putea fi extinsă această funcție pentru a lua decizii diferite în funcție de diferite niveluri /
# ale statutului VIP? De exemplu, cum am putea distinge între membrii Gold și Platinum pe baza diferitelor praguri de cheltuieli?

# def total_timp(suma):
#     if suma > 2500:
#         return True
#     else:
#         return False
# ans_1 = total_timp(40000)
# print(f"Este client fidel {ans_1}")



def total(suma):
    return suma > 2500
suma_introdusa = int(input("introdu suma:"))

rezultast = total(suma_introdusa)
print(f"Suma este {suma_introdusa} si rezultatrul este {rezultast}")


# v2

def tot(sum):
    return sum > 5000
sum_introdus = int(input("introdu un numar"))

if tot(sum_introdus):
    mesaj = "Gold"
else:
    mesaj = "silver"

rezultate = tot(sum_introdus)
print(f"Status {mesaj}")
print(f"Suma este {sum_introdus} si rezultatul {rezultate}")
