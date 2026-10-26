nombre = int(input("Entrez un nombre entier positif : "))

if nombre < 0:
    print ("Erreur : veuillez entrer un nombre positif.")
else:
    somme = 0

    for i in range (1, nombre + 1):
        somme += i

print(f"la somme des entiers de 1 à {nombre} est : {somme}")