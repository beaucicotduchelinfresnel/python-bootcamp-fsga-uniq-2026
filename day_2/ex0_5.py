#Problème 5 - Validation de données analytiques
# Lors de l'importation de données dans un système d'analyse, certaines valeurs peuvent
# compromettre les calculs statistiques (valeurs nulles, négatives, ou aberrantes).
# Travail demandé :
# Construire une logique de contrôle qui examine une valeur numérique saisie et détermine si
# elle est exploitable (valeur positive et non nulle).
# Le programme doit expliquer clairement pourquoi la donnée est acceptée ou rejetée

valeur_numerique = float(input("Entrer la valeur a exploiter : "))

if valeur_numerique > 0 and valeur_numerique != 0 :
    print("Cette valeur est exploitable")
else:
    print("Cette valeur n'est pas exploitable")