# Exercice 2 – Paquets de bouteilles
#
# Une usine emballe des bouteilles dans des cartons contenant un nombre fixe de bouteilles.
#
#     Proposer des variables permettant de stocker :
#         le nombre total de bouteilles,
#         la capacité d’un carton,
#         le nombre de cartons complets,
#         le nombre de bouteilles restantes.
#
#     Demander les valeurs à l’utilisateur avec input().
#
#     Calculer le nombre de cartons complets et le reste de bouteilles.
#
#     Afficher les résultats sous forme de phrase.

total_bouteilles = int(input("Donnez le nombre de total de bouteilles : "))
capacite_carton = int(input("Donne la capacite d'un carton : "))
# carton_complets =
# reste_bouteilles =

carton_complets = total_bouteilles // capacite_carton
reste_bouteilles = total_bouteilles % capacite_carton
print("==================================================")
print(f"Le nombre total de bouteilles est {total_bouteilles}")
print(f"La capacite d'un carton est {capacite_carton}")
print(f"Le nombre de cartons complets est {carton_complets}")
print(f"Le nombre de bouteilles restantes est {reste_bouteilles}")

