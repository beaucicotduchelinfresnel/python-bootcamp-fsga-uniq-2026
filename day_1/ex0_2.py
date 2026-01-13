total_bouteilles = int(input("Donnez le nombre de total de bouteilles : "))
capacite_carton = int(input("Donne la capacite d'un carton : "))
# carton_complets =
# reste_bouteilles =

carton_complets = total_bouteilles // capacite_carton
reste_bouteilles = total_bouteilles % capacite_carton
print("==================================================")
print(f"Le nombre total de bouteilles est {total_bouteilles}")
print(f"La capacite d'un carton est {capacite_carton}")
print(f"Le nombre de cartons complets est {carton_complets}")
print(f"Le nombre de bouteilles restantes est {reste_bouteilles}")

