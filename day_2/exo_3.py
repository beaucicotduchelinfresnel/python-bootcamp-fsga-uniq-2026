# Problème 3 - Décision combinée
# Une salle de cinéma propose un tarif réduit selon les critères suivants :
# ● le client est étudiant, ou
# ● le client a moins de 25 ans.
# Travail demandé :
# Développer une logique utilisant les opérateurs logiques appropriés pour déterminer si un
# utilisateur est éligible au tarif réduit.
# Le programme doit demander l'âge et le statut (étudiant ou employé), puis afficher la
# décision.

sys_age = 25
sys_status = "étudiant"

age = int(input("Entrer votre age : "))
statut = input("Entre votre statut (étudiant ou employé)(tapez le correctement) : ")

if age < sys_age or statut == sys_status:
    print("utilisateur est éligible au tarif réduit")
else:
    print("utilisateur non-éligible")