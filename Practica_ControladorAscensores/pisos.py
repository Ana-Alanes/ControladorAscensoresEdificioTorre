import time

class Piso:
    def __init__(self, numero_piso, ascensor):
        self.numero_piso = numero_piso
        self.boton_arriba = False
        self.boton_abajo = False
        self.ascensor = ascensor
        self.tiempo_de_apertura_ascensor = 5

    """ En esta funcion hace que si el ascensor va arriba significa true,
        y si el usuario quiere bajar es false """
    def llamar_ascensor(self, arriba):
        if arriba:
            self.boton_arriba = True
            self.abrir_ascensor()
            self.boton_arriba = False
        else:
            print("Bajando:.........")
            self.boton_abajo = True
            self.abrir_ascensor()
            self.boton_abajo = False

    def get_ascensor_mas_cercano(self):
        if not self.ascensores:
            return None  # Manejar el caso en el que no haya ascensores disponibles
        diferencia_de_pisos_real = float('inf')  # Inicializar con infinito para encontrar la mínima diferencia
        ascensor_mas_cercano = None
        for ascensor in self.ascensores:
            diferencia_de_pisos = abs(ascensor.piso_actual - self.numero_piso)  # Utiliza valor absoluto
            if diferencia_de_pisos < diferencia_de_pisos_real:
                diferencia_de_pisos_real = diferencia_de_pisos
                ascensor_mas_cercano = ascensor
        return ascensor_mas_cercano

    def abrir_ascensor(self):
        print("<<<<<< ABRIR ASCENSOR >>>>>>")
        self.ascensor.abierto = True
        time.sleep(2)
        self.ascensor.abierto = False
        print("<<<<<< CERRAR ASCENSOR  >>>>>>")

