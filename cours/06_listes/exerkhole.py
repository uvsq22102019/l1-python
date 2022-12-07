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


u = int(input("Choisir un nombre dans la liste dans la liste: [2; 16; 18; 21; 29; 36; 57; 62; 77; 81; 105]"))


def nombre_supérieur(liste):
    liste_sup = []
    for i in range (len(liste)):
        if (u < liste[i]):
            liste_sup.append(liste[i])
    print(liste_sup)
nombre_supérieur([2, 16, 18, 21, 29, 36, 57, 62, 77, 81, 105])



carre_mag = [[4, 14, 15, 7], [9, 7, 6, 12], [5, 11, 10, 8], [16, 2, 3, 13]]
carre_pas_mag = []
for num_ligne in range(len(carre_mag)):
    carre_pas_mag.append([])
    for num_colonne in range(len(carre_mag[num_ligne])):
        carre_pas_mag[num_ligne].append(carre_mag[num_ligne][num_colonne])
carre_pas_mag[3][2] = 7
def afficheCarre(carre):
    """ Affiche la liste à 2 dimensions carre comme un carré"""
    for ligne in carre:
        print(ligne)
    print()

afficheCarre(carre_mag)
afficheCarre(carre_pas_mag)



sum_ligne = 0
for element in range (0, len(num_ligne)):
        sum_ligne += num_ligne[element]

