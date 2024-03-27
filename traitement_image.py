from PIL import Image
import numpy as np

def initialiser_matrice(m,n):     #initialise une matrice de taille m,n
  matrice=[]
  j=[0]
  for i in range(m):
    matrice.append(j*n)
  return matrice
def appliquer_rgb_to_gry(chemin_image_couleur,chemin_sauvegarde_gris):
    image_couleur= Image.open(chemin_image_couleur)
    img_array = np.array(image_couleur)
        for i in range(len(img_array)):
            for j in range(len(img_array[0])):
                for k in range(2):
                    img_array[i][j][k]=((img_array[i][j][0])+(img_array[i][j][1]+img_array[i][j][2]))/3


img_gris = Image.fromarray(img_array)
img_gris.save(chemin_sauvegarde_gris)

def appliquer_transformation_1(image_gris):
    image_gris=np.array(image_gris)
    for i in range( 1 : len(image_gris)-1) :
        for j in range(1: len(image_gris[0]) - 1):     #parcour le tableau 20 image gris

            gc= image_gris[i][j]
            binaire = 0
            matrice=initialiser_matrice(3,3)    #crée une matrice qui va stocker les information binaire
            matrice[1][1]=image_gris[i][j]
            for f in range(i-1:i+1):
                for k in range(j-1,j+1):
                    if image_gris[f][k] >= image_gris[i][j]:
                        matrice[1+f][1-f]=1
            if image_gris[f][k] >= image_gris[i][j]:
                matrice[1 + f][1 - f] = 1







def appliquer_transformation_2(image_int,rayon):
