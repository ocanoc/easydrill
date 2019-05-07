import sys

from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class DatosFluidos:
    app = QApplication(sys.argv)
    app.setStyle('Fusion')
    imagen_tipo = QLabel()
    imagen_tipo.setPixmap(QPixmap("Imagenes/GraficaBingham.png"))
    imagen_tipo.setScaledContents(True)
    imagen_tipo.setFixedSize(260, 310)
