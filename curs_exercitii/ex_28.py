def saluta(nume):
    return f"Salut, {nume}  !"

persoana = "Ana"
mesaj = saluta(persoana)
print(mesaj)





# Alt exemplu


def prezinta(nume, varsta):
    return f"Salut, {nume}! Ai {varsta} de ani."

mesaj = prezinta("Ana", 20)
print(mesaj)


# varianta fara def

nume = "Ana"
varsta = 20
mesaj = f"Salut, {nume}! Ai {varsta} de ani."
print(mesaj)




