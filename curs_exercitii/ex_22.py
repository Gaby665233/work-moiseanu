# Regula de aur (ține-o minte!)

# 🔑 Dacă variabila măsoară „ce s-a consumat / ce a trecut” → crește (+=)
# 🔑 Dacă variabila măsoară „ce a rămas / ce mai există” → scade (-=)


# max_cupoane = 100
# durata_timp = 7
# # Starea curenta
# cupoane_utilizate = 0
# zile_ramase = durata_timp

# while (cupoane_utilizate < max_cupoane) and (zile_ramase > 0):
#     # Simuleaza utilizarea cupoanelor si trecerea timpului
#     cupoane_utilizate += 10
#     zile_ramase -= 1
#     print(f"Cupoane utilizate: {cupoane_utilizate}, Zile ramase: {zile_ramase}")
# print("Promotia a fost finalizata.")



# Alex trebuie să urmărească o promoție care se încheie atunci când se consumă 40 de cupoane sau când rămân mai puțin de/
#  3 zile până la finalul promoției.

#  Sarcina:

# Definiți variabilele pentru numărul maxim de cupoane și durata inițială a promoției.
# Stabiliți bucla while cu operatorul or care controlează cele două condiții: numărul de cupoane utilizate și numărul de zile rămase.
# În interiorul buclei, simulați utilizarea unui anumit număr de cupoane și reducerea zilelor rămase.
# În fiecare pas, afișați starea promoției și opriți bucla atunci când se îndeplinește oricare dintre condiții.
# Întrebare de reflecție:

# Ar dura promoția mai mult sau mai puțin decât în exemplul cu operatorul and ? Să ne gândim cum se diferențiază operatorul /
# or în contextul controlului fluxului buclei.

# nr_max_cupoane = 40
# durata_initiala = 0
# zile = 8
# while durata_initiala <= 40 or zile >= 3:
#     durata_initiala = durata_initiala + 10
#     zile = zile - 1
#     print(f"Cupoane utilizate: {durata_initiala} si zile ramase {zile}: ")
#     if durata_initiala >= 40 or zile <= 3:
#         print("promotia s a incheiat")
#         break



# Definește variabilele:
# Un magazin online trebuie să urmărească o ofertă specială care se încheie când stocul ajunge la 0 /
# produse sau când au trecut mai mult de 7 zile de la lansarea ofertei.

# numărul inițial de produse din stoc

# numărul maxim de zile ale ofertei

# Creează o buclă while care:

# rulează cât timp mai există produse în stoc SAU nu s-au depășit 7 zile

# folosește operatorul or

# În interiorul buclei:

# scade numărul de produse (simulează vânzări)

# crește numărul de zile trecute

# afișează starea ofertei

# Oprește bucla atunci când:

# stocul ajunge la 0 sau

# au trecut mai mult de 7 zile

# stocul = 60
# nr_max_zile_oferta = 7
# durata = 0
# while stocul > 0 and nr_max_zile_oferta > durata:
#     stocul = stocul - 12
#     durata = durata + 1
#     print(f"Stocul este {stocul} si zile trecute {durata}")
#     if stocul <= 0 :
#         print("s a incheiat")
#         break





# Un magazin online are o promoție pentru un joc. Promoția se termină când s-au vândut 30 de /
# jocuri sau când mai sunt mai puțin de 2 zile până la finalul promoției.

# 🔹 Sarcina ta

# Definește variabilele:

# jocuri_vandute = 0

# zile_ramase = 5

# Creează o buclă while care continuă cât timp nu s-au vândut toate jocurile și mai sunt cel puțin 2 zile.

# În fiecare zi:

# Se vând 6 jocuri

# Scad zilele rămase

# Afișează starea promoției (jocuri_vandute și zile_ramase)

# Oprește bucla când se atinge oricare dintre condiții și afișează mesajul:
# "Promoția s-a încheiat!"

promotia = 30
jocuri = 0
zile_ramase = 8
while jocuri <= promotia and zile_ramase >= 2:
    jocuri = jocuri + 4
    zile_ramase = zile_ramase - 1
    print(f"Jocuir vandute {jocuri} si {zile_ramase} ramase")
    if jocuri >= promotia or zile_ramase <= 2:
        print("s a incheiat")
        break

