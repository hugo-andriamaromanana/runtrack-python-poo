class Operation:
    def __init__(self, nombre1, nombre2):
        self.nombre1 = nombre1
        self.nombre2 = nombre2

Operation.nombre1 = 12
Operation.nombre2 = 3

print(f'Le nombre1 est {Operation.nombre1}')
print(f'Le nombre2 est {Operation.nombre2}')