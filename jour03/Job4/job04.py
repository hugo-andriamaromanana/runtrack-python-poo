class Joueur:
    def __init__(self,nom,numero,position,nb_de_buts,passe_decisive,cartons_jaunes,cartons_rouges):
        self.nom= nom
        self.numero= numero
        self.position= position
        self.nb_de_buts= nb_de_buts
        self.passe_decisive= passe_decisive
        self.cartons_jaunes= cartons_jaunes
        self.cartons_rouges= cartons_rouges
    def ajouterBut(self):
        self.nb_de_buts+=1
    def ajouterPasseDecisive(self):
        self.passe_decisive+=1
    def ajouterCartonJaune(self):
        self.cartons_jaunes+=1
    def ajouterCartonRouge(self):
        self.cartons_rouges+=1
    def print_attributes(self):
        return f'Nom: {self.nom} Numero: {self.numero} Position: {self.position} Nombre de buts: {self.nb_de_buts} Passe décisive: {self.passe_decisive} Cartons jaunes: {self.cartons_jaunes} Cartons rouges: {self.cartons_rouges}'


class Equipe:
    def __init__(self):
        self.nom= ''
        self.liste_joueurs=[]
    def ajouterJoueur(self,joueur):
        self.liste_joueurs.append(joueur)
    def afficherJoueurs(self):
        for joueur in self.liste_joueurs:
            print(joueur.print_attributes())
    def print_player_attributes(self, nom):
        for joueur in self.liste_joueurs:
            if joueur.nom==nom:
                print(joueur.print_attributes())
    def update_player_attributes(self, nom, numero, position):
        for joueur in self.liste_joueurs:
            if joueur.nom==nom:
                joueur.numero= numero
                joueur.position= position
print('--------------------------------------------------------------------------------------------------')
equipe_1=Equipe()
equipe_1.nom="Manchester United"
joueur_1=Joueur("Paul Pogba", 6, "Milieu", 0, 0, 0, 0)
joueur_2=Joueur("Bruno Fernandes", 18, "Milieu", 0, 0, 0, 0)
joueur_3=Joueur("Marcus Rashford", 10, "Attaquant", 0, 0, 0, 0)
joueur_4=Joueur("Anthony Martial", 11, "Attaquant", 0, 0, 0, 0)
joueur_5=Joueur("Harry Maguire", 5, "Défenseur", 0, 0, 0, 0)
joueur_6=Joueur("Luke Shaw", 23, "Défenseur", 0, 0, 0, 0)
joueur_7=Joueur("David de Gea", 1, "Gardien", 0, 0, 0, 0)
equipe_1.ajouterJoueur(joueur_1)
equipe_1.ajouterJoueur(joueur_2)
equipe_1.ajouterJoueur(joueur_3)
equipe_1.ajouterJoueur(joueur_4)
equipe_1.ajouterJoueur(joueur_5)
equipe_1.ajouterJoueur(joueur_6)
equipe_1.ajouterJoueur(joueur_7)
equipe_1.afficherJoueurs()
print('--------------------------------------------------------------------------------------------------')
equipe_1.print_player_attributes("Paul Pogba")
print('--------------------------------------------------------------------------------------------------')
equipe_1.update_player_attributes("Paul Pogba", 6, "Milieu")
print('--------------------------------------------------------------------------------------------------')
equipe_1.print_player_attributes("Paul Pogba")
print('--------------------------------------------------------------------------------------------------')
equipe_2=Equipe()
equipe_2.nom="Manchester City"
joueur_8=Joueur("Kevin De Bruyne", 17, "Milieu", 0, 0, 0, 0)
joueur_9=Joueur("Raheem Sterling", 7, "Attaquant", 0, 0, 0, 0)
joueur_10=Joueur("Sergio Agüero", 10, "Attaquant", 0, 0, 0, 0)
joueur_11=Joueur("Aymeric Laporte", 14, "Défenseur", 0, 0, 0, 0)
joueur_12=Joueur("John Stones", 5, "Défenseur", 0, 0, 0, 0)
joueur_13=Joueur("Ederson", 31, "Gardien", 0, 0, 0, 0)
equipe_2.ajouterJoueur(joueur_8)
equipe_2.ajouterJoueur(joueur_9)
equipe_2.ajouterJoueur(joueur_10)
equipe_2.ajouterJoueur(joueur_11)
equipe_2.ajouterJoueur(joueur_12)
equipe_2.ajouterJoueur(joueur_13)
equipe_2.afficherJoueurs()
print('--------------------------------------------------------------------------------------------------')
equipe_2.print_player_attributes("Kevin De Bruyne")
print('--------------------------------------------------------------------------------------------------')
equipe_2.update_player_attributes("Kevin De Bruyne", 17, "Milieu")
print('--------------------------------------------------------------------------------------------------')
equipe_2.print_player_attributes("Kevin De Bruyne")
print('--------------------------------------------------------------------------------------------------')

#Game simulation

print("Match de football entre Manchester United et Manchester City")
print("Le match commence")
print("Manchester United attaque")
print("Manchester United tire")
print("But de Manchester United")
print('--------------------------------------------------------------------------------------------------')
joueur_1.ajouterBut()       
joueur_2.ajouterPasseDecisive()
print(joueur_1.print_attributes())
print('--------------------------------------------------------------------------------------------------')
print("Manchester United attaque")
print("Manchester United tire")
print("But de Manchester United")

joueur_2.ajouterBut()
print(joueur_2.print_attributes())
print('--------------------------------------------------------------------------------------------------')
print("Manchester City attaque")
print("Manchester City tire")
print("But de Manchester City")
joueur_9.ajouterBut()
print(joueur_9.print_attributes())
print('--------------------------------------------------------------------------------------------------')


print('Faute de Paul Pogba')
joueur_1.ajouterCartonJaune()
print('--------------------------------------------------------------------------------------------------')
print(joueur_1.print_attributes())
print('Faute de Bruno Fernandes')
joueur_2.ajouterCartonJaune()
print('--------------------------------------------------------------------------------------------------')
print(joueur_2.print_attributes())

print('Faute de Paul Pogba')
joueur_1.ajouterCartonRouge()
print('--------------------------------------------------------------------------------------------------')
print(joueur_1.print_attributes())
