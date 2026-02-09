from person import Person

class Employee(Person):
    def __init__(self, name, email, salary, address):
        super().__init__(name, email, address)
        self.__salary = salary  # private

    # Getter și Setter pentru salary
    def get_salary(self):
        return self.__salary

    def set_salary(self, salary):
        self.__salary = salary

    # Metodă pentru creșterea salariului
    def increase_salary(self, percentage):
        self.__salary += self.__salary * (percentage / 100)

    # Polimorfism: afișează informațiile angajatului
    def display_info(self):
        info = f"Employee Name: {self.name}\n"
        info += f"Email: {self._email}\n"
        info += f"Address: {self._address}\n"
        info += f"Salary: ${self.__salary:.2f}"
        return info