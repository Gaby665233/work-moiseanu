# meteo = "ploaie"
# temperatura = 10  # In grade Celsius
# if meteo == "ploaie":
#     print("Ia-ti umbrela!")
#     if temperatura < 15:
#         print("Imbraca o geaca, e frig!")
#     else:
#         print("Ploua, dar e cald, nu ai nevoie de geaca.")
# else:
#     if meteo == "soare":
#         if temperatura > 25:
#             print("Pune-ti ochelari de soare si imbraca-te mai lejer!")
#         else:
#             print("Bucura-te de soare, dar imbraca-te confortabil!")
#     else:
#         print("Este innorat, nu ai nevoie de nimic special.")


# Mini activitate: Modificarea codului cu operatori logici

# Alex a scris deja un program care folosește structuri if imbricate pentru a recomanda ce să ia în funcție /
# de condițiile meteorologice și de temperatură. Acum, sarcina noastră este să simplificăm acest cod, evitând abordarea imbricată și, /
# în schimb, folosind structura if-elif și operatorii logici precum and.

# Sarcină: Modificați codul prezentat anterior, evitând structurile if imbricate. /
# În schimb, folosiți structura if-elif cu operatorul logic and, pentru a verifica atât condițiile meteorologice, /
# cât și temperatura într-o singură linie.

# Hint: Condițiile precum acestea pot fi scrise împreună:

# if meteo == "ploaie" and temperatura < 15:
meteo = input("Cum este azi: ploaie/soare: ")
temperatura = int(input("Cate grade sunt: "))

if meteo == "ploaie" and temperatura < 15:
     print("Ia-ti umbrela!")
elif meteo == "soare" and temperatura > 25:
     print("Pune-ti ochelari de soare si imbraca-te mai lejer")
else:
     print("nu ai nevoie de nimic special")
     
        
     
 