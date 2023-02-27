class Cercle:
    def __init__(self, rayon):
        self.rayon = rayon

    def aire(self):
        return self.rayon * self.rayon * 3.14

    def circonference(self):
        return self.rayon * 2 * 3.14

    def diametre(self):
        return self.rayon * 2

    def afficher_infos(self):
        return f'Le rayon est {self.rayon} \n l aire est {self.aire(self)}\n la circonference est {self.circonference(self)}\n le diametre est {self.diametre(self)}'


cercle_4=Cercle(4)

print(f' Le rayon est {Cercle.afficher_infos(Cercle)}')

cercle_7=Cercle(7)

print(f' Le rayon est {Cercle.afficher_infos(Cercle)}')
