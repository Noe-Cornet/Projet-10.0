import math
import numpy as np
from PIL import Image

def appliquer_transformation_2(image_gris, rayon):
    num_rows, num_cols = image_gris.shape
    # Créer un tableau NumPy de zéros, avec les mêmes dimensions que l'image en niveau de gris
    tableau = np.zeros((num_rows, num_cols))

    """
    Transformer les données visiuelles complexes d'une image en ensembles de caractéristiques plus simples et plus significatives.

    Arguments:
        image_gris (np.array): Un tableau 2D NumPy représentant une image en niveaux de gris.
        rayon (int): Un entier spécifiant le rayon du voisinage à considérer pour chaque pixel lors de la transformation. 
        
    Retourne:
        np.array: Un tableau 2D NumPy résultant de la transormation appliquée. Cette transformation est basée sur le rayon spécifié
        et peut modifier les caractéristiques visuelles originales de l'image.
    """

    # Boucles afin d'éviter les erreurs ''out of bounds''
    for i in range(num_rows):
        for j in range(num_cols):
            cell = image_gris[i,j]
            if i - rayon < 0: # Vérification haut
                continue
            if j - rayon < 0: # Vérification gauche
                continue
            if j + rayon >= num_cols: # Vérification droite
                continue
            if i + rayon  >= num_rows: # Vérification bas
                continue
            # Appliquer les transformations
            O = math.log10(1 + abs(image_gris[i, j + rayon] - 2 * image_gris[i, j] + image_gris[i, j - rayon])) + \
                math.log10(1 + abs(image_gris[i + rayon, j] - 2 * image_gris[i, j] + image_gris[i - rayon, j])) + \
                math.log10(1 + abs(image_gris[i - rayon, j + rayon] - 2 * image_gris[i, j] + image_gris[i + rayon, j - rayon]))
            O = math.floor(O)
            tableau[i,j] = O

    return tableau

   


