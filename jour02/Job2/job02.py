class Livre:
    def __init__(self,titre, auteur, nb_pages):
        self.__titre= titre
        self.__auteur= auteur
        self.__nb_pages= nb_pages
    def modify_attributes(self, titre, auteur, nb_pages):
        if self.__nb_pages>0 and type(self.__nb_pages)==int:
            self.__titre= titre
            self.__auteur= auteur
            self.__nb_pages= nb_pages
        else:
            print("Le nombre de pages doit être un entier positif")
    def print_attributes(self):
        return f'Titre: {self.__titre} Auteur: {self.__auteur} Nombre de pages: {self.__nb_pages}'
    

livre_1=Livre("Flamme de l'étalon noir", "Walter Farley", 100)
print(livre_1.print_attributes())
livre_1.modify_attributes("Flamme de l'étalon noir", "Walter Farley", 0.5)
livre_1.modify_attributes("Flamme de l'étalon noir", "Walter Farley", 100)
livre_1.modify_attributes("Flamme de l'étalon noir", "Walter Farley", 200)
print(livre_1.print_attributes())        