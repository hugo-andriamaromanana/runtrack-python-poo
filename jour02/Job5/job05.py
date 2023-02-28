class Voiture:
    def __init__(self, marque, modele, annee, kilometrage, en_marche=False, reservoir=50):
        self.marque = marque
        self.modele = modele
        self.annee = annee
        self.kilometrage = kilometrage
        self.en_marche = en_marche
        self.reservoir = reservoir
    def demarrer(self):
        if self.en_marche :
            return "La voiture est déjà démarrée"
        elif self.reservoir > 5:
            self.en_marche = True
            return "La voiture est démarrée"
        elif self.reservoir <= 5:
            return "La voiture n'a pas assez d'essence"
    def arreter(self):
        if self.en_marche:
            self.en_marche = False
            return "La voiture est arrêtée"
        else:
            return "La voiture est déjà arrêtée"
    def verifier_reservoir(self):
        return f"Le réservoir contient {self.reservoir} litres"
    def rouler(self, distance):
        if self.en_marche:
            if distance <= self.reservoir * 100:
                self.kilometrage += distance
                self.reservoir -= distance / 100
                return f"La voiture a parcouru {distance} km"
            else:
                return f"La voiture n'a pas assez d'essence pour {distance} km"
        else:
            return "La voiture n'est pas démarrée"
    def remplir_reservoir(self):
        self.reservoir = 50
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