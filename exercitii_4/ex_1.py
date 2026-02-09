# Creează un program Python care:

# Permite introducerea unor cuvinte de la tastatură.

# Folosește o funcție care numără consoanele din cuvânt.

# După fiecare introducere, programul afișează numărul de consoane.

# Programul continuă să ruleze până când utilizatorul introduce un cuvânt care nu conține nicio consoană.

# Când nu există consoane, programul se oprește.

# 🔧 Instrucțiuni (ghidare, nu soluție)

# Scrie o funcție care:

# primește un cuvânt

# folosește un contor

# parcurge fiecare caracter cu for

# verifică dacă este literă

# verifică dacă NU este vocală

# Vocalele sunt: a, e, i, o, u (mari și mici)

# Folosește o buclă while.

# Folosește if și break.


def numara_consoane(cuvant):
    vocale = ["a", "e", "i", "o", "u" , "A", "E", "I", "O", "U",]
    contor = 0


    for caracter in cuvant:
        if caracter.isalpha() and caracter not in vocale:
            contor += 1
    return contor

while True:
    cuvant = input("intorduceti un cuvant: ")
    numar_consoana = numara_consoane(cuvant)
    print(f"numarul de consoane: {numar_consoana}")


    if numar_consoana == 0:
        print("nu ai nicio consoana")
        break




