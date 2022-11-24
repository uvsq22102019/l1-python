carre_mag = [[4, 14, 15, 7], [9, 7, 6, 12], [5, 11, 10, 8], [16, 2, 3, 13]]
carre_pas_mag = []


def afficheCarre(carre):
    """ Affiche la liste à 2 dimensions carre comme un carré"""
    for num_ligne in range(len(carre_mag)):
        carre_pas_mag.append([])
        for num_colonne in range(len(carre_mag[num_ligne])):
            carre_pas_mag[num_ligne].append(carre_mag[num_ligne][num_colonne])
    carre_pas_mag[3][2] = 7


afficheCarre(carre_mag)
afficheCarre(carre_pas_mag)



