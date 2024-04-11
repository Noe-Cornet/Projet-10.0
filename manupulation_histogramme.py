import numpy as np

'''
Description :

Génère un histogramme pour chaque pixel de l'image en utilisant un
carré de voisinage de taille spécifiée.

Arguments :
 
tableau_2D (numpy.ndarray): Un tableau 2D NumPy représentant une
image.

w (int): La taille du carré de voisinage autour de chaque pixel pour
lequel l'histogramme est calculé.

Retourne : numpy.ndarray: Un tableau 2D NumPy où chaque ligne représente un
histogramme pour le carré correspondant de l'image.

'''


def calculer_histogramme(tableau_2D, w):
    # definition de max_value
    t = 0
    # Definition de la valeur maximale
    max_value = 0
    nb_ligne, nb_colonne = tableau_2D.shape
    for i in range(nb_ligne):
        for j in range(nb_colonne):
            if tableau_2D[i][j] > max_value:
                max_value = tableau_2D[i][j]
    M = w // 2
    tableau_sortie = []

    # parcour la matrice

    for i in range(M, nb_colonne - M):
        for j in range(M, nb_colonne - M):
            # création d'une fenêtre wxw
            window = []
            for k in range(i - M, i + M + 1):
                for l in range(j - M, j + M + 1):
                    window.append(tableau_2D[k][l])
            hist, _ = np.histogram(window, bins=[0, max_value / 4, max_value / 2, (3 * max_value) / 4, max_value],
                                   range=(0, max_value))
            tableau_sortie.append(hist)
    tableau_sortie = np.array(tableau_sortie)
    return tableau_sortie


tableau = np.array([[255, 160, 10, 49], [20, 170, 1, 121], [30, 233, 230, 100], [255, 23, 155, 88]])
print(calculer_histogramme(tableau, 3))

'''
Description : Calculer la distance entre deux histogrammes


Arguments :

histogramme1 (numpy.ndarray): Premier histogramme sous forme de
tableau 1D NumPy.

histogramme2 (numpy.ndarray): Deuxième histogramme sous forme de
tableau 1D NumPy

Retourne : float: La distance entre les deux histogrammes.


'''


def calculer_distance_1(histogramme1, histogramme2):
    distance = 0
    colonne = histogramme1.shape

    # soustraction de l'histogramme 1 par le 2 en tout en les parcourants
    for i in range(colonne[0]):
        r = float(histogramme1[i]) - float(histogramme2[i])
        distance = distance + r ** 2

    # arrondi la distance à 2 chiffre après la virgule

    distance = round(distance ** 0.5, 2)
    return distance


'''
Description : Calculer la distance entre deux histogrammes.

Arguments :

histogramme1 (numpy.ndarray): Premier histogramme sous forme de
tableau 1D NumPy.

histogramme2 (numpy.ndarray): Deuxième histogramme sous forme de
tableau 1D NumPy


Retourne : Calculer la distance entre deux histogrammes.

'''


def calculer_distance_2(histogramme1, histogramme2):
    distance = 0
    # obtention des dimentions des histogrammes
    colonne = histogramme1.shape

    # Parcour les histogrammes et fait la somme somme de la soutraction de l'histogramme2 par l'histogramme1

    for i in range(colonne[0]):
        distance += histogramme2[i] - histogramme1[i]

    # arrondi la distance à 2 chiffre après la virgule

    distance = round(distance, 2)
    return distance
