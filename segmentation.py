from manupulation_histogramme import calculer_distance_1
import random
def regrouper_points(data,k,max_iteration):

    # tirage aléatoire des points

    points_random=[]
    nb_lignes_data,nb_colonne_data=data.shape

    # boucle i permet de selections k points de façon aléatoire
    while len(points_random) != k:
        f=[random.randint(0,nb_lignes_data),random.randint(0,nb_colonne_data)]
        print(f)
        # verification que le point n'a pas deja été tiré au sort
        if f not in points_random:
            points_random.append(f)
    # points_randome est un de kx2 chaque ligne corresponds à une coordoné de points 