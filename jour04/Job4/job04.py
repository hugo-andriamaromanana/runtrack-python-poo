class Forme:
    def aire(self,hauteur,largeur):
        return 0

class Rectangle(Forme):
    def __init__(self,hauteur,largeur):
        self.hauteur=hauteur
        self.largeur=largeur
        
    def aire(self,hauteur,largeur):
        return hauteur*largeur
        
Rectangle_1=Rectangle(2,3)
print(Rectangle_1.aire(2,3))
    