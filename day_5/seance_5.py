#Jour 5 - Fonctions
import uniq


notes = [3, 5, 7]
print(uniq.calculer_moyenne(notes))

# print(sum(notes))

# somme = 0
# for note in notes:
#     somme += note
# print(somme)


# def ajouter(val, liste=[]):
#     liste.append(val)
#     return liste

# array = ajouter(5)
# print(array)
# array = ajouter(7)
# array = ajouter(7, array)
# array = ajouter(11, array)
# print(array)



# x = 10
#
# def test():
#     x=5
#     print('local : ', x)
# print('global : ', x)










# def stats(a, b):
#     return a + b, a * b, a % b
#
# sum, prod, mod = stats(a=4, b=3)
# print(stats(10, 3))
# print(sum, prod, mod)




# def stats(a, b):
#     produit = a * b
#     somme = a + b
#     modulo = a % b
#     return somme, produit, modulo
#
# sum, prod, mod = stats(a=4, b=3)
# print(stats(10, 3))
# print(sum, prod, mod)



# def dire_bonjour(prenom, nom='Joseph', sexe='f'):
#     prefix = 'Mme.' if sexe == 'f' else 'M.'
#     print(f'Bonjour {prefix} {nom.upper()}, {prenom}')

# dire_bonjour(nom='Jean', prenom='Junior', sexe='m')
# dire_bonjour(nom='Joseph', prenom='Magdala')
# dire_bonjour(prenom='Duchelin', nom='Beaucicot')
# dire_bonjour(prenom='Gertrude')
# dire_bonjour('jean', 'gertrude')


# def dire_bonjour(nom, prenom, sexe='f'):
#     prefix = ''
#     if sexe == 'f':
#         prefix = 'Mme.'
#     else:
#         prefix = 'M.'
#     print(f'Bonjour {prefix} {nom.upper()}, {prenom}')
#
# dire_bonjour(nom='Jean', prenom='Junior', sexe='m')
#
# dire_bonjour('Edouard')
# dire_bonjour('Jean Marie')
# dire_bonjour('Marie')



# def carre(x):
#     return x ** 2
# print(carre(8))

