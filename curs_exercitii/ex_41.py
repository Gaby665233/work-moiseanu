

try:
    x = 100 / 0
except :
    print("Hey, you can't divide by zero!")

# try:
#     x = 100 / 0
#     y = 10 
# except:
#     print("Hey, you can't divide by zero!")
# print(y)

# Aici, Alex aşteaptă ca variabila y să fie definită în blocul try, dar din cauza erorii din expresia x = 100 / 0, /
# Python a ieşit din blocul try înainte ca y să fie valoarea atribuită. Rezultatul este "NameError: name 'y' is not defined",/
#  ceea ce înseamnă că Python a revenit la partea principală de cod fără existenţa variabilei y. 


# try:
#     str1 = (input("Enter the first string: "))
#     str2 = (input("Enter the second string: "))
#     result = str1 / str2
    

# except:
#     print("Division of strings is not possible.")




# try:
#     x=100/0

# except NameError:
#     print("Hey, you can't divide by zero!")




# Vom primi mesajul: ZeroDivisionError: division by zero. Motivul este că am folosit obiectul NameError,/
#  al cărui scop era să monitorizeze variabilele declarate eronat, în timp ce noi trebuie să monitorizăm/
#  dacă s-a efectuat împărţirea la zero. Prin urmare, dacă am folosi logica acestui exemplu, ar trebui să /
# folosim şi obiectul ZeroDivisionError, deoarece el apare la împărţirea la zero; deci, codul corectat ar arăta astfel:


try:
    x=100/0

except ZeroDivisionError:
    print("Hey, you can't divide by zero!") 


# Dacă întâmplător bănuim că ar exista mai multe tipuri de erori, ceea ce se poate întâmpla frecvent, în Python putem folosi mai multe blocuri except.
print("-------=============-----------")
try:
    x=100/0

except NameError:
    print("You won't see me!")

except ZeroDivisionError:
    print("Hey, you can't divide by zero!")

except Exception:
    print("I'm here just in case you didn't find anything")


# Sarcină: Să îl ajutăm pe Alex să creeze un program care va aduna numerele şi care repetă intrarea până ce/
#  utilizatorul introduce corect ambele numere. Dacă utilizatorul introduce din greşeală un anumit text, /
# programul va afişa mesajul corespunzător şi îi va oferi o nouă posibilitate de intrare.

# După eroare, programul trebuie să înceapă din nou execuţia, deci să repete inserarea numerelor.

# while True:
#     try:
#         nr_1 = int(input("introdu primul numar"))
#         nr_2 = int(input("introdu al doilea numar"))
#         rezultat = nr_1 + nr_2
#         print(f"rezultatul este {rezultat}")
#         break
#     except ValueError:
#         print("poti introduce doar cifre")

print("---________-------")
try:
    x=100
    y=0
    print(x/y)
except NameError:
    print("You won't see me!")
except ZeroDivisionError:
    print("Hey, you can't divide by zero!")
except Exception:
    print("I'm here just in case you didn't find anything")
finally:
    print("Value of y is: ",y)

# Sarcină: Să îl ajutăm pe Alex să modifice exerciţiul anterior în care scria un program, care solicită de la /
# utilizator să introducă două stringuri, apoi încearcă să le împartă, aşa că, /
# dacă se captează o excepţie de tip TypeError, se va lista mesajul: "Strings cannot be divided".

print("---===-")

# nr_1 = (input("introdu primul numar: "))
# nr_2 = (input("introdu al doilea numar: "))
# try:
#     rezult = nr_1 / nr_2
#     print(rezult)
# except TypeError:
#     print("nu este biner")


# raise Exception("My error!")

# De exemplu, Alex scrie o funcţie de împărţire care returnează o eroare atunci când numerele sunt mai mari decât 10./
# Python nu are are probleme cu numerele mari, însă Alex vrea o anumită limită ca parte a logicii de afaceri.
def divide(a,b):
    if b == 0:
        return 0
    else:
        return a/b

print(divide(14,2))

# Python, ca limbaj, nu are nicio treabă cu împărţirea numerelor mai mari decât zece, /
# adică nu va genera nicio excepţie dacă introducem un număr mai mare decât 10 în funcţie, /
# aşadar, această situaţie trebuie efectuată manual. Acest lucru se poate face în felul următor:


# print("-=-=-=-==")

# def divide(a,b):
#     if b == 0:
#         return 0
#     if a>10 or b>10:
#         raise ArithmeticError("Number is larger than 10")
#     else:
#         return a/b

# print(divide(14,2))


# Sarcină: Alex lucrează la un program care procesează adresele de e-mail ale clienţilor. /
# El vrea să se asigure că fiecare intrare conţine semnul '@', în caz contrar se va genera o excepţie şi se va lista mesajul: "Invalid email address"


# varianta gantita de mine
email_list = ["marko@example.com", "anaexample.com", "ivan@example.com"]
for i in email_list:
    if '@' not in i:
        print(f"eroare de emal {i}")
    else:
        print(f"email acceptat {i}")



def validate_email(email):
    if '@' not in email:
        raise ValueError("Invalid email address")

email_list = ["marko@example.com", "anaexample.com", "ivan@example.com"]

for email in email_list:

    try:
        validate_email(email)
        print(f"The email address {email} is valid.")
    except ValueError as e:
        print(f"Error: {e} ({email})")