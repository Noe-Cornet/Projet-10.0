from transformation_geometrique import calculer_reflexion_point
from transformation_geometrique import calculer_inclinaison_point
from transformation_geometrique import calculer_rotate_point



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

def appliquer_transormation_clou(point_clou,centre_rotation,angle_rotation,direction_inclinaison,angle_inclinaision,axe_reflexion):
    #print(f'point_clou = {point_clou}')
    #print(f'angle_rotation = {angle_rotation}')
    #print(f'centre_rotation = {centre_rotation}')
    #print(f'angle_inclinaision = {angle_inclinaision}')
    #print(f'direction_inclinaison = {direction_inclinaison}')
    #print(f'axe_reflexion = {axe_reflexion}')
    liste_point=['pt_0','pt_1','pt_2','pt_3','pk_2','pk_0','pk_1',]
    point_reflextion=[]
    point_rotate=[]
    point_inclinaison=[]
    for i in range(7):
        point_reflextion.append((liste_point[i],calculer_reflexion_point(point_clou[i][1],axe_reflexion)))
        point_rotate.append((liste_point[i],calculer_rotate_point(point_clou[i][1],angle_rotation,centre_rotation)))
        point_inclinaison.append((liste_point[i],calculer_inclinaison_point(point_clou[i][1],angle_inclinaision,direction_inclinaison)))

    return point_reflextion, point_rotate, point_inclinaison





