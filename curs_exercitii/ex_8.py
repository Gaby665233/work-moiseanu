# Să ne imaginăm că Alex analizează datele pentru martie și aprilie pentru a trage concluzii despre succesul vânzărilor. Are următoarele informații:

# numărul de clienți: 155
# valoarea medie a achizițiilor în aprilie: 58.00 lei
# Sarcină:

# Să creăm variabile care să stocheze aceste date.
# Să folosim operatori logici pentru a răspunde la următoarele întrebări:
# Este numărul de clienți din martie mai mare de 150 sau valoarea medie a achizițiilor din aprilie mai mare de 60 de lei?
# Numărul de clienți în martie nu este mai mic de 100, folosind operatorul not?
# Să afișăm rezultatele folosind funcția print().
#  Hint: Folosiți operatorii and, or și not pentru a combina condițiile.

numărul_de_clienți = 155
valoarea_medie_aprilie = 58.00 

profit = numărul_de_clienți > 150 and valoarea_medie_aprilie > 60
nu_mai_mare = not(numărul_de_clienți < 100)

print(profit)
print(nu_mai_mare)
