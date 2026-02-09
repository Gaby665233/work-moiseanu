class Product:
    def __init__(self, name, price, quantity, description):
        self.name = name  # public
        self.__price = price  # private
        self.quantity = quantity  # public
        self._description = description  # protected

    # Getter și Setter pentru price
    def get_price(self):
        return self.__price

    def set_price(self, price):
        self.__price = price

    # Getter și Setter pentru description
    def get_description(self):
        return self._description

    def set_description(self, description):
        self._description = description

    # Verifică cantitatea de pe stoc
    def check_quantity(self):
        return self.quantity >= 10