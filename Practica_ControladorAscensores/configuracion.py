from pisos import Piso
from botonesdepiso import BotonDePiso
from ascensor import Ascensor

class Configuracion():
    def __init__(self, numero_de_piso, numero_de_ascensores):
        self.numero_de_piso = numero_de_piso
        self.numero_de_ascensores = numero_de_ascensores
        self.ascensores = list(filter(lambda ascensor: ascensor, [Ascensor([BotonDePiso(i) for i in range(numero_de_piso + 1)]) for _ in range(numero_de_ascensores + 1)]))
        self.ascensores = [Ascensor([BotonDePiso(i) for i in range(numero_de_piso + 1)]) for _ in range(numero_de_ascensores +1)]
        self.pisos = [Piso(i, self.ascensores[0]) for i in range(numero_de_piso + 1)]
        #enumera y nos lista la cantidad e ascensores , el +1 hace que me cuete des el numero 1 de ascensores y no el 0
        for i, ascensor in enumerate(self.ascensores):
            print(f'Ascensor {i+1}')
