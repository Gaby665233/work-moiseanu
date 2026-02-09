# Alex trebuie să implementeze acum o coadă pentru imprimarea documentelor. Programul în Python ar trebui să utilizeze /
# o listă și să permită gestionarea cozii de documente de pe diferite dispozitive și să simuleze imprimarea.

# Sarcină:

# să creăm o listă pentru a simula coada pentru imprimare;
# să implementăm metoda add_document(device, document_name)care adaugă documentul la coada pentru imprimare ca un tuplu ordonat;
# să implementăm metoda print_document() care elimină documentul de la începutul listei și simulează imprimarea prin afișarea /
# pe ecran a numelui documentului și a dispozitivului de pe care a fost trimis;
# să adăugăm exemple de testare în care simulăm adăugarea de documente de pe diferite dispozitive, precum și eliminarea lor, respectiv imprimarea.

coada_imprimare = []

def add_document(device, document_name):
    coada_imprimare.append((device, document_name))

    print(f"document:{document_name} de pe dispoziticul {device} a fost adaugat")

def print_document():
    if coada_imprimare:
        device, document_name = coada_imprimare.pop(0)
        print(f"Se imprima documentul {document_name} de pe dispozitivul {device} adaugat in coada")

def adauga_documente():
    if coada_imprimare:
        print("coada curenta")
        for i, (device, document) in enumerate(coada_imprimare, start=1):
            print(f"{i}.{document} de pe {device}")
    else:
        print("coada este goala")
def main_program():
    while True:
        print("\nAlege o opțiune:")
        print("1. Adaugă document la coadă")
        print("2. Printează document")
        print("3. Afișează coada")
        print("4. Ieșire")

        alegere = input("Introdu numărul opțiunii: ")


        if alegere == '1':
            device = input("Introdu dispozitivul: ")
            document_name = input("Introdu numele documentului: ")
            add_document(device, document_name)

        elif alegere == '2':
            print_document()
        elif alegere == '3':
            adauga_documente()
        elif alegere == '4':
            print("Exit")
            break
        else:
            print("intre 1-4")
main_program()





# Alex trebuie să implementeze o coadă de comenzi într-un restaurant.

# Fiecare comandă conține:

# numele clientului

# produsul comandat

# Programul trebuie să folosească o listă și să simuleze procesarea comenzilor.

# 🎯 Sarcină

# Scrie un program în Python care:

# 1️⃣ Creează o listă goală pentru coada de comenzi
# 2️⃣ Creează funcția add_order(client, product) care:

# adaugă comanda în coadă sub formă de tuplu (client, product)

# 3️⃣ Creează funcția serve_order() care:

# scoate prima comandă din listă (FIFO)

# afișează ce client este servit și ce produs a comandat

# 4️⃣ Creează funcția show_orders() care:

# afișează toate comenzile din coadă numerotate

# 5️⃣ Creează un main_program() care:

# afișează un meniu

# folosește input() pentru a permite utilizatorului:

# să adauge comenzi

# să servească o comandă

# să vadă coada

# să iasă din program

procesarea_comezii = []

def add_order(client, product):
    procesarea_comezii.append((client,product))
    print(f"clientul {client} cu produsul {product} a fost adaugat")

def serve_order():
    if procesarea_comezii:
        client, product = procesarea_comezii.pop(0)
        print(f"este servit {client} - {product}")
    else:
        print("nu exista comenzii")

def show_orders():
    if procesarea_comezii:
        print("comenzi in coada")
        for i,(client,produs) in enumerate(procesarea_comezii, start=1):
            print(f"{i}.{client}-{produs}")
    else:
        print("Coada de comenzi este goală.")
def main_program():
    while True:
        print("\n alege o optiune")
        print("1.adauga comanda")
        print("2.serveasca comanda")
        print("3.vada coada")
        print("4.sa iasa")

        alege_numar = input("alege un nummar:")

        if alege_numar == '1':
            client = input("numele clientului:")
            product = input("produsul comandat:")
            add_order(client, product)
        elif alege_numar == '2':
            serve_order()
        elif alege_numar =='3':
            show_orders()
        elif alege_numar == '4':
            print("exit")
            break
        else:
            print("numar intre 1-4")
main_program()



print("__________-----ATL EXERCITIU----------________________")


# Exercițiu: Gestionarea cozii la o farmacie

# Alex trebuie să creeze un program care să gestioneze pacienții care așteaptă să ridice medicamentele.

# Fiecare pacient are:

# numele pacientului

# medicamentul cerut

# Programul va folosi o listă ca și coadă (FIFO) și va avea funcții pentru:

# 🎯 Cerințe

# 1️⃣ Creează o listă goală pentru coada pacienților.

# 2️⃣ Funcția add_patient(name, medicine)

# Adaugă pacientul la coadă ca tuplu (name, medicine)

# Afișează mesaj: „Pacientul X a cerut medicamentul Y și a fost adăugat în coadă.”

# 3️⃣ Funcția serve_patient()

# Scoate primul pacient din coadă

# Afișează mesaj: „Se servește pacientul X pentru medicamentul Y”

# Dacă coada e goală, afișează „Nu există pacienți în coadă.”

# 4️⃣ Funcția show_queue()

# Afișează toți pacienții din coadă numerotat

# Exemplu:

# 1. Maria - Paracetamol
# 2. Ion - Aspirină


# 5️⃣ main_program()

# Creează un meniu interactiv cu opțiunile:

# 1. Adaugă pacient
# 2. Servește pacient
# 3. Vezi coada
# 4. Ieșire


# Folosește input() pentru a primi datele de la utilizator.

