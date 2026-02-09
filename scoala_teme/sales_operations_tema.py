# sales_operations.py

def validate_sales_data(sales_data):
    """
    Verifică dacă datele de vânzări sunt valide:
    - cantități negative sau foarte mari (>100000)
    """
    valid_data = {}
    for product, quantity in sales_data.items():
        try:
            if not isinstance(quantity, int):
                raise ValueError(f"Valoare invalidă pentru {product}: {quantity}")
            if quantity < 0 or quantity > 100000:
                raise ValueError(f"Valoare neobișnuită pentru {product}: {quantity}")
            valid_data[product] = quantity
        except ValueError as e:
            print(f"Atenție: {e}")
    return valid_data

def total_sold(sales_data):
    """Returnează totalul unităților vândute."""
    try:
        return sum(sales_data.values())
    except Exception as e:
        print(f"Eroare la calculul totalului: {e}")
        return 0

def most_sold_product(sales_data):
    """Returnează produsul cu cele mai multe vânzări."""
    try:
        return max(sales_data.items(), key=lambda x: x[1])
    except ValueError:
        return None
    except Exception as e:
        print(f"Eroare la identificarea produsului cel mai vândut: {e}")
        return None

def least_sold_product(sales_data):
    """Returnează produsul cu cele mai puține vânzări."""
    try:
        return min(sales_data.items(), key=lambda x: x[1])
    except ValueError:
        return None
    except Exception as e:
        print(f"Eroare la identificarea produsului cel mai puțin vândut: {e}")
        return None

def get_product_sales(sales_data, product):
    """Returnează vânzările pentru un produs specific, cu gestionarea excepțiilor."""
    try:
        return sales_data.get(product, 0)
    except AttributeError as e:
        print(f"Eroare: date invalide pentru sales_data - {e}")
        return 0

def critical_stock_products(stock_data, threshold=5):
    """
    Returnează lista de produse cu stoc critic folosind list comprehension și lambda.
    """
    try:
        return [product for product, quantity in stock_data.items() if quantity <= threshold]
    except Exception as e:
        print(f"Eroare la identificarea produselor cu stoc critic: {e}")
        return []

from sales_operations import (
    validate_sales_data,
    total_sold,
    most_sold_product,
    least_sold_product,
    get_product_sales,
    critical_stock_products
)

# Exemplu de date
sales_data = {
    "Laptop": 120,
    "Mouse": 450,
    "Tastatura": 300,
    "Monitor": 50,
    "Casti": -10,   # valoare invalidă
    "USB": 150000   # valoare prea mare
}

stock_data = {
    "Laptop": 10,
    "Mouse": 3,
    "Tastatura": 0,
    "Monitor": 7,
    "Casti": 2,
    "USB": 50
}

# Validarea datelor de vânzări
sales_data = validate_sales_data(sales_data)

print(f"Date de vânzări validate: {sales_data}")

# Calcul total vânzări
print(f"Total vândut: {total_sold(sales_data)} unități")

# Cel mai vândut produs
most_product = most_sold_product(sales_data)
if most_product:
    print(f"Cel mai vândut produs: {most_product[0]} ({most_product[1]} unități)")

# Cel mai puțin vândut produs
least_product = least_sold_product(sales_data)
if least_product:
    print(f"Cel mai puțin vândut produs: {least_product[0]} ({least_product[1]} unități)")

# Vânzări pentru un produs specific
product_name = "Mouse"
print(f"Vânzări {product_name}: {get_product_sales(sales_data, product_name)} unități")

# Produse cu stoc critic
critical_products = critical_stock_products(stock_data, threshold=5)
print(f"Produse cu stoc critic: {critical_products}")
