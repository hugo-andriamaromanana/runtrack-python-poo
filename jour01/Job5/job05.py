class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def afficher_les_points(self):
        return f'Le point est ({self.x}, {self.y})'
    def afficher_x(self):
        return f'Le point x est ({self.x})'
    def afficher_y(self):
        return f'Le point y est ({self.y})'
    def changer_x(self, x):
        self.x = x
    def changer_y(self, y):
        self.y = y

point=Point(3,4)

print(f'Le point est affiché {point.afficher_les_points()}')
print(f'Le point x est affiché {point.afficher_x()}')
print(f'Le point y est affiché {point.afficher_y()}')
print(f'Le point x est changé {point.changer_x(3)}')
print(f'Le point y est changé {point.changer_y(4)}')
print(f'Le point est affiché {point.afficher_les_points()}')