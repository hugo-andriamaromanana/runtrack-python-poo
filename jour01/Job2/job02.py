class Operation:
    def __init__(self, nombre1, nombre2):
        self.nombre1 = nombre1
        self.nombre2 = nombre2

nombre=Operation(3,7)

print(f'le nombre 1 est {nombre.nombre1}')
print(f'le nombre 2 est {nombre.nombre2}')