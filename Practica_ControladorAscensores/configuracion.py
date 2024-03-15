from pisos import Piso
from botonesdepiso import BotonDePiso
from ascensor import Ascensor

class Configuracion():
    def __init__(self, numero_de_piso, numero_de_ascensores):
        self.numero_de_piso = numero_de_piso
        self.numero_de_ascensores = numero_de_ascensores
        self.ascensores = [Ascensor(self.numero_de_piso + 1) for i in range(self.numero_de_piso + 1)]

        self.pisos = [Piso(i, self.ascensores[0]) for i in range(numero_de_piso + 1)]



