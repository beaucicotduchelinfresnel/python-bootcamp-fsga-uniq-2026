# Exercice 5 – Facture Internet
#
# Un fournisseur Internet calcule la facture mensuelle d’un client.
# La facture est donnée par la relation :
#
# facture = forfait mensuel + coût supplémentaire
#
#     Proposer des noms de variables permettant de stocker :
#         le forfait mensuel,
#         le coût supplémentaire,
#         le montant total de la facture.
#
#     Demander à l’utilisateur de saisir le forfait et le supplément.
#
#     Écrire les instructions permettant de calculer la facture.
#
#     Afficher le montant à payer.

forfait = int(input("Saisissez le forfait mensuel : "))
supplement = int(input("Saisissez le supplement : "))

total = forfait + supplement

print("==================================================")
print(f"Le montant a payer est : {total} gourdes")