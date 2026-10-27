mesure = ["22", "erreur", "12.6", "nan"]
somme = 0.0
invalides = 0

for m in mesure:
    try:
        valeur = float(m)
        if not __import__('math').isnan(valeur):
            somme += valeur
        else:
            invalides += 1
    except ValueError:
        invalides += 1
print(f"La somme des mesures valides est: {somme}, et le nombre de mesures invalides est: {invalides}")