# În timpul importării modulului, putem abrevia numele său sau îi putem atribui un alt nume folosind aliasul şi cuvântul-cheie as/
# . Aliasurile sunt utile pentru îmbunătăţirea lizibilităţii şi pentru simplificarea scrierii codului, în special atunci /
# când folosim module cu alte denumiri.

import math as m

# Using the alias "m" to access math module functionalities
print(m.pi)  # Displays the value of π from the math module
print(m.sqrt(16))  # Calculates the square root of 16 

# Aliasurile fac codul mai scurt şi mai lizibil, însă este important să folosim aliasuri descriptive pentru ca şi codul să rămână uşor de înţeles.