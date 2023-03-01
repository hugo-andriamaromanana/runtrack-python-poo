STATUS = ['En cours', 'Annulée', 'Terminée']
PLATS={
    'Pâtes': 10,
    'Pizza': 12,
    'Salade': 8,
    'Hamburger': 9,
    'Sushi': 15,
    'Tacos': 11,
    'Poulet': 13
}
TVA= 0.2

class Commande:
    def __init__(self, numero_de_commande,listes_de_plats_commande,statut= STATUS[0]):
        self.__numero_de_commande= numero_de_commande
        self.__listes_de_plats_commande= listes_de_plats_commande
        self.__statut= statut
    def ajout_plat(self, plat):
        self.__listes_de_plats_commande[plat]= PLATS[plat]
    def retirer_plat(self, plat):
        self.__listes_de_plats_commande.pop(plat)
    def annuler_commande(self):
        self.__statut= STATUS[1]
        self.__listes_de_plats_commande= {}
    def calculer_prix(self):
        prix= 0
        for plat in self.__listes_de_plats_commande:
            prix+= PLATS[plat]
        return prix*(1+TVA)
    def etat_commande(self):
        return {
            'numero_de_commande': self.__numero_de_commande,
            'listes_de_plats_commande': self.__listes_de_plats_commande,
            'statut': self.__statut,
            'prix': self.__calculer_prix()
        }
    def payer_commande(self):
        self.__statut= STATUS[2]
        self.__listes_de_plats_commande= {}

def pretty(d, indent=0):
   for key, value in d.items():
      print('\t' * indent + str(key))
      if isinstance(value, dict):
         pretty(value, indent+1)
      else:
         print('\t' * (indent+1) + str(value))

commande_1=Commande(1,{'Pâtes': 10, 'Pizza': 12, 'Salade': 8}, STATUS[0])

print('------------------')
print('----STATUT 1------')
print(pretty(commande_1.etat_commande()))
print('------------------')
commande_1.ajout_plat('Hamburger')
print(pretty(commande_1.etat_commande()))
print('------------------')
commande_1.retirer_plat('Pizza')
print(pretty(commande_1.etat_commande()))
print('------------------')
commande_1.annuler_commande()
print(pretty(commande_1.etat_commande()))
print('------------------')

commande_2=Commande(2,{'Pâtes': 10, 'Pizza': 12, 'Salade': 8}, STATUS[0])

print('------------------')
print('----STATUT 2------')
print(pretty(commande_2.etat_commande()))
print('------------------')
commande_2.ajout_plat('Hamburger')
commande_2.ajout_plat('Sushi')
commande_2.ajout_plat('Tacos')
commande_2.ajout_plat('Poulet')
print(pretty(commande_2.etat_commande()))
print('------------------')
commande_2.payer_commande()
print(pretty(commande_2.etat_commande()))