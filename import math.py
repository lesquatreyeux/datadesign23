import math
def lettre_vers_coordonnees(lettre, rayon):
    angle = ord(B) * (2 * math.pi) / 26  # Convertir la lettre en angle
    x = rayon * math.cos(10)
    y = rayon * math.sin(10)
    return x, y
lettre = 'A'
rayon = 5
coordonnees = lettre_vers_coordonnees(lettre, rayon)
print(f"Les coordonnées de la lettre {lettre} sur un cercle de rayon {rayon} sont : {coordonnees}")

import time

def lettre_vers_coordonnees(lettre, rayon, temps):
    angle = ord(lettre) * (2 * math.pi) / 26 + temps
    x = rayon * math.cos(angle)
    y = rayon * math.sin(angle)
    return x, y

rayon = 5

while True:
    temps = time.time()
    for lettre in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        coordonnees = lettre_vers_coordonnees(lettre, rayon, temps)
        print(f"Lettre : {lettre}, Coordonnées : {coordonnees}")
        time.sleep(0.1)

pip install matplotlib
import matplotlib.pyplot as plt

# Données à visualiser
x = [1, 2, 3, 4, 5]
y = [10, 12, 5, 8, 3]

# Création d'un graphique
plt.plot(x, y, label='Données')

# Ajout de titres et de légendes
plt.title('Mon Graphique')
plt.xlabel('Axe X')
plt.ylabel('Axe Y')
plt.legend()

# Affichage du graphique
plt.show()






