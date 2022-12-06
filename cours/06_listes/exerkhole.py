chaine1 = "chaussette"


def occurence(chaine1):
    n = len(chaine1)
    L = []
    for i in range(0, n):
        if chaine1[i] not in L:
            L.append(chaine1[i])
            
            print([chaine1.count(chaine1[i])])

occurence(chaine1)



def compteur_lettres(chaine) :
    """ Renvoie une liste de couples (lettre, nb_apparition), pour indiquer combien de fois est
        présente chaque lettre"""
    liste_compteur = []
    s = set(chaine)
    for e in s :
        liste_compteur.append([e, chaine.count(e)])
    print(liste_compteur)
        
ma_chaine = 'abracatambra'
compteur_lettres(ma_chaine)


lap = [5, 6, 7]
n = 8

def max(lap):
    if lap[0] > n:
        print(lap[0:3])
    elif lap(1) > n:
        print(lap[1:2])
    elif lap(2) > n:
        print(lap[2])
    else:
        print(max(n))

max(n)

