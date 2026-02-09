# Să ne imaginăm că Alex vrea să monitorizeze o promoție care are o condiție specială: dacă rămân mai puțin de 5 cupoane, /
# promoția se oprește temporar și se oferă un avertisment. Acest lucru îl putem face folosind condiția if în cadrul buclei while.

# Numarul maxim de cupoane si durata promotiei
max_cupoane = 100
durata_timp = 7

# Starea curenta
cupoane_utilizate = 0
zile_ramase = durata_timp

while (cupoane_utilizate < max_cupoane) and (zile_ramase > 0):
    cupoane_utilizate += 15
    zile_ramase -= 1

         # Conditie suplimentara de avertizare
    if max_cupoane - cupoane_utilizate < 5:
        print("Avertisment: Au ramas mai putin de 5 cupoane!")

    print(f"Cupoane folosite: {cupoane_utilizate}, Zile ramase: {zile_ramase}")

print("Promotia s-a incheiat.")





# Mini activitate: Monitorizarea stării comenzilor cu Alex

# Alex lucrează la urmărirea stării comenzilor online pentru compania sa. Pentru a se asigura că toate comenzile sunt procesate la timp, /
# trebuie să monitorizeze starea stocurilor de produse și timpul rămas până la termenul de livrare. Comenzile sunt procesate atât timp cât /
# inventarul este suficient și până când timpul nu expiră.

#  Sarcină: Creați o buclă while cu condiții if și operatori logici care:

# monitorizează numărul de articole rămase în stoc,
# afișează un avertisment atunci când stocul atinge un nivel critic scăzut (de exemplu, mai puțin de 10 articole),
# bucla se oprește când stocul scade sub nivelul critic sau când expiră timpul de livrare (de exemplu, 8 ore).
#  Instrucțiuni:

# definiți numărul inițial de articole (de exemplu, 50) și termenul de livrare (de exemplu, 8 ore),
# folosiți o buclă while cu operatorul or pentru a monitoriza inventarul și timpul de livrare,
# în cadrul buclei, folosiți condiția if pentru a afișa un avertisment atunci când stocul scade sub 10 articole.
# Notă: Putem adăuga condiții suplimentare dacă dorim să testăm cum ar reacționa Alex la schimbările din stocuri în timp real.

#  Exemplu de ieșire:

# „Avertisment: Nivel critic scazut al stocului!”
# „Termenul de livrare a expirat – comenzile sunt inchise.”

# Prin această exercițiu, veți explora cum se gestionează resursele în timpul procesului de comandă și cum puteți utiliza o buclă while/
#  cu condiții if pentru a monitoriza multiple condiții în contextul de afaceri real.

stoc = 200
timp_ramas = int(input("Itrodu timpul ramas: "))
critic = 10
vertisment_afisat = False

while True:
    stoc = stoc -7
    timp_ramas =  timp_ramas - 1

    if stoc < critic and not vertisment_afisat:
        print("a ajuns la critic")
        vertisment_afisat = True
        # Cu print aici este negatic pt ca se scade apoi printeaza
    print(f"timp ramas {timp_ramas} ore si stocul de {stoc}: ")

    if stoc <= 0 or timp_ramas <= 0:
        print("Termenul de livrare a expirat")
        break
#  aici se opreste la ultima cifra pozitiva pt ca se aplica si ultima conditie

   


stoc = 200
timp_ramas = int(input("Introdu timpul ramas: "))
critic = 10
avertisment_afisat = False

while True:
    stoc -= 7
    timp_ramas -= 1

    # Oprirea buclei înainte să afișeze valori negative
    if stoc <= 0 or timp_ramas <= 0:
        print("Termenul de livrare a expirat")
        break

    # Afișarea avertismentului doar o dată
    if stoc < critic and not avertisment_afisat:
        print("A ajuns la critic")
        avertisment_afisat = True

    # Afișăm doar valori pozitive
    print(f"Timp ramas {timp_ramas} ore si stocul de {stoc}")




    #  Mini activitate: Monitorizarea stării comenzilor cu Alex

# Alex lucrează la urmărirea stării comenzilor online pentru compania sa. Pentru a se asigura că toate comenzile sunt procesate la timp, /
# trebuie să monitorizeze starea stocurilor de produse și timpul rămas până la termenul de livrare. Comenzile sunt procesate atât timp cât /
# inventarul este suficient și până când timpul nu expiră.

#  Sarcină: Creați o buclă while cu condiții if și operatori logici care:

# monitorizează numărul de articole rămase în stoc,
# afișează un avertisment atunci când stocul atinge un nivel critic scăzut (de exemplu, mai puțin de 10 articole),
# bucla se oprește când stocul scade sub nivelul critic sau când expiră timpul de livrare (de exemplu, 8 ore).
#  Instrucțiuni:

# definiți numărul inițial de articole (de exemplu, 50) și termenul de livrare (de exemplu, 8 ore),
# folosiți o buclă while cu operatorul or pentru a monitoriza inventarul și timpul de livrare,
# în cadrul buclei, folosiți condiția if pentru a afișa un avertisment atunci când stocul scade sub 10 articole.
# Notă: Putem adăuga condiții suplimentare dacă dorim să testăm cum ar reacționa Alex la schimbările din stocuri în timp real.

#  Exemplu de ieșire:

# „Avertisment: Nivel critic scazut al stocului!”
# „Termenul de livrare a expirat – comenzile sunt inchise.”

# Prin această exercițiu, veți explora cum se gestionează resursele în timpul procesului de comandă și cum puteți utiliza o buclă while/
#  cu condiții if pentru a monitoriza multiple condiții în contextul de afaceri real.

stocuri = 200
timpul = 30
critic = 10
avertisment_afisat = False

while True:
    stocuri = stocuri -7
    timpul = timpul - 1
    if stocuri <= 0 or timpul <= 0:
        print("inventarul s a oprit")
        break
    if stocuri < critic and not avertisment_afisat:

        print(f"ai scazut sub {stocuri}: ")
        avertisment_afisat = True

    
    print(f"Stocuri ramase {stocuri} si timpul ramas {timpul}: ")
