from collections import deque

# Crearea unei cozi goale
queue = deque()

# Adăugarea de elemente la o coadă
queue.append("Task 1")
queue.append("Task 2")
queue.append("Task 3")

# Eliminarea elementelor din coadă (FIFO)
print(queue.popleft())  # Output: Task 1
print(queue.popleft())  # Output: Task 2


print_queue = []  # Initializing the queue as an empty list

# Adding elements to the queue
print_queue.append("TV")
print_queue.append("Monitor")
print(f"Queue after adding items: {print_queue}")

next_item = print_queue.pop(0)  # Removing the first element
print(f"Processed item: {next_item}")
print(f"Queue after removal: {print_queue}")

print_queue.append("TV")
print_queue.append("Monitor")

# Checking if the queue is empty
if len(print_queue) == 0:
    print("Queue is empty.")
else:
    print("Queue is not empty.")

print_queue = ["TV", "Mouse", "Camera"]


print("_______________--------------------------_________________")
# Peek at the first element without removing it
if print_queue:  # Checking if the queue is not empty
    first_el = print_queue[0]
    print(f"The first document in the print queue is: {first_el}")
else:
    print("The queue is empty.")

 




#  O listă simplă în Python poate fi folosită ca o coadă: adăugând elemente la sfârșitul listei și /
# eliminând elemente de la început, simulăm o coadă pe principiul FIFO. Deși acest lucru este simplu,/
#  este important să ținem cont că pentru cozile foarte mari poate exista o scădere a performanței.

queue = [] 
queue.append("Telephone") 
queue.append("Smart TV") 
queue.append("Video camera") 
print("Queue after adding items:", queue)  # Displays: ['Telephone', 'Smart TV', 'Video camera']

queue.pop(0)  # Removes the first element
print("Queue after removal:", queue)  # Displays: ['Smart TV', 'Video camera']


print("-----EXEmPLU----")
customers = []

customers.append("anais")
customers.append("bogdan")
customers.append("stefanut")
customers.append("celestea")
customers.append("batman")
print("coada:", customers)
 
while len(customers) > 0:
    next_customers = customers.pop(0)
    print("urmatorul este:", next_customers)
    print("coada:", customers)



# Pentru lucrul mai eficient cu cozile, Python oferă deque (double-ended queue) din modulul collections,/
#  care permite adăugarea și eliminarea mai rapidă a elementelor de pe ambele părți ale listei.

# Pentru a putea folosi această structură, este necesar să scriem următoarea linie de cod chiar la începutul scriptului Python:

# from collections import deque

# prin care specificăm că vom folosi un modul extern. Despre acesta și despre multe alte module vom discuta/
#  mai mult într-una dintre lecțiile următoare ale acestui curs.

from collections import deque 

# Initializing a deque
que = deque() 
que.append('Apple') 
que.append('Mango') 
que.append('Banana') 

# Displaying the deque
print(que) 

# Removing elements from the left side
print(que.popleft())  # Removes 'Apple'
print(que.popleft())  # Removes 'Mango'
print(que.popleft())  # Removes 'Banana'


print("------------___________________-----------------")



# Alex trebuie să creeze un sistem pentru o coadă virtuală pentru a cumpăra un iPhone nou, în care clienții intră/
#  la capătul cozii și primul client este servit după principiul FIFO.

# A implementat următoarele funcții:

# Funcția add_to_queue(name) – adaugă numele clientului (sub formă de string) la sfârșitul cozii.
# Funcția serve_customer() – elimină primul client (dacă coada nu este goală) și afișează un mesaj despre servire./
#  Dacă coada este goală, funcția ar trebui să afișeze mesajul "No more customers in the queue".
# Funcția display_queue() – afișează toți clienții actuali din coadă. Dacă coada este goală, funcția ar trebui să afișeze "The queue is empty".
# Funcția main_program() – programul principal care permite selectarea opțiunii de lucru cu coada:
# adăugarea unui client la coadă;
# servirea clientului;
# vizualizarea cozii curente;
# întreruperea programului;
# Alex folosește o buclă pentru a permite executarea mai multor acțiuni până când selectăm  opțiunea de întrerupere.
print("-----------------")
coada = []

def ad_quaue(name):
    coada.append(name)
    print(f"{name} a fost adaugat")

def serve_customer():
    if coada:
        name = coada.pop(0)
        print(f"{name} a fost servit")
    else:
        print("The queue is empty")

def display_queue():
    if coada:
        print("coada curenta")
        for i, name in enumerate(coada, start=1):
            print(f"{i}.{name}")
    else:
        print("The queue is empty")

def main_program():
    while True:
        print("\nselecteaza o actiune")
        print("1.adauga un client la coada")
        print("2.servirea clientului")
        print("3.vizualizarea cozii curente")
        print("4.Exit")

        alege = input("alege o cifra:")

        if alege == '1':
            name = input("alege numele clientului:")
            ad_quaue(name)
        elif alege == '2':
            serve_customer()
        elif alege == '3':
            display_queue()
        elif alege == '4':
            print("problema rezolvata")
            break
        else:
            print("introdu un numar intre 1-4")
        

main_program()



    
