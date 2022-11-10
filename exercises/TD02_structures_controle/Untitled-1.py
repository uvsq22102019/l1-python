delk = "Infos"
print(len(delk))



annee =int(input("Saisir une année"))
if annee % 4 == 0 and annee % 100 !=0 or annee % 400 == 0:
    print("C'est une année bissextile")
else:
    print("Ce n'est pas une année bissextile")



    