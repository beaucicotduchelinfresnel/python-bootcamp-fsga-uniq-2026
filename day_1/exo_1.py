# Exercice 1 – Répartition d’élèves en groupes
#
# Une école souhaite répartir des élèves en groupes de travail de taille fixe.
#
#     Proposer des noms de variables permettant de stocker :
#         le nombre total d’élèves,
#         le nombre d’élèves par groupe,
#         le nombre de groupes complets,
#         le nombre d’élèves restants.
#
#     Écrire les instructions permettant de demander les valeurs à l’utilisateur à l’aide de input().
#
#     Écrire les instructions permettant de calculer :
#         le nombre de groupes complets,
#         le nombre d’élèves restants.
#
#     Afficher un résumé clair des résultats.


total_eleves = int(input("Donnez le nombre total d'eleves : "))
groupe_eleves = int(input("Donnez le nombre d'eleves par groupe : "))
# groupes_complets = int(input("Donnez le nombre de groupes complets : "))
# reste_eleves = int(input("Donnez le nombre d'eleves restants : "))

groupes_complets = total_eleves // groupe_eleves
reste_eleves = total_eleves % groupe_eleves
print("==================================================")
print(f"Le nombre total d'eleves est : {total_eleves}")
print(f"Le nombre d'eleves par groupe est : {groupe_eleves}")
print(f"Le nombre de groupes complets est : {groupes_complets}")
print(f"Le nombre d'eleves restants est : {reste_eleves}")

