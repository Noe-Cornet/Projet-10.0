import math


def calculer_reflexion_point(iterable,axe):   #reflexion selon l'axe x
    if axe == 'x' :
        x=int ( iterable[0] )
        y= -1 * int(iterable[1])               #retourne les x
        un_tuple=(x,y)
        return un_tuple

    elif axe == 'y' :                       #reflexion selon l'axe y
        x = -1 * int(iterable[0])
        y = int(iterable[1])
        un_tuple=(x,y)                      #retourne les y
        return un_tuple


def calculer_rotate_point(un_tuple, un_angle, un_centre):  # angle en degrees
    angle = un_angle * (math.pi / 180)  # convertie les degrès en radian
    distance_x = un_tuple[0] - un_centre[0]  # calcul la distance en x   #calcul la distance en y
    distance_y = un_tuple[1] - un_centre[1]  # calcul la distance en y
    nv_x = distance_x * math.cos(angle) - distance_y*math.sin(angle) + un_centre[0]      # calcul les nouvelles coordonné en x
    nv_y = distance_x * math.sin(angle) + distance_y * math.cos(angle) + un_centre[1]      # calcul les nouvelles coordonné en y
    nv_x = round(nv_x, 2)
    nv_y = round(nv_y, 2)
    nv_pt = (nv_x, nv_y)  # initialisation d'un tuple

    return nv_pt


def calculer_inclinaison_point(point_1,angle_1,direction):
    angle_1=angle_1*(math.pi/180)
    m = float(math.tan(angle_1))
    if direction == 'x':
        n_x = round(point_1[0]+m*point_1[1],2)
        n_y = float(point_1[1])

    elif direction == 'y':
        n_x =  point_1[0]
        n_y =  round(point_1[0]*m+point_1[2],2)
    return n_x,n_y