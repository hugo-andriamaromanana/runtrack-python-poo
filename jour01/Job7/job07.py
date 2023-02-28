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

personnage=Personnage(0,0)

print(f'Le personnage est en position {personnage.afficher_position()}')

personnage.move_right()
personnage.move_right()
personnage.move_right()
print(f'Le personnage est en position {personnage.afficher_position()}')
personnage.move_down()
personnage.move_down()
personnage.move_down()
print(f'Le personnage est en position {personnage.afficher_position()}')
personnage.move_left()
personnage.move_left()
personnage.move_left()
print(f'Le personnage est en position {personnage.afficher_position()}')
personnage.move_up()
personnage.move_up()
personnage.move_up()
print(f'Le personnage est en position {personnage.afficher_position()}')