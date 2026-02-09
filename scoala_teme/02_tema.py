clienţi_luni = int(input("introduceti numarul de clienti pentru luni"))
clienţi_marti = int(input("introduceti numarul de clienti pentru marti"))
clienţi_miercuri = int(input("introduceti numarul de clienti pentru miercuri"))
clienţi_joi = int(input("introduceti numarul de clienti pentru joi"))
clienţi_vineri = int(input("introduceti numarul de clienti pentru vineri"))
clienţi_sambata = int(input("introduceti numarul de clienti pentru sambata"))
clienţi_duminica = int(input("introduceti numarul de clienti pentru duminica"))
# numărul total de clienți pentru întreaga săptămână
total_saptamana = ( clienţi_luni + clienţi_marti + clienţi_miercuri + clienţi_joi + clienţi_vineri + clienţi_sambata + clienţi_duminica )
print ( total_saptamana )
#  total de clienți pentru zilele lucrătoare
total_zile_luratoare = ( clienţi_luni + clienţi_marti + clienţi_miercuri + clienţi_joi + clienţi_vineri )
print ( total_zile_luratoare )
#  clienți pentru zilele de weekend
total_weekend = ( clienţi_sambata + clienţi_duminica )
print ( total_weekend )
#  duminica mai mulți clienți decât sâmbăta
print ( "Duminică a fost o zi de vânzări mai bună decât sâmbătă"
       if clienţi_duminica > clienţi_sambata
       else "Sâmbătă a fost o zi de vânzări mai bună decât duminică" )
if total_zile_luratoare > total_weekend:
    print ( " zilele lucrătoare mai mare decât numărul total de clienți pentru zilele de weekend " ) 
else:
    print ( " zilele de weeken mai mare decât numărul total de clienți pentru zilele lucrătoare " )
if clienţi_sambata > 100 and clienţi_duminica > 100:
    print("Ambele zile de weekend au avut mai mult de 100 de clienți.")
elif clienţi_sambata > 100 or clienţi_duminica > 100:
    print("Doar o zi de weekend a avut mai mult de 100 de clienți.")
else:
    print("Nici o zi de weekend nu a avut mai mult de 100 de clienți.")
    
       
        


    


