class Livre:
    def __init__(self,titre, auteur, nb_pages):
        self.titre= titre
        self.auteur= auteur
        self.nb_pages= nb_pages
    def modify_attributes(self, titre, auteur, nb_pages):
        if self.nb_pages>0 and type(self.nb_pages)==int:
            self.titre= titre
            self.auteur= auteur
            self.nb_pages= nb_pages
        else:
            print("Le nombre de pages doit être un entier positif")
    def print_attributes(self):
        return f'Titre: {self.titre} Auteur: {self.auteur} Nombre de pages: {self.nb_pages}'
    

livre_1=Livre("Flamme de l'étalon noir", "Walter Farley", 100)
print(livre_1.print_attributes())
livre_1.modify_attributes("Flamme de l'étalon noir", "Walter Farley", 0.5)
livre_1.modify_attributes("Flamme de l'étalon noir", "Walter Farley", 100)
livre_1.modify_attributes("Flamme de l'étalon noir", "Walter Farley", 200)
print(livre_1.print_attributes())        