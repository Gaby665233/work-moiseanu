# Definirea listei de clienti si a statutului lor de membru
clienti = ['Ana', 'Marco', 'Ivana', 'Lena']
club_premium = ['Ana']
club_loial = ['Ana', 'Marco', 'Ivana']

# Parcurgerea tuturor clientilor
for client in clienti:
    if client in club_premium:
        print(f"Stimate {client}, aveti acces exclusiv la oferta premium!")
    elif client in club_loial:
        print(f"Draga {client}, va multumim ca sunteti client loial! Avem o oferta speciala pentru dumneavoastra.")
    elif not client in club_loial:
        print(f"Stimate {client}, deveniti membru loial si bucurati-va de beneficii!")





# Mini activitate: Segmentarea clienților pe baza mai multor criterii

# Alex trebuie acum să creeze o campanie detaliată, care va oferi diferite beneficii în funcție de statutul de membru al clienților. /
# La dispoziția sa se află o listă cu toți clienții, o listă cu membrii fideli și o listă cu membrii premium. Unii clienți nu sunt membri ai /
# niciunui club. Vom folosi bucla for în combinație cu operatorii elif, not și in pentru a determina care clienți primesc anumite beneficii.

# Sarcină: Utilizăm următoarele liste pentru segmentarea clienților și pentru a afișa mesajul corespunzător:

# clienti = ['Sara', 'Tom', 'Lena', 'Marco', 'Ana']
# club_loial = ['Tom', 'Lena', 'Ana']
# club_premium = ['Ana']

# Pe baza acestor liste, pentru fiecare client, să afișăm un mesaj:

# Dacă clientul este membru al clubului premium, mesajul ar trebui să fie:
# "Stimate [nume client], aveti acces exclusiv la oferta noastra premium!"
# Dacă clientul este membru al clubului loial, dar nu este membru premium, mesajul ar trebui să fie:
# "Draga [nume client], va multumim pentru loialitate! Va asteapta o oferta speciala."
# Dacă clientul nu este nici în clubul loial, nici în cel premium, mesajul ar trebui să fie:
# "Stimate [nume client], alaturati-va clubului nostru si bucurati-va de beneficii!"
# Întrebare pentru reflecție: Cum am putea extinde codul pentru a segmenta clienții și după criterii suplimentare, cum ar /
# fi locația sau achizițiile anterioare? Gândiți-vă cum ar putea fi utilizată s

clienti = ['Sara', 'Tom', 'Lena', 'Marco', 'Ana']
club_loial = ['Tom', 'Lena', 'Ana']
club_premium = ['Ana']

for i in clienti:
    if i in club_premium:
        print(f"Stimate ,{i} aveti acces exclusiv la oferta noastra premium!")
    elif i in club_loial:
        print(f"Draga {i}, va multumim pentru loialitate! Va asteapta o oferta speciala.")
    if not i in club_loial:
        print(f"Stimate {i}, alaturati-va clubului nostru si bucurati-va de beneficii!")
