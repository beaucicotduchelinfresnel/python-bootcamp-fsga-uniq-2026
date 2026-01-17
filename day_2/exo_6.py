# Problème 6 - Calcul conditionnel d’une vente
# En tant que propriétaire d’un restaurant, vous appliquer une politique de remise suivante :
# ● tout d’un montant supérieure ou égale à 5750,50 HTG
# ● et inférieure ou égale à 7000 HTG bénéficie d’une réduction de 10%.
# Travail demandé :
# Programmer une logique qui calcule le montant final à payer en appliquant la remise si les
# conditions sont remplies, puis afficher le résultat.

montant = float(input("Entrer le montant a payer : "))

if montant >= 5750.50 and montant <= 7000:
    taxe_montant = montant - (montant * 10)/100
    print(f"Le montant a payer est {taxe_montant} HTG")
else:
    print(f"Le montant a payer est {montant} HTG")