def syracuse(n: int):
    liste = [n]
    while n != 1:
        if n % 2 == 0:
            n  = n //  2 
        else:
            n = n * 3 + 1
        liste.append(n)
    return liste


print(syracuse(3))


def testeConjecture(n_max):
    """ Teste la conjecture de Collatz pour toutes les valeurs de 1 à n_max """
    for i in range (1, n_max + 1):
       syracuse (i)
    return True


print(testeConjecture(10000))


def tempsVol(n: int):
    """ Retourne le temps de vol de n """
    return len(syracuse(n)) - 1

print("Le temps de vol de", 3, "est", tempsVol(3))


def tempsVolListe(n_max):
    """ Retourne la liste de tous les temps de vol de 1 à n_max """
    liste = []
    liste = [tempsVol(i) for i  in range(1, n_max + 1)]
    return liste

print(tempsVolListe(100))


max = 0
for i in range(1, 10000 + 1):
    max = [tempsVol(i) ]
print(max(max))