class Personne:
    def __init__(self, prenom, nom):
        self.prenom = prenom
        self.nom = nom
    def SePresenter(self):
        return f'Je suis {self.prenom} {self.nom}'
    
print(Personne.SePresenter(Personne('John', 'Doe')))
print(Personne.SePresenter(Personne('Jean', 'Dupont')))