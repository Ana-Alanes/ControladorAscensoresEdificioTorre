from Ascensor import Ascensor
from Pisos import Piso
class BotonDePiso:
    def __init__(self, numero_de_piso):
        self.numero_de_piso = numero_de_piso
        self.encendido = False
class Configuracion():
    def __init__(self, numero_de_piso, ascensor):
        self.numero_de_piso = numero_de_piso
        self.ascensor = ascensor
        self.botones_de_pisos_A = [BotonDePiso(i) for i in range(self.numero_de_piso + 1)]
        self.botones_de_pisos_B = [BotonDePiso(i) for i in range(self.numero_de_piso + 1)]
        self.botones_de_pisos_C = [BotonDePiso(i) for i in range(self.numero_de_piso + 1)]
        self.ascensorA = Ascensor(self.botones_de_pisos_A)
        self.ascensorB = Ascensor(self.botones_de_pisos_B)
        self.ascensorC = Ascensor(self.botones_de_pisos_C)
        self.pisos = [Piso(i, self.ascensorA) for i in range(self.numero_de_piso + 1)]