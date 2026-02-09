sales = {
    "Laptop": 15,
    "Mouse": 150,
    "Keyboards": 85,
    "Monitor": 30,
    "USB cables": 200
    }


total_sold = sum(sales.values())


most_sold_product = max(sales, key=sales.get)
least_sold_product = min(sales, key=sales.get)


if "Web camera" not in sales:
    sales["Web camera"] = 0



sales["Monitor"] += 5



def critical_products(sales_dict, threshold=50):
    """
    Returnează o listă cu produsele care au vânzări sub pragul specificat.
    """
    return [product for product, quantity in sales_dict.items() if quantity < threshold]

critical_list = critical_products(sales)



def validate_sales_data(sales_dict):
    """
    Verifică dacă există cantități negative în datele de vânzări.
    """
    for product, quantity in sales_dict.items():
        if quantity < 0:
            return False, product
    return True, None

is_valid, invalid_product = validate_sales_data(sales)

# ==============================
# Afișarea rezultatelor
# ==============================

print("=== Dicționarul de vânzări actualizat ===")
for product, quantity in sales.items():
    print(f"{product}: {quantity} unități")

print("\n=== Analiza vânzărilor ===")
print(f"Cantitatea totală de produse vândute: {total_sold}")
print(f"Cel mai vândut produs: {most_sold_product}")
print(f"Cel mai puțin vândut produs: {least_sold_product}")
print("Produsul 'Web camera' este prezent în dicționar:", "Web camera" in sales)

print("\n=== Produse cu vânzări critice (sub 50 unități) ===")
print(critical_list)

print("\n=== Verificare validitate date ===")
if is_valid:
    print("Datele sunt valide. Nu există cantități negative.")
else:
    print(f"Date invalide pentru produsul: {invalid_product}")