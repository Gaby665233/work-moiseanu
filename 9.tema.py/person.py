from abc import ABC, abstractmethod

class Person(ABC):
    def __init__(self, name, email, address):
        self.name = name  # public
        self._email = email  # protected
        self._address = address  # protected

    # Getter și Setter pentru email
    def get_email(self):
        return self._email

    def set_email(self, email):
        self._email = email

    # Getter și Setter pentru address
    def get_address(self):
        return self._address

    def set_address(self, address):
        self._address = address

    # Verifică dacă email-ul este valid
    def check_email(self):
        return '@' in self._email

    # Metoda abstractă
    @abstractmethod
    def display_info(self):
        pass