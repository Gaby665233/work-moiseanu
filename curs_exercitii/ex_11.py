# Alex lucrează la analiza datelor despre clienți și dorește să permită introducerea numărului de achiziții pentru diferiți clienți. /
# Pe baza acestor date, programul ar trebui să calculeze numărul total de achiziții și să personalizeze mesajul.

# Sarcina noastră este să îl ajutăm să creeze un program Python care:
# cere utilizatorului numele primului client și numărul achizițiilor sale;
# cere utilizatorului numele celui de-al doilea client și numărul achizițiilor sale;
# calculează numărul total de achiziții;
# afișează un mesaj personalizat, de exemplu, „Clienții Alex și Max au realizat împreună 50 de achiziții.”
# Sarcină bonus: Să permitem introducerea vârstei clienților și să afișăm un mesaj precum: „Clientul Alex, în vârstă de 30 de ani, a realizat 20 de achiziții.”
# Hint: Folosim funcția input() pentru introducerea datelor și să nu uităm să convertim datele în tip numeric folosind int() când este necesar pentru calcule.

primul_client = input("cum te cheamna: ")
ani_1 = int(input("cati ani ai: "))
nr_achizitie_1 = int(input("numarul achizitiei tale: "))


al_doilea_client = input("cum te cheama: ")
ani_2 = (int(input("cati ani ai: ")))
nr_achizitie_2 = int(input("cate ai cumparat: "))

total = nr_achizitie_1 + nr_achizitie_2
print(f"achizitia totala este: {total}")

print(f"clientii {primul_client} si {al_doilea_client} au realizat inpreuna {total} de achizitii.")

print(f"Clienttul {primul_client}, in varsta de {ani_1} de ani, a realizati {nr_achizitie_1} de achizitii")

print(f"Clienttul {al_doilea_client}, in varsta de {ani_2} de ani, a realizati {nr_achizitie_2} de achizitii")
