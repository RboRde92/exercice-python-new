import random

nbr_secret = random.randint(1, 100)
trouve = False 

print(" --- Bienvenue au jeu du nombre ! --- ")
print("J'ai choisi un nombre entre 1 et 100. A vous de le trouver")

while not trouve :
    proposition = int(input("Entrez votre proposition : "))

    if proposition < nbr_secret:
        print("C'est plus grand !")
    elif proposition > nbr_secret:
        print("C'est plus petit !")
    else:
        print(f"Félicitation ! Vous avez trouvé le nombre secret : {nbr_secret}")
        trouve = True