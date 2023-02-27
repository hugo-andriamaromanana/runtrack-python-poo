class Produit:
    def __init__(self, nom, prixHT, TVA):
        self.nom = nom
        self.prix = prixHT
        self.TVA = TVA

    def CalculerPrixTTC(self):
        return self.prix * (1 + self.TVA / 100)

    def AfficherPrixTTC(self):
        return f'Le prix TTC de {self.nom} est {self.CalculerPrixTTC()}'

    def ModifierNometPrix(self, nom, prixHT):
        self.prix = prixHT
        self.nom = nom

    def infos(self):
        return f'Le nom du produit est {self.nom} \n son prix est {self.prix} \n sa TVA est {self.TVA} \n son prix TTC est {self.CalculerPrixTTC(self)}'

Produit.nom = 'Pomme'
Produit.prix = 1.5
Produit.TVA = 20

print(f'Le prix TTC de {Produit.nom} est {Produit.CalculerPrixTTC(Produit)}')

Produit.nom = 'Poire'
Produit.prix = 2.5
Produit.TVA = 20

print(f'Le prix TTC de {Produit.nom} est {Produit.CalculerPrixTTC(Produit)}')

Produit.ModifierNometPrix(Produit, 'Poire_deluxe', 3.5)

print(f'Le prix TTC de {Produit.nom} est {Produit.CalculerPrixTTC(Produit)}')

print(f'Les infos du produit sont {Produit.infos(Produit)}')