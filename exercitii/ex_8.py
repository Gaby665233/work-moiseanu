# Cantitatea de energie consumată (kWh)

# Utilizatorul introduce consumul zilnic.
# Calcule:

# total lunar (7 zile simulate)

# verifică dacă a depășit limita de 150 kWh

# calculează media consumului

# verifică dacă weekendul consumă mai mult decât restul
consum = []
zile = [ "luni", "marti", "miercuri", "joi", "vineri", "sambata", "duminica"]
for i in zile:
    con = (int(input(f"consum zilnic {i}:")))
    consum.append(con)

total = sum(consum)
depaseste_150 = total > 150
med_consum = int(total / 7)
weekend = sum(consum[5:])
zile_lucratoare = sum(consum[:5])
weekend_mai_mult = weekend > zile_lucratoare

print(f"total lunar: {total}")
print(f"daca depaseste limita: {depaseste_150}")
print(f"media consumului: {med_consum}")
print(f"consum mai mult in weekend: {weekend_mai_mult}")
