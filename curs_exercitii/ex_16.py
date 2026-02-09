# meteo = "noros"
# if mete == "ploaie":
#     print("Ia-ti umbrela!")
# elif meteo == "soare":
#     print("Pune-ti ochelari de soare!")
# else:
#     print("Este noros, nu ai nevoie de nimic special."



# Mini activitate: Să experimentăm cu condițiile

# Alex urmărește vânzările produselor și, pe baza numărului de unități vândute, trage concluzii despre succesul zilei. Folosește structura /
# if-elif-else, dar există două moduri diferite în care putem seta condiția în blocul elif. Oare ambele moduri oferă același rezultat?

# Folosim operatorul logic

# În primul exemplu, folosim operatorul logic and pentru a conecta două condiții. Să vedem cum arată:

# vanzare = int(input("Introduceti numarul de unitati vandute: "))
# if vanzare > 100:
#     print("Vanzarea a fost foarte reusita!")
# elif vanzare >= 50 and vanzare <= 100:
#     print("Vanzarea este solida, dar ganditi-va la actiuni suplimentare.")
# else:
#     print("Vanzarea este slaba. Propuneti actiuni promotionale urgente.")

#  Sarcină

# Ce se întâmplă când introducem vânzări de 100 de unități? Recunoaște acest program corect situația în care vânzările sunt de 100?
# Acum vom modifica condiția din ramura elif, omitem verificarea pentru exact 100 de unități.
vanzare = int(input("Introduceti numarul de unitati vandute: "))
if vanzare > 100:
     print("Vanzarea a fost foarte reusită!")
elif 50 <= vanzare < 100:   # Acest bloc elif NU verifica vanzarea de 100 de unitati
     print("Vanzarea este solida, dar ganditi-va la actiuni suplimentare.")
else:
     print("Vanzarea este slaba. Propuneti actiuni promotionale urgente.")

#     3. Să rulăm programul și să introducem vânzări de 100 de unități. Unde clasifică programul acest rezultat? Ne duce în blocul else și de ce? /
#     Cum putem corecta acest cod?

vanzare = int(input("Introduceti numarul de unitati vandute: "))
if vanzare > 100:
     print("Vanzarea a fost foarte reusită!")
elif 50 <= vanzare:   # Acest bloc elif NU verifica vanzarea de 100 de unitati
     print("Vanzarea este solida, dar ganditi-va la actiuni suplimentare.")
else:
     print("Vanzarea este slaba. Propuneti actiuni promotionale urgente.")