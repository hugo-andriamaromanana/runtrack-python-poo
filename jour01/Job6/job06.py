class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = 0
    def print_age(self):
        return f"Animal is {self.age} years old"
    def viellir(self):
        self.age += 1
        self.print_age()
    def name_animal(self,username):
        self.name=username
        return(f"Animal is {self.name}")

animal=Animal("Toto",0)
print(animal.print_age())
animal.viellir()
print(animal.print_age())