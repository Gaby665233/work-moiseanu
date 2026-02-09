# Mini activitate: Recomandarea încălțămintei în funcție de condițiile meteorologice

# Alex a extins programul său astfel încât, pe lângă recomandările pentru condițiile meteorologice, /
# acum să includă și sugestii pentru încălțăminte adecvată în funcție de vreme. Vrem să scriem o funcție /
# care recomandă tipul de încălțăminte pe baza condițiilor meteorologice introduse.

#  Sarcină: Scrieți o funcție numită recomanda_incaltaminte, care, pe baza condițiilor meteorologice (soare, ploaie, zăpadă),/
#  va returna o recomandare pentru încălțăminte. De exemplu, dacă vremea este „ploaie”, funcția ar trebui să recomande cizme din cauciuc.

#  Exemplu de condiții meteorologice și încălțăminte recomandată:
# „soare”: „Purtati sandale usoare.”
# „ploaie”: „Recomandam cizme din cauciuc.”
# „zapada”: „Incaltati-va cu cizme calduroase.”
# „alte conditii: „Purtati adidasi confortabili.”
# Întrebare pentru reflecție: Cum am putea adapta funcția dacă dorim ca Alex să ofere recomandări pentru diferite tipuri de încălțăminte în /
# funcție de intensitatea ploii? De exemplu, o ploaie ușoară ar putea necesita doar adidași impermeabili, în timp ce o ploaie puternică ar necesita /
# cizme din cauciuc.


# def vremea(meteo):
#     if meteo == "soare":
#         return "Purtati sandale usoare."
#     elif meteo == "ploaie":
#         return "Recomandam cizme din cauciuc."
#     elif meteo == "zapada":
#         return "Incaltati-va cu cizme calduroase."
#     else:
#         return "Purtati adidasi confortabili."
    
# while True:
#     vremea_curenta = input("Introduceti vremea de azi: soare/ploaie/zapada: ")
#     rezultat = vremea(vremea_curenta)
#     print(rezultat)

# v2 sa se opreasca

# def vremea(meteo):
#     if meteo == "soare":
#         return "Purtati sandale usoare."
#     elif meteo == "ploaie":
#         return "Recomandam cizme din cauciuc."
#     elif meteo == "zapada":
#         return "Incaltati-va cu cizme calduroase."
#     else:
#         return None
    
# while True:
#     vremea_curenta = input("Introduceti vremea de azi: soare/ploaie/zapada: ").lower()
#     rezultat = vremea(vremea_curenta)
    

#     if rezultat is None:
#         print("Programul se opreste")
#         break
    
#     print(rezultat)


# Mini activitate: Monitorizarea timpului petrecut la sarcini

# Alex dorește să-și îmbunătățească productivitatea și începe să monitorizeze cât timp petrece la diferite sarcini pe parcursul zilei. \
# Această analiză îl va ajuta să gestioneze mai bine timpul și să identifice sarcinile care îi consumă cel mai mult timp. Planifică să \
# creeze o funcție care primește o listă cu durata fiecărei sarcini și la final afișează cât timp a petrecut în total la toate sarcinile.

# Sarcină: Să scriem o funcție numită total_timp care:

# va primi o listă cu orele petrecute la diferite sarcini;
# va utiliza o buclă for pentru a aduna timpul total petrecut la sarcini;
# va face funcția să returneze un mesaj cu numărul total de ore petrecute la sarcini.
# Întrebare pentru reflecție: Cum ar putea Alex să adapteze această funcție astfel încât să afișeze un mesaj în care compară timpul total \
# cu obiectivul de 8 ore? Gândiți-vă la adăugarea unei condiții suplimentare care va permite funcției să afișeze un mesaj despre faptul \
# dacă obiectivul zilnic a fost depășit sau nu.

lista = [4, 5, 9, 1, 2, 2]


def numar(ore):
    total = 0
    for i in ore:
        total = total + i
    return (f"Numarul de ore petrecut este de {total}")

mesaj = numar(lista)
print(mesaj)


    