nombre = int(input("Entrz un nombre :"))

print(f"Table de multiplication de {nombre}")

for i in range (1, 11):
    resultat = nombre * i
    print(f"{nombre} x {i} = {resultat}")