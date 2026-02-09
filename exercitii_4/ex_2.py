# Creează un program Python care:

# Permite introducerea unor texte de la tastatură.

# Folosește o funcție care numără cifrele (0–9) din text.

# După fiecare introducere, programul afișează numărul de cifre.

# Programul continuă să ruleze până când utilizatorul introduce un text care nu conține nicio cifră.

# Când nu există cifre, programul se oprește.

# 🔧 Indicii (ca să-l faci singur)

# Scrie o funcție care:

# primește un text

# folosește un contor

# parcurge fiecare caracter cu for

# verifică dacă este cifră

# Poți folosi:

# caracter.isdigit()


# Folosește o buclă while.

# Folosește if și break.


def numara_cifre(cifre):
    contor = 0

    for caracter in cifre:
         if caracter in "0123456789":
          contor += 1
    
    return contor



while True:
        cifre = input("introduceti textul: ")
        numar_cifre = numara_cifre(cifre)
        print(f"numarul de cifre {numar_cifre}")


        if numar_cifre == 0:
            print("textul nu contine cifre")
            break

        

