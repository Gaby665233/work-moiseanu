# Ore de somn pe noapte

# Introduci orele dormite în fiecare zi.
# Calcule:

# totalul orelor dormite

# media pe zi

# verifică dacă s-a dormit minim 8 ore în 5 zile

# verifică dacă în weekend s-a dormit mai mult

# verifică dacă totalul depășește 50 ore

ore = []
zile = ["luni", "marti", "miercuri", "joi", "vineri", "sambata", "duminica"]
for i in zile:
    oree = int(input(f"ore de somn {i}: "))
    ore.append(oree)

total = sum(ore)
media = total / 7
minim_8_ore = sum( o >= 8 for o in ore) >= 5
weekend = sum(ore[5:])
lucratiare = sum(ore[:5])
mai_mult_weekend = weekend > lucratiare
tot_mare_50 = total > 50

print(f"total ore: {total}")
print(f"media zi: {media}")
print(f"mai mult de 8 ore in 5 zile: {minim_8_ore}")
print(f"weekend mai mult: {mai_mult_weekend}")
print(f"totul depaseste 50: {tot_mare_50}")
