temperaturi = []
zile = ["luni", "marti", "miercuri", "joi", "vineri", "sambata", "duminica"]
for i in zile : 
    temp = float(input(f"temperatura in {i}: "))
    temperaturi.append(temp)

max_temp = max(temperaturi)
min_temp = min(temperaturi)
media = int(sum(temperaturi) / 7)
zile_lucratoare = sum(temperaturi[:5])
zile_weekend = sum(temperaturi[5:])
weekend_mai_cald = zile_weekend > zile_lucratoare 
peste_30_grade = sum(t > 30 for t in temperaturi) >= 3

print(f"temperatura max:{ max_temp }")
print(f"temperatura min:{min_temp}")
print(f"media: {media}")
print(f"weekend mai cald: {weekend_mai_cald}")
print(f"mai mult de 3 zile peste 30: {peste_30_grade}")