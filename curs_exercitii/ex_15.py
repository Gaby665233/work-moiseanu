# Mini activitate: Verificarea succesului vânzărilor pe baza reducerilor și numărului de clienți

# Alex a primit sarcina de a verifica dacă vânzările din timpul weekendului au depins de utilizarea reducerilor și de numărul de clienți. /
# Pe baza acestor date, el trebuie să pregătească recomandări pentru următoarea acțiune promoțională.

# Alex analizează datele despre numărul de clienți și reduceri. Programul trebuie să introducă numărul de clienți și /
# informația dacă aceștia au utilizat reducerea. Pe baza acestor date, programul va afișa un mesaj despre succesul vânzărilor.

# Întrebare înainte de sarcină: Cum am putea adapta codul pentru a verifica diferite reduceri pentru diferite produse? /
# De exemplu, ce s-ar întâmpla dacă am dori să aplicăm un prag diferit pentru succesul vânzărilor pentru produse cu diferite reduceri?

# Sarcină: Să scriem un program care:

# introduce numărul de clienți;
# introduce informația dacă clienții au utilizat reducerea;
# dacă numărul de clienți este mai mare de 100 și reducerea a fost utilizată, programul afișează mesajul „Vânzare reușită!”; în /
# caz contrar, se afișează o recomandare pentru a desfășura o promoție.
# Hint 1: Să ne gândim cum am putea folosi funcția input() pentru a introduce datele despre numărul de clienți și reduceri. /
# Să ne amintim că valoarea introdusă prin input() este întotdeauna un string, deci s-ar putea să avem nevoie de funcția int() /
# pentru a converti numărul de clienți într-un număr întreg.

# Hint 2: Condiția care trebuie verificată include ambii factori – atât numărul de clienți, cât și reducerea. Putem folosi operatorul logic /
# and pentru a ne asigura că ambele condiții sunt adevărate înainte ca programul să afișeze mesajul despre succesul vânzărilor.

nr_clienti = int(input("Numarul de clienti: "))
reduceri = input("reduceri utilizate: da sau nu: ")
if nr_clienti > 100 and reduceri == "da":
    print("vanzari de succes:")
else:
    print("nu")