# Dacă suma este mai mică de 100 de dolari, clientul nu primește reducere. Dacă suma este între 100 și 500 de dolari, /
# clientul primește o reducere de 5%. Dacă suma este între 500 și 1000 de dolari, clientul primește o reducere de 10%./
# Dacă suma este mai mare de 1000 de dolari, clientul /
# primește o reducere de 15%. aici pot face si if-elif-elif-else

suma = int(input("introdu suma: "))
if 100 < suma:
    print("nu primesti nimic")
elif 100 > suma < 500:
    print("5%")
elif 500 > suma < 1000:
    print("10%")
else:
    print("15%")


# v2
suma = float(input("Introdu suma cumpărăturilor: "))

if suma < 100:
    reducere = 0
elif suma < 500:
    reducere = 0.05
elif suma < 1000:
    reducere = 0.10
else:
    reducere = 0.15

print(f"Reducerea aplicată este de {reducere * 100}%")