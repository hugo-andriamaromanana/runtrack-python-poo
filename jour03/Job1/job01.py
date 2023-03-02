class Ville:
    def __init__(self, nom, nb_habitants):
        self.__nom = nom
        self.nb_habitants = nb_habitants

    def ajouterHabitant(self):
        self.nb_habitants += 1


class Personne:
    def __init__(self, nom, age, ville):
        self.__nom = nom
        self.__age = age
        self.__ville = ville

    def ajouterPopulation(self):
        self.__ville.ajouterHabitant()


print('------------------')
ville_1 = Ville("Antananarivo", 6*10**6)
ville_2 = Ville("Toamasina", 1*10**6)
print(ville_1.nb_habitants)
print(ville_2.nb_habitants)
print('------------------')
personne_1 = Personne("John", 20, ville_1)
personne_1.ajouterPopulation()
print(ville_1.nb_habitants)
print(ville_2.nb_habitants)
print('------------------')
personne_2 = Personne("John", 20, ville_2)
personne_2.ajouterPopulation()
print(ville_1.nb_habitants)
print(ville_2.nb_habitants)
print('------------------')
