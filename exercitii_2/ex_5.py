# Un magazin online înregistrează comenzile zilnice.

# 🔹 Programul trebuie să:

# citească comenzile pentru fiecare zi

# calculeze:

# total săptămânal

# total lucrătoare

# total weekend

# compare sâmbăta și duminica (if pe o linie)

# verifice dacă zilele lucrătoare au depășit weekendul

# verifice dacă weekendul a fost profitabil (peste 100 comenzi/zi)

comenzi = []
zile = ["luni", "marti", "miercuri", "joi", "vineri", "samabata", "duminica" ]

while True:
    try:
        comenzi.clear()
        for i in zile:
            com = int(input(f"comenzi inregistrate {i}: "))
            comenzi.append(com)
        break
    except ValueError:
        print("incearca din nou")

total = sum(comenzi)
zile_luc = sum(comenzi[:5])
weekend = sum(comenzi[5:])

print(f"total saptamana: {total}")
print(f"lucratoare total:{zile_luc}")
print(f"weekend:{weekend}")

print("sambata a avut mai multe comenzi" if comenzi[5] > comenzi[6] else "duminica au fost mai multe")

if zile_luc > weekend:
    print("mai smecheri in weekend")
else:
    print("in weekend este sporul")

if comenzi[5] > 100 and comenzi[6] > 100:
    print("au avut")
elif comenzi[5] > 100 or comenzi[6] > 100:
    print(f"doar {"sambata" if comenzi[5] > comenzi[6] else "duminca"} au fost mai multe:"
          f"{comenzi[5] if comenzi[5] > comenzi[6] else comenzi[6]}")
else:
    print("nimic")


        