total_secondes = int(input("entrez une durée en secondes : "))

if total_secondes < 0:
    print("erreur : la durée ne peux pas être négative.")
else:
    heures = total_secondes // 3600
    reste = total_secondes % 3600
    minutes = reste // 60
    secondes = reste % 60

print(f"sortie : {heures} heures {minutes} minutes {secondes} secondes")