def validate_sales_data(sales_data):
    """
    Verifică dacă datele de vânzări sunt valide:
    - cantități negative
    - cantități foarte mari (>100000)
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
        print(f"Eroare: {e}")
        return None


def least_sold_product(sales_data):
    """Returnează produsul cu cele mai puține vânzări."""
    try:
        return min(sales_data.items(), key=lambda x: x[1])
    except ValueError:
        return None
    except Exception as e:
        print(f"Eroare: {e}")
        return None


def get_product_sales(sales_data, product):
    """Returnează vânzările unui produs."""
    try:
        return sales_data[product]
    except KeyError:
        print(f"Produsul '{product}' nu există.")
        return 0
    except TypeError:
        print("Datele de vânzări nu sunt valide.")
        return 0


def critical_stock_products(stock_data, threshold=5):
    """Produse cu stoc critic."""
    try:
        return list(
            filter(lambda item: item[1] <= threshold, stock_data.items())
        )
    except Exception as e:
        print(f"Eroare: {e}")
        return []