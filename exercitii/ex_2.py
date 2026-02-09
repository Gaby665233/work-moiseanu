ore = []
zile = ["luni", "marti", "miercuri", "joi", "vineri", "sambata", "duminica"]
for i in zile:
    stutiu = int(input(f"ore studiu {i}:"))
    ore.append(stutiu)

total_saptamana = sum(ore)
total_weekend = sum(ore[5:])
total_lucratoare = sum(ore[:5])
cel_putin_2_ore = all( o >= 2 for o in ore)
peste_20 = total_saptamana > 20

print(f"total saptamanal: {total_saptamana}")
print(f"total weekend: {total_weekend}")
print(f"total zile lucratoare: {total_lucratoare}")
print(f"daca elevul a stutial cel putin 2 ore: {cel_putin_2_ore}")
print(f"totalul depaseste 20: {peste_20}")
