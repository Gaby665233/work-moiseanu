clienti_preferinte = ['sport', 'tehnologie', 'electrocasnice', 'sport', 'electrocasnice']
preferinta = input("ce preferi:")
for i in clienti_preferinte:
    if preferinta == i:
        if i == 'sport':
            print("Oferta speciala pentru echipament sportiv!")
        elif i == 'electrocasnice':
            print("Oferta speciala pentru electrocasnice!")
        else:
            print("Consultati noile noastre produse!")
        



# Mini activitate: Personalizarea ofertelor pe baza preferințelor

# Alex plănuiește o campanie promoțională și dorește să personalizeze ofertele în funcție de interesele clienților săi. /
# Folosind o buclă for și operatorul elif, să adaptăm mesajele pentru diferite preferințe.

#  Sarcină: Avem o listă de preferințe ale clienților:

# preferinte = ['sport', 'moda', 'tehnologie', 'electrocasnice', 'moda']

# Să scriem un cod care pentru fiecare preferință din listă va afișa mesajul corespunzător:

# Dacă clientului îi place sportul, scriem: "Oferta speciala pentru echipamentul sportiv!"
# Dacă clientului îi place moda, scriem: Cele mai noi colectii la pret redus!"
# Dacă clientului îi plac electrocasnicele, scriem: "Reduceri la electrocasnice care va vor usura viata!"
# Pentru toate celelalte cazuri, scriem: "Vezi ofertele noastre actuale!"
# Să încercăm să scriem codul singuri, apoi să-l testăm și să verificăm dacă funcționează conform așteptărilor.

# Întrebare pentru reflecție: Ce s-ar întâmpla dacă ați schimba ordinea condițiilor elif? Gândiți-vă la modul în care /
# ordinea condițiilor poate influența rezultatul, în special atunci când aveți preferințe sau categorii similare care se suprapun.

preferinte = ["sport", "moda", "tehnologie", "electrocasnice", "moda"]


prefera = input("ce iti place :sport', 'moda', 'tehnologie', 'electrocasnice:").lower()
for i in preferinte:
    if prefera == i :
        if i == "sport":
            print("Oferta speciala pentru echipamentul sportiv!")
        elif i == "moda":
            print("Cele mai noi colectii la pret redus!")
        elif i == "electrocasnice":
            print("Reduceri la electrocasnice care va vor usura viata!")
        else:
            print("Vezi ofertele noastre actuale!")




# asa este gresit pentru ca se repeta dar prost
# preferinte = ["sport", "moda", "tehnologie", "electrocasnice", "moda"]

# while True:
#     prefera = input("ce iti place :sport', 'moda', 'tehnologie', 'electrocasnice:").lower()
#     for i in preferinte:
#         if prefera == i :
#             if i == "sport":
#                 print("Oferta speciala pentru echipamentul sportiv!")
#             elif i == "moda":
#                 print("Cele mai noi colectii la pret redus!")
#             elif i == "electrocasnice":
#                 print("Reduceri la electrocasnice care va vor usura viata!")
#             else:
#                 print("Vezi ofertele noastre actuale!")
#             break
#         else:
#             print("nu se stie")
            









# sa se repede daca scriem altceva si este corect
preferinte = ["sport", "moda", "tehnologie", "electrocasnice"]

# cerem input până când este valid
while True:
    prefera = input("Ce iti place (sport, moda, tehnologie, electrocasnice): ").lower()
    
    if prefera in preferinte:
        if prefera == "sport":
            print("Oferta speciala pentru echipamentul sportiv!")
        elif prefera == "moda":
            print("Cele mai noi colectii la pret redus!")
        elif prefera == "electrocasnice":
            print("Reduceri la electrocasnice care va vor usura viata!")
        else:  # tehnologie sau orice altceva valid
            print("Vezi ofertele noastre actuale!")
        break  # iesim din bucla când inputul este valid
    else:
        print("Preferinta introdusa nu este valida. Te rog incearca din nou.")
