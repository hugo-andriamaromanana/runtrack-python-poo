class Livre:
    def __init__(self,titre, auteur, nb_pages,disponible):
        self.__titre= titre
        self.__auteur= auteur
        self.__nb_pages= nb_pages
        self.__disponible= disponible
    def modify_attributes(self, titre, auteur, nb_pages):
        if self.__nb_pages>0 and type(self.__nb_pages)==int:
            self.__titre= titre
            self.__auteur= auteur
            self.__nb_pages= nb_pages
        else:
            print("Le nombre de pages doit être un entier positif")
    def print_attributes(self):
        return f'Titre: {self.__titre} Auteur: {self.__auteur} Nombre de pages: {self.__nb_pages}'
    def emprunter(self):
        if self.__disponible:
            self.__disponible= False
            return "Livre emprunté"
        else:
            return "Livre non disponible"
    def rendre(self):
        if self.__disponible:
            return "Livre déjà disponible"
        else:
            self.__disponible= True
            return "Livre rendu"
    def est_disponible(self):
        if self.__disponible:
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

