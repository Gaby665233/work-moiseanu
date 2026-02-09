# Un meteorolog înregistrează temperaturile zilnice.

# 🔹 Programul trebuie să:

# citească temperaturile pentru 7 zile

# calculeze:

# media săptămânii

# media zilelor lucrătoare

# media weekendului

# compare sâmbătă cu duminică (if pe o linie)

# compare media lucrătoare vs weekend (if-else)

# verifice dacă ambele zile de weekend au avut peste 25°C folosind and și or




temperaturi =[]
zile = ["luni", "marti", "miercuri", "joi", "vineri", "sambata", "duminca"]

for i in zile:
    while True:
        try:
            temp = input(f"temperatura in: {i} ")
            temperaturi.append(temp)
            break
        except ValueError:
            print("introdu un numar, incercati din nou")


med_saptamana = sum(temperaturi) / 7
med_zile_lucratoare = sum(temperaturi[:5]) /5
med_weekend = sum(temperaturi[5:]) / 2
print(f"media saptamanii:{med_saptamana}")
print(f"media zile lucratoare:{med_zile_lucratoare}")
print(f"media weekend:{med_weekend}")

print("sambata au fost inregistrate mai multe temperaturi" if temperaturi[5] > temperaturi[6] else "duminica au fost inregistrate mai multe temperaturi" )
if med_zile_lucratoare > med_weekend:
    print("temperatura zilelor lucratoare au fost mai ridicate")
else:
    print("temperatura zilelor din weekend au fost mai ridicate")

if temperaturi[5] > 25 and temperaturi[6] > 25:
    print("ambele zile au avut peste 25")
elif temperaturi[5] > 25 or temperaturi[6] > 25:
    print(f"doar o zi a avut peste 25:{"sambata" if temperaturi[5] > temperaturi[6] else "duminca"}")
else:
    print("nu este nicio zi peste 25")


