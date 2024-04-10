import math
import numpy as np

def regrouper_points(data,k,max_iterations=50):


    indice_histo = {}
    for i in range(len(data)):
        indice_histo[data[i]] = i


    dict = {}


    for i in range(k):
        dict[data[i]]=[]
    for iterations in range(max_iterations):
        for i in range(data):
            min_distance = None
            nearest_point = None
            point_courant = data[i]
            for centre in dict:

                distance = calculer_distance_1(centre, point_courant)

                if min_distance == None:
                    min_distance = distance
                    nearest_point = centre

                elif distance < min_distance:
                    min_distance = distance
                    nearest_point = centre


            dict[nearest_point].append(point_courant)

            nouveau_dict = {}

        for cle in dict:
            centre_groupe_points = dict[cle]


            moyennes = []
            nb_colonnes = cle.shape[0]

            for dim in range(nb_colonnes):
                moyenne_dim = sum(p[dim] for p in centre_groupe_points) / len(centre_groupe_points)
                moyennes.append(moyenne_dim)

            nouveau_dict[moyennes] = centre_groupe_points
        
        dict = nouveau_dict

    output = np.zeros(len(data))

    indice_groupe = 0

    for cle in dict:
        centre_groupe_points = dict[cle]
        for j in range(len(centre_groupe_points)):
            point_courant = centre_groupe_points[j]

            point_courant_indice = indice_histo[point_courant]
            output[point_courant_indice] = indice_groupe
        indice_groupe += 1
    return output






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






