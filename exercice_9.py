mdp_correct = input("définissez un mot de passe : ")

print ("Connexion ...")

saisie = input("Entrez le mot de passe : ")

while saisie != mdp_correct:
    print ("Mot de passe incorrect. Veuillez réessayer !")
    saisie = input("Entrez le mot de passe : ")

    print("Accès autorisé !")