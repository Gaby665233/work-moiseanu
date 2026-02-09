# Context: Alex a primit sarcina să analizeze datele de vânzări în cadrul companiei sale pentru a obţine nişte analize cheie – /
# venitul total, prețul mediu al produsului, precum și identificarea celor mai scumpe și mai ieftine produse. Pentru accelerarea /
# muncii şi evitarea repetării codului, Alex optează pentru crearea unui modul cu numele sales_analysis/
# . Acest modul va conţine funcţii specifice pentru analiza vânzării, pe care Alex le poate folosi în viitoarele proiecte.


def total_revenue(sales):
    """Calculates the total revenue based on product prices."""
    return sum(item['price'] for item in sales)

def average_price(sales):
    """Calculates the average price of products."""
    return total_revenue(sales) / len(sales) if sales else 0

def most_expensive(sales):
    """Finds the most expensive product in sales."""

    return max(sales, key=lambda x: x['price'], default=None)

def cheapest(sales):
    """Finds the cheapest product in sales."""
    return min(sales, key=lambda x: x['price'], default=None)