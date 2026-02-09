# e putem transmite prin moştenire?
# Atunci când o clasă moşteneşte o altă clasă, ea poate prelua următorii membri:

# Membrii publici (public): Aceşti membri sunt disponibili peste tot, atât în subclasă, cât şi în afara ei.
# Membrii protejaţi (protected): Sunt disponibili în subclasă, dar nu şi în afara ei (excepţie fiind accesul din clasă sau din copii).
# Membrii privaţi (private) nu sunt disponibili subclaselor, deoarece sunt destinaţi exclusiv utilizării în cadrul clasei. Dacă încercăm să-i /
# accesăm, Python va semnala o eroare.

# Exemplu în Python

class Employee:
    def __init__(self, name, email, _salary, __bonus):
        self.name = name  # Public
        self._salary = _salary  # Protected
        self.__bonus = __bonus  # Private

    def show_info(self):
        return f"Name: {self.name}, Salary: {self._salary}"

class Manager(Employee):
    def __init__(self, name, email, _salary, __bonus, department):
        super().__init__(name, email, _salary, __bonus)
        self.department = department

    def show_manager_info(self):
        return f"{self.show_info()}, Department: {self.department}"

# Testing
m = Manager("Alice", "alice@company.com", 50000, 5000, "Sales")
print(m.show_manager_info())  # Outputs: Name: Alice, Salary: 50000, Department: Sales
print(m._salary)  # Protected member is accessible
try:
    print(m.__bonus)  # Error: AttributeError
except AttributeError as e:
    print(f"Error: {e}")

 

# Reguli cheie:

# Membrii publici (public): Complet disponibili subclaselor şi utilizatorilor.
# Membrii protejaţi (protected): Trebuie folosiţi atent, deoarece modificarea acestor valori poate distruge integritatea codului.
# Membrii privaţi (private): Nu sunt deloc disponibili subclaselor. Python foloseşte name mangling pentru ascunderea membrilor privaţi /
# (de exemplu, __bonus devine _Employee__bonus).

print("---")


class Employee:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def display_info(self):
        print(f"Employee: {self.name}, Email: {self.email}")

# Subclass that overrides the method
class SalesManager(Employee):
    def display_info(self):
        print(f"Sales Manager: {self.name}, Contact: {self.email}")

# Creating instances
employee = Employee("Alex Johnson", "alex.johnson@example.com")
manager = SalesManager("Emily Smith", "emily.smith@company.com")

# Calling methods
employee.display_info()  # Uses the method from Employee class
manager.display_info()   # Uses the overridden metho

print("---")



