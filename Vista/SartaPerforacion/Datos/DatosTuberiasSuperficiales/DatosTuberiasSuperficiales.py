from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class DatosTuberiasSuperficiales(QDialog):
    def __init__(self, *args, **kwargs):
        super(DatosTuberiasSuperficiales, self).__init__(*args, **kwargs)
        self.setWindowTitle("Tabla conexiones superficiales")
        self.setFixedSize(800, 400)
        tabla = QLabel()
        tabla.setPixmap(QPixmap("Imagenes/TP/TablaConexiones.png"))
        tabla.setScaledContents(True)
        tabla.setFixedSize(700, 400)
        layout = QHBoxLayout()
        layout.addWidget(tabla)
        self.setLayout(layout)
