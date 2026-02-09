# meteo = "ploaie"
# temperatura = 10  # In grade Celsius

# if meteo == "ploaie":
#     print("Ia-ti umbrela!")

#     if temperatura < 15:
#         print("Imbraca o geaca, e frig!")
#     else:
#         print("Ploua, dar este cald, nu ai nevoie de geaca.")

# else:
#     if meteo == "soare":
#         if temperatura > 25:
#             print("Pune-ti ochelari de soare si imbraca-te mai lejer!")
#         else:
#             print("Bucura-te de soare, dar imbraca-te confortabil!")
#     else:
#         print("Este innorat, nu ai nevoie de nimic special.")

# Deși codul funcționează corect, Alex și-a dat seama că aceste condiții simple ar fi putut fi scrise într-un mod mai concis./
# Acest lucru este deosebit de important în munca sa, unde analizează frecvent cantități mari de date și trebuie să ia rapid decizii /
# bazate pe aceste analize. Fiecare linie de cod este prețioasă, iar scurtarea codului poate accelera semnificativ procesul.

# Atunci a descoperit operatorul ternar – un instrument care îi permite să ia decizii rapide într-o singură linie de cod. În loc de blocuri/
# lungi if-else, acum poate verifica și executa decizii într-o singură linie, ceea ce este perfect pentru situații simple, cum ar fi recomandările de /
# îmbrăcăminte. De exemplu, în loc de această parte a codului care verifică dacă temperatura este sub 15 grade, ar putea folosi operatorul ternar pentru a scrie /
# decizia într-o singură linie:

# print("Imbraca o geaca, e frig!") if temperatura < 15 else print("Ploua, dar este cald, nu ai nevoie de geaca.")









# Mini activitate: Să reformulăm codul folosind operatorul ternar

# Alex a folosit structura clasică if-else pentru a decide dacă utilizatorul ar trebui să primească o reducere sau nu, /
# pe baza statutului de membru al programului de loialitate. Sarcina noastră este să reformulăm acest cod folosind operatorul ternar.

# Codul original:

# stare = "membru"
# if stare == "membru":
#     reducere = 10
# else:
#     reducere = 0
# print(f"Reducerea este {reducere}%")

# Sarcină: Să reformulăm acest cod folosind operatorul ternar.

# Hint: Să ne amintim că operatorul ternar folosește următoarea structură: <actiune_daca_adevarat> if <conditie> else <actiune_daca_fals>


stare = "membru"
reducere = 10 if stare else  0
print(f"Reducerea este {reducere}%")



# age = 20
# if age >= 18:
#     status = "Major"
# else:
#     status = "Minor"
# print(status)

# Totuși, cu ajutorul operatorului ternar, Alex poate scurta codul și accelera procesul de decizie:

# age = 20
# status = "Major" if age >= 18 else "Minor"
# print(status)




# count = 15
# if count == 1:
#     word = "produs"
# else:
#     word = "produse"
# print(f"In stoc: {count} {word}")

# Însă acum folosește operatorul ternar pentru a scurta această verificare simplă:

# count = 15
# word = "produs" if count == 1 else "produse"
# print(f"In stoc: {count} {word}")




# suma = 120
# if suma > 100:
#     reducere = "Reducere aprobata!"
# else:
#     reducere = "Fara reducere."
# print(reducere)

# Acum, cu ajutorul operatorului ternar, poate accelera procesul de decizie:

# suma = 120
# reducere = "Reducere aprobata!" if suma > 100 else "Fara reducere."
# print(reducere)