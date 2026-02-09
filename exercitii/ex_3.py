litri = []
zile = ["luni", "marti", "miercuri", "joi","vineri", "sambata", "duminica"]
for i in zile:
    lit = int(input(f"litri in {i}:"))
    litri.append(lit)

total_saptamana = sum(litri)
media_zi = int(sum(litri) / 7 )
peste_2l = all( l > 2 for l in litri)
weekend = sum(litri[5:])
rest_zile = sum(litri[:5])
weekend_mai_mult = weekend > rest_zile

print(f"total: {total_saptamana}")
print(f"media: {media_zi}")
print(f"peste 2L: {peste_2l}")
print(f"mai mult in weekend: {weekend_mai_mult}")
