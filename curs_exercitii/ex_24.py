#Lista cu statutul de client
# clienti = ['membru', 'nu e membru', 'membru', 'nu e membru', 'membru']

# for status in clienti:
#     if not status == 'membru':  # Verificam daca clientul este membru
#        print("Acest client nu este membru al clubului de loialitate.")
#     else:
#        print("Oferta speciala pentru membrii loiali")


# Mini activitate: Găsirea clienților neloiali

# Alex pregătește o listă de clienți pentru a verifica cine sunt membrii loiali ai clubului și pe cine ar trebui să contacteze cu oferte/
#  promoționale speciale pentru a stimula loialitatea. Lista clienților arată astfel:

# clienti = ["Marco", "Ana", "Lena", "Tom", "Iva"]
# clienti_loiali = ["Ana", "Tom", "Iva"]

# Sarcina: Folosind operatorul not și bucla for, scrieți codul care va afișa un mesaj doar pentru clienții neloiali:

# "Stimate [nume client], avem o oferta speciala pentru dvs. pentru a deveni membru loial!"

# Încercați să scrieți codul singuri!

# Întrebare de reflecție: Cum ar putea Alex să extindă acest cod dacă ar dori să segmenteze suplimentar clienții neloiali /
# în funcție de oferte diferite, pe baza intereselor lor?

clienti = ["Marco", "Ana", "Lena", "Tom", "Iva"]
clienti_loiali = ["Ana", "Tom", "Iva"]

for i in clienti:
    if i in clienti_loiali:
        print(f"Stimate {i}, avem o oferta speciala pentru dvs. pentru a deveni membru loial!")

# v2 cum cere cerinta

clienti = ["Marco", "Ana", "Lena", "Tom", "Iva"]
clienti_loiali = ["Ana", "Tom", "Iva"]

for i in clienti:
    if i not in clienti_loiali:
        print(f"clienti neloiali {i}")
    else:
        print(f"Stimate {i}, avem o oferta speciala pentru dvs. pentru a deveni membru loial!")


# v3

for client in clienti:
    if client in clienti_loiali:
        print(f"{client} este client loial.")
    else:
        print(f"{client} NU este client loial.")




      
      
      