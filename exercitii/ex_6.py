minute =[]
zile = ["luni", "marti", "miercuri", "joi", "vineri", "sambata" ,"duminica"]
for i in zile:
    min = int(input(f"minute: {i} "))
    minute.append(min)

total_saptamana = sum(minute)
med_zi = sum(minute) / 7
weeken_sport = sum(minute[5:]) 
mai_mare = weeken_sport > total_saptamana
total_300 = total_saptamana > 300
cel_putin_o_zi = any( m < 10 for m in minute )

print(f"total saptamana: { total_saptamana}")
print(f"media zi: {med_zi}")
print(f"weekend mai mult sport:{weeken_sport}")
print(f"mai mult in weekend:{mai_mare}")
print(f"totul depaseste 300: {total_300}")
print(f"cel putin o zi:{cel_putin_o_zi}")
