class Animal:
    def __init__(self, name):
        self.name = name
        self.age = 0
    def print_age(self):
        print(f"Animal is {self.age} years old")
    def viellir(self):
        self.age += 1
        self.print_age(self)
    def name_animal(self,username):
        self.name=username
        print(f"Animal is {self.name}")

Animal.age=5
Animal.print_age(Animal)
Animal.viellir(Animal)
Animal.name_animal(Animal,"Toto")