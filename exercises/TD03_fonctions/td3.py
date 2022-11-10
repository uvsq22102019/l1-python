# temps[0] : jours, temps[1]: heures, temps[2]: minutes, temps[3]: secondes

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


afficheTemps(proportionTemps((2, 0, 36, 0), 0.2))

# appeler la fonction en échangeant l'ordre des arguments


def tempsEnDate(temps: tuple):
    return temps[0] * 


annee = 1970
jours = 1
heures = 0
minutes = 0
secondes = 0


def afficheDate(date: int = -1):
    return(annee, jours, heures, minutes, secondes)


temps = secondeEnTemps(1000000000)
afficheTemps(temps)
afficheDate(tempsEnDate(temps))
afficheDate()