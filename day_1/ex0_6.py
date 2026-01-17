# Exercice 6 – Crédit téléphonique
#
# Un utilisateur recharge son crédit téléphonique.
# Le montant total de crédit obtenu est donné par :
#
# crédit total = nombre de recharges × valeur d’une recharge
#
#     Proposer des noms de variables permettant de stocker :
#         le nombre de recharges,
#         la valeur d’une recharge,
#         le crédit total.
#
#     Demander à l’utilisateur de saisir le nombre de recharges et la valeur de chaque recharge.
#
#     Écrire les instructions permettant de calculer le crédit total.
#
#     Afficher le résultat.

nbre_recharge = int(input("Saisissez le nombre de recharges : "))
val_recharge = int(input("Saisissez la valeur de chaque recharge : "))
#calcul
credit = nbre_recharge * val_recharge
print("==================================================")
print(f"Le montant total de credit est : {credit} gourdes")