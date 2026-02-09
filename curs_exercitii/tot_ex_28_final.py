# Mini proiect: Analiza datelor despre clienți

# Sarcina noastră este să creăm două funcții, calculate_discount și check_vip_status, care vor fi utilizate împreună pentru a/
#  genera o ofertă personalizată pentru fiecare client.

#  Instrucțiuni:

# Calculăm prețul cu reducere: Scriem funcția calculate_discount care primește prețul inițial al produsului și/
#  procentul de reducere, iar apoi returnează noul preț al produsului, cu reducerea aplicată.
# Verificăm statutul VIP: Scriem funcția check_vip_status care primește prețul total al achiziției după /
# reducere și verifică dacă suma este mai mare de 10.000. Dacă este, funcția trebuie să returneze True (clientul este VIP), altfel returnează False.
# Combinăm funcțiile:
# Utilizăm aceste două funcții împreună pentru a crea un mesaj personalizat pentru client. Dacă clientul este VIP, mesajul ar trebui /
# să fie: "Felicitari! Cu o reducere de [procent reducere]% ati obținut statutul VIP si beneficii suplimentare"
# Dacă nu este VIP, mesajul ar trebui să fie: "Cu o reducere de [procent reducere]% ati obținut un pret total de [pret calculat]! Va asteptam /
# din nou si poate deveniti membru VIP!"
# Testăm codul: Testăm funcționalitatea cu diferite valori ale prețurilor și reducerilor, pentru a ne asigura că combinația noastră de funcții/
#  funcționează în toate scenariile.
#  Întrebare pentru reflecție: Cum am putea extinde această sarcină pentru a include diferite niveluri de statut VIP, cum ar fi aur, /
# platină și diamant? Să ne gândim cum am putea introduce praguri de cheltuieli suplimentare și mesaje personalizate pentru fiecare /
# nivel de membru VIP.

def calculate_discount(pret, procent):
    nou_pret = pret - (pret * procent) / 100
    return nou_pret


def check_vip_status(pret_total):
    return pret_total > 10000

def mesaf(pret, procent):
    nou_pret = calculate_discount(pret, procent)
    vip = check_vip_status(nou_pret)
    if vip:
        return f"Felicitari! Cu o reducere de {procent}% ati obținut statutul VIP si beneficii suplimentare"
    else:
        return f"Cu o reducere de {procent}% ati obținut un pret total de {nou_pret}! Va asteptam din nou si poate deveniti membru VIP!"

while True:
    try:
        pret = int(input("Introdu pretul:"))
        procent = int(input("Care este procentul:"))
        break
    except ValueError:
        print("Nu ai intordus ce trenuie:")
print(mesaf(pret, procent))




