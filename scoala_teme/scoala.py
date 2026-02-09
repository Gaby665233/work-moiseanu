luni = 230
marti = 200
miercuri = 300
joi = 290
vineri = 400
sambata = 150
duminica = 180
## să calculeze numărul total de clienți pentru întreaga săptămână
total_saptamani = luni + marti + miercuri + joi + vineri + sambata + duminica
print ( total_saptamani )
# să afișeze numărul total de clienți pentru zilele lucrătoare (luni - vineri)
total_zile_lucratore = luni + marti + miercuri + joi + vineri 
print ( total_zile_lucratore )
# să afișeze numărul total de clienți pentru weekend (sâmbătă și duminică)
total_weekend = sambata + duminica 
print ( total_weekend )
# să verifice dacă duminică au fost mai mulți clienți decât sâmbătă;
mai_multi_clieti_duminica = duminica > sambata
print ( mai_multi_clieti_duminica )
# să verifice dacă numărul total de clienți pentru zilele lucrătoare este mai mare decât numărul total de clienți pentru weekend;
zile_lucratoare_mai_multi = total_zile_lucratore > total_weekend
print ( zile_lucratoare_mai_multi )
# să verifice dacă săptămâna este considerată de succes dacă numărul total de clienți din acea săptămână a fost mai mare de 1000 sau dacă în weekend au fost mai mult de 500 de clienți în total; verificați succesul.
saptamana_succes = (total_saptamani > 1000) or (total_weekend > 500)
print (saptamana_succes)