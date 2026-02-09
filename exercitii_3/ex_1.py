# Programul cere vârsta utilizatorului.

# Vârsta trebuie să fie între 18 și 65.

# Altfel → „Eroare: Vârstă invalidă.”

# Programul cere salariul.

# Salariul trebuie să fie mai mare de 2000.

# Altfel → „Eroare: Salariu prea mic.”

# Programul cere statusul angajării: „angajat”, „șomer”.

# Dacă este „angajat” → se acceptă.

# Dacă este „șomer” → „Persoană neeligibilă”.

# Altceva → „Status necunoscut”.

# ✅ Programul se oprește doar când toate datele sunt corecte.

while True:
    try:
        varsta = int(input("introduceti varsta (18-65): "))
        if varsta < 18 or varsta > 65:
            print("eroare:vasta invalida")
            continue
    except ValueError:
        print("eroare:intordu un numar")
        continue
    try:
        salariu = float(input("introduceti salariu (peste 2000)"))
        if salariu <= 2000:
            print("Eroare:salariu prea mic")
            continue
    except ValueError:
        print("eroare:Introdu un salariu valid")
        continue

    status = input("status angajare: ").lower()


    if status == "angajat":
        print("persoana accepatata")
        break
    elif status == "somer":
        print("trebuie sa te angajezi")
        continue
    else:
        print("status necunoscut")
        continue

    
