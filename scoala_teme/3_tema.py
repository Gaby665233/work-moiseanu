while True:
    # Verificare număr de produse
    try:
        numar_produse = int(input("Introduceți numărul de produse (1-50): "))
        if numar_produse < 1 or numar_produse > 50:
            print("Eroare: Număr de produse invalid.")
            continue
    except ValueError:
        print("Eroare: Introduceți un număr valid.")
        continue

    # Verificare preț
    try:
        pret = float(input("Introduceți prețul comenzii (mai mare decât 0): "))
        if pret <= 0:
            print("Eroare: Prețul trebuie să fie mai mare decât 0.")
            continue
    except ValueError:
        print("Eroare: Introduceți un preț valid.")
        continue

    # Verificare status plată
    status_plata = input("Introduceți statusul plății (plătit/neplătit/în așteptare): ").lower()

    if status_plata == "plătit":
        # Comanda este validă → ieșim din buclă
        print("\nComandă validată cu succes!")
        print(f"Număr de produse: {numar_produse}, preț: {pret}, status plată: {status_plata}")
        break
    # ori elif status_plata in ["neplătit", "în așteptare"]: 
        # sau asa acelasi lucru status_plata == "neplătit" or status_plata == "în așteptare"

        print("Comanda nu este plătită, nu poate fi procesată.")
        continue
    else:
        print("Eroare: Status de plată necunoscut.")
        continue
