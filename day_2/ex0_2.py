# Problème 2 - Authentification conditionnelle
# Dans le cadre d'un système de connexion, vous devez vérifier les identifiants d'un utilisateur.
# Le programme dispose déjà d'un compte enregistré avec un identifiant et un mot de passe
# prédéfinis (Ex : username = “user1” et password = “pass1”).
# Travail demandé :
# Concevoir une logique qui compare les identifiants saisis avec celles enregistrés et afficher
# un message distinct selon les situations suivantes :
# ● accès autorisé;
# ● identifiant incorrect ;
# ● mot de passe incorrect.

username = "user1"
password = "pass1"

username_client = input("Entrer votre username : ")
password_client = input("Entrer votre password : ")

if username_client == username and password_client == password:
    print("Accès autorisé")
elif password_client != password:
    print("mot de passe incorrect")
else:
    print("identifiant incorrect")