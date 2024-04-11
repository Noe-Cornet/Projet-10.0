from PIL import Image
import numpy as np
import math

'''
Description : initialise une matrice une en fonction des dimentions donné

Arguments :
 
m(int) : nombre de ligne
n(int)= nombre de colonne

Retou
rne: une matrice de dimention m n nul

'''


# initialise une matrice de taille m,n
def initialiser_matrice(m, n):
    matrice = []
    j = [0]
    for i in range(m):
        matrice.append(j * n)
    return matrice


# transphorme une liste de binaire en un nombre decimal


'''
Description : parcour une liste et la tranphome en le nombre decimal correspondant 

Argument :

liste_binaire : un liste avec des nombre qui représente un chiffre binaire 

Retourne: somme(int): nombre décimal 

'''


def binaire_en_decimal(liste_binaire):

    # obtenition de la longeur de la liste
    n = len(liste_binaire)

    # initialisation des variables somme et j
    somme = 0
    j = n - 1

    # convertion des nombre binaire en decimal en parcourant la liste
    for i in range(n):
        somme = somme + liste_binaire[i] * 2 ** j
        j -= 1
    return somme


'''
Description :Cette fonction transforme une image en couleur en une nouvelle image
en niveaux de gris.


Arguments :

chemin_image_couleur (str): Le chemin de l'image en couleur à
transformer.

chemin_sauvegarde_gris (str): Le chemin où sauvegarder l'image
résultante en niveaux de gris.


Retourne :None: La fonction ne retourne rien mais sauvegarde l'image en niveaux
de gris au chemin spécifié.

'''


def appliquer_rgb_to_gry(chemin_image_couleur, chemin_sauvegarde_gris):

    # ouvre l'image et la convertie en un tableau np array
    image_couleur = Image.open(chemin_image_couleur)
    img_array = np.array(image_couleur)

    # parcoure le tableau 3D et changer les modifier la couleur vers le noire et blanc
    for i in range(len(img_array)):
        for j in range(len(img_array[0])):
            for k in range(2):
                img_array[i][j][k] = ((img_array[i][j][0]) + (img_array[i][j][1] + img_array[i][j][2])) / 50
    img_gris = Image.fromarray(img_array)
    img_gris.save(chemin_sauvegarde_gris)


'''
Description :Cette fonction prend une image en niveaux de gris sous forme d'un
tableau NumPy 2D et applique une transformation pour simplifier et
extraire des caractéristiques significatives de l'image.


Argument :

image_gris (numpy.ndarray): Un tableau 2D NumPy représentant une
image en niveaux de gris. Chaque élément du tableau correspond à
l'intensité d'un pixel de l'image.


Retourne:numpy.ndarray: Un tableau 2D NumPy résultant de la transformation
appliquée.

'''


def appliquer_transformation_1(image_gris):

    image_gris = np.array(image_gris)
    nb_ligne = len(image_gris)
    nb_colone = len(image_gris[1])
    image_transphorme = initialiser_matrice(nb_ligne, nb_colone)

    # parcour le tableau sauf les bordure
    for i in range(1, len(image_gris) - 1):
        for j in range(1, len(image_gris[0]) - 1):

            gc = image_gris[i][j]
            liste_b = []

            # parcour la ligne superieur
            for k in range(j - 1, j + 2):
                if image_gris[i - 1][k] < image_gris[i][j]:
                    n = 0
                    liste_b.append(n)

                elif image_gris[i - 1][k] >= image_gris[i][j]:
                    n = 1
                    liste_b.append(n)

            # parcour la colone de droite
            if image_gris[i][j + 1] < image_gris[i][j]:
                n = 0
                liste_b.append(n)

            elif image_gris[i][j + 1] >= image_gris[i][j]:
                n = 1
                liste_b.append(n)

            # parcour la ligne inferieure
            for k in range(j + 1, j - 2, -1):
                if image_gris[i + 1][k] < image_gris[i][j]:
                    n = 0
                    liste_b.append(n)

                elif image_gris[i + 1][k] >= image_gris[i][j]:
                    n = 1
                    liste_b.append(n)

            # parcour la colone de gauche
            if image_gris[i][j - 1] < image_gris[i][j]:
                n = 0
                liste_b.append(n)

            elif image_gris[i][j - 1] >= image_gris[i][j]:
                n = 1
                liste_b.append(n)

            # transphorme la liste de nombre binaire en un nombre réel
            reel = binaire_en_decimal(liste_b)
            image_transphorme[i][j] = reel
    return image_transphorme


'''
Description :Transformer les données visuelles complexes d’une image en
ensembles de caractéristiques plus simples et plus significatives.

Argument :

image_gris (numpy.ndarray): Un tableau 2D NumPy représentant une
image en niveaux de gris.

rayon (int): Un entier spécifiant le rayon du voisinage à considérer pour
chaque pixel lors de la transformation.

Retourne:

numpy.ndarray: Un tableau 2D NumPy résultant de la transformation
appliquée. Cette transformation est basée sur le rayon spécifié et peut
modifier les caractéristiques visuelles originales de l'image.

'''

def appliquer_transformation_2(image_gris, rayon):
    num_rows, num_cols = image_gris.shape
    tableau = np.zeros((num_rows, num_cols))

    #Eviter les erreurs ''out of bounds''
    for i in range(num_rows):
        for j in range(num_cols):
            cell = image_gris[i,j]
            if i - rayon < 0: #haut
                continue
            if j - rayon < 0: #gauche
                continue
            if j + rayon >= num_cols: #droite
                continue
            if i + rayon  >= num_rows: #bas
                continue
            O = math.log10(1 + abs(image_gris[i, j + rayon] - 2 * image_gris[i, j] + image_gris[i, j - rayon])) + \
                math.log10(1 + abs(image_gris[i + rayon, j] - 2 * image_gris[i, j] + image_gris[i - rayon, j])) + \
                math.log10(1 + abs(image_gris[i - rayon, j + rayon] - 2 * image_gris[i, j] + image_gris[i + rayon, j - rayon]))
            O = math.floor(O)
            tableau[i,j] = O

    return tableau

    hauteur, largeur = image_gris.shape
    image_sortie = np.zeros((hauteur, largeur))
    return output