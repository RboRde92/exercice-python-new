nom = str(input("Entrez votre nom :"))
age = int(input("Entrez votre âge :"))

if age <= 17:
    print("Vous n'êtes pas éligible pour voter")
else :
    print(f"{nom} vous avez {age} ans, vous êtes éligible pour voter")