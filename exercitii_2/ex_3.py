# EXERCIȚIUL 3 – Numărul de pași zilnici

# O persoană își monitorizează pașii zilnic.

# 🔹 Programul trebuie să:

# citească pașii pentru fiecare zi

# calculeze:

# total pași săptămânali

# total pași lucrătoare

# total pași weekend

# compare sâmbătă și duminică (ternar)

# verifice dacă în weekend s-au depășit 10.000 pași/zi:

# ambele zile

# doar una

# niciuna

pasi = []
zile = ["luni", "marti", "miercuri", "joi", "vineri", "sambata", "duminica"]


while True:
        try:
            pasi.clear()
            for i in zile:
                pas = int(input(f"pasii facuti {i}: "))
                pasi.append(pas)
            break
        except ValueError:
            print("introdu din nou")
        

total_pasi = sum(pasi)
total_lucratoare = sum(pasi[:5])
total_weekend = sum(pasi[5:])

print(f"pasi saptamanali:{total_pasi}")
print(f"pasi zile lucratoare:{total_lucratoare}")
print(f"pasi in weekend:{total_weekend}")

print("sambata au fost mai multi pasi:" if pasi[5] > pasi[6] else "duminica au fost mai multi pasi")

if pasi[5] > 10000 and pasi[6] > 10000:
    print("in ambele zile s au pebasit 10000 pasi")
elif pasi[5] > 10000 or pasi[6] >10000:
    print(f"doar {"sambata" if pasi[5] > pasi[6] else "duminica"} au fost mai multi pasi ")
else:
    print( "nicio zi")
