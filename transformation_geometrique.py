import math

'''
calculer_point_reflexion

Description:

Cette fonction applique une réflexion (miroir) à un point par rapport à un
axe spécifié.

Arguments:

point (tuple): Un tuple (x, y) représentant les coordonnées du point à
réfléchir.

axe (str): L'axe de réflexion. Doit être 'x' ou 'y'. Si l'axe est 'x', la
réflexion se produit par rapport à l'axe vertical (mirroir horizontal),
changeant la coordonnée y du point. Si l'axe est 'y', la réflexion se
produit par rapport à l'axe horizontal (mirroir vertical), changeant la
coordonnée x.
 
Retourne:

tuple: Un tuple (x', y') représentant les nouvelles coordonnées du point
après la réflexion. Si l'axe de réflexion est 'x', y' sera l'opposé de y. Si
l'axe est 'y', x' sera l'opposé de x.


'''


def calculer_reflexion_point(point, axe):
    # reflexion selon l'axe x
    if axe == 'x':
        x = point[0]
        y = -1 * point[1]
        un_tuple = (x, y)
        return un_tuple

    # reflexion selon l'axe y
    elif axe == 'y':
        x = -1 * int(point[0])
        y = point[1]
        un_tuple = (x, y)
        return un_tuple


'''
Description: Cette fonction prend un point dans le plan cartésien et le fait pivoter
autour d'un point central donné (le centre de rotation) d'un certain angle.


Arguments:

point (tuple): Un tuple (x, y) représentant les coordonnées du point à
faire pivoter.

angle (float): L'angle de rotation en degrés. Une valeur positive entraîne
une rotation antihoraire, tandis qu'une valeur négative entraîne une
rotation horaire.

center (tuple): Un tuple représentant les coordonnées du centre de
rotation. Par défaut, il s'agit de l'origine (0, 0).

Retourne: tuple: Un tuple (x', y') représentant les nouvelles coordonnées du point
après la rotation. Les résultats doivent être arrondis à deux chiffres
après la virgule.
'''


def calculer_rotate_point(point, un_angle, un_centre):  # angle en degrees
    angle = float(un_angle) * (math.pi / 180)  # convertie les degrès en radian
    distance_x = point[0] - un_centre[0]  # calcul la distance en x
    distance_y = point[1] - un_centre[1]  # calcul la distance en y

    # calcul les nouvelles coordonné en x et en y
    nv_x = distance_x * math.cos(angle) - distance_y * math.sin(angle) + un_centre[0]
    nv_y = distance_x * math.sin(angle) + distance_y * math.cos(angle) + un_centre[1]

    # arrondissement des résultat à deux chiffres après la virgule
    nv_x = round(nv_x, 2)
    nv_y = round(nv_y, 2)
    nv_pt = (nv_x, nv_y)  # initialisation d'un tuple

    return nv_pt


'''
Description:Cette fonction applique une transformation d'inclinaison (cisaillement)
sur un point. L'inclinaison est déterminée par un angle en degrés et
peut être appliquée selon l'axe des x ou l'axe des y.

Arguments:
point (tuple): Un tuple (x, y) représentant les coordonnées du point à
incliner.

angle (float): L'angle d'inclinaison en degrés. L'angle détermine
l'intensité de la transformation de cisaillement.

direction (str): La direction de l'inclinaison. Doit être 'x' pour une
inclinaison horizontale ou 'y' pour une inclinaison verticale.

Retourne : Un tuple (x', y') représentant les nouvelles coordonnées du point après
l'inclinaison. Les résultats doivent être arrondis à deux chiffres après la
virgule

'''

def calculer_inclinaison_point(point_1, angle_1, direction):

    # convertion des degrès en radiant
    angle_radian = float(angle_1) * (math.pi / 180)
    m = float(math.tan(angle_radian))

    # inclinaison selon l'axe X
    if direction == 'x':
        n_x = round(point_1[0] + m * point_1[1], 2)
        n_y = float(point_1[1])

    # inclinaison selon l'axe y
    elif direction == 'y':
        n_x = point_1[0]
        n_y = round(point_1[0] * m + point_1[1], 2)

    return n_x, n_y
