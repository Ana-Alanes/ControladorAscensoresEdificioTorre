from configuracion import Configuracion

class Edificio:

    def __init__(self, pisos, ascensores):
        self.pisos = pisos
        self.ascensores = ascensores


edificio_torre = Configuracion(20, 4)
edificio_torre.pisos[0].llamar_ascensor(arriba=True)
print('------ASCENSOR "A"----------')
edificio_torre.ascensor.ir_al_piso(25)
edificio_torre.ascensor.ir_al_piso(2)
#
