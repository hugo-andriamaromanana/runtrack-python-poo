class Personne:
    def __init__(self, prenom, nom):
        self.prenom = prenom
        self.nom = nom
    def SePresenter(self):
        return f'Je suis {self.prenom} {self.nom}'
    
dude_1=Personne('John', 'Doe')
dude_2=Personne('Jean', 'Dupont')

print(f'Je suis {dude_1.SePresenter()}')
print(f'Je suis {dude_2.SePresenter()}')