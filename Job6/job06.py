class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def afficher_les_Points(self):
        return f'Le point est ({self.x}, {self.y})'
    def afficher_x(self):
        return f'Le point x est ({self.x})'
    def afficher_y(self):
        return f'Le point y est ({self.y})'
    def changer_x(self, x):
        self.x = x
    def changer_y(self, y):
        self.y = y

Point.x=1
Point.y=2

print(f'Le point est affiché {Point.afficher_les_Points(Point)}')
print(f'Le point x est affiché {Point.afficher_x(Point)}')
print(f'Le point y est affiché {Point.afficher_y(Point)}')
print(f'Le point x est changé {Point.changer_x(Point, 3)}')
print(f'Le point y est changé {Point.changer_y(Point, 4)}')
print(f'Le point est affiché {Point.afficher_les_Points(Point)}')