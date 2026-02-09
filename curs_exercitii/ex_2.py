# Alex a observat în proiectul său de analiză a datelor că liniile de cod devin prea lungi, ceea ce îngreunează citirea. Îl vom ajuta să separe liniile pentru ca codul să fie mai clar și mai lizibil.

# Să luăm codul pe care Alex l-a primit pentru calcularea sumei:
# sum = 50 + 100 + 150 + 200 + 250 + 300 + 350 + 400 + 450 + 500 + 550 + 600 + 650 + 700 + 750 + 800 + 850 + 900 + 950 + 1000

# print(sum)

# Sarcina noastră este:
# să separăm linia de cod: folosim semnul \ pentru a separa linia astfel încât nicio linie să nu depășească 79 de caractere; separăm codul în puncte logice, având grijă să păstrăm o structură clară;
# să verificăm dacă codul se execută corect: după ce am separat linia, salvăm fișierul și rulăm codul pentru a verifica dacă se afișează valoarea corectă a sumei;
# să comparăm situația înainte și după: să vedem cum arată codul nostru înainte și după separare; care versiune este mai clară și mai ușor de înțeles?
# Întrebare pentru reflecție: Să comparăm codul original și cel separat. Cum ne ajută separarea liniilor să urmărim mai ușor logica codului? Observăm o diferență în lizibilitate?

# Să vedem soluția



sum = 50 + 100 + 150 + 200 + 250 + 300 + 350 + 400 + 450 + 500 \
    + 550 + 600 + 650 + 700 + 750 + 800 + 850 + 900 + 950 + 1000

print(sum)