poids = float(input("Entrez votre poids : "))

taille = float(input("Entrez votre taille : "))

if taille <= 0:
    print ("erreur : la taille doit être supérieure à 0.")
else : 
    imc = poids / (taille ** 2)

print(f"Résultats: {imc:.2f}")

