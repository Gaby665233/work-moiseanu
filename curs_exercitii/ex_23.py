nume = ['Alex', 'Sara', 'Tom']
for i in nume:
      print(f"Buna, {i}!")




# Alex ajută echipa de vânzări să pregătească o campanie promoțională. Are sarcina de a pregăti /
# mesaje personalizate pentru fiecare client, dar deocamdată fără să folosească bucla for. Cum ar putea să afișeze mesajele /
# personalizate pentru fiecare client din listă?

# Sarcină:

# Să aruncăm o privire asupra listei de clienți pentru care Alex intenționează să pregătească mesajele:

# clienti = ['Sara', 'Tom', 'Lena', 'Max']

# Pentru moment, să încercăm să afișăm mesajul pentru fiecare client în parte, fără a folosi bucla for.

# Stimate [nume client], ne face plăcere să vă oferim o reducere specială la toate produsele săptămâna aceasta!"

# Întrebare pentru reflecție:
# Dacă Alex ar avea 50 sau mai mulți clienți, cât timp i-ar lua să scrie manual mesajele pentru fiecare client? Gândiți-vă cum ar/ 
# putea bucla for să simplifice această sarcină!

clienti = ['Sara', 'Tom', 'Lena', 'Max']

for i in clienti:
      print(f"Stimate {i}, ne face plăcere să vă oferim o reducere specială la toate produsele săptămâna aceasta!")





# Mini activitate: Mesaje promoționale automatizate folosind bucla for

# Acum că Alex a scris manual mesajele pentru fiecare client, și-a dat seama cât de obositor este acest proces atunci când are mulți clienți. /
# Vom descoperi cum îi poate ajuta bucla for să economisească timp și să finalizeze această sarcină mai eficient.

# Sarcină: Vom folosi din nou lista de clienți pe care Alex intenționează să-i contacteze:

# clienți = ['Sara', 'Tom', 'Lena', 'Max']

# Cu ajutorul buclei for, să creăm un cod care va genera și afișa automat un mesaj promoțional pentru fiecare client din listă. Mesajul ar trebui /
# să fie în următorul format:

# Stimate [nume client], suntem încântați să vă oferim o reducere specială la toate produsele în această săptămână!

# Să construim o buclă for care va itera prin lista clienti și va afișa automat un mesaj personalizat pentru fiecare client.

# Întrebare pentru reflecție:

# Cum ar putea Alex să folosească bucla for dacă ar avea mai multe mesaje diferite pentru diferite categorii de clienți? De exemplu, cum ar /
# putea fi adaptat acest cod astfel încât să ofere reduceri diferite în funcție de loialitatea clienților?



clienti = {
    'Sara': 'loial',
    'Tom': 'nou',
    'Lena': 'loial',
    'Max': 'ocazional'
}

for i, categorie in clienti.items():
    if categorie == 'loial':
        reducere = '30%'
    elif categorie == 'nou':
        reducere = '15%'
    else:
        reducere = '10%'

    print(f"Stimate {i}, vă oferim o reducere de {reducere} la toate produsele în această săptămână!")







    #Definim numarul de e-mailuri care trebuie trimis
numar_emailuri = 5

#Bucla for pentru a urmari trimiterea e-mailurilor
for numar in range(1, numar_emailuri + 1):
    print(f"E-mail {numar} a fost trimis clientului.")




# Mini activitate: Calcularea costului total folosind range()

# Alex urmărește costurile campaniei și are o listă de prețuri pentru diferite articole. /
# Scopul său este să calculeze costul total, dar de această dată fără a adăuga manual. Cu ajutorul buclei for și al/
# funcției range(), poate itera rapid prin toate prețurile și calcula suma totală.

# Sarcină: Folosind bucla for și range(), să iterăm prin lista de prețuri și să calculăm costul total. Iată lista de prețuri pe care Alex a adunat-o:

# prețuri = [120.50, 89.99, 45.00, 150.75, 60.00]

# Sarcina noastră este să scriem un cod care va aduna toate prețurile din listă și va afișa costul total.

# Întrebare pentru reflecție:
# Există o altă modalitate de a itera prin listă, fără a folosi range()? Gândiți-vă cum ați putea folosi bucla for direct cu lista, în loc cu indicii ei.


# v1
prețuri = [120.50, 89.99, 45.00, 150.75, 60.00]


for i in range(len(prețuri)):
     print(f"sunt {prețuri[i]}: ")
     suma = sum((prețuri))

print(f"suma este: {suma}")


# v2
prețuri = [120.50, 89.99, 45.00, 150.75, 60.00]
suma = 0

for i in range(len(prețuri)):
     suma = suma + prețuri[i]
     print(suma)

print(f"Suma {suma}")


