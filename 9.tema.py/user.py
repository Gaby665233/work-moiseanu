from person import Person

class User(Person):
    def __init__(self, name, email, phone, address):
        super().__init__(name, email, address)
        self.phone = phone  # public
        self.shopping_history = []  # public

    # Getter și Setter pentru phone
    def get_phone(self):
        return self.phone

    def set_phone(self, phone):
        self.phone = phone

    # Adaugă produs în shopping_history
    def add_product(self, product):
        self.shopping_history.append(product)

    # Calculează suma totală cheltuită
    def total_spent(self):
        total = sum(product.get_price() for product in self.shopping_history)
        return total

    # Polimorfism: afișează informațiile utilizatorului
    def display_info(self):
        info = f"User Name: {self.name}\n"
        info += f"Email: {self._email}\n"
        info += f"Address: {self._address}\n"
        info += f"Phone: {self.phone}\n"
        info += f"Products Bought: {[product.name for product in self.shopping_history]}"
        return info