class Forme:
    def  __init__(self) -> None:
        pass

    def aire(self,hauteur,largeur):
        return 0

class Cercle(Forme):
    def __init__(self,radius):
        self.radius=radius
    def aire(self):
        return 3.14*self.radius**2
    
class Rectangle(Forme):
    def __init__(self,hauteur,largeur):
        self.hauteur=hauteur
        self.largeur=largeur
        
    def aire(self,hauteur,largeur):
        return hauteur*largeur

print('-'*20)
cercle_1=Cercle(2)
print(cercle_1.aire())
print('-'*20)
Rectangle_1=Rectangle(2,3)
print(Rectangle_1.aire(2,3))
print('-'*20)