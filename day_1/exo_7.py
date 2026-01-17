# Exercice 7 – Programme avec plusieurs erreurs à corriger
#
# Le programme suivant contient plusieurs erreurs.
# Identifier et corriger toutes les erreurs afin qu’il fonctionne correctement.
#
# prenom = "Floria'
# Nom = "Carpon"
# AGE = "19"
#
# ville = Port au Prince
# formation = code de la route
#
# mois_inscription = "04"
# mois_reussite = "06"
# nb_mois = mois_reussite + mois_inscription
#
# print('L'élève', Prenom, nom, "âgé de", age, "ans a suivi la formation", Formation, "à", ville, "pendant", nbmois, "mois")

prenom = "Floria"
Nom = "Carpon"
AGE = "19"
ville = "Port au Prince"
formation = "code de la route"
mois_inscription = int(4)
mois_reussite = int(6)
nb_mois = mois_reussite + mois_inscription
print(f"Lélève {prenom} {Nom}, âgé de {AGE} ans a suivi la formation {formation} à, {ville} pendant {nb_mois} mois")