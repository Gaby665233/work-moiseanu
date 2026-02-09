# Un elev își notează câte ore a studiat zilnic.

# 🔹 Programul trebuie să:

# citească numărul de ore pentru fiecare zi

# calculeze:

# totalul orelor pe săptămână

# total luni–vineri

# total weekend

# verifice dacă a studiat mai mult duminica decât sâmbăta

# verifice dacă a studiat mai mult în weekend decât în timpul săptămânii

# verifice dacă ambele zile de weekend au avut peste 3 ore de studiu

ore = []
zile = ["luni", "marti", "miercuri", "joi", "vineri", "sambata", "duminica"]
while True:
    try:
        ore.clear()
        for i in zile:
            M = float(input(f"ore studiate{i}: "))
            ore.append(M)
        break
    except ValueError:
        print("incearca din nou")


total = sum(ore)
total_lucratoare = sum(ore[:5])
total_wek = sum(ore[5:])

print(f"total{total}")
print(f"zile lucratoare{total_lucratoare}")
print(f"weekend{total_wek}")

print("duminica a avut mai mult" if ore[6] > ore[5] else "sambata a avut mai mult")

if total_wek > total_lucratoare:
    print("se pare ca a studiat mai mult in weekend")
else:
    print("ii nebun a avut mai mult chef in cursu saptamanii")

if  ore[6] > 3 and ore[5] > 3:
    print("a avut se pare")
else:
    print("ii era lene")



