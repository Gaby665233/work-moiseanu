# counter = 0
# while counter < 10:
#     counter = counter + 1
#     print("ass")

baterrie = 50
while baterrie < 100:
    print(f"Bateria este {baterrie}%... Incarcare.")
    baterrie = baterrie + 1
print("Bateria este plina! Opriti incarcatorul.")


alex_suna = 1
while alex_suna < 50:
    print(f"Apelari Alex: {alex_suna}")
    alex_suna = alex_suna + 1
print("A raspuns")

# Alex folosește acum bucla while pentru a urmări numărul de cupoane utilizate pe parcursul campaniei promoționale. /
# Scopul este ca programul să ruleze atâta timp cât numărul de cupoane utilizate nu atinge un anumit prag, să zicem 100. /
# În acest mod, el poate înregistra cu ușurință datele despre promoție.

# Numar maxim predeterminat de cupoane utilizate
numar_maxim_cupoane = 100
 
# Numarul actual de cupoane utilizate
contor_cupoane = 0
 
while contor_cupoane <numar_maxim_cupoane:
     contor_cupoane += 1 # Crestem contorul pentru fiecare cupon folosit
     print(f" Cupon {contor_cupoane} este folosit.")
 
print(f"Numarul total de cupoane utilizate: {contor_cupoane}")




# Mini activitate: Numărătoare inversă până la Black Friday

# Alex lucrează intens la pregătirile pentru Black Friday în compania sa. Pentru a-i reaminti echipei de timpul rămas până la această zi /
# importantă, a decis să creeze un program simplu în Python care să numere zilele rămase până la Black Friday folosind bucla while.

# Sarcină: Să-l ajutăm pe Alex să scrie un program care va număra zilele până la Black Friday, începând de la a 7-a zi. /
# Programul ar trebui să afișeze în fiecare zi câte zile mai sunt rămase, până când numărul zilelor ajunge la zero. Când numărul zilelor ajunge /
# la 0, programul ar trebui să afișeze: "A sosit Black Friday!"

#  Instrucțiuni:

# Setează numărul inițial de zile la 7.
# Cu fiecare execuție a buclei, scade numărul de zile cu una.
# Bucla ar trebui să se oprească atunci când numărul de zile ajunge la 0, cu un mesaj final că Black Friday a sosit.
#  Exemplu de ieșire:

# Mai sunt 7 zile pana la Black Friday!
# Mai sunt 6 zile pana la Black Friday!
# Mai sunt 5 zile pana la Black Friday!
# Mai sunt 4 zile pana la Black Friday!
# Mai sunt 3 zile pana la Black Friday!
# Mai sunt 2 zile pana la Black Friday!
# Mai este 1 zi pana la Black Friday!
# A sosit Black Friday!

# Întrebare pentru reflecție: Să ne gândim cum putem adapta acest program pentru orice altă numărătoare inversă, cum ar fi zilele până la /
# lansarea unui nou produs sau până la o sărbătoare mare.
reducere = 8
while reducere > 0:
    reducere = reducere - 1
    print(f"Mai sunt {reducere} zile pana la Black Friday!")

print("A sosit Black Friday")

