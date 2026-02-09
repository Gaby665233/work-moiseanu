variabila = 20 # variabila
print(variabila)
## declaratie -> cu litera mica


def functie(): # functie
    x = 10
    print(x)

functie()
functie()
functie()
functie()
functie()




print("-=-=-=-=-=-=")

def functie():   # functie
    x = 10
    print(x)

rezultat = functie()
print(rezultat)

# sa nu aviseze note punem return

print("\nnaruto usimeia\n")



def functie():
    x = 10
    return x
rezultat = functie()
print(rezultat)

print("-=-=-=--=")
class Clasa:
    # atribut
    atribut = 20
    def metoda(self):
        x = 10
        print(x)
        print(Clasa.atribut)

# creăm un obiect
obj = Clasa()

# apelăm metoda
obj.metoda()

lista = []
if not lista:
      print("Adevarat")
else:
      print("Fals")


print("=-=-=-=-=")


def min_max(lista):
    if not lista:
        return "Lista este goala"
    
    minim, maxim = lista[0], lista[0]

    for i in lista:
        if i > maxim:
            maxim = i
        if i < minim:
            minim = i

    return minim, maxim


l = [ 42 , 13 , 61 , 2 , -42, 868 , 1, -11 , -32, 300]
print(min_max(l))

print(min_max([]))

# AICI AM REFaCUT EU
def min_max(lista):
    if not lista:
        return "lista e goala"
    minim, maxim = lista[0] , lista[0]

    for i in lista:
        if i > maxim:
            maxim = i
        if i < minim:
            minim = i

    return minim ,  maxim
l = [ 42 , 13 , 61 , 2 , -42, 868 , 1, -11 , -32, 300]
print(min_max(l))


l = [ 42 , 13 , 61 , 2 , -42, 868 , 1, -11 , -32, 300]
print(min(l), max(l))

## AICI "min" este o functie built in 
print(min([312, 321, 51, 10, 0]))

## AICI "min" este o variabila
# min = 10
# print(min([312, 321, 51, 10, 0]))
# si da eroare


## list o functie built-in (vine instalata cu Python)
print(list("telefon"))


# la fel si aici devine variabiala si da eroare
# list = ["dsa", "3"]
# print(list("telefon"))
print("-=-=-=-=")

def adunare(x, y):
    print(x + y)

adunare(2, 3)


def scadere(x, y):
    return x - y

rezultat = scadere(10, 1)
print(rezultat)


print("________---Cand se foloseste return si cand nu-------------__________")
def functie():   # functie
    x = 10
    print(x)
# aici fac fara return cand vreau doar sa printez adica fara
# rezultat = functie()
# print(rezultat)
# pwntru ca aici apare nope

print("----Prin return nu mai apare nope-----")

def functie():
    x = 10
    return x
rezultat = functie()
print(rezultat)




lista = ["apa", "mancare", "somn", "pastile"]

for i in lista:
    if not len(i) > 5:
        print("Este mai mic ")
        break
    else:
        print("Mai mare")



def filtrare_cuvinte(lista):
    lista = ["apa", "mancare", "somn", "pastile"]
    lista_noua = []
    for i in lista:
        if len(i) > 5:
            lista_noua.append(i)
    return lista_noua



lista = ["apa", "mancare", "somn", "pastile"]
print(filtrare_cuvinte(lista))


print("#" * 10)
print("#" + " " * 10 + "#")
print("#" * 10)

print("--------=-=-=-=-=Scmeker-=-=-=-=-=-")


print("#" * 10)
print("#" + " " * 8 + "#")
print("#" * 10)

print("#" * 10)
print("#" + " " * 8 + "#")
print("#" + " " * 8 + "#")
print("#" + " " * 8 + "#")
print("#" * 10)


print("#" * 10)
for i in range(8):
    print("#" + " " * 8 + "#")
print("#" * 10)



width = 10


print("#" * width)
for i in range(8):
    print("#" + " " * (width - 2) + "#")
print("#" * width)




width = 20


print("#" * width)
for i in range(8):
    print("#" + " " * (width - 2) + "#")
print("#" * width)



width = 20
height = 10

print("#" * width)
for i in range(height-2):
    print("#" + " " * (width - 2) + "#")
print("#" * width)


width = 20
height = 5

print("#" * width)
for i in range(height-2):
    print("#" + " " * (width - 2) + "#")
print("#" * width)


width = 3
height = 5

print("#" * width)
for i in range(height-2):
    print("#" + " " * (width - 2) + "#")
print("#" * width)



def render(width, height):
    print("#" * width)
    for i in range(height-2):
        print("#" + " " * (width - 2) + "#")
    print("#" * width)
render(10, 10)

print("-=-=-=-=-=-")


def salut():
    print("Salut")
salut()

class Persoana:
    def salut(self):
        print("Salut")

p = Persoana()
p.salut()


def mareste(x):
    return x + 1

print(mareste(5))  # 6
# Cu clasă:
# python
# Copiază codul
class Contor:
    def __init__(self):
        self.valoare = 0

    def mareste(self):
        self.valoare += 1

c = Contor()
c.mareste()
c.mareste()
print(c.valoare)  # 2


print("-=-=-=-=-=454545-=-=-=-=")



def render_producedural(width, height):
    print("#" * width)
    for i in range(height-2):
        print("#" + " " * (width - 2) + "#")
    print("#" * width)

render_producedural(10, 10)




class Printer:
    
    ## metoda (trebuie sa aibe acel self, daca nu, nu functioneaza)
    def render(self, width, height):
        print("#" * width)
        for i in range(height-2):
            print("#" + " " * (width - 2) + "#")
        print("#" * width)


## Un obiect (instanta)
obiect = Printer()
obiect.render(10, 10)
obiect.render(20, 30)



class Printer:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    
    ## metoda (trebuie sa aibe acel self, daca nu, nu functioneaza)
    def render(self):
        print("#" * self.width)
        for i in range(self.height-2):
            print("#" + " " * (self.width - 2) + "#")
        print("#" * self.width)


## Un obiect (instanta)
obiect = Printer(10, 20)
obiect.render()


obiect2= Printer(3, 3)
obiect2.render()



