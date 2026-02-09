# Mini activitate: Reamintirea cunoștințelor anterioare

# Alex a creat anterior un program care urmărește produsele cele mai bine vândute folosind variabile de bază. /
# Acum, compania sa îi cere să adauge informații pentru cinci produse, inclusiv numele și prețurile acestora.

# Să-l ajutăm pe Alex să finalizeze această sarcină folosind variabile individuale. Urmărim următoarele date /
# despre cele mai bine vândute produse:

# Laptop – 1200 euro
# Mouse – 50 euro
# TV – 600 euro
# Monitor – 300 euro
# Microfon – 100 euro
# Sarcină: Înainte să mergem mai departe, să încercăm să scriem singuri un program folosind variabilele pentru aceste/
#  produse. Creăm variabile pentru fiecare produs, respectiv numele și prețul său, și prezentăm datele folosind funcția/
#  print() astfel încât Alex să poată vizualiza cu ușurință informațiile.

# Pauză de reflecție
# Cât timp ne ia să introducem datele pentru cinci produse? Cum am extinde programul dacă avem și mai multe /
# produse? Facem o pauză și testăm soluția noastră.

nume_1 = "Laptop" 
nume_1_1 = 1200 
nume_2 = "Mouse" 
nume_2_2 = 50 
nume_3 = "TV" 
nume_3_3 = 600 
nume_4 = "Monitor" 
nume_4_4 = 300 
nume_5 = "Microfon" 
nume_5_5 = 100 

print( nume_1, "-", nume_1_1)
print( nume_2, "-", nume_2_2)
print( nume_3, "-", nume_3_3)
print( nume_4, "-", nume_4_4)
print( nume_5, "-", nume_5_5)



product = ["Laptop", "Mouse", "TV", "Monitor", "Microphone"]
print(product)



# Mini activitate: Să facem o listă cu termenii cheie din Python

# Acum este rândul nostru! Să ne imaginăm că lucrăm cu Alex la crearea unui ghid pentru /
# începători, în care trebuie să enumere concepte importante din programare pe care le-a folosit în cursul anterior.

# Sarcină:

# să facem o listă de operatori aritmetici pe care i-am folosit în cursul anterior;
# să creăm o listă cu tipurile de date pe care le-am folosit până acum;
# să afișăm ambele liste folosind funcția print().
# Hint: Dacă nu ne amintim toți operatorii sau tipurile de date, să ne amintim cum am folosit + pentru /
# a adăuga numere sau "int" pentru un număr întreg.

# Hint: Elementele listei, indiferent dacă sunt operatori aritmetici sau tipuri de date, le punem în stringuri.

# Întrebare pentru reflecție: Cum ar arăta dacă am folosi variabile individuale pentru fiecare operator și tip de date?/
#  Cât de ușor ar fi să se lucreze cu această listă comparativ cu variabile individu


opearatori = ["+","-","/","*","%","//"]
tipuri_de_date = ["int","float","str","bool"]

print(f"operatorii sunt: {opearatori}")
print(f"tipurile de date: {tipuri_de_date}")


# cu for
opearatori = ["+","-","/","*","%","//"]
tipuri_de_date = ["int","float","str","bool"]

for i in opearatori:
    print(i)

for t in tipuri_de_date:
    print(t)

# cu join

opearatori = ["+","-","/","*","%","//"]
tipuri_de_date = ["int","float","str","bool"]
print("Operatori",", ".join(opearatori))
print("tipuri", ", ".join(tipuri_de_date))


print("--------ALTCEVA-------")
product = ["Laptop", "Mouse", "TV", "Monitor", "Microphone"]
# Access to the second element in the list (Mouse)
item = product[1]
print(item)  # The program prints: Mouse


products = ["Laptop", "Mouse", "TV", "Monitor", "Microphone"]

# Access to the last element in the list
last_product = products[-1]
print(last_product)  # Prints: Microphone



# Mini activitate: Accesarea ultimului element al listei

# Să scriem un program în care se accesează și tipărește numele ultimului element dintr-o listă care conține nume de produse.

# Hint: Este permisă și indexarea negativă.

# Întrebare pentru reflecție: Cât de eficient este să accesăm datele folosind un index, /
# comparativ cu gestionarea fiecărui produs individual prin variabile separate?

product = ["Laptop", "Mouse", "TV", "Monitor", "Microphone"]
ultim_produs = product[-1]
print(ultim_produs)


print("---------ALTCEVA IAR--------")

prices = [99.99, 149.99, 199.99, 249.99, 299.99, 349.99, 399.99, 449.99, 499.99]

# Prompt the user to enter a price
user_price = float(input("Enter the price of the product you are looking for: "))

# Check if the price exists in the list
if user_price in prices:
    print(f"A product with the price {user_price} has been found.")
else:
    print(f"No product with the price {user_price} was found.")



# Mini proiect: Numărarea produselor cu prețuri favorabile

# În magazin există o listă cu prețurile produselor, prezentată ca o listă prices.

#  Sarcină:

# Este necesar:

# să definim o listă prices care conține prețurile produselor disponibile în magazin;
# să permitem utilizatorului să introducă prețul maxim pe care îl consideră favorabil, prin utilizarea funcției input();
# să numărăm și să imprimăm câte produse au un preț mai mic sau egal cu valoarea introdusă.
# Să vedem soluția

# List of product prices

prices = [100, 250, 150, 300, 50, 200, 175, 80, 120, 275]

# Allow the user to enter the maximum price they consider affordable
max_price = int(input("Enter the maximum price you consider affordable: "))

# Initialize a counter
affordable_count = 0

# Count the number of products with a price less than or equal to the entered value
for price in prices:
    if price <= max_price:
        affordable_count += 1

# Advanced waw to count the number of products with a price less than or equal to the entered value
#affordable_count = sum(1 for price in prices if price <= max_price)

# Display the result
print(f"The number of products with a price less than or equal to {max_price} is: {affordable_count}")




