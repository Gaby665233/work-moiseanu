# Să vedem un exemplu practic în care folosim câmpul static tax pentru a calcula impozitul pe produse:


class Product:
    tax = 0.2

    def __init__(self,name,price,quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def calcul_total_price(self):
        "pretul total incluzand si taxa"
        return self.price * (1 + Product.tax ) * self.quantity
    
    def dispaly_product(self):
        return f"numele: {self.name}, pret per unitate(cu taxa): {self.price * (1 + Product.tax)}, cantitatea: {self.quantity}, Pretul total: {self.calcul_total_price()}"
    
product1 = Product ("Laptop", 700, 2)
product2 = Product ("Phone", 400, 3)

print(product1.dispaly_product())

print(product2.dispaly_product())


# Mini activitate: Să aplicăm cunoștințele

# Sarcină: Să îl ajutăm pe Alex să creeze o clasă Employee cu următoarele caracteristici:

# Câmpuri de instanță: name, position, și salary (date unice pentru fiecare angajat).
# Câmp static: company_name (același pentru toți angajații).
# Să adăugăm metoda display_employee_info()care afișează toate informațiile despre angajat, inclusiv numele companiei.
# Să vedem soluția:
print("---------------------------------------")
class Employee:
    company_name = "TechCorp"


    def __init__(self,name,position,salary):
        self.name = name
        self.position = position
        self.salary = salary
    
    def display_employee_info(self):
        return f"numeele: {self.name}, positia: {self.position}, din compania {Employee.company_name}, cu salariul: {self.salary}"
    
employee1 = Employee("Alex Johnson", "Software Engineer", 120000)
employee2 = Employee("Maria Smith", "Project Manager", 150000)

print(employee1.display_employee_info())
print(employee2.display_employee_info())

# Metodele de instanță sunt un element de bază al programării orientate pe obiecte care permite lucrul direct cu date/
#  specifice unui obiect individual. Acestea sunt metode care există în contextul unui obiect și folosesc datele și /
# comportamentele sale specifice. Alex le-a folosit deja în lecțiile anterioare, dar acum vom explora în detaliu cum/
#  funcționează și de ce sunt esențiale pentru manipularea datelor în obiecte.

# O metodă de instanță este o funcție care:

# funcționează în contextul obiectului: Are acces la toți membrii obiectului, inclusiv câmpurile și alte metode.
# are întotdeauna un parametru de bază self: Python transmite automat o referință la obiectul pe care a fost apelată metoda prin self.
# Să vedem un exemplu al metodei de instanță calculate_total_price, care calculează prețul total al unui produs cu taxe:

# class Product:
#     tax = 0.2  # Static field for tax

#     def __init__(self, name, price, quantity):
#         self.name = name
#         self.price = price
#         self.quantity = quantity

#     def calculate_total_price(self):
#         """Calculates the total price of the product including tax."""
#         return self.price * (1 + Product.tax) * self.quantity

# În acest exemplu, metoda calculate_total_price folosește:

# self.price și self.quantity: Câmpuri specifice pentru obiectul curent.
# Product.tax: Câmp static de clasă pentru calculul taxei.
# Când apelăm această metodă, Python trece automat obiectul curent ca self. De exemplu:

# product1 = Product("Laptop", 700, 2)
# print(product1.calculate_total_price())  # Result: 1680.0

# Astfel, metoda de instanță are un parametru de bază self care indică o instanță a clasei Product, doar atunci când metoda este apelată. /
# După ce o metodă de instanță este activată, aceasta are acces liber la toate câmpurile și metodele obiectului pe care a fost apelată./
#  Acest lucru ne oferă o putere mare de a schimba starea obiectelor. Datele sunt modificate la nivel de instanță, așa cum am putut vedea /
# în exemplul anterior.

 

# Apelarea metodelor de instanță
# Metodele de instanță pot fi apelate doar printr-un obiect de clasă. Să ne uităm la un exemplu cu un apel la metoda display_product_info care/
#  este o parte din clasa Product:

# product1 = Product("Laptop", 700, 2)
# product2 = Product("Phone", 400, 3)

# product1.display_product_info()
# product2.display_product_info()

# Crearea obiectelor: Obiectele product1 și product2 sunt create din clasa Product.
# Apelarea metodelor: Metoda display_product_info este apelată pe fiecare obiect, ceea ce permite afișarea informațiilor specifice fiecărui produs.
 
    

print ("extindem clasa")
#    Sarcină: Să îl ajutăm pe Alex să extindă clasa Product prin adăugarea unei metode update_price care permite actualizarea prețului unui produs.

# Instrucțiuni:

# să adăugăm metoda update_price(new_price) care modifică valoarea câmpului price;
# să afișăm prețul nou folosind metoda display_product_info;
# să testăm metoda prin actualizarea prețului pentru unul din produse.    
class Product:
    tax = 0.2

    def __init__(self,name,price,quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def calcul_total_price(self):
        "pretul total incluzand si taxa"
        return self.price * (1 + Product.tax ) * self.quantity
    
    def dispaly_product(self):
        return f"numele: {self.name}, pret per unitate(cu taxa): {self.price * (1 + Product.tax)}, cantitatea: {self.quantity}, Pretul total: {self.calcul_total_price()}"
    
    def update_price(self, new_price):
        """Updates the product price."""
        self.price = new_price
        print(f"Price for {self.name} has been updated to {self.price}")
    
product1 = Product ("Laptop", 700, 2)
product2 = Product ("Phone", 400, 3)

print(product1.dispaly_product())
product1.update_price(900)
print(product1.dispaly_product())


print(product2.dispaly_product())
product2.update_price(1000)
print(product2.dispaly_product())


print("-=-=-")
class Product:
    tax = 0.2  # Static field for tax

    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    @staticmethod
    def set_tax(new_tax):
        """Static method to set a new tax rate."""
        Product.tax = new_tax
        return f"New tax rate set to: {Product.tax * 100}%"
print(Product.set_tax(0.25) )
print(Product.tax)

print("-=-=-=-")
class CurrencyConverter:
    @staticmethod
    def convert_to_euros(amount_in_dinars, rate):
        return amount_in_dinars * rate 

print(CurrencyConverter.convert_to_euros(10000, 0.0085))


class Employee:
    company_name = "TechCorp"  # Static field

    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary

    @staticmethod
    def set_company_name(new_name):
        """Sets a new company name."""
        Employee.company_name = new_name
        print(f"Company name updated to: {Employee.company_name}")
print("-=-=-")
# Testarea metodei:
print(Employee.company_name)
Employee.set_company_name("InnoTech")  # Updates the compa




print("-=-=-")

class User:
    def __init__(self, name, userid, number):
        self.name = name
        self.userid = userid
        self.number = number

    @classmethod
    def input_user(cls):
        """Allows direct input of user data through the class."""
        name = input('Name: ')
        userid = input('User ID: ')
        number = input('Phone number: ')
        return cls(name, userid, number)

# Adding a new user through the class method
new_user = User.input_user()
print(f"Name: {new_user.name}, UserID: {new_user.userid}, Number: {new_user.number}")




# Mini activitate: Automatizarea inserării datelor pentru produse

# Sarcină: Alex gestionează un număr mare de produse în companie şi doreşte să accelereze procesul de inserare a acestora. Sarcina noastră este să îmbunătăţim clasa Product în aşa fel încât vom adăuga o metodă de clasă create_from_input. Această metodă trebuie:

# să permită inserarea atributelor produsului (name, price, quantity) direct din consolă;
# să creeze automat o nouă instanţă a clasei Product pe baza rezultatelor inserate.
# Instrucţiuni:

# creăm metoda create_from_input cu decoratorul @classmethod;
# implementăm inserarea datelor pentru nume, preţ şi cantitatea de produse.
# Ne asigurăm că metoda returnează o nouă instanţă a clasei folosind valorile inserate.
# Să vedem soluţia:

class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
    
    def dysplay_product(self):
        return f"Product: {self.name}, Price: {self.price}, Quantity: {self.quantity}"


    @classmethod
    def create_from_input(cls):
        """Creates a new product by taking input from the console."""
        name = input("Enter product name: ")
        price = float(input("Enter product price: "))
        quantity = int(input("Enter product quantity: "))
        return cls(name, price, quantity)

# Creating a product using the class method
product1 = Product.create_from_input()
print(product1.dysplay_product())