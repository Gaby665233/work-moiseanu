# 1.Domeniul încorporat (Built-in Scope): Conţine funcţii şi valori Python încorporate, cum ar fi print(), len()
# 2.Domeniul global (Global Scope): Variabile definite în afara tuturor funcţiilor, disponibile în întreg programul.
# 3.Domeniul nelocal (Nonlocal Scope): Domeniu valabil în cadrul funcţiilor încorporate, însă nu cuprinde domeniul global.
# 4.Domeniul local (Local Scope): Variabile definite în cadrul funcţiilor, vizibile doar în acele funcţii.

# Sarcină: Să scriem un program în care se elimină un element inexistent în set.

# Ne vom reaminti de funcţia încorporată type() care ne afişează tipul de variabilă. Acum vom scrie propria noastră funcţie cu acelaşi nume./
#  Definim funcţia type() cu un parametru x, care listează "You entered x = ___". După ce definim această funcţie, o vom apela cu un anumit /
# număr şi vom compara rezultatul cu cel aşteptat.

# Întrebare pentru reflecție: Care dintre funcţii a fost apelată, încorporată sau nou definită? De ce?

# Hint: La definirea variabilei cu acelaşi nume ca funcţia încorporată type(), am pierdut posibilitatea să folosim aceeaşi funcţie, /
# însă nu am eliminat-o. În acest caz, compilatorul a căutat mai întâi în comanda type(x) domeniul local şi a găsit numele dat.

# Să vedem soluţia:

def type(x):
    print(f"You entered x = {x}")
type(5)


# AM FACUT SA MI REAMINTESC
def numar(x,y):
    formula = x * y
    return formula
    
    # SAU
def numar(x, y):
    return x * y


print(numar(6,4))
# SAU
rezultat = numar(20,2)
print(rezultat)




# ASTA ESTE FACUTA TOT PT MINE SA INTELEG MAI BINE
def y(n,m):
    return n + m
n = 20
m = 2
rezulta = y(n,m)
print(f"se aduna {n} cu {m} si rezultatul este {rezulta}")


# La definirea variabilei cu acelaşi nume ca funcţia încorporată type(), am pierdut posibilitatea să folosim aceeaşi funcţie/
# , însă nu am eliminat-o. În acest caz, compilatorul a căutat în comanda type() mai întâi domeniul local şi a găsit numele /
# dat. Dacă vrem în continuare să folosim funcţia încorporată type(), va trebui să definim în ce domeniu se găseşte. Acest /
# lucru se rezolvă folosind modulul builtins (modul care conţine toate funcţiile încorporate, care trebuie introdus manual în program).
# import builtins
import builtins
def type(x):
    print(f"You entered x = {x}")

x = 1
print(builtins.type(x))  # calls the built-in type() function
type(x)  # calls our new type() f


# Domeniul global (Global Scope)

# Domeniul global se referă la variabile definite în afara tuturor funcţiilor şi claselor, de obicei în vârful modulului./
#  Aceste variabile sunt disponibile din toate funcţiile şi clasele din modul, cu excepţia cazului în care sunt definite local. De exemplu:

x = 20  # Global variable

def function():
    print(x)  # Accesses the global variable

function()


# Domeniul închis (nelocal) (Enclosing Scope)
# Domeniul nelocal se referă la variabile definite în funcţii externe care sunt disponibile funcţiilor încorporate (interne)./
#  Atunci când variabila din funcţia externă se foloseşte în funcţia încorporată, o putem modifica cu ajutorul cuvântului-cheie/
#  nonlocal, prin care semnalizăm clar că nu aparţine domeniului local al funcţiei interne.

# De exemplu:


def function_outer():
    x = 5  # Defined in the enclosing scope (outer function)
    def function_inner():
        nonlocal x  # Accesses the variable from the enclosing scope
        x = 10
        print(f"Inside inner function x = {x}")
    function_inner()
    print(f"Inside outer function x = {x}")
function_outer()



# Domeniul local (Local Scope)
# Domeniul local se referă la nume (variabile, funcţii) definite în cadrul funcţiei, clasei sau a modulului curent./
#  Variabilele definite în acest domeniu sunt disponibile doar în cadrul funcţiei respective sau a clasei şi nu se pot folosi în afara ei.

def function():
    x = 10  # Local variable, accessible only within the function
    print(x)

function()



# Atunci când Pyhon caută valoarea variabilei, urmează regula LEGB care defineşte ordinea căutării în diferite domenii:

# L – Local (Domeniul local): Python caută mai întâi variabile în domeniul local al funcţiei curente.
# E – Enclosing (Domeniul închis): Dacă variabila nu s-a găsit la nivel local, se va căuta în domeniul funcţiei externe (în cazul funcţiilor imbricate).
# G – Global (Domeniul global): Dacă variabila nu este în domeniul local sau în domeniul închis, Python o caută în domeniul global al modulului.
# B – Built-in (Domeniul încorporat): Dacă variabila nu se găseşte în niciunul dintre domeniile anterioare, Python caută domeniul încorporat cu /
# funcţii precum print() şi len().
# De exemplu:


x = "global"

def outer():
    x = "enclosing"

    def inner():
        x = "local"
        print(x)  # Displays "local" because it's a local variable in the inner function

    inner()
    print(x)  # Displays "enclosing" because `inner` has completed, returning to `outer`

outer()
print(x)  # Displays "



# VARIANTA PT MINE FARA GLOBAL
total_sales = 1000

def update_sales(current_total, new_sale):
    return current_total + new_sale  # returnează noul total

# Apelăm funcția și reasignăm valoarea
total_sales = update_sales(total_sales, 500)

print(total_sales)
# CU GLOBAL



total_sales = 1000

def update_sales(new_sale):
    global total_sales
    total_sales += new_sale
update_sales(500)
print(total_sales)  # Now total_sales is 1500




def create_discount():
    discount = 0.1
    def apply_discount():
        nonlocal discount
        discount += 0.05
    apply_discount()
    return discount

print(create_discount())


# DACA PUN EGAL SE INLOCUIESTE
def create_discount():
    discount = 0.1
    def apply_discount():
        nonlocal discount
        discount = 0.05
    apply_discount()
    return discount

print(create_discount())




# Context: Alex vrea să conceapă un sistem de monitorizare şi actualizare a stocurilor de diferite produse. /
# El trebuie să creeze un program care foloseşte /;
# funcţii şi diferite domenii ale variabilelor pentru actualizarea şi afişarea informaţiilor privind stocurile.

# Instrucţiuni: Cum rezolvăm această provocare?

# Definim variabila globală total_stock, care reprezintă stocul iniţial al tuturor produselor.
# Creăm funcţia add_to_stock(), care foloseşte cuvântul-cheie global pentru a actualiza valoarea total_stock pentru cantitatea dată.
# Creăm funcţia check_stock(), care listează valoarea curentă total_stock.
# Creăm funcţia order(), care reduce valoarea lui total_stock pentru cantitatea de comenzi, monitorizează /
# variabila locală total_price şi calculează preţul comenzii. Dacă stocul nu este suficient, funcţia /
# listează mesajul privind stocul epuizat. (Hint: Preţul produselor trebuie definit în cadrul funcţiei folosind variabila locală).
# Programul principal:
# iniţializăm variabila globală total_stock la o valoare iniţială (de exemplu, 100).
# apelăm funcţiile add_to_stock(), check_stock() şi order() pentru demonstrarea gestionării stocurilor şi /
# folosirea diferitelor domenii ale variabilelor.

total_stock = 100
def add_to_stock(quantity):
    global total_stock
    total_stock += quantity
    print(f"sunt {quantity} in stock")
def check_stock():
    print(f"stocul curent este de {total_stock}")

def order(product, quantity):
    global total_stock
    product_prices = {
        'Laptop': 80000,
        'Mouse': 1500,
        'Keyboard': 5000,
        'Monitor': 20000
    }
    if product in product_prices:
        unit_price = product_prices[product]
        if quantity <= total_stock:
            total_stock -= quantity
            total_price = unit_price * quantity  # Local variable
            print(f"Order: {product} x{quantity} units. Total price: {total_price} dinars.")
        else:
            print(f"Not enough stock for {product}. Available: {total_stock} units.")
    else:
        print(f"Product {product} not found.")

# Main program
check_stock()
add_to_stock(50)
check_stock()
order('Laptop', 20)
check_stock()
order('Mouse', 150)
check_stock()
