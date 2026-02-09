pasi = []
zile = ["luni", "marti", "miercuri", "joi", "vineri", "samtaba", "duminica"]
for i in zile:
    pa = int(input(f"pasi in {i}: "))
    pasi.append(pa)

total_pasi = sum(pasi)
max_pasi = max(pasi)
min_pasi = min(pasi)
obiectiv_10000_pasi = sum( p >= 10000 for p in pasi) >= 4
total_peste_70000 = total_pasi > 70000

print(f"total pasi: {total_pasi}")
print(f"pasi maxim: {max_pasi}")
print(f"pasi minim: {min_pasi}")
print(f"10000 pasi in 4 zile: {obiectiv_10000_pasi}")
print(f"pasi peste 70000: {total_peste_70000}")