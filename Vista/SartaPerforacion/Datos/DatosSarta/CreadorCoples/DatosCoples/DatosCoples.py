from PyQt5.QtWidgets import *

from VentanaTuberiaHerramientas.Administradores.Datos.Datos import Datos


class Prueba(QDialog):
    aceptado = False
    data = []
    area_toberas = 0

    def __init__(self):
        super(Prueba, self).__init__()
        self.datos = Datos(13)
