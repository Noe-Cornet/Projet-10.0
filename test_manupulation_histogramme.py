from manupulation_histogramme import calculer_histogramme
from manupulation_histogramme import calculer_distance_1
from manupulation_histogramme import calculer_distance_2
import numpy as np
def test_manupulation_histogramme():
   r = np.array([[4,0,2,3],[3,2,2,2],[4,0,2,3],[2,3,2,2]])
   tableau=np.array([[255,160,10,49],[20,170,1,121],[30,233,230,100],[255,23,155,88]])
   assert np.all(calculer_histogramme(tableau,3) == r)

def test_calculer_distance1():
    histogramme1 = np.array(range(1, 6))
    histogramme2 = np.array(range(2, 7))
    assert calculer_distance_1(histogramme1,histogramme2)==2.24


def test_calculer_distance_2():
    histogramme1 = np.array(range(1, 6))
    histogramme2 = np.array(range(2, 7))
    assert calculer_distance_2(histogramme1,histogramme2)==5

