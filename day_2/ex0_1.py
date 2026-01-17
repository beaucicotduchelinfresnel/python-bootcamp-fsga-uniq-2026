# Problème 1 - Validation d’un compte utilisateur
# Un utilisateur souhaite créer un compte sur un nouveau réseau social.
# Pour que le compte
# soit validé, les conditions suivantes doivent être respectées :
# ● Le nom d’utilisateur doit contenir au moins 5 caractères ;
# ● Le mot de passe doit contenir au moins 8 caractères ;
# Travail demandé :
# Implémenter une logique vérifiant les deux critères et afficher:
# ● un message de succès si le compte est valide ;
# ● un message d’erreur précisant la raison de l'échec dans le cas contraire

username = input("Entrer votre nom d'utilisateur : ")
password = input("Entrer votre mot de passe : ")

if len(username) < 5:
    print("Votre nom d’utilisateur doit contenir au moins 5 caractères")
elif len(password) < 8:
    print("Votre mot de passe doit contenir au moins 8 caractères")
else:
    print("Votre compte est valide !")



