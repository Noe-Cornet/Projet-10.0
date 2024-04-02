from PIL import Image
import numpy as np

#initialise une matrice de taille m,n
def initialiser_matrice(m,n):
  matrice=[]
  j=[0]
  for i in range(m):
    matrice.append(j*n)
  return matrice
#transphorme une liste de binaire en un nombre decimal
def binaire_en_decimal(liste_binaire):    #
  n=len(liste_binaire)
  somme=0
  j=n-1
  for i in range(n):
    somme=somme + liste_binaire[i]*2**j
    j-=1
  return somme
liste=[1,1,1,0,1,0]
print(binaire_en_decimal(liste))


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
        image_gris = np.array(image_gris)
        nb_ligne = len(image_gris)
        nb_colone = len(image_gris[1])
        image_transphorme = initialiser_matrice(nb_ligne, nb_colone)

        # parcour le tableau sauf les bordure
        for i in range(1, len(image_gris) - 1):
            for j in range(1, len(image_gris[0]) - 1):

                gc = image_gris[i][j]
                liste_b = []

                # parcour la ligne superieur
                for k in range(j - 1, j + 2):
                    if image_gris[i - 1][k] < image_gris[i][j]:
                        n = 0
                        liste_b.append(n)

                    elif image_gris[i - 1][k] >= image_gris[i][j]:
                        n = 1
                        liste_b.append(n)

                # parcour la colone de droite
                if image_gris[i][j + 1] < image_gris[i][j]:
                    n = 0
                    liste_b.append(n)

                elif image_gris[i][j + 1] >= image_gris[i][j]:
                    n = 1
                    liste_b.append(n)

                # parcour la ligne inferieure
                for k in range(j + 1, j - 2, -1):
                    if image_gris[i + 1][k] < image_gris[i][j]:
                        n = 0
                        liste_b.append(n)

                    elif image_gris[i + 1][k] >= image_gris[i][j]:
                        n = 1
                        liste_b.append(n)

                # parcour la colone de gauche
                if image_gris[i][j - 1] < image_gris[i][j]:
                    n = 0
                    liste_b.append(n)

                elif image_gris[i][j - 1] >= image_gris[i][j]:
                    n = 1
                    liste_b.append(n)

                # transphorme la liste de nombre binaire en un nombre réel
                reel = binaire_en_decimal(liste_b)
                image_transphorme[i][j] = reel
         return image_transphorme













def appliquer_transformation_2(image_int,rayon):