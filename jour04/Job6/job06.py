class Vehicule:
    def __init__(self,marque,annee,prix):
        self.marque=marque
        self.annee=annee
        self.prix=prix
    def infos_v(self):
        return f'La marque est {self.marque} , l\'année est {self.annee} et le prix est {self.prix}'
    def rouler(self):
        return f'Le véhicule roule'

class Voiture(Vehicule):
    def __init__(self,marque,annee,prix):
        super().__init__(marque,annee,prix)
        self.portes= 4
    def infos_v(self):
        return f'La marque est {self.marque} , l\'année est {self.annee} et le prix est {self.prix} et le nombre de portes est {self.portes}'
    def rouler(self):
        return f'La voiture roule'

class Moto(Vehicule):
    def __init__(self,marque,annee,prix):
        super().__init__(marque,annee,prix)
        self.roues= 2
    def infos_v(self):
        return f'La marque est {self.marque} , l\'année est {self.annee} et le prix est {self.prix} et le nombre de roues est {self.roues}'
    def rouler(self):
        return f'La moto roule'
    
print('-'*50)
vehicule_1=Vehicule('Peugeot',2020,10000)
print(vehicule_1.infos_v())
print(vehicule_1.rouler())
print('-'*50)
voiture_1=Voiture('Peugeot',2012,10000)
print(voiture_1.infos_v())
print(voiture_1.rouler())
print('-'*50)
moto_1=Moto('Peugeot',2022,10000)
print(moto_1.infos_v())
print(moto_1.rouler())
print('-'*50)
