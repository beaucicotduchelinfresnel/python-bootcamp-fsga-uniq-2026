total_eleves = int(input("Donnez le nombre total d'eleves : "))
groupe_eleves = int(input("Donnez le nombre d'eleves par groupe : "))
# groupes_complets = int(input("Donnez le nombre de groupes complets : "))
# reste_eleves = int(input("Donnez le nombre d'eleves restants : "))

groupes_complets = total_eleves // groupe_eleves
reste_eleves = total_eleves % groupe_eleves
print("==================================================")
print(f"Le nombre total d'eleves est : {total_eleves}")
print(f"Le nombre d'eleves par groupe est : {groupe_eleves}")
print(f"Le nombre de groupes complets est : {groupes_complets}")
print(f"Le nombre d'eleves restants est : {reste_eleves}")

