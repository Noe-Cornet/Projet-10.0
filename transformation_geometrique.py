import math


def calculer_reflexion_point(point,axe):   #reflexion selon l'axe x
    if axe == 'x' :
        x= point[0]
        y= -1 * point[1]              #retourne les x
        un_tuple=(x,y)
        return un_tuple

    elif axe == 'y' :                       #reflexion selon l'axe y
        x = -1 * int(point[0])
        y = point[1]
        un_tuple=(x,y)                      #retourne les y
        return un_tuple


def calculer_rotate_point(point, un_angle, un_centre):  # angle en degrees
    angle = float(un_angle) * (math.pi / 180)  # convertie les degrès en radian
    distance_x = point[0] - un_centre[0]  # calcul la distance en x
    distance_y = point[1] - un_centre[1]  # calcul la distance en y
    nv_x = distance_x * math.cos(angle) - distance_y*math.sin(angle) + un_centre[0]      # calcul les nouvelles coordonné en x
    nv_y = distance_x * math.sin(angle) + distance_y * math.cos(angle) + un_centre[1]      # calcul les nouvelles coordonné en y
    nv_x = round(nv_x, 2)
    nv_y = round(nv_y, 2)
    nv_pt = (nv_x, nv_y)  # initialisation d'un tuple

    return nv_pt


def calculer_inclinaison_point(point_1,angle_1,direction):
    angle_radian= float(angle_1)*(math.pi/180)
    m = float(math.tan(angle_radian))
    if direction == 'x':
        n_x = round(point_1[0]+m*point_1[1],2)
        n_y = float(point_1[1])

    elif direction == 'y':
        n_x = point_1[0]
        n_y = round(point_1[0]*m+point_1[1],2)
    return n_x,n_y
