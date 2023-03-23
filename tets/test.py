import unittest 
from punto import Punto,rectangulo 

class test(unittest.TestCase):
    def test_constructor(self):
        A=Punto(2,3)
        B=Punto(5,5)
        C=Punto(-3,-1)
        D=Punto(0,0)
        self.assertEqual(A.__init__(),"(2,3)")
        self.assertEqual(B.__init__(),"(5,5)")
        self.assertEqual(C.__init__(),"(-3,-1)")
        self.assertEqual(D.__init__(),"(0,0)")
    



