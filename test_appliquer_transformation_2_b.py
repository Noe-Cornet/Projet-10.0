import unittest
import numpy as np
from appliquer_transformation_2 import appliquer_transformation_2

class TestAppliquerTransformation2(unittest.TestCase):

    def test_appliquer_transformation_2_b(self):
        image_gris_test = np.array([
            [88, 102, 133, 49, 145, 123],
            [14, 100, 200, 121, 55, 56],
            [40, 101, 92, 100, 99, 30],
            [255, 23, 155, 88, 12, 78],
            [100, 200, 23, 82, 155, 254]
        ], dtype=np.uint8)

        rayon = 2
        tableau_attendu = np.array([
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 4, 5, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0]
        ], dtype=np.uint8)  # Vous devez définir manuellement les valeurs attendues
        tableau_obtenu = appliquer_transformation_2(image_gris_test, rayon)

        self.assertTrue(np.array_equal(tableau_obtenu, tableau_attendu),
                        "Le tableau obtenu ne correspond pas au tableau attendu.")

if __name__ == '__main__':
    unittest.main()
