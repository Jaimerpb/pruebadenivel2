import unittest 
from punto import Punto,rectangulo 

class test(unittest.TestCase):
    def test_constructor(self):
        A=Punto(2,3)
        B=Punto(5,5)
        C=Punto(-3,-1)
        D=Punto(0,0)
        self.assertEqual(A.__init__(),None)
        self.assertEqual(B.__init__(),None)
        self.assertEqual(C.__init__(),None)
        self.assertEqual(D.__init__(),None)
    def test_cuadrante(self,A,C,D):
        self.assertEqual(A.cuadrante(),None)
        self.assertEqual(C.cuadrante(),None)
        self.assertEqual(D.cuadrante(),None)
    def test_vector(self,A,B):
        self.assertEqual(A.vector(B),None)
        self.assertEqual(B.vector(A),None)
    def test_distancia(self,A,B):
        self.assertEqual(A.distancia(B),None)
    
    def test_rectangulo()





