# Exercice 4 – Salaire mensuel
#
# Une entreprise souhaite calculer le salaire mensuel d’un employé.
# Le salaire est donné par :
#
# salaire = nombre d’heures travaillées × taux horaire
#
#     Proposer des noms de variables permettant de stocker :
#         le prénom,
#         le nom,
#         le nombre d’heures travaillées,
#         le taux horaire,
#         le salaire mensuel.
#
#     Affecter les variables pour 176 heures à 750 gourdes par heure.
#
#     Écrire les instructions permettant de calculer le salaire mensuel.
#
#     Écrire l’instruction permettant d’afficher :
#     Salaire mensuel de <prénom> <nom> : <salaire> gourdes.

prenom = "Duchelin Fresnel"
nom = "Beaucicot"
heures = int(176)
taux = int(750)

salaire = heures * taux

print(f"Salaire mensuel de {prenom} {nom} : {salaire} gourdes.")