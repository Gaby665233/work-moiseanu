from sales_operations import (
    validate_sales_data,
    total_sold,
    most_sold_product,
    least_sold_product,
    get_product_sales,
    critical_stock_products
)

sales_data = {
    "Laptop": 120,
    "Telefon": 300,
    "Casti": 50,
    "Mouse": -3,          # invalid
    "Tastatura": 150000   # prea mare
}

stock_data = {
    "Laptop": 3,
    "Telefon": 10,
    "Casti": 2,
    "Mouse": 1
}

valid_sales = validate_sales_data(sales_data)

print("Total vânzări:", total_sold(valid_sales))
print("Cel mai vândut produs:", most_sold_product(valid_sales))
print("Cel mai puțin vândut produs:", least_sold_product(valid_sales))
print("Vânzări Laptop:", get_product_sales(valid_sales, "Laptop"))
print("Produse cu stoc critic:", critical_stock_products(stock_data))
input("Apasă Enter pentru a închide programul...")