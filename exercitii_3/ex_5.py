# EXERCIȚIUL 5 – Comandă într-un magazin online

# Cantitate produse: 1–100

# Valoare comandă: > 50 lei

# Metodă plată: „card”, „cash”, „ramburs”

# Dacă metoda este validă → afișează comanda
# Altul → eroare

import unicodedata
def normalizare(text):
    text = text.lower()
    text = unicodedata.normalize("NFD", text)
    text = "".join(ch for ch in text if unicodedata.category(ch) != "Mn" )
    return(text)

while True:


    while True:
        try:
            cantitate = int(input("introduceti cantitatea de produse: intre 1-100"))
            if cantitate < 1 or cantitate > 100:
                print("cantitate invalida")
                continue
            break
        except ValueError:
            print("introdu o cantitate valita")
            continue


    while True:
        try:
            valoare = int(input("introdu valoarea comenzii: "))
            if valoare < 50:
                print("valoarea prea mica")
                continue
            break
        except ValueError:
            print("introdu o cifra")
            continue


    plata = input("intorduceti metoda de plata: ")
    plata_normalize = normalizare(plata)

    if plata_normalize in ["card", "cash", "ramburs"]:
        print("\ncomanda valida")
        print(f"cantitate: {cantitate}, Pret: {valoare}, Plata: {plata}")
        break
    else:
        print("eroare")

