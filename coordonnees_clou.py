def calculer_coordonnees_clou(A,B,C,D,E):
    pt_0=(float(-B/2),float(C/2))
    pt_1=(float(-B/2),float(-C/2))
    pt_2=(float((-B/2)-D),float(-A/2))
    pt_3=(float((-B/2)-D),float(A/2))
    pk_0=(float((B/2)+E),float(0))
    pk_1=(float(B/2),float(-C/2))
    pk_2=(float(B/2),float(C/2))
    point_=('ot')
    liste=[[('pt_0', pt_0), ('pt_1', pt_1), ('pt_2',pt_2), ('pt_3', pt_3), ('pk_2', pk_2), ('pk_0', pk_0), ('pk_1', pk_1)]]
    return pt_0,pt_1, pt_2,pt_3,pk_2,pk_0,pk_1,

print(calculer_coordonnees_clou(3,10,1,0.75,2))