# Mini activitate: Ce fel de cafea va bea Alex?

# În timp ce reflecta asupra structurilor de control, Alex și-a dat seama că acest lucru este asemănător unei decizii cotidiene: /
# dacă are lapte în frigider, va face cafea cu lapte, iar dacă nu, va face cafea neagră. Să scriem un program care să îl ajute pe Alex să ia această decizie.

# Dacă are lapte, programul va afișa: "Cafea cu lapte."
# Dacă nu are lapte, programul va afișa: "Cafea neagră."
# Hint: Să ne amintim cum folosim input() pentru a introduce text și cum să stabilim structura if-else pentru a verifica condiția "da" sau "nu".

cafea = input("Cum bei cafea : cu Lapte sau fara:")
if cafea == "lapte":
    print("Cafea cu lapte")
else:
    print("Cafea neagra")




# Introducerea numarului de unitati vandute si informatiile despre stocuri
# numar_vandute = int(input("Introducetii numarul de unitati vandute: "))
# stocuri = int(input("Introduceti numarul de unitati ramase in stoc: "))

# # Verificarea rezultatelor de vanzari
# if numar_vandute > 100:
#     print("Vanzare reusita.")
# else:
#     print("Vanzare sub asteptari. Propuneti actiuni promotionale.")

# # Verificarea starii stocurilor
# if stocuri < 50:
#     print("Avertizare: Stocuri reduse. Trebuie comandate produse noi.")
# else:
#     print("Stocuri la nivel satisfacator.")


#
# 
# 
# 
# 
#  Să adăugăm o condiție suplimentară – dacă vânzările depășesc 200 de unități, programul ar trebui să recomande comenzi suplimentare, /
# chiar și în cazul în care stocurile sunt reduse. Astfel, ne vom asigura că reacționăm rapid la cererea crescută.

# Hint: Să adăugăm un alt bloc if pentru a verifica condiția suplimentară, unde numărul de unități vândute se verifică dacă este mai mare de 200. /
# În interiorul acestui bloc if, putem adăuga un nou mesaj care sugerează comanda de produse suplimentare. Să nu uităm să verificăm și starea /
# stocurilor – dacă sunt scăzute, vom recomanda o comandă.

vanzari = int(input("Itrodu nr de vanzari: "))
stocuri = input("Stocuri: scazute sau ridicate: ")
if vanzari > 200:
    print("comenzi suplimentare")
else:
    print("nu este nevoie")

if stocuri == "scazute":
    print("recomandam o comanda")
else:
    print("ii ok")


