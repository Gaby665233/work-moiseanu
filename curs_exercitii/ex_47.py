#  Mini activitate: Îmbunătăţirea clasei Product

#  Sarcină: Să îl ajutăm pe Alex să îmbunătăţească clasa Product în aşa fel încât va adăuga metoda pentru actualizarea sigură a/
#  preţului produsului. Metoda trebuie să accepte o nouă valoare a preţului şi să verifice dacă preţul este valid /
# (de exemplu, mai mare decât zero), înainte de actualizarea valorii atributului _price.

#  Întrebare pentru reflecție: Ce avantaje vedem în această abordare cu valorile protejate faţă de accesul direct la atribute?

# Să vedem soluţia:

class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self._price = price  # Protected member for price
        self.quantity = quantity

    def update_price(self, new_price):
        if new_price > 0:
            self._price = new_price
            print(f"Price updated to: {self._price}")
        else:
            print("Invalid price. Must be greater than zero.")

# Testing the method
p = Product("Laptop", 1000, 10)
p.update_price(1200)  # Updates the price
p.update_price(-500)  # Reports an error




class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.__price = price 
        self.quantity = quantity

    # Setter for price with validation
    def set_price(self, new_price):
        if new_price > 0:
            self.__price = new_price
        else:
            print("Price must be a positive value!")  

    def get_price(self):
        return self.__price

p = Product("tv", 500, 5)
p.set_price(330)
print(p.get_price())

# Acum avem două metode noi: get_price, care va reprezenta metoda getter, şi set_price, care va reprezenta metoda setter./
#  Metoda get_price, aşa cum îi spune şi numele, preia valoarea, în timp ce metoda setter setează, respectiv creează, o /
# valoare. Aici avem condiţia ca, în caz că valoarea preţului nou este negativă sau egală cu zero, programul va lista un/
#  mesaj şi nu va permite modificarea valorii, însă dacă preţul este un număr pozitiv, va avea loc modificarea lui.

# Dacă acum rulăm programul cu un parametru transmis greşit, vom vedea că nu există o întrerupere în funcţionarea programului /
# şi nici nu se va semnala o eroare, deoarece am definit ce se întâmplă şi cum se va trata variabila în cazul unei inserări greşite./
#  Desigur, dacă transmitem un număr pozitiv, vom obţine o funcţionare normală, prevăzută, a programului.

# Exemplul specificat îi permite lui Alex să protejeze preţul produsului. Acum, dacă cineva încearcă să introducă un preţ negativ, /
# sistemul nu va permite acest lucru.

class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self._price = price 
        self.quantity = quantity
    # Getter for price
    def get_price(self):
        return self._price

    # Setter for price with validation
    def set_price(self, new_price):
        if new_price > 0:
            self._price = new_price
        else:
            print("Price must be a positive value!")    

p = Product("tv", 500, 5)
p.set_price(-150)
print(p.get_price())




#  Sarcină: Să îl ajutăm pe Alex să-şi dezvolte clasa User cu următoarele specificaţii:

# Clasa User trebuie să aibă atribute private:
# __name: numele utilizatorului;
# __age: vârsta utilizatorului;
# __balance: soldul contului.
# Vom crea metodele getter şi setter pentru toate atributele private:
# set_age(new_age) şi get_age(): permit o inserare controlată şi citirea vârstei/anilor;
# add_balance(amount) şi withdraw_balance(amount): controlează tranzacţii, validând ca soldul să nu poată fi negativ.
# Testăm funcţionarea metodei încercând să accesăm direct atributele, iar apoi folosind metodele.

#  Să vedem soluţia:

class User:
    def __init__(self, name, age, balance):
        self.__name = name
        self.__age = age
        self.__balance = balance

    # Getter and setter for age
    def get_age(self):
        return self.__age

    def set_age(self, new_age):
        if new_age > 0:
            self.__age = new_age
        else:
            print("Age must be positive!")

    # Methods for working with balance
    def add_balance(self, amount):
        if amount > 0:
            self.__balance += amount
        else:
            print("Amount must be positive!")

    def withdraw_balance(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient funds or invalid amount!")

    # Display user information
    def display_user_info(self):
        print(f"Name: {self.__name}, Age: {self.__age}, Balance: {self.__balance}")

# Testing
user = User("Alex", 25, 1000)
user.display_user_info()
user.add_balance(500)
user.withdraw_balance(300)
user.withdraw_balance(1500)  # Error
user.display_user_info()



class User:
    def __init__(self, name, age):
        self.__name = name  # Private attribute
        self.__age = age    # Private attribute

    def get_name(self):
        return self.__name  # Getter method for __name

# Creating an instance of the User class
u1 = User("Mark", 20)

# Creating a new public attribute __name (this does not affect the private attribute)
u1.__name = ""

# Printing the value of the new __name attribute
print(u1.__name)  # Output: ""

# But the private attribute is still accessible via the getter method
print(u1.get_name())  # Output: "Mark"