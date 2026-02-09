# Mini activitate: Extrageți părți din numele vostru

#  Să încercăm să ne jucăm cu numele noastre. Să scriem un program în care:

# Definim o variabilă string care conține numele nostru complet.
# Afișăm doar inițialele.
# Afișăm ultimele trei caractere ale numelui nostru.
# Întrebare pentru reflecție: Cum am putea extinde această sarcină pentru situația în care apar litere de/
#  mijloc în nume? Gândiți-vă cum puteți folosi tăierea pentru a afișa prima literă din fiecare parte a numelui.


nume = "Moiseanu Gabriel Alexandru"
parti = nume.split()
initiale = ""

for i in parti:
    initiale += i[0] + " "
print("initiale", initiale )
print("ultimle 3:",nume[-3:])



ass = "sasung, peleso, piula"

lista = ass.split(", ")
for i in lista:
    print(i)

# v2 cu virgula

ass = "sasung, peleso, piula"

lista = ass.split()
for i in lista:
    print(i)



mesaj = "Astazi este o zi minunata"
cuvinte = mesaj.split()
print(cuvinte)



salut = " Bine ati venit la curs "

print(salut.upper())  # Afiseaza: 'BINE ATI VENIT LA CURS'
print(salut.lower())  # Afiseaza: 'bine ati venit la curs'
print(salut.strip())  # Elimina toate spatiile goale de la inceputul si sfarsitul stringului

# Mini activitate

# Sarcină: Transformați stringul „ Bună tuturor! ” astfel încât să fie scris cu majuscule și fără spații.

saluta = " Bună tuturor! " 
rezultat = saluta.upper().replace(" ", "")
print(rezultat)



mesaj = "Bine ati venit la cursul de programare!"
pozitie = mesaj.find("curs")
print(f"Cuvantul 'curs' incepe din pozitia {pozitie}.")



# Mini activitate

# Sarcină: Găsiți cuvântul „sarcină” în textul „Aceasta este o sarcină pentru exersare” și înlocuiți-l cu „activitate”.

mesaj = "Aceasta este o sarcina pentru exersare"
pozitie = mesaj.replace("sarcina", "activitate")
print(pozitie)





# Mini activitate

# Sarcină: Creați propoziția „Python-este-interesant” utilizând o listă de cuvinte și metoda join().


p = "Python", "este", "interesant"
mesaj = "-".join(p)
print(mesaj)



text = "Python este interesant si Python este popular."
numar_repetari = text.count("Python")
lungime = len(text)
print(f"Cuvantul 'Python' apare de {numar_repetari} ori.")
print(f"Lungimea textului este de {lungime} caractere.")

# Sarcină: Calculați de câte ori apare cuvântul „este” în propoziția „Python este interesant și este popular.”

text = "Python este interesant și este popular." 
numar = text.count("este")
print(f"cuvantul este apare de {numar} ori")