# Primești câte un număr de clienți pentru 7 departamente (nu zile).
# Calcule:

# totalul clienților

# departamentul cu cei mai mulți clienți

# dacă totalul > 1000

# dacă toate departamentele au peste 50 clienți

clienti = []
for i in range(1,8):
    clienti.append(int(input(f"clienti departament {i}: ")))
total_clienti = sum(clienti)
mai_multi = max(clienti)
total_mai_mare = total_clienti > 1000
peste_50 = all( c > 50 for c in clienti)

print(f"totalul clientilor:{total_clienti}")
print(f"departament cu mai multi clienti: {mai_multi}")
print(f" totalul mai mult de 1000:{total_mai_mare}")
print(f"toate peste 50: {peste_50}")
