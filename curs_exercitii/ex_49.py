class Product:
    def __init__(self,name,price):
        self.name=name
        self.price=price
    def tax(self):
        return self.price * 1.2
    def buy(self):
        print("You bought a product",self.name,"with a price",self.tax(),"dollars")
p = Product("Shoes",100)
p.buy()


# Pentru a defini o metodă abstractă, folosim decoratorul @abstractmethod din același pachet. Va marca metoda de sub decorator ca abstractă./
# 
#  Prin urmare, putem face metoda tax() abstractă:

# EROARE

# import abc
# class Product(abc.ABC):
#     def __init__(self,name,price):
#         self.name=name
#         self.price=price

#     @abc.abstractmethod
#     def tax(self):
#         return self.price * 1.2
#     def buy(self):
#         print("You bought a product",self.name,"with a price",self.tax(),"dollars")

# p = Product("Shoes",100)
# p.buy()

# Din acest moment, clasa Product este abstractă cu metoda abstractă tax(). Dacă acum încercăm să rulăm acest cod, vom obţine o eroare:

# TypeError: Can't instantiate abstract class Product with abstract methods tax.

# Nu mai putem instanţia clasa, deoarece este abstractă. S-a întâmplat o serie de schimbări:

# nu putem instanţa clasa, ci o putem folosi doar ca părinte;
# metoda tax(), care este abstractă, nu trebuie să aibă corp, deoarece nu poate executa un anumit cod, dar suntem obligaţi, atunci/
#  când moştenim clasa, să folosim şi metoda tax()


# Pasul 1: Definirea clasei de bază cu metoda abstractă

# Dacă definim o nouă clasă, Shoes, care moștenește Product, fără a face nimic în ea, adică fără a adăuga nicio/
# \ logică în ea și fără a implementa metoda tax(), vom obţine aceeași eroare ca înainte, că folosim o metodă /
# abstractă. Metoda abstractă ne cere să scriem logica pentru calcularea taxelor în cadrul metodei tax(), adică să urmărim șablonul:

import abc
class Product(abc.ABC):
    def __init__(self,name,price):
        self.name=name
        self.price=price

    @abc.abstractmethod
    def tax(self):
        pass

    def buy(self):
        print("You bought a product",self.name,"with a price",self.tax(),"dollars")

# Pasul 2: Implementarea clasei Shoes

# În cazul în care clasa Shoes nu implementează metoda tax(), Python va genera o eroare. Să adăugăm implementarea:

class Shoes(Product):
    def tax(self):
        return self.price * 1.2

# Testăm:

p = Shoes("Nike",100)
p.buy()





print("-=-")
from abc import ABC, abstractmethod

class OnlineProduct(ABC):
    @abstractmethod
    def calculate_discount(self):
        pass

    @abstractmethod
    def display_details(self):
        pass

class DigitalProduct(OnlineProduct):

    def __init__(self, name, price, file_size):
        self.name = name
        self.price = price
        self.file_size = file_size

    def calculate_discount(self):
        return self.price * 0.10  # 10% reducere la produsele digitale

    def display_details(self):
        print(f"Digital Product: {self.name}, Price: ${self.price}, File Size: {self.file_size}MB")

class PhysicalProduct(OnlineProduct):

    def __init__(self, name, price, weight):
        self.name = name
        self.price = price
        self.weight = weight

    def calculate_discount(self):
        return self.price * 0.05  # 5% reducere la produsele fizice

    def display_details(self):
        print(f"Physical Product: {self.name}, Price: ${self.price}, Weight: {self.weight}kg")

class  SubscriptionProduct(OnlineProduct):
    def __init__(self,name,price,service):
        self.name = name
        self.price = price
        self.service = service
    
    def calculate_discount(self):
        return self.price * 0.15
    
    def display_details(self):
        print(f"nume {self.name},pretul {self.price} si adonamentul: {self.service}")
    

ebook = DigitalProduct("E-book on Python", 20, 15)

laptop = PhysicalProduct("Gaming Laptop", 1500, 2.5)
ebook.display_details()

laptop.display_details()
print(f"Discount for {ebook.name}: ${ebook.calculate_discount()}")

print(f"Discount for {laptop.name}: ${laptop.calculate_discount()}")


abonament = SubscriptionProduct("vasile",20,"VIP")

abonament.display_details()
print(f"reducere pentru: {abonament.name}: ${abonament.calculate_discount()}")
# Sarcină: Să îl ajutăm pe Alex să extindă exemplul anterior şi să implementeze o nouă subclasă SubscriptionProduct care modelează abonamente (de exemplu, abonament la serviciul de streaming):

# Atribute: nume, preţ, durata abonamentului.
# Reducere: 15%.
# Metode:
# calculate_discount: calculează reducerea.
# display_details: afişează informaţii despre abonament.


# Mini activitate:

# Sarcină: Să îl ajutăm pe Alex să definească clasa abstractă Order cu metodele abstracte calculate_total şi send_confirmation./
#  Apoi va trebui să creeze clasele derivate OnlineOrder şi InStoreOrder care implementează aceste metode. /
# Testaţi aceste metode creând instanţele lor şi apelând metode.


from abc import ABC , abstractmethod
class Order(ABC):
    def __init__(self,id,suma):
       self.id = id
       self.suma = suma
    @abstractmethod
    def calculate_total(self):
        pass
    
    @abstractmethod
    def send_confirmation():
        pass



class OnlineOrder(Order):
    
    
    def calculate_total(self):
         transport = 10
         return self.suma + transport

    def send_confirmation(self):
        print(f"numele: {self.id},pretul: {self.suma}, cu tramsport: {self.calculate_total()}")
    

class InStoreOrder(Order):
    def calculate_total(self):
        tax = 0.1 * self.suma
        return tax + self.suma
    def send_confirmation(self):
        print(f"numele: {self.id},pretul: {self.suma},suma totala: {self.calculate_total()}")


online = OnlineOrder("laptop", 1000,)
online.send_confirmation()
fizic = InStoreOrder("pisica",200)
fizic.send_confirmation()     
    

        
        