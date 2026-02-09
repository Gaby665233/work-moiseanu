# EXERCIȚIU BONUS – Notare elev

# Nota: între 1 și 10

# Prezență: „da” / „nu”

# Dacă nota ≥ 5 și prezența = „da” → promovat

# Altfel → respins

while True:
    try:
        notare = int(input("introduceti nota: "))
        if notare < 1 or notare > 10:
            print("nu ai introdus corect")
            continue
    except ValueError:
        print("introdu o cifra")
        continue

    
    prezentare = input("inroduceti prezenta: da/nu: ")

    if notare >= 5 and prezentare =="da":
        print("ai trecut")
        print(f"nota:{notare}, prezenta: {prezentare}")
        break
    else:
        print("respins")
        break