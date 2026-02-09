comentarii = [
    "Excelent!",
    "Livrare rapida si serviciu excelent.",
    "Prea scump",
    "Campania a fost excelenta.",
    "Problema cu comanda.",
    "Totul este în regula.",
    "Usor de comandat, multumesc!"
]

for comentariu in comentarii:
    if " " not in comentariu:
        print(f"Comentariul simplu a fost sarit: '{comentariu}'")
        continue
    print(f"Comentariul '{comentariu}' este ok.")
 
    if "problema" in comentariu.lower():
        print(f"Comentariu suspect gasit: '{comentariu}'. Intrerupem analiza.")
        break
   
    print(f"Analizam comentariul: '{comentariu}'")



# Mini activitate: Revizuirea datelor de vânzări

# Sarcina: Alex urmărește comentariile utilizatorilor și le analizează în funcție de pozitivitate. Să ne imaginăm că are o listă de comentarii /
# care conțin diferite evaluări. El dorește:

# să sară peste comentariile cu o evaluare mai mică de 3, deoarece nu le consideră suficient de pozitive pentru /
# o analiză ulterioară (folosind continue);
# să întrerupă revizuirea comentariilor de îndată ce întâlnește o evaluare de 5, deoarece acel comentariu ar putea fi/
# excelent pentru a fi evidențiat ca exemplu pentru echipă (folosind break).
#  Instrucțiuni:

# Să creăm o listă de evaluări ale comentariilor, de exemplu, evaluari_comentarii = [4, 2, 3, 5, 1, 3, 4].
# Să folosim buclă for pentru a trece prin toate evaluările.
# Să sărim peste toate comentariile cu o evaluare mai mică de 3 folosind continue.
# Dacă întâlniți o evaluare de 5, întrerupeți revizuirea comentariilor folosind break.
# Afișați doar evaluările care nu au fost sărite sau întrerupte.
#  Întrebare pentru reflecție: Ce s-ar întâmpla dacă Alex ar dori să revizuiască toate comentariile cu evaluări de/
# 3 sau mai mari, dar să le înregistreze doar pe cele cu evaluarea de 5? Cum ar influența această modificare logica codului său?


evaluari_comentarii = [4, 2, 3, 5, 1, 3, 4]



for i in evaluari_comentarii:
    if i < 3:
        print(f"a scazut de {i}")
        continue
    elif i == 5:
        print(f"Excelet {i}")
        break
    else:
       print(f"pozitive {i}")



# fara print continue sare peste acel ceva ex la mine sare si nu mai prineteaza

for i in evaluari_comentarii:
    if i < 3:
        continue
    elif i == 5:
        print(f"Excelet {i}")
        break
    else:
       print(f"pozitive {i}")

# v2

evaluari_comentarii = [4, 2, 3, 5, 1, 3, 4]

for evaluare in evaluari_comentarii:
    if evaluare < 3:
        continue  # sărim comentariile prea slabe
    if evaluare == 5:
        print(f"Evaluare excelentă: {evaluare} - Oprim analiza")
        break  # oprim revizuirea la evaluarea de 5
    print(f"Evaluare pozitivă: {evaluare}")