class Livre:
    def __init__(self,titre, auteur, nb_pages,disponible):
        self.titre= titre
        self.auteur= auteur
        self.nb_pages= nb_pages
        self.disponible= disponible
    def modify_attributes(self, titre, auteur, nb_pages):
        if self.nb_pages>0 and type(self.nb_pages)==int:
            self.titre= titre
            self.auteur= auteur
            self.nb_pages= nb_pages
        else:
            print("Le nombre de pages doit être un entier positif")
    def print_attributes(self):
        return f'Titre: {self.titre} Auteur: {self.auteur} Nombre de pages: {self.nb_pages}'
    def emprunter(self):
        if self.disponible:
            self.disponible= False
            return "Livre emprunté"
        else:
            return "Livre non disponible"
    def rendre(self):
        if self.disponible:
            return "Livre déjà disponible"
        else:
            self.disponible= True
            return "Livre rendu"
    def est_disponible(self):
        if self.disponible:
            return "Livre disponible"
        else:
            return "Livre non disponible"
    
Livre.disponible= True

livre_1=Livre("Flamme de l'étalon noir", "Walter Farley", 100, True)
print(livre_1.print_attributes())
livre_1.modify_attributes("Flamme de l'étalon noir", "Walter Farley", 200)
print(livre_1.print_attributes())
print(livre_1.emprunter())
print(livre_1.est_disponible())
print(livre_1.rendre())
print(livre_1.est_disponible())

