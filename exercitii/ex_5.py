cheltuieli =[]
zile = ["luni", "marti", "miercuri", "joi", "vineri", "sambata", "duminica"]
for i in zile:
    chel = int(input(f"cheltuieli {i}: "))
    cheltuieli.append(chel)

suma_total = sum(cheltuieli)
chel_med = sum(cheltuieli) / 7
tot_weekend = sum(cheltuieli[5:])
tot_zile_lucratoare = sum(cheltuieli[:5])
total_dep_500_lei = suma_total > 500
zile_lucratoare_mare_weekend = tot_zile_lucratoare > tot_weekend

print(f"suma totala: {suma_total}")
print(f"cheltuiala media: { chel_med}")
print(f"totalul in weekend: {tot_weekend}")
print(f"cheltuieli peste 500 lei: {total_dep_500_lei}")
print(f"zile lucratoare mai mare decat weekend: {zile_lucratoare_mare_weekend}")
