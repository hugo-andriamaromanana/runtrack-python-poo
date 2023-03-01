class Tache:
    def __init__(self, titre, description, statut):
        self.titre= titre
        self.description= description
        self.statut= statut

class ListedeTache:
    def __init__(self):
        self.taches= []
    def ajouterTache(self, tache):
        self.taches.append(tache)
    def supprimerTache(self, tache):
        self.taches.remove(tache)
    def tache_done(self, titre):
        for tache in self.taches:
            if tache.titre==titre:
                tache.statut= "Done"
    def tache_undone(self, titre):
        for tache in self.taches:
            if tache.titre==titre:
                tache.statut= "Undone"
    def print_Taches(self):
        for tache in self.taches:
            print(tache.titre, tache.description, tache.statut)

tache_1= Tache("Tache 1", "Description de la tache 1", "Undone")
tache_2= Tache("Tache 2", "Description de la tache 2", "Undone")
tache_3= Tache("Tache 3", "Description de la tache 3", "Undone")

print('------------------')
liste_taches= ListedeTache()
liste_taches.ajouterTache(tache_1)
liste_taches.ajouterTache(tache_2)
liste_taches.ajouterTache(tache_3)

liste_taches.print_Taches()
print('------------------')
liste_taches.tache_done("Tache 1")
liste_taches.print_Taches()

print('------------------')
liste_taches.supprimerTache(tache_2)
liste_taches.print_Taches()