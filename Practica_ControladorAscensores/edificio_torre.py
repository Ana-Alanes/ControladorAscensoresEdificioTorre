from configuracion import Configuracion

class Edificio:

    def __init__(self, pisos, ascensores):
        self.pisos = pisos
        self.ascensores = ascensores


edificio_torre = Configuracion(numero_de_piso=20, numero_de_ascensores=3)
edificio_torre.pisos[0].llamar_ascensor(arriba=True)
edificio_torre.ascensores[0].ir_al_piso(25)
edificio_torre.ascensores[2].ir_al_piso(2)
edificio_torre.ascensores[3].ir_al_piso(8)


