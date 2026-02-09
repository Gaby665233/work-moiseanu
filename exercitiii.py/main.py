import sales_analysis as sa

sales = [
    {'name': 'Laptop', 'price': 85000},
    {'name': 'Phone', 'price': 50000},
    {'name': 'TV', 'price': 60000},
    {'name': 'Camera', 'price': 25000}
]

print("Total Revenue:", sa.total_revenue(sales))
print("Average Price of Products:", sa.average_price(sales))
print("Most Expensive Product:", sa.most_expensive(sales))
print("Cheapest Product:", sa.cheapest(sales))