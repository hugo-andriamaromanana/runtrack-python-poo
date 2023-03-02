class Personnage:
    def __init__(self, nom, vie):
        self.nom = nom
        self.vie = vie

    def subirDegats(self, degats):
        print(f"{self.nom} subit {degats} points de dégâts !")
        self.vie -= degats

    def attaquer(self, ennemi):
        print(f"{self.nom} attaque {ennemi.nom} !")
        ennemi.subirDegats(self.vie)

    def estVivant(self):
        return self.vie > 0


class Jeu:
    def __init__(self):
        self.niveau = 0

    def choisirNiveau(self):
        self.niveau = int(
            input("Choisissez le niveau de difficulté (1, 2 ou 3): "))

    def lancerJeu(self):
        self.choisirNiveau()
        if self.niveau == 1:
            joueur = Personnage("Joueur", 100)
            ennemi = Personnage("Ennemi", 100)
        elif self.niveau == 2:
            joueur = Personnage("Joueur", 200)
            ennemi = Personnage("Ennemi", 200)
        elif self.niveau == 3:
            joueur = Personnage("Joueur", 300)
            ennemi = Personnage("Ennemi", 300)
        else:
            print("Niveau de difficulté invalide")
            return
        while joueur.estVivant() and ennemi.estVivant():
            joueur.attaquer(ennemi)
            print(f"Vie de l'ennemi: {ennemi.vie}")
            ennemi.attaquer(joueur)
            print(f"Vie du joueur: {joueur.vie}")
        if joueur.estVivant():
            print("Vous avez gagné !")
        else:
            print("Vous avez perdu !")


jeu = Jeu()
jeu.lancerJeu()
