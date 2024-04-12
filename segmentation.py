import numpy as np
from manupulation_histogramme import calculer_distance_1

def regrouper_points(data,k,max_iterations=50):

    """
    Description: 
    
    Diviser un ensemble de points dans un plan 2D en un nombre défini de groupes.

    Arguments:   
    
    Data(numpy.ndarray) : Un tableay 2D numpy représentant l'ensemble de données à partionner. Chaque ligne du tableau
    représente un histogramme décrivant un point.

    k(int): Le nombre de groupes à indentifier dans l'ensemble de données.

    max_itérations(int): Le nombre maximal d'itérations que l'algorithme exécutera. La valeur par défaut est de 50.
    
        
    Retourne:
    
    np.array: Un tableau numpy 1D ou chaque élément correspond à l'indice du centre le plus proche pour chaque point de l'ensemble
    de données. C'est un vecteur d'entiers de la même longueur que le nombre de points dans 'data', indiquant l'affectation de  
    groupe pour chaque point.

    Spécification :

    Pour calculer la distance entre deux points utiiser la fonction 'Calcul_distance_1'

    """

    # Création d'un dictionnaire pour stocker les histogrammes par centre
    histogrammes_par_centre = {}

    # Création d'un tableau pour stocker les indices des points dans le tableau data, la sortie est un tableau 1D
    sortie = np.zeros(len(data))

    # Repeter max_iterations fois
    for iteration in range(max_iterations):
        # Si aucun groupe deja present, on initiale k centres avec aucun histogramme associer
        if len(histogrammes_par_centre) == 0:
            for i in range(k):
                shape = data[0].shape
                histo_aleatoire = np.random.rand(*shape)
                temp = tuple(histo_aleatoire)
                histogrammes_par_centre[temp]=[]

        histogrammes_par_centre_iteration = {} # Dictionnaire avec les centres de l'iteration courante

        # Initialiser les indices qui representent les centres du tableau de sortie
        indices_par_centre = {}
        indice = 0
        for centre in histogrammes_par_centre:
            indices_par_centre[centre] = indice
            indice += 1

        # Pour chaque histogramme, trouver le centre le plus proche de l'histogramme
        for i in range(len(data)):
            min_distance = None
            nearest_centre = None
            point_courant = data[i]
            # Pour chaque centre, trouver la distance minimale entre un hsitogramme et tous les centres
            for centre in histogrammes_par_centre:
                distance = calculer_distance_1(np.array(centre), point_courant)

                if min_distance == None:
                    min_distance = distance
                    nearest_centre = centre

                elif distance < min_distance:
                    min_distance = distance
                    nearest_centre = centre

            if nearest_centre not in histogrammes_par_centre_iteration:
                histogrammes_par_centre_iteration[nearest_centre] = []
            histogrammes_par_centre_iteration[nearest_centre].append(point_courant)
            sortie[i] = indices_par_centre[nearest_centre]

        histogrammes_par_centre_iteration_bis = {} # Dictionnaire avec les nouveaux centres de l'iteration courante

        # Pour chaque centre, calculer la moyenne des histogrammes et mettre à jour les centres
        for centre_precedent in histogrammes_par_centre_iteration:
            histogrammes_centre = histogrammes_par_centre_iteration[centre_precedent]

            moyennes = []
            nb_colonnes_histogramme = np.array(centre).shape[0]

            # Calculer la moyenne de chaque dimension de tous les histogrammes du centre
            for dim in range(nb_colonnes_histogramme):
                moyenne_dim = sum(p[dim] for p in histogrammes_centre) / len(histogrammes_centre)
                moyennes.append(moyenne_dim)

            histogrammes_par_centre_iteration_bis[tuple(moyennes)] = histogrammes_centre
        
        histogrammes_par_centre = histogrammes_par_centre_iteration_bis

    return sortie








