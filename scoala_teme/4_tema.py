def numara_vocale(nume):
    vocale = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    contor = 0

    for caracter in nume:
        if caracter in vocale:
            contor += 1

    return contor


while True:
    nume_client = input("Introduceți numele clientului: ")

    numar_vocale = numara_vocale(nume_client)

    print(f"Numărul de vocale din nume este: {numar_vocale}")

    if numar_vocale == 0:
        print("Numele introdus nu conține vocale.")
        break
