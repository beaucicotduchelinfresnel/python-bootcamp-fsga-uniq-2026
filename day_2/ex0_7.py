# Problème 7 - Détection d’anomalie de température
# Un système de surveillance contrôle la température d'une salle serveur à l'Université
# Quisqueya.
# La plage de fonctionnement normal est comprise entre 20°C et 65°C.
# En dehors de cette plage, le système distingue les situations suivantes:
# 1. Température trop basse : < 20°C ;
# 2. Température élevée mais acceptable : 65-75°C ;
# 3. Température critique nécessitant un arrêt d'urgence : > 75°C ;
# Travail demandé :
# Programmer une logique de surveillance qui classe la température saisie dans la catégorie
# appropriée et affiche un message d'alerte adapté.
# Pour une température normale, le message doit confirmer le bon fonctionnement du
# système


temperature = float(input("Entrer la temperature de la salle : "))

if temperature < 20 :
    print("Température trop basse")
elif temperature <= 65 :
    print("Température normal")
elif temperature <= 75 :
    print("Température élevée mais acceptable")
else:
    print("ALERTE !!! Température critique nécessitant un arrêt d'urgence")