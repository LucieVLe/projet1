# -*-coding:Utf-8 -*
print("hello")


# En utilisant des boucles while lorsque le nombre d'itérations n'est pas connu et des boucles for lorsque le nombre d'itérations est connu :


# 1. Écrire un algorithme qui demande un entier positif, et le rejette tant que le nombre saisi n’est pas conforme.
#FAUX:
# i_entier = int(float(input("1. Veuillez saisir un nombre entier positif: ")))
# while i_entier <0 or i_entier!=int:
#     print ("Le nombre saisi n'est pas conforme. Merci de saisir un nombre entier positif.")
#     break
# else:
#     print ("Le nombre saisi est conforme")

#Correction:
# i = -1
# while (i < 0):
#     i = int(float(input("Veuillez saisir un entier positif: ")))
#     if i < 0:
#         print ("Le nombre", i, "saisi est négatif, donc non conforme")
# print ("Le nombre", i, "saisi est positif, donc conforme.")


# # 2. Écrire un algorithme qui demande 10 entiers, compte le nombre d’entiers positifs saisis, et affiche ce résultat.
# équivalent à for i in (0,1,2,3,4,5,6,7,8,9)
#FAUX:
# i = 0
# for i in range(10):
#     i = int(float(input("Veuillez saisir un entier: ")))
#     sum i > 0:
#         print ("Vous avez saisi", sum ,"nombres entiers positifs")

#Correction:
# cpt = 0
# for i in range(10):
#     a = int(float(input("Saisir un entier: ")))
#     if a >=0:
#         cpt = cpt + 1
# print ("Le nombre d'entiers positifs saisi est", cpt)


# 3. Écrire un algorithme qui demande des entiers positifs à l’utilisateur, les additionne, et qui s’arrête en affichant le
# résultat dès qu’un entier négatif est saisi.
#1ere suggestion (fonctionne):
# somme=0
# i=0
# while i>=0:
#     i = float(input("Veuillez entrer un entier positif: "))
#     if i < 0:
#         print ("Le nombre", i, "est négatif et non conforme. La somme des nombres saisis est", somme)
#     else:
#         somme = somme + i

# Correction:
# i = 1
# somme = 0
# while i >= 0:
#     i = int(float(input("Veuillez saisir un entier positif: ")))
#     if i >= 0:
#         somme += i
# print ("La somme des entiers positifs saisis est égale à", somme)


# 4. Modifier ce dernier algorithme pour afficher la moyenne de la série d’entiers positifs saisis.
i = 1
somme = 0
moyenne = 0
nb_i = 0
while i >= 0:
    i = int(float(input("Veuillez saisir un entier positif: ")))
    if i >= 0:
        somme += i
        nb_i = nb_i + 1
    if i < 0:
        break
moyenne = somme / nb_i
print ("La moyenne des entiers positifs est", moyenne)


