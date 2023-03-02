# BLACKJACK

import random


class Cartes:
    def __init__(self, couleur, valeur):
        self.couleur = couleur
        self.valeur = valeur

    def __str__(self):
        return f"{self.valeur} de {self.couleur}"

    def deck(self):
        couleurs = ["pique", "coeur", "carreau", "trefle"]
        valeurs = ["as", "2", "3", "4", "5", "6", "7",
                   "8", "9", "10", "valet", "dame", "roi"]
        deck = []
        for couleur in couleurs:
            for valeur in valeurs:
                deck.append(Cartes(couleur, valeur))
        return deck


class Jeu:
    def __init__(self, nom):
        self.nom = nom
        self.deck = Cartes.deck(self)
        self.main = []
        self.score = 0
        self.score_ordi = 0
        self.choix = ""

    def __str__(self):
        return f"{self.nom} a {self.score} points"

    def eval_score(self):
        for carte in self.main:
            if carte.valeur in ["valet", "dame", "roi"]:
                self.score += 10
            if carte.valeur in ["2", "3", "4", "5", "6", "7", "8", "9", "10"]:
                self.score += int(carte.valeur)
            if carte.valeur == "as":
                if self.score <= 10:
                    self.score += 11
                else:
                    self.score += 1
        return self.score

    def eval_score_ordi(self):
        for carte in self.main:
            if carte.valeur in ["valet", "dame", "roi"]:
                self.score_ordi += 10
            if carte.valeur in ["2", "3", "4", "5", "6", "7", "8", "9", "10"]:
                self.score_ordi += int(carte.valeur)
            if carte.valeur == "as":
                if self.score_ordi <= 10:
                    self.score_ordi += 11
                else:
                    self.score_ordi += 1
        return self.score_ordi

    def tirer(self):
        carte = random.choice(self.deck)
        self.deck.remove(carte)
        self.main.append(carte)
        return carte

    def tirer_ordi(self):
        carte = random.choice(self.deck)
        self.deck.remove(carte)
        self.main.append(carte)
        return carte

    def afficher_main(self):
        for carte in self.main:
            print(carte)

    def afficher_main_ordi(self):
        for carte in self.main:
            print(carte)

    def afficher_score(self):
        print(f"{self.nom} a {self.score} points")

    def afficher_score_ordi(self):
        print(f"{self.nom} a {self.score_ordi} points")

    def choix_joueur(self):
        self.choix = input("Voulez-vous tirer une carte ? (o/n) : ")
        return self.choix

    def choix_ordi(self):
        if self.score_ordi < 17:
            self.choix = "o"
        else:
            self.choix = "n"
        return self.choix

    def reset(self):
        self.main = []
        self.score = 0
        self.score_ordi = 0
        self.choix = ""
        self.deck = Cartes.deck(self)

    def reset_score(self):
        self.score = 0

    def reset_score_ordi(self):
        self.score_ordi = 0


def main():
    jeu = Jeu("Joueur")
    jeu_ordi = Jeu("Ordinateur")
    while True:
        print('-' * 15)
        print("Bienvenue au BlackJack !")
        print('-' * 15)
        jeu.reset()
        jeu_ordi.reset()
        jeu.tirer()
        jeu.tirer()
        jeu_ordi.tirer()
        jeu_ordi.tirer()
        jeu.eval_score()
        jeu_ordi.eval_score_ordi()
        print("Voici votre main :")
        jeu.afficher_main()
        jeu.afficher_score()
        print('-' * 15)
        print("Voici la main de l'ordinateur :")
        jeu_ordi.afficher_main_ordi()
        jeu_ordi.afficher_score_ordi()
        print('-' * 15)
        while jeu.choix_joueur() == "o":
            jeu.reset_score()
            jeu.tirer()
            jeu.eval_score()
            jeu.afficher_main()
            jeu.afficher_score()
            if jeu.score > 21:
                print("Vous avez perdu !")
                break
        if jeu.score <= 21:
            while jeu_ordi.choix_ordi() == "o":
                jeu_ordi.reset_score_ordi()
                jeu_ordi.tirer_ordi()
                jeu_ordi.eval_score_ordi()
                jeu_ordi.afficher_main_ordi()
                jeu_ordi.afficher_score_ordi()
                if jeu_ordi.score_ordi > 21:
                    print("Vous avez gagné !")
                    break
            if jeu_ordi.score_ordi <= 21:
                if jeu.score > jeu_ordi.score_ordi:
                    print("Vous avez gagné !")
                elif jeu.score < jeu_ordi.score_ordi:
                    print("Vous avez perdu !")
                else:
                    print("Egalité !")
        if input("Voulez-vous rejouer ? (o/n) : ") == "n":
            break


if __name__ == "__main__":
    main()
