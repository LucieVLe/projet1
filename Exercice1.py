# -*-coding:Utf-8 -*
print("hello")

#1. Écrire un algorithme qui demande un entier à l’utilisateur, teste si ce nombre est positif (>= 0) ou non, et affiche
#“positif” ou “négatif”.
# i_entier = int(input("1. Veuillez saisir un nombre entier: "))
# if i_entier >= 0:
#     print ("Positif")
# else:
#     print ("Négatif")


#2. Écrire un algorithme qui demande un entier à l’utilisateur, teste si ce nombre est strictement positif, nul ou strictement
#négatif, et affiche ce résultat.
# i_entier = int(float(input("2. Veuillez saisir un nombre entier: ")))
# if i_entier >0:
#     print ("Strictement positif")
# elif i_entier ==0:
#     print ("Nul")
# else:
#     print ("Strictement Négatif")


# #3. Écrire un algorithme qui demande un réel à l’utilisateur et affiche sa valeur absolue (sans utiliser de fonction
# #prédéfinie évidemment).
# i_reel = float(input("Veuillez écrire un réel: "))
# if i_reel < 0:
#     i_reel = -i_reel
#
# print("la valeur absolue de i_reel est ", (i_reel))


#4. Écrire un algorithme qui demande un réel à l’utilisateur et l’arrondit à l’entier le plus proche (les x,5 seront arrondis
#à l’entier supérieur).
# a = float(input("4. Veuillez entrer un nombre réel: "))
# a_tronqué=int(a)
# if a < 0:
#     if a_tronqué-a >= 0.5:
#         print(int(a)-1)
#     else:
#         print(int(a))
# elif a-a_tronqué >=0.5:
#     print(int(a)+1)
# else:
#     print(int(a))


#5. Écrire un algorithme qui demande le numéro d’un mois et affiche le nombre jours que comporte ce mois (sans tenir
#compte des années bissextiles).
# mois = int(input("5. Veuillez entrer le numéro d'un mois de 1 à 12: "))
# if mois in [1,3,5,7,8,10,12]:
#     print ("Il y a 31 jours.")
# elif mois==2:
#     print("Il y a 28 ou 29 jours.")
# else:
#     print ("Il y a 30 jours.")


#6. Écrire un algorithme qui vérifie si une année est bissextile. On rappelle qu’il y a des années bissextiles tous les
#4 ans, mais la première année d’un siècle ne l’est pas (1800, 1900 n’étaient pas bissextiles) sauf tous les 400 ans
#(2000 était une année bissextile).
# annee = int(input("6. Veuillez entrer une annee: "))
# # Pour vérifier si l'année est un multiple de 4 mais pas un multiple de 100 ou si c'est un multiple de 400:
# if (annee%4==0 and annee%100!=0) or annee%400==0:
#     print ("L'année", annee, "est bissextile.")
# else:
#     print ("L'année", annee, "n'est pas bissextile.")


# #7. Écrire un algorithme qui demande une date sous la forme de 2 nombres entiers (numéro du jour et numéro du mois)
# #et affiche la saison (ex : 12/02; hiver). On supposera que le premier jour de la saison est toujours le 21.
# 1ere suggestion (fonctionne):
# jour = int(input("7.Veuillez entrer le jour, compris entre 1 et 31: "))
# mois = int(input("Veuillez entrer le mois, compris entre 1 et 12: "))
# if mois%3==0 and jour>=21 and mois!=12:
#     mois = mois + 1
# if mois==12 and jour >=21:
#     mois=1
# if mois in [1,2,3]:
#     print("C'est l'hiver!")
# elif mois in [4,5,6]:
#     print ("C'est le printemps!")
# elif mois in [7,8,9]:
#     print ("C'est l'été!")
# elif mois in [10,11,12]:
#     print ("C'est l'automne!")

# Correction:
jour = int(input("7.Veuillez entrer le jour, compris entre 1 et 31: "))
mois = int(input("Veuillez entrer le mois, compris entre 1 et 12: "))
if (jour >= 21 and mois ==12) or mois == 1 or mois == 2 or (jour<21 and mois == 3):
    print ("C'est l'hiver, il fait froid!")
elif (jour >= 21 and mois == 3) or mois == 4 or mois == 5 or (jour < 21 and mois == 6):
    print("C'est le printemps, y'a des fleurs!")
elif (jour >= 21 and mois == 6) or mois == 7 or mois == 8 or (jour < 21 and mois == 9):
    print("C'est l'été, il faut chaud!")
else:
    print ("C'est l'automne, il pleut!")
