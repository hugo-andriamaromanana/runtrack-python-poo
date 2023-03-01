class Voiture:
    def __init__(self, marque, modele, annee, kilometrage, en_marche=False, reservoir=50):
        self.__marque = marque
        self.__modele = modele
        self.__annee = annee
        self.__kilometrage = kilometrage
        self.__en_marche = en_marche
        self.__reservoir = reservoir
    def demarrer(self):
        if self.__en_marche :
            return "La voiture est déjà démarrée"
        elif self.__reservoir > 5:
            self.__en_marche = True
            return "La voiture est démarrée"
        elif self.__reservoir <= 5:
            return "La voiture n'a pas assez d'essence"
    def arreter(self):
        if self.__en_marche:
            self.__en_marche = False
            return "La voiture est arrêtée"
        else:
            return "La voiture est déjà arrêtée"
    def verifier_reservoir(self):
        return f"Le réservoir contient {self.__reservoir} litres"
    def rouler(self, distance):
        if self.__en_marche:
            if distance <= self.__reservoir * 100:
                self.__kilometrage += distance
                self.__reservoir -= distance / 100
                return f"La voiture a parcouru {distance} km"
            else:
                return f"La voiture n'a pas assez d'essence pour {distance} km"
        else:
            return "La voiture n'est pas démarrée"
    def remplir_reservoir(self):
        self.__reservoir = 50
        return "Le réservoir est plein"
        

voiture_1 = Voiture("Peugeot", "308", 2015, 100000)
print('-----------------')
print(voiture_1.demarrer())
print(voiture_1.rouler(1000))
print(voiture_1.verifier_reservoir())
print(voiture_1.rouler(1000))
print(voiture_1.verifier_reservoir())
print('-----------------')
print(voiture_1.rouler(5000))
print(voiture_1.verifier_reservoir())
print(voiture_1.remplir_reservoir())
print('-----------------')