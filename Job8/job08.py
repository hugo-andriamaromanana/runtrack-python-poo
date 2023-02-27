class Personnage:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def move_right(self):
        self.x += 1
    def move_left(self):
        self.x -= 1
    def move_up(self):
        self.y += 1
    def move_down(self):
        self.y -= 1
    def afficher_position(self):
        pos=(self.x,self.y)
        return f'Le personnage est en position {pos}'

Personnage.x=0
Personnage.y=0

print(f'Le personnage est en position {Personnage.afficher_position(Personnage)}')

Personnage.move_right(Personnage)
Personnage.move_right(Personnage)
Personnage.move_right(Personnage)
print(f'Le personnage est en position {Personnage.afficher_position(Personnage)}')
Personnage.move_down(Personnage)
Personnage.move_down(Personnage)
Personnage.move_down(Personnage)
print(f'Le personnage est en position {Personnage.afficher_position(Personnage)}')
Personnage.move_up(Personnage)
Personnage.move_up(Personnage)
Personnage.move_up(Personnage)
print(f'Le personnage est en position {Personnage.afficher_position(Personnage)}')
Personnage.move_left(Personnage)
Personnage.move_left(Personnage)
Personnage.move_left(Personnage)