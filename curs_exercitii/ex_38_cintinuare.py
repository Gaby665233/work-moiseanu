coada = []

def ad_quaue(name):
    coada.append(name)
    print(f"{name} a fost adaugat")

def serve_customer():
    if coada:
        customer = coada.pop(0)
        print(f"{customer} a fost servit")
    else:
        print("The queue is empty")

def display_queue():
    if coada:
        print("coada curenta")
        for i, customer in enumerate(coada, start=1):
            print(f"{i}.{customer}")
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