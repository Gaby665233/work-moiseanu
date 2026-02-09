stack = []

# append() function to push elements onto the stack
stack.append('notepad')
stack.append('balloon')
stack.append('Iphone')
print('Stack:')
print(stack)

# pop() function to pop elements from stack in LIFO order
print('Elements popped from stack:')
print(stack.pop())
print(stack.pop())
print(stack.pop())

# Display the stack after all pops
print(stack)


stack = []

# append() function to push elements onto the stack
stack.append('notepad')
stack.append('balloon')
stack.append('Iphone')
print('Stack:')
print(stack)
while len(stack)>0:
    cite = stack.pop()
    print(cite)
    print(stack)

print("-------_____________---------")


from collections import deque

# Creating a stack as an empty list
stack = deque()

# append() function to push element in the stack
stack.append('iPhone')
stack.append('mouse')
stack.append('tv')

print('Stack:')
print(stack)

# pop() function to pop  element from stack in  LIFO order
print('Elements popped from stack:')
print(stack.pop())
print(stack.pop())
print(stack.pop())

print(stack)


# Exemplu: Gestionarea modificărilor produselor în vânzările online

# Alex actualizează în mod regulat informațiile despre produse pe site-ul companiei, inclusiv prețurile și descrierile. /
# În timpul unor reduceri sezoniere majore, Alex trebuie să schimbe rapid prețurile a sute de produse. Conștient de /
# posibilele erori care pot apărea, el decide să implementeze un stack, ca să poată anula cu ușurință cele mai recente /
# modificări dacă apare o eroare.

# De ce este util stack în această situație?

# Stack îi permite lui Alex să adauge fiecare modificare ca acțiune în partea de sus a „grămezii” de modificări,/
#  pe baza principiului „ultimul intrat, primul ieșit” (LIFO). Dacă observă o greșeală, poate anula rapid ultimele/
#  modificări introduse – eliminându-le pur și simplu din partea de sus a stack-ului.

# Cum funcționează acest lucru în practică?

# Când un script modifică prețul sau descrierea unui produs, acea modificare se adaugă la stack.
# Dacă Alex observă că a apărut o eroare, poate elimina cu ușurință ultima acțiune și poate întoarce sistemul la starea anterioară.
# În felul acesta, toate modificările sunt reversibile, ceea ce reduce riscul de informare incorectă pe site.
# Această abordare nu numai că economisește timp, dar reduce și riscul de nemulțumire a clienților din cauza informațiilor /
# incorecte. Folosind stack, Alex gestionează eficient o serie de modificări și se asigură că fiecare modificare poate fi/
#  anulată cu ușurință dacă este necesar, ceea ce este vital într-un mediu dinamic de vânzări online.

# Codul pentru gestionarea modificărilor cu stack

# Initializing an empty stack to track changes
changes = []

# Function to add a new change to the stack
def add_change(change):
    changes.append(change)
    print(f"Change added to stack: {change}")

# Function to undo the last change
def undo_last_change():
    if changes:
        last_change = changes.pop()
        print(f"Undone change: {last_change}")
    else:
        print("No changes to undo.")

# Function to display the current state of the stack
def display_stack():
    print("Current changes in stack:", changes)

# Example usage
add_change("Change in price of product A")
add_change("Change in description of product B")
add_change("Change in price of product C")

# Displaying state after adding changes
display_stack()

# Undoing the last change
undo_last_change()

# Displaying state after undoing
display_stack()

# Undoing additional changes if needed
undo_last_change()
display_stack()
undo_last_change()

# Final state of the stack
display_stack()

# Explicaţie:

# Inițializare:
# Lista de modificări este folosită ca un stack pentru a stoca toate modificările pe care Alex le face prețurilor și descrierilor produselor.

# Funcția add_change(change):
# Fiecare modificare este adăugată în partea de sus a stack-ului folosind metoda append(). Acest lucru asigură faptul/
#  că cele mai recente modificări sunt în partea de sus, făcându-le mai ușor de anulat.

# Funcția undo_last_change():
# Când Alex vrea să anuleze ultima modificare, apelează această funcție. Utilizează operația pop(), care elimină ultimul/
#  element din stack. În felul acesta, Alex poate reveni rapid și ușor la starea anterioară a sistemului.

# Dacă stack este gol, este listat mesajul că nu există modificări de anulat.

# Afișarea Stack-ului display_stack():
# Această funcție afișează modificările curente care se află pe stack, ceea ce ajută la urmărirea modificărilor rămase.

# Exemplu de utilizare:
# În cod sunt simulate mai multe modificări (Modificarea prețului produsului A, Modificarea descrierii produsului B etc.).

# După aceea, se anulează ultima modificare și apoi se afișează starea stack-ului, permițându-i lui Alex să evalueze rapid starea.

# Această abordare îi permite lui Alex să gestioneze eficient schimbările și să asigure o revenire rapidă la starea anterioară/
#  în cazul unei erori – ceea ce este crucial pentru lucrul într-un mediu dinamic de vânzări online.