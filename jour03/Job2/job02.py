class CompteBancaire:
    def __init__(self, nom, prenom, solde, decouvert):
        self.__nom = nom
        self.__prenom = prenom
        self.__solde = solde

    def afficher(self):
        return f'Nom: {self.__nom} Prénom: {self.__prenom} Solde: {self.__solde}'

    def versement(self, somme):
        if somme > 0:
            self.__solde += somme

    def retrait(self, somme):
        if somme > 0:
            self.__solde -= somme
        else:
            print("No money? No honey!")

    def auth_decouvert(self, somme):
        if somme > self.__solde:
            return True
        else:
            return False

    def virement(self, compte, somme):
        if somme > 0:
            self.__solde -= somme
            compte.__solde += somme
        else:
            print("No money? No honey!")

    def agios(self):
        if self.__solde < 0:
            self.__solde -= 5
        else:
            print("No money? No honey!")


compte_1 = CompteBancaire("Doe", "John", 5000, 0)
compte_2 = CompteBancaire("Doe", "Jane", 5000, 0)
print(compte_1.afficher())
print(compte_2.afficher())
compte_1.virement(compte_2, 50)
print(compte_1.afficher())
print(compte_2.afficher())
compte_1.virement(compte_2, 5000)
print(compte_1.afficher())
print(compte_2.afficher())
