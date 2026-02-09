# O persoană își urmărește orele de somn zilnic.

# 🔹 Programul trebuie să:

# citească orele dormite în fiecare zi

# calculeze:

# total ore săptămână

# media zilelor lucrătoare

# media weekendului

# compare duminica și sâmbăta

# verifice dacă a dormit mai bine în weekend decât în timpul săptămânii

# verifice dacă a dormit peste 8 ore în ambele zile de weekend

somn = []
zile = ["luni", "marti","miercuri","joi","vineri","sambata","duminica"]
while True:
    try:
        somn.clear()
        for i in zile:
            som = int(input(f"ore dormine {i}: "))
            somn.append(som)
        break
    except ValueError:
        print("ai gresit hahaha incearca din nou")


total = sum(somn)
zile_lucratoare = sum(somn[:5])
wekkend = sum(somn[5:])
media_zile_luc = sum(somn[:5]) / 5
med_weekend = sum(somn[5:]) / 2

print(f" total ore saptamanale:{total}")
print(f"media zile lucratoare:{media_zile_luc}")
print(f"media weekend:{med_weekend}")

if somn[5] > somn[6]:
    print("sambata a dormit mai mult")
else:
    print("duminica a dormit mai mult")

print("in weekend a dormit mai bine" if wekkend > zile_lucratoare else "in timpul saptamanii a dormit mai mult")

if somn[5] > 8 and somn[6] > 8:
    print("a dormit peste 8 ore")
elif somn[5] > 8 or somn[6] > 8:
    print(f"a dormit mai mult {"sambata:" if somn[5] > somn[6] else "duminica:"}"
    f"{somn[5] if somn[5] > somn[6] else somn[6]}")
else:
    print("nu a avut somn")

