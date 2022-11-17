# temps[0] : jours, temps[1]: heures, temps[2]: minutes, temps[3]: secondes
import time


def tempsEnSeconde(temps: tuple) -> int:
    """ Renvoie la valeur en seconde de temps donné comme jour, heure, minute,
    seconde."""
    return temps[0] * 86400 + temps[1] * 3600 + temps[2] * 60 + temps[3]


temps = (3, 23, 1, 34)
print(type(temps))
print(tempsEnSeconde(temps))


def secondeEnTemps(seconde):
    """Renvoie le temps (jour, heure, minute, seconde) qui
    correspond au nombre de secondes passé en argument"""
    jours = seconde // 86400
    reste = seconde % 86400
    heures = reste // 3600
    reste = reste % 3600
    minutes = reste // 60
    reste = reste % 60
    secondes = reste  # optionnel car le reste au dessus= seconde
    return (jours, heures, minutes, secondes)  # ou return(j, h, min, reste)


temps = secondeEnTemps(100000)
print(temps[0], "jours", temps[1], "heures",
      temps[2], "minutes", temps[3], "secondes")


# fonction auxiliaire ici


def affichePluriel(nombre: int,  mot: str) -> None:
    if nombre > 0:
        print("", nombre, mot, end="")
    if nombre > 1:
        print("s", end="")


def afficheTemps(temps: tuple) -> None:
    affichePluriel(temps[0], "jour")
    affichePluriel(temps[1], "heure")
    affichePluriel(temps[2], "minute")
    affichePluriel(temps[3], "seconde")
    print()


afficheTemps((1, 0, 14, 23))


def demandeTemps() -> tuple:
    jours = -1
    heures = -1
    minutes = -1
    secondes = -1
    while (jours < 0):
        jours = int(input("Saisir un nombre de jours "))
    while (heures < 0 or heures >= 24):
        heures = int(input("Saisir un nombre d'heures "))
    while(minutes < 0 or minutes >= 60):
        minutes = int(input("Saisir un nombre de minutes "))
    while(secondes < 0 or secondes >= 60):
        secondes = int(input("Saisir un nombre de secondes "))
    return (jours, heures, minutes, secondes)


afficheTemps(demandeTemps())


def sommeTemps(temps1: tuple, temps2: tuple):
    return secondeEnTemps(tempsEnSeconde(temps1) + tempsEnSeconde(temps2))


afficheTemps(sommeTemps((2, 3, 4, 25), (5, 22, 57, 1)))


def proportionTemps(temps: tuple, proportion: float):
    return secondeEnTemps(int(tempsEnSeconde(temps) * proportion))


afficheTemps(proportionTemps(proportion=0.2, temps=(2, 0, 36, 0)))

# appeler la fonction en échangeant l'ordre des arguments


def tempsEnDate(temps):
    annee = 1970 + temps[0] // 365
    numero_de_jour = 1 + temps[0] % 365
    return(annee, numero_de_jour, temps[1], temps[2], temps[3])


def afficheDate(date: tuple = ()):
    if len(date) == 0:
        date = tempsEnDate(secondeEnTemps(int(time.time())))
    print("Jour numéro", date[1], "de l'année", date[0], "à",
         str(date[2]) + ":" + str(date[3]) + ":" + str(date[4]))


temps = secondeEnTemps(1000000000)
afficheTemps(temps)
afficheDate(tempsEnDate(temps))
afficheDate()

print(time.time())


def estbisextile(annee: int):
    return annee % 4 == 0 and (annee % 100 != 0 or annee % 400 == 0)


def bisextile(jours: int):
    annee = 1970
    while(jours >= 365):
        if estbisextile(annee):
            print("L'année" + str(annee) + "est bisextile")
            jours -= 366
        else:
            jours -= 365
        annee += 1


bisextile(20000)


def nombrebisextile(jours: int):
    annee = 1970
    compteur_bisextile = 0
    while(jours >= 365):
        if estbisextile(annee):
            compteur_bisextile += 1
            jours -= 366
        else:
            jours -= 365
        annee += 1
    return compteur_bisextile


def tempsEnDateBisextile(temps: tuple):
    jour, heure, minute, seconde = temps
    jour = jour - nombrebisextile(jour)
    temps_ajuste = (jour, heure, minute, seconde)
    return tempsEnDate(temps_ajuste)


afficheDate(tempsEnDateBisextile(secondeEnTemps(int(time.time()))))


# Question optionnelle : Gestion des mois dans l'affichage


def afficheDateV2(date: tuple()):
    if len(date) == 0:
        date = tempsEnDateBisextile(secondeEnTemps(int(time.time())))
    # On étblit deux listes: 
    # Une liste des noms de chaque mois
    nom_des_mois = ["Janvier", "Février", "Mars", "Avril", "Mai", "Juin",
                    "Juillet", "Aout", "Septembre", "Octobre", "Novembre",
                    "Décembre"]
    # Ainsi qu'une liste du nombre de jours de chaque mois
    nb_jours_des_mois = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    # Si l'année est bisextile, Février a un jour de plus
    if estbisextile(date[0]):
        nb_jours_des_mois[1] += 1

    mois = ""
    jour = date[1]
    # On parcourt les mois en retirant le nombre de jours de chaque mois à la 
    # variable jour
    for i in range(12):
        if jour <= nb_jours_des_mois[i]:
            mois = nom_des_mois[i]