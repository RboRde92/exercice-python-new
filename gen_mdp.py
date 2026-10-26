import random
import string
print("--- Générateur de mots de passe ---")

longueur = int(input("Entrez la longeur souhaitée pour le mot de passe : "))

if longueur < 4:
    print("Pour des raisons de sécurité, veuillez définir une longueur d'au moins 4 caractères. ")

minuscules = string.ascii_lowercase
majuscules = string.ascii_uppercase
chiffres = string.digits
symboles = "!@#$%^&*()_+-=[]{}|;:,.<>?"

nb_min = max(1, longueur // 4)
nb_maj = max(1, longueur // 4)
nb_chiffres = max(1, longueur // 4)
nb_symboles = longueur - (nb_min + nb_maj + nb_chiffres)

mdp_liste = (
    random.sample(minuscules, nb_min) +
    random.sample(majuscules, nb_maj) +
    random.sample(chiffres, nb_chiffres) +
    random.sample(symboles, nb_symboles) 
)

random.shuffle(mdp_liste)

mdp = "".join(mdp_liste)

print(f"Votre mot de passe sécurisé : {mdp}")