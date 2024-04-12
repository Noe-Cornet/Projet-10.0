import numpy as np
from appliquer_transformation_2 import appliquer_transformation_2

# Données de test
image_gris_test = np.array([
    [88, 102, 133, 49, 145, 123],
    [14, 100, 200, 121, 55, 56],
    [40, 101, 92, 100, 99, 30],
    [255, 23, 155, 88, 12, 78],
    [100, 200, 23, 82, 155, 254]
])

# Rayon donné dans le PDF
rayon = 1

tableau_attendu = np.array([
    [0, 0, 0, 0, 0, 0],
    [0, 3, 6, 3, 6, 0],
    [0, 6, 5, 3, 5, 0],
    [0, 7, 5, 3, 6, 0],
    [0, 0, 0, 0, 0, 0]
])

# Appliquer la transformation
tableau_obtenu = appliquer_transformation_2(image_gris_test, rayon)

# Vérification avec assert
assert np.array_equal(tableau_obtenu, tableau_attendu), "Le tableau obtenu ne correspond pas au tableau attendu."

# Print un message si le test passe avec succes
print("Le test 2a a passé avec succès.")
