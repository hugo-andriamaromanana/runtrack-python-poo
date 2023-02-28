class Rectangle:
    def __init__(self,longueur, largeur):
        self.longueur= longueur
        self.largeur= largeur
    def modify_attributes(self, longueur, largeur):
        self.longueur= longueur
        self.largeur= largeur
    def print_attributes(self):
        return f'Longueur: {self.longueur} Largeur: {self.largeur}'
    

rect_1=Rectangle(10, 20)
print(rect_1.print_attributes())
rect_1.modify_attributes(20, 30)
print(rect_1.print_attributes())
