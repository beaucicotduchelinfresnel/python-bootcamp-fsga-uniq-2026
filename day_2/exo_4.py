# Problème 4 - Classification de données numériques
# En analyse de données, la classification des valeurs en catégories facilite l'interprétation des
# résultats.
# Travail demandé :
# Implémenter une logique qui classe une valeur numérique dans l'une des catégories
# suivantes :
# ● faible ;
# ● moyenne;
# ● élevée.
# Remarque important :
# Les seuils de classification doivent être définis par l'étudiant et clairement documentés
# dans le code sous forme de commentaires


#Classification des valeurs
#faible inferieur a 30
#moyenne entre 30 et 70
#eleve 70 

valeur = float(input("Entrer une valeur : "))

if valeur < 30 :
    categorie = "faible"
elif valeur < 70 :
    categorie = "moyenne"
else:
    categorie = "élevée"

print(f"La categorie de votre valeur est : {categorie}")