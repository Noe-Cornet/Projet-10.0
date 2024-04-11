from transformation_geometrique import calculer_reflexion_point
from transformation_geometrique import calculer_inclinaison_point
from transformation_geometrique import calculer_rotate_point


'''
Descirption : Cette fonction détermine les coordonnées d'un clou en suivant la
paramétrisation illustrée dans la Figure 1.

Arguments: A, B, C, D, E (float): Dimensions spécifiques du clou, utilisées pour
calculer les coordonnées.

Retourne :
list: Une liste de tuples, où chaque tuple contient :

● Une chaîne de caractères indiquant le nom du point (par
exemple, "pt_0").
● Un tuple de deux nombres (float, float) représentant les
coordonnées du point dans un plan 2D.

La liste des points retournée suit l'ordre : pt_0, pt_1, pt_2, pt_3, pk_2,
pk_0, pk_1. Ces points représentent différentes parties du clou en
suivant la paramétrisation de la Figure 1.


'''

def calculer_coordonnees_clou(A,B,C,D,E):
    pt_0 = (float(-B/2),float(C/2))
    pt_1 = (float(-B/2),float(-C/2))
    pt_2 = (float((-B/2)-D),float(-A/2))
    pt_3 = (float((-B/2)-D),float(A/2))
    pk_0 = (float((B/2)+E),float(0))
    pk_1 = (float(B/2),float(-C/2))
    pk_2 = (float(B/2),float(C/2))
    liste = [('pt_0', pt_0), ('pt_1', pt_1), ('pt_2',pt_2), ('pt_3', pt_3), ('pk_2', pk_2), ('pk_0', pk_0), ('pk_1', pk_1)] #teste ne pas effaccer
    return liste

print(calculer_coordonnees_clou(3,10,1,0.75,2))

'''
Description :Cette fonction prend un ensemble de points clés représentant un clou et
applique trois types de transformations géométriques : réflexion,
rotation et inclinaison. Chaque transformation est appliquée
séquentiellement à tous les points clés.


Argument:

points_clou (list): Une liste de tuples, où chaque tuple contient :
● Une chaîne de caractères indiquant le nom du point (par
exemple, "pt_0").
● Un tuple de deux nombres (float, float) représentant les
coordonnées du point dans un plan 2D.

center_rotation (tuple): Le centre de rotation pour la transformation de
rotation.

angle_rotation (float): L'angle de rotation en degrés.

angle_inclinaison (float): L'angle d'inclinaison en degrés.

direction_inclinaison (str): La direction de l'inclinaison ('x' ou 'y').

axe_reflexion (str): L'axe de réflexion ('x' ou 'y').

tuple : Trois listes de tuples. Chaque liste correspond aux coordonnées
des points clés après l'application d'une des transformations (réflexion,
rotation, inclinaison). Cela permet une analyse et une visualisation
détaillées de l'impact de chaque transformation sur la structure du clou.

Retourne: tuple : Trois listes de tuples. Chaque liste correspond aux coordonnées
des points clés après l'application d'une des transformations (réflexion,
rotation, inclinaison). Cela permet une analyse et une visualisation
détaillées de l'impact de chaque transformation sur la structure du clou.


'''
def appliquer_transormation_clou(point_clou,centre_rotation,angle_rotation,direction_inclinaison,angle_inclinaision,axe_reflexion):

    # intitialisation d'un liste avec les coordonné des points
    liste_point=['pt_0','pt_1','pt_2','pt_3','pk_2','pk_0','pk_1',]

    # initialisation des tuples que l'on va retourner
    point_reflextion=[]
    point_rotate=[]
    point_inclinaison=[]

    # chaque points de la liste va subir une transphomation géometrique
    # les nouvelles coordoné du points sont ajouter au tuple correspondant
    for i in range(7):
        point_reflextion.append((liste_point[i],calculer_reflexion_point(point_clou[i][1],axe_reflexion)))
        point_rotate.append((liste_point[i],calculer_rotate_point(point_clou[i][1],angle_rotation,centre_rotation)))
        point_inclinaison.append((liste_point[i],calculer_inclinaison_point(point_clou[i][1],angle_inclinaision,direction_inclinaison)))

    return point_reflextion, point_rotate, point_inclinaison





