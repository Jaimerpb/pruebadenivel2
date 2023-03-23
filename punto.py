import math

class Punto:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def __str__(self):
        return f"Punto de coordenadas: ({self.x},{self.y}) "

    @staticmethod
    def cuadrante(self):
        if self.x>0 and self.y>0 :
             return f"El punto ({self.x},{self.y}) está en el primer cuadrante"
        elif self.x<0 and self.y>0:
            return f"El punto ({self.x},{self.y}) está en el segundo cuadrante"
        elif self.x<0 and self.y<0:
            return f"El punto ({self.x},{self.y}) está en el tercer cuadrante"
        elif self.x>0 and self.y>0:
            return f"El punto ({self.x},{self.y}) está en el cuarto cuadrante"
        elif self.x==0 and self.y!=0:
            return f"El punto ({self.x},{self.y}) está sobre el eje y" 
        elif self.x!=0 and self.y==0:
            return f"El punto ({self.x},{self.y}) está sobre el eje x"
    @staticmethod 
    def vector(self,Punto):
        return f"Vector: {abs(Punto.x-self.x)},{abs(Punto.y-self.y)}"
    @staticmethod 
    def distancia(self,Punto):
        #import amth 
        return f"Distancia entre {Punto} y {self}:{math.sqrt((Punto.x-self.x)**2+(Punto.y-self.y)**2)}"
    
class rectangulo(Punto):
    
        



        
    
        
        

