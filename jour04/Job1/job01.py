class Personne:
    def __init__(self,nom):
        self.age = 14
        self.nom = nom
    
    def __add__(self,other):
        self.age += other
        return self.age

class Eleve:
    def __init__(self,nom):
        self.eleve=Personne(nom)
    
    def aller_a_l_ecole(self):
        return f'Je m\'appelle {self.eleve.nom} Je vais à l\'école'
    
    def get_age(self):
        return f'J\'ai {self.eleve.age} ans'
    
class Professeur:
    def __init__(self,nom,__matiere):
        self.professeur=Personne(nom)
        self.matiere=__matiere
    
    def enseigner(self):
        return f'Je m\'appelle {self.professeur.nom} Je suis professeur'
    
    def get_age(self):
        return f'J\'ai {self.professeur.age} ans'

    def enseigner(self):
        return f'Je m\'appelle {self.professeur.nom} Je suis professeur de {self.matiere}'
    
personne_1=Eleve('Jean')
print(personne_1.aller_a_l_ecole())
print(personne_1.get_age())
personne_2=Professeur('Leo','Mathématiques')
print(personne_2.enseigner())
print(personne_2.get_age())