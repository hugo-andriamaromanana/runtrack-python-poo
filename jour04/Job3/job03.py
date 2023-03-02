class Rectangle:
    def __init__(self, largeur, longeur):
        self.__largeur = largeur
        self.__longeur = longeur

    def get_largeur(self):
        return self.__largeur

    def get_longeur(self):
        return self.__longeur

    def set_largeur(self, largeur):
        self.__largeur = largeur

    def set_longeur(self, longeur):
        self.__longeur = longeur

    def perimetre(self):
        return 2*(self.__largeur+self.__longeur)

    def surface(self):
        return self.__largeur*self.__longeur


class Parallelepipede(Rectangle):
    def __init__(self, largeur, longeur, hauteur):
        super().__init__(largeur, longeur)
        self.__hauteur = hauteur

    def get_hauteur(self):
        return self.__hauteur

    def set_hauteur(self, hauteur):
        self.__hauteur = hauteur

    def volume(self):
        return self.__hauteur*self.surface()


print('-'*20)
rectangle_1 = Rectangle(2, 3)
print(rectangle_1.surface())
print('-'*20)
print(rectangle_1.perimetre())
print('-'*20)
rectangle_1.set_largeur(4)
print(rectangle_1.surface())
print('-'*20)
parallelepipede_1 = Parallelepipede(2, 3, 4)
print(parallelepipede_1.volume())
print('-'*20)
parallelepipede_1.set_hauteur(5)
print(parallelepipede_1.volume())
print('-'*20)
