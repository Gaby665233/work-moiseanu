# EXERCIȚIUL 4 – Validarea unui bilet de tren

# Număr de locuri: între 1 și 6

# Preț total: > 0

# Tip bilet: „întreg”, „student”, „pensionar”

# Dacă tipul este valid → afișează biletul
# Altul → „Tip de bilet invalid”

import unicodedata
def normalizare(text):
    text = text.lower()
    text = unicodedata.normalize("NFD", text)
    text = "".join(ch for ch in text if unicodedata.category(ch) != "Mn")
    return(text)

while True:
    try:
        locuri = int(input("introdu numarul de locuri (1-6):"))
        if locuri < 1 or locuri > 6:
            print("numar de locuri invalit")
            continue
    except ValueError:
        print("numar invalit")
        continue

    try:
      pret = float(input(" introduceti pretul: "))
      if pret <= 0:
         print("introdu un pret mai mare: ")
    except ValueError:
        print("introdu un pret")
        continue

    status = input("tipul biletului: intreg, Student, Pensionar: ")
    status_normalize = normalizare(status)

    if status_normalize in ["intreg", "student", "pensionar"]:
        print("bilet valit")
        print(f"numar de locuri{locuri}, pret{pret}, Tip bilet{status}")
        break
    else:
        print("bilet invalit")
        continue


# se repede doar ce gresesti

while True:
    try:
        locuri = int(input("Număr de locuri (1-6): "))
        if locuri < 1 or locuri > 6:
            print("Număr de locuri invalid.")
            continue
    except ValueError:
        print("Introduceți un număr valid.")
        continue

    # BUCLE SEPARATE pentru PREȚ
    while True:
        try:
            pret = float(input("Preț total: "))
            if pret <= 0:
                print("Preț invalid.")
                continue   # repetă doar pretul
            break          # preț corect → ieșim din bucla interioară
        except ValueError:
            print("Introduceți un preț valid.")
            continue

    tip = input("Tip bilet (întreg/student/pensionar): ").lower()

    if tip in ["întreg", "student", "pensionar"]:
        print("Bilet valid!")
        print(f"numar de locuri{locuri}, pret{pret}, Tip bilet{tip}")
        break
    else:
        print("Tip de bilet invalid.")
        continue

    

      