coada = []

def add_pacineti(name, medicine):
    coada.append((name,medicine))
    print(f"clientul {name} cu medicamendul {medicine} a fost adaugat")

def serve_patient():
    if coada:
        name, medicine = coada.pop(0)
        print(f"Se servește pacientul {name} pentru medicamentul {medicine}")
    else:
        print("Nu există pacienți în coadă.")

def arata_coada():
    if coada:
        print("coada curenta")
        for i,(name,medicine) in enumerate(coada,start=1):
            print(f"{i}.{name}-{medicine}")
    else:
        print("-")
def main_program():
    while True:
        print("\n alege o optiune")
        print("1. Adaugă pacient")
        print("2. Servește pacient")
        print("3. Vezi coada")
        print("4. Ieșire")

        alege = input("ce doresti")

        if alege =='1':
            name = input("introdu un nume")
            medicine = input("ce ai cumparat")
            add_pacineti(name, medicine)
        elif alege == '2':
            serve_patient()
        elif alege =='3':
             arata_coada()
        elif alege == '4':
            print("exit")
            break
        else:
            print("nu te pricepi")
main_program()


print("EXERCITIY NOU_____--------______")
# Alex trebuie să creeze un program care gestionează rezervările clienților la un service auto.

# Fiecare rezervare conține:

# numele clientului

# tipul serviciului (ex: „schimb ulei”, „revizie”, „ITP”)

# Programul va folosi o listă ca și coadă (FIFO).

# 🎯 Cerințe

# 1️⃣ Creează o listă goală numită service_queue.

# 2️⃣ Creează funcția add_booking(client, service)

# Adaugă o rezervare în coadă sub formă de tuplu (client, service)

# Afișează:
# „Rezervarea pentru X (serviciu: Y) a fost adăugată în coadă.”

# 3️⃣ Creează funcția process_booking()

# Scoate prima rezervare din coadă

# Afișează:
# „Se procesează rezervarea: X – Y”

# Dacă nu există rezervări:
# „Nu există rezervări în coadă.”

# 4️⃣ Creează funcția show_bookings()

# Afișează toate rezervările numerotate

# 5️⃣ Creează main_program() cu meniu:

# 1. Adaugă rezervare
# 2. Procesează rezervare
# 3. Afișează coada
# 4. Ieșire

service_queue = []

def add_booking(client, service):
    service_queue.append((client, service))
    print(f"Rezervarea pentru {client}(serviciul: {service}) a fost adaugat in coada")

def process_booking():
    if service_queue:
        client, service = service_queue.pop(0)
        print(f"Se proceseaza rezervarea: {client} - {service}")
    else:
        print("Nu există rezervări în coadă.")
def show_booking():
    if service_queue:
        for i,(client, service) in enumerate(service_queue,start=1):
            print(f"{i}.{client} - {service}")
    else:
        print("nu mai este nimic")

def main_program():
    while True:
        print("\n alege optiunea")
        print("1. Adaugă rezervare")
        print("2. Procesează rezervare")
        print("3. Afișează coada")
        print("4. Ieșire")

        alege = input("alege un numar: ")

        if alege == '1':
            client = input("numele clientului")
            service = input("ce problema ai")
            add_booking(client, service)
        elif alege =='2':
            process_booking()
        elif alege == '3':
            show_booking()
        elif alege =='4':
            print("exit")
            break
        else:
            print("nu te pricepi")
main_program()






# Exercițiu: Gestionarea cozii pentru înscriere la curs

# Alex trebuie să creeze un program care gestionează coada de înscriere a studenților la un curs.

# Fiecare înscriere conține:

# numele studentului

# numele cursului

# Programul va folosi o listă ca și coadă (FIFO).

# 🎯 Cerințe

# 1️⃣ Creează o listă goală numită inscrieri.

# 2️⃣ Creează funcția add_student(name, course)

# Adaugă o înscriere în listă sub formă de tuplu (name, course)

# Afișează:
# „Studentul X s-a înscris la cursul Y.”

# 3️⃣ Creează funcția process_enrollment()

# Scoate prima înscriere din listă

# Afișează:
# „Se procesează înscrierea: X – Y.”

# Dacă lista e goală:
# „Nu există înscrieri.”

# 4️⃣ Creează funcția show_enrollments()

# Afișează toate înscrierile numerotate

# 5️⃣ Creează un main_program() cu meniu:

# 1. Adaugă înscriere
# 2. Procesează înscriere
# 3. Afișează coada
# 4. Ieșire


coada = []

def add_student(name, course):
    coada.append(name, course)
    print(f"Studentul {name} s-a înscris la cursul {course}.")

def process_enrollment():
    if coada:
        name, course = coada.pop(0)
        print(f"Se procesează înscrierea: {name} - {course}")
    else:
        print("Nu există înscrieri.")

def show_enrollments():
    if coada:
        for i,(name, course) in enumerate (coada, start=1):
            print(f"{i}.{name} - {course}")
    
    else:
        print("nu este nimic")
    
def main_program():
    while True:
        print("\n alege o varianta")
        print("1. Adaugă înscriere")
        print("2. Procesează înscriere")
        print("3. Afișează coada")
        print("4. Ieșire")


        alege = input("alege un numar")

        if alege == '1':
            name = input("intro un nume")
            course = input("intrdu numele cursului")
            add_student(name, course)

        elif alege == '2':
            process_enrollment()

        elif alege =='3':
            show_enrollments()
        
        elif alege =='4':
            print("Exit")
            break
        else:
            print("ai doar 4 cifre")

main_program()








