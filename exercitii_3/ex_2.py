# EXERCIȚIUL 2 – Validarea unei rezervări la hotel

# Programul verifică o rezervare.

# Cerințe:

# Număr de nopți: între 1 și 30.

# Preț pe noapte: mai mare decât 0.

# Status rezervare: „confirmată”, „anulată”, „în așteptare”

# Doar dacă este „confirmată” se afișează rezervarea.

# Altfel → rezervarea nu este validă.

#
# 
# 
# 
# 
#  while True:
#     try:
#         nopti = int(input("introduceti numarul de nopti: intre 1 si 30: "))
#         if nopti < 1 or nopti > 30:
#             print("introdu intre 1 si 30: ")
#             continue
#     except ValueError:
#         print("introdu un numar valit")
#         continue
#     try:
#         pret = float(input("pret pe noapte: "))
#         if pret <= 0:
#             print("pret prea mic")
#     except ValueError:
#         print("introdu o cifra")
#         continue
#     status = (input("status rezervare: ")).lower()

#     if status == "confirmata":
#         print("\nRezevare cu succes")
#         print(f"numar de norpti: {nopti},Pret: {pret} si status rezervare: {status}" )
#         break
#     elif status in [ "anulat", "in asteptare"]:
#         print("comanda nu este platita")
#         continue
#     else:
#         print("status necunoscut")
#         continue
            


# Varianta cu orice modolitate de a scrie(diactritice sau fara, litere mari sau mici)

import unicodedata
def normalizare(text):
    text = text.lower()
    text = unicodedata.normalize('NFD', text)
    text = ''.join(ch for ch in text if unicodedata.category(ch) != 'Mn')
    return(text)





while True:
    try:
        nopti = int(input("introduceti numarul de nopti: intre 1 si 30: "))
        if nopti < 1 or nopti > 30:
            print("introdu intre 1 si 30: ")
            continue
    except ValueError:
        print("introdu un numar valit")
        continue
    try:
        pret = float(input("pret pe noapte: "))
        if pret <= 0:
            print("pret prea mic")
    except ValueError:
        print("introdu o cifra")
        continue
    status = (input("status rezervare: "))
    status_normalizare = normalizare(status)

    if status_normalizare == "confirmata":
        print("\nRezevare cu succes")
        print(f"numar de norpti: {nopti},Pret: {pret} si status rezervare: {status}" )
        break
    elif status_normalizare in [ "anulat", "anulata", "in asteptare"]:
        print("comanda nu este platita")
        continue
    else:
        print("status necunoscut")
        continue