# număr_clienti = int(input("Introduceti numarul de clienti de azi: "))
# reducere = input("Au folosit clientii reducerea (da/nu)? ")

# # Verificarea conditiilor pentru recomandari catre echipa de vanzari
# 
# if numar_clienti > 100 and reducere == "da":
#     print("Vanzare reusita, datorita reducerilor!")

# 
# if numar_clienti > 100 and reducere == "nu":
#     print("Vanzare buna, dar puteti atrage mai multi clienti facand reduceri.")

# 
# if 50 <= numar_clienti <= 100 and reducere == "da":
#     print("Vanzare solida, reducerile au dat roade. Ganditi-va la reduceri mai mari.")

# 
# if 50 <= numar_clienti <= 100 and reducere == "nu":
#     print("Vanzare solida, dar se poate imbunatati prin introducerea reducerilor.")

# 
# if numar_clienti < 50 and reducere == "da":
#     print("Vanzare slaba, desi sunt oferite reduceri. Luati in considerare promotii suplimentare.")

# 
# if numar_clienti < 50 and reducere == "nu":
#     print("Vanzare slaba. Introduceti urgent masuri precum reduceri sau oferte speciale.")


# 
# 
# 
# 
# 
# Alex a primit datele despre vânzări pentru ziua de azi și trebuie să verifice dacă vânzările au fost peste medie. Numărul mediu de clienți este 100. /
# Să scriem un program care să permită introducerea numărului de clienți și să afișeze mesajul:

# Dacă numărul de clienți este mai mare de 100, afișează: "Vanzarea este peste medie."
# Dacă numărul de clienți este egal sau mai mic de 100, nu afișează nimic.
# Hint: Să ne amintim că funcția input() întotdeauna returnează un string, așa că va trebui să convertim valoarea în int() înainte de a o folosi în comparație. 
# /De asemenea, să ne gândim la modul în care putem formula corect condiția în instrucțiunea if pentru a verifica dacă numărul este mai mare de 100.

nr_clienti = int(input("Numarul de clienti:"))
if nr_clienti > 100:
    print("Vanzarea este peste medie")
else:
    print("nimic")