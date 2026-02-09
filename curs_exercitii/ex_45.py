# Motivaţie pentru învăţarea ulterioară: Cum poate rezolva o clasă problemele lui Alex?
# Alex analizează zilnic datele despre produse – preţurile, stocurile şi reducerile acestora. Înainte să înceapă să folosească clasele, codul său era supraîncărcat de şiruri de funcţii şi variabile, ceea ce făcea ca fiecare modificare să fie mult mai complicată şi să dureze mai mult.

# De exemplu, ne vom imagina că Alex vrea să monitorizeze informaţiile privind articolele de vânzare, inclusiv preţul lor, numărul de articole în stoc şi reducerea:

# Product data
name = "T-Shirt"
price = 1000
stock = 30
discount = 10

def calculate_discount(price, discount):
    return price - (price * discount / 100)

new_price = calculate_discount(price, discount)
print(f"Price with discount: {new_price}")



# Vom combina tot ceea ce am învăţat într-un exemplu simplu:

class Laptop:
    pass  # Empty class for demonstration

# Creating an object of the Laptop class
item = Laptop()

# Displaying the object
print(f"An object has been created: {item}")

# Când rulăm acest cod, Python va afişa ceva de genul:

# An object has been created: <__main__.Laptop object at 0x7f9d30a3f4f0>

# Acest lucru indică faptul că a fost creat obiectul clasei Laptop şi afişează locaţia sa în memorie.


# Sarcină: Să-l ajutăm pe Alex să îmbunătățească exemplul anterior prin:

# crearea unui obiect din clasa Product;
# atribuirea de valori pentru name, price și quantity;
# afișarea de informații despre produs folosind următorul format: Chocolate: price = 56, quantity = 7.
class Product:
    name = ""
    price = 0.0 
    quantity = 0

item = Product()

item.name = "Chocolate"
item.price = 56
item.quantity = 7
print(f"{item.name}: pretul = {item.price}, cantitatea = {item.quantity} ")



print("Varianta 1")
# Sarcină: Să-l ajutăm pe Alex să îmbunătățească exemplul anterior creând două obiecte din clasa Product pentru două produse diferite, fiecare cu propriile date:

# 1. Primul produs:

Nume: "Laptop"
Preț: 1200.99
Cantitate: 5
# 2. Alt produs:

Nume: "Smartphone"
Preț: 699.50
Cantitate: 10
# Să afișăm datele despre fiecare produs folosind f-string.

# Să vedem soluția:

class Product:
    name = ""
    price = 0.0
    quantity = 0

# Create the first object of the Product class
item1 = Product()
item1.name = "Laptop"
item1.price = 1200.99
item1.quantity = 5

# Create the second object of the Product class
item2 = Product()
item2.name = "Smartphone"
item2.price = 699.50
item2.quantity = 10

print(f"{item1.name}: price = {item1.price}, quantity = {item1.quantity}")
print(f"{item2.name}: price = {item2.price}, quantity = {item2.quantity}")

# SAU varianta 2 mult mqi ok pt mine
print("Varianta 2")
class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

# Crearea obiectelor
item1 = Product("Laptop", 1200.99, 5)
item2 = Product("Smartphone", 699.50, 10)

print(f"{item1.name}: price = {item1.price}, quantity = {item1.quantity}")
print(f"{item2.name}: price = {item2.price}, quantity = {item2.quantity}")

print("----______-------------")
class Product: 
    name = "" 
    price = 0.0 
    quantity = 0 

    # Define a method for applying a discount 
    def apply_discount(self): 
        self.price *= 0.9 

# Create an object 
item = Product() 
item.price = 150 

# Display the original price 
print(f"Original price: {item.price}") 

# Apply the discount method 
item.apply_discount() 
print(f"Discounted price: {item.price}")



class Consumer: 
    def say_hello(self): 
        print("Hello!!") 

# Creating an object and calling the method 
c = Consumer() 
c.say_hello() 

print("-=-=-=-=-=")

# Mini activitate: Adunarea numerelor folosind metode

# Sarcină: Să-l ajutăm pe Alex să scrie clasa Calculator care are o metodă de a aduna două numere.

# Instrucțiuni:

# definim clasa Calculator, care conține metoda add pentru a aduna două numere;
# metoda add trebuie să primească doi parametri a și b;
# metoda add trebuie să returneze rezultatul adunării a și b;
# creăm o instanță a clasei Calculator;
# apelăm metoda add cu valorile 2 și 3, apoi listăm rezultatul.
# Hint: Parametrul self permite metodei să acceseze câmpurile clasei.
class Calculator:
    def add(self , a , b):
        return a + b
    
cal = Calculator()
rezultat = cal.add(2,3)
print(rezultat)


# Mini activitate: Extinderea clasei Calculator

# Sarcină: Să extindem clasa Calculator din exemplul anterior adăugând:

# câmpurile number1 și number2 pentru stocarea numerelor;
# metoda add, care returnează ca rezultat suma a doi operanzi;
# metoda sub, care returnează ca rezultat diferența a doi operanzi;
# metoda mul, care returnează ca rezultat produsul a doi operanzi;
# metoda div, care returnează ca rezultat câtul a doi operanzi;
# testarea metodelor prin crearea a două instanțe ale clasei Calculator cu valori diferite ale câmpurilor number1 și number2.

class Calculator:
    number1 = 0
    number2 = 0

    def add(self):
        return self.number1 + self.number2
    
    def sub(self):
        return self.number1 - self.number2
    
    def mul(self):
        return self.number1 * self.number2
    
    def div(self):
        if self.number2 == 0:
            return "Eroare"
        return self.number1 / self.number2
    
calc = Calculator()
calc.number1 = 10
calc.number2 = 5
rezult = calc.mul()
print(rezult)

print("-=-=-=-=-")

class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def display_info(self):
        return f"Product: {self.name}, Price: {self.price} euros, Quantity: {self.quantity}"

# Creating objects with initial values
product1 = Product("Laptop", 700, 10)
product2 = Product("Phone", 400, 5)

# Displaying product information
print(product1.display_info())
print(product2.display_info())


# Sarcină: Să-l ajutăm pe Alex să creeze o clasă User cu următoarele cerințe:

# clasa trebuie să aibă câmpuri pentru name, surname și email;
# constructorul setează automat valorile acestor câmpuri;
# să adăugăm o metodă display_user() care afișează informații despre utilizator într-un format care poate fi citit de om;
# să creăm două instanțe ale clasei User și afișăm datele utilizatorului folosind metoda display_user().

print("ex nou-=-=-=-=")
class User():
    def __init__(self,name,surname,email):
        if "@" not in email:
            raise ValueError("trebuiw sa contina '@'")
        self.name = name
        self.surname = surname
        self.email = email
    
    def display_user(self):
        return f"numele: {self.name}, surname: {self.surname} si email-ul este {self.email}"
    
user1 = User("mitica", "mitica123","mitica@.com")
user2 = User("ion","ion213","iom@gamil.com")

print(user1.display_user())
print(user2.display_user())



print("O VARIANTA SI MAI BUNA")


class User():
    def __init__(self, name, surname, email):
        self.name = name
        self.surname = surname
        self.email = email
    
    def display_user(self):
        return f"Numele: {self.name}, prenumele: {self.surname}, email-ul este {self.email}"


# --- AICI este input-ul ---
name = input("Introdu numele: ")
surname = input("Introdu prenumele: ")

while True:
    email = input("Introdu email-ul: ")
    if "@" in email:
        break
    print("❌ Email invalid! Mai încearcă.")

user = User(name, surname, email)
print(user.display_user())


"un exemplu mai avansat"
print("-=-=-=-=-=-")

class User():
    def __init__(self, name, surname, email):
        self.name = name
        self.surname = surname
        self.email = email
    
    def display_user(self):
        return f"Numele: {self.name}, prenumele: {self.surname}, email-ul este {self.email}"


name = input("Introdu numele: ")
surname = input("Introdu prenumele: ")

while True:
    email = input("Introdu email-ul: ")

    if email.count("@") != 1:
        print("❌ Emailul trebuie să conțină un singur @")
        continue

    name_part, domain = email.split("@")

    if not name_part:
        print("❌ Email invalid")
        continue

    if domain not in ["gmail.com", "yahoo.com", "outlook.com"]:
        print("❌ Domeniu invalid! Exemplu: nume@gmail.com")
        continue

    break

user = User(name, surname, email)
print(user.display_user())


        
