import random

class Quesiti:
    def __init__(self,testo,difficolta,rispostacorretta,risposta1,risposta2,risposta3):
        self.testo=testo
        self.difficolta = difficolta
        self.rispostacorretta = rispostacorretta
        self.risposte=[risposta1,risposta2,risposta3,rispostacorretta]

class Persone:
    def __init__(self,nome,punti):
        self.nome = nome
        self.punti = punti

def listadomande(file):
    file = open(file, "r")
    domande = []
    domandequiz = []
    for i in file.readlines():
        if i != "\n":
            domande.append(i.replace("\n", ""))
    i = 0
    while i != len(domande):
        testo = domande[i]
        difficolta = int(domande[i + 1])
        rc = domande[i + 2]
        rs = [domande[i + 3], domande[i + 4], domande[i + 5]]
        dom = Quesiti(testo, difficolta, rc, rs[0], rs[1], rs[2])
        domandequiz.append(dom)
        i = i + 6
    file.close()
    return domandequiz


def gioco(massimo,domande):
    k = 0
    while k != massimo:
        sublist = []
        for i in domande:
            if i.difficolta == k:
                sublist.append(i)
        random.shuffle(sublist)
        d = sublist[0]
        random.shuffle(d.risposte)
        print(d.testo)
        n = 1
        c = 0
        for i in d.risposte:
            if i.__eq__(d.rispostacorretta):
                c = n
            print(f'{n}. {i}')
            n = n + 1
        r = input("inserisci risposta:")
        if int(r) == c:
            k = k + 1
        else:
            print(f"risposta sbagliata, quella corretta era {c}")
            break
    print()
    print(f'punteggio raggiunto {k}')
    nickname = input("inserire nickname:")
    return Persone(nickname,k)

def personepresenti(file):
    punti = open("punti.txt", "r")
    persone = []
    for i in punti.readlines():
        i.strip("\n")
        p = Persone(i.split(" ")[0],int(i.split(" ")[1]))
        persone.append(p)
    punti.close()
    return persone

def scrivi_nel_file(file,persone):
    punteggi = open(file, "w")
    c=0
    for i in persone:
        if c ==0:
            punteggi.write(f'{i.nome} {i.punti}')
            c+=1
        else:
            punteggi.write(f'\n{i.nome} {i.punti}')




domande = listadomande("domande.txt")
massimo = max([v.difficolta for v in domande])
player = gioco(massimo,domande)
persone_presenti =personepresenti("punti.txt")
persone_presenti.append(player)
ordinamento_per_punteggio = sorted(persone_presenti,key=lambda x:x.punti,reverse=True)
scrivi_nel_file("punti.txt",ordinamento_per_punteggio)



