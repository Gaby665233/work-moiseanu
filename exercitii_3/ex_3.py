# Programul verifică logarea unui utilizator.

# Cerințe:

# Nume utilizator: minim 3 caractere.

# Parolă: minim 6 caractere.

# Status cont: „activ”, „blocat”

# Dacă este „activ” → acces permis.

# Dacă este „blocat” → acces respins.

# Programul se repetă până la date corecte.

while True:
    try:
        logare = (input(" nume utilizator: "))
        if len(logare) <= 3:
            print("numele trebuie sa fie mai lung")
            continue
    except ValueError:
        print("introdu un nume")
        continue

    parola = input("introdu parola: ")
    if len(parola) < 6:
        print("parola prea scurta: ")
        continue

    status = input("Status cont: ")
    if status == "activ":
        print("\nActivat cu succes")
        print(f"Nume untilizator: {logare}, Parola: {parola}, Status: {status}")
        break
    elif status == "blocat":
        print("Acces respins: ")
        continue
    else:
        print("nu te pricepi")


