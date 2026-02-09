#  exercotiul 1
# carianta cu int la media
luni = int(input("produse luni: "))
marti = int(input("produse marti: "))
miercuri = int(input("produse miercuri: "))
joi = int(input("produse joi: "))
vineri = int(input("produse vineri: "))
sambata = int(input("produse sambata: "))
duminica = int(input("produse duminica: "))

total = luni + marti + miercuri + joi + vineri + sambata + duminica
media = int(total / 7)
weekend = sambata + duminica
luni_mai_mare_vineri = luni > vineri
total_saptamana = total > 2000

print (f"total saptamana: { total }")
print (f"media zilnica: { media }")
print (f"total weekend: { weekend }")
print (f"luni mai mare decat vineri: { luni_mai_mare_vineri}")
print (f"total mai mare 2000: {total_saptamana}") 

# vara int
luni = int(input("produse luni: "))
marti = int(input("produse marti: "))
miercuri = int(input("produse miercuri: "))
joi = int(input("produse joi: "))
vineri = int(input("produse vineri: "))
sambata = int(input("produse sambata: "))
duminica = int(input("produse duminica: "))

total = luni + marti + miercuri + joi + vineri + sambata + duminica
media = total / 7
weekend = sambata + duminica
luni_mai_mare_vineri = luni > vineri
total_saptamana = total > 2000

print (f"total saptamana: { total }")
print (f"media zilnica: { media }")
print (f"total weekend: { weekend }")
print (f"luni mai mare decat vineri: { luni_mai_mare_vineri}")
print (f"total mai mare 2000: {total_saptamana}") 

# varianta profesionista 
zile = ["Luni", "Marti", "Miercuri", "Joi", "Vineri", "Sambata", "Duminica"]
produse = [int(input(f"Produse {zi}: ")) for zi in zile]

total = sum(produse)
media = total / 7
weekend = produse[5] + produse[6]
luni_vs_vineri = produse[0] > produse[4]
total_peste_2000 = total > 2000

print(total, media, weekend, luni_vs_vineri, total_peste_2000)



