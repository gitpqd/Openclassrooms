'''
Affiche la liste des vendredis 13 présents dans une année
paramètres demandés : jour de la semaine au 1er janvier et année bissextile ou non.
Python 3.x uniquement.

Pol
'''

cal=[]
J=["lundi","mardi","mercredi","jeudi","vendredi","samedi","dimanche"]
print("Bonjour!")
print("Je vais t'indiquer la liste des Vendredi 13 d'une année que nous allons définir ensemble")

#année bissextile
bissextile='z'
while bissextile.lower() not in ('o','n'):
        bissextile=str(input("Souhaites-tu que l'année soit bissextile? (o pour oui, n pour non): "))
if bissextile=='o': f=29
else : f=28

#saisie du jour au 1er janvier
j="dredi"
while j.lower() not in (J):
        j=str(input("A quel jour de la semaine correspond le 1er janvier de ton annee? : "))
a=J.index(j.lower())

M=[["janvier",31],["février",f],["mars",31],["avril",30],["mai",31],["juin",30],["juillet",31],["aout",31],["septembre",30],["octobre",31],["novembre",30],["décembre",31]]
jour=[]
num=[]
mois=[]

#remplissage du calendrier
for j in range(12):
        for i in range (M[j][1]):
                jour.append(J[(a)%7])
                num.append(i+1)
                mois.append(M[j][0])
                cal.append([jour[i],num[i],mois[i]])
                a=a+1
        jour=[]
        num=[]
        mois=[]

#affichage (en enlevant la condition tu as un joli calendrier sur l'année ...)
print("Et voici la liste :")
for i in range(365):
        if cal[i][0]=="vendredi" and cal[i][1]==13:
                print("- ",end='')
                for z in range (3):
                        print(cal[i][z],end=' ')
                print()

print("Au revoir!")
input("tape ENTREE pour terminer")
