# Să îl ajutăm pe Alex să creeze un modul numit Calculator care conţine patru funcţii aritmetice de bază: adunarea,/
#  scăderea, înmulţirea şi împărţirea. Apoi, Alex testează funcţionalitatea modulului într-un alt program Python.

# Sarcină:

# Să creăm modulul Calculator: Creăm modulul Calculator.py. În el trebuie definite patru funcţii:/
#  add(a, b), add(a, b), multiply(a, b) şi devide(a, b). /
# (Hint: Funcţia devide trebuie să verifice dacă divizorul este zero şi, dacă da, să returneze mesajul corespunzător).
# Să testăm modulul Calculator: Creăm un nou fişier de testare (test_calculator.py).

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def devide(a, b):
    if b == 0:
        return "Error: Division by zero!"
    else:
        return a / b

