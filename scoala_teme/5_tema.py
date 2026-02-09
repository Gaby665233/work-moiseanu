# Funcție pentru verificarea numelui și prenumelui
def introdu_nume():
    while True:
        nume_complet = input("Introduceți numele și prenumele: ").strip()
        # Verificăm dacă sunt cel puțin două cuvinte
        if len(nume_complet.split()) >= 2:
            nume, prenume = nume_complet.split()[0], " ".join(nume_complet.split()[1:])
            return nume, prenume
        else:
            print("Numele nu a fost introdus corect. Vă rugăm să introduceți numele și prenumele.")

# Funcție pentru determinarea statutului utilizatorului
def determinare_statut(suma_totala, numar_achizitii):
    if suma_totala > 100000 and numar_achizitii > 10:
        return "VIP", 0.10
    else:
        return "STANDARD", 0.05

# Funcție principală
def main():
    # 1. Introducerea numelui și prenumelui
    nume, prenume = introdu_nume()

    # 2. Introducerea numărului de achiziții
    while True:
        try:
            numar_achizitii = int(input(f"Introduceți numărul total de achiziții efectuate de {nume} {prenume} în ultimul an: "))
            if numar_achizitii < 0:
                print("Numărul de achiziții nu poate fi negativ.")
                continue
            break
        except ValueError:
            print("Vă rugăm să introduceți un număr valid.")

    achizitii = []
    # 3. Introducerea sumelor pentru fiecare achiziție
    for i in range(1, numar_achizitii + 1):
        while True:
            try:
                suma = float(input(f"Introduceți suma pentru achiziția {i} (în lei): "))
                if suma < 0:
                    print("Suma nu poate fi negativă.")
                    continue
                achizitii.append(suma)
                break
            except ValueError:
                print("Vă rugăm să introduceți un număr valid.")

    # 4. Calcularea sumei totale
    suma_totala = sum(achizitii)
    # 5. Numărarea achizițiilor cu sumă peste 10.000 lei
    achizitii_peste_10000 = len([s for s in achizitii if s > 10000])

    print(f"\nSuma totală cheltuită: {suma_totala:.2f} lei")
    print(f"Numărul achizițiilor cu sumă peste 10.000 lei: {achizitii_peste_10000}")

    # 6. Determinarea statutului și a reducerii
    statut, reducere = determinare_statut(suma_totala, numar_achizitii)
    print(f"Statutul utilizatorului {nume} {prenume}: {statut}")
    print(f"Reducerea aplicabilă pentru următoarele achiziții: {reducere*100:.0f}%")

    # 7. Calcularea prețului cu reducere pentru o nouă achiziție
    while True:
        try:
            pret_articol = float(input("Introduceți prețul articolului pe care doriți să-l cumpărați: "))
            if pret_articol < 0:
                print("Prețul nu poate fi negativ.")
                continue
            pret_final = pret_articol * (1 - reducere)
            print(f"Prețul articolului cu reducere: {pret_final:.2f} lei")
            break
        except ValueError:
            print("Vă rugăm să introduceți un număr valid.")

# Apelarea funcției principale
if __name__ == "__main__":
    main()
