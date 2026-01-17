# Exercice 3 – Calcul d’expression
#
# On veut calculer la valeur de l’expression :
#
# f(x) = 4x + 3
#
# Écrire un programme en Python qui :
#
#     demande à l’utilisateur de saisir la valeur de x,
#     calcule f(x) en utilisant une autre variable,
#     affiche le résultat avec une phrase explicite, par exemple :
#     Pour x = <x>, f(<x>) = <f(x)>.

x = int(input("Saisissez la valeur de x : "))

#calcul
fonction = 4 * x +3

print(f"Pour x = {x}, f({x}) = f({fonction})")