import sys

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class DatosTuberia(QFrame):
    app = QApplication(sys.argv)
    app.setStyle('Fusion')

    campo_longitud = QLineEdit()
    campo_id = QLineEdit()
    campo_od = QLineEdit()
    campo_bl = QLineEdit()

    tipo_tuberia = QComboBox()
    tipo_tuberia.addItems({"Liner", "TR"})

    layout_izquierda = QFormLayout()
    layout_izquierda.addRow("Tipo de tuberia", tipo_tuberia)
    layout_izquierda.addRow("Longitud [m]", campo_longitud)
    layout_izquierda.setVerticalSpacing(20)
    layout_izquierda.setFormAlignment(Qt.AlignTop)

    layout_derecha = QFormLayout()
    layout_derecha.addRow("ID [pg]", campo_id)
    layout_derecha.addRow("OD [pg]", campo_od)
    layout_derecha.addRow("B.L [m]", campo_bl)
    layout_derecha.setVerticalSpacing(20)
    layout_derecha.setFormAlignment(Qt.AlignTop)

    layout_campos = QHBoxLayout()
    layout_campos.addLayout(layout_izquierda)
    layout_campos.addLayout(layout_derecha)

    layout_pantalla = QVBoxLayout()
    layout_pantalla.addLayout(layout_campos)

    def __init__(self):
        super(DatosTuberia, self).__init__()
        self.setLayout(self.layout_pantalla)
        self.setFont(QFont('Calibri (Cuerpo)', 12, QFont.Bold))
        palette = QPalette()
        self.setAutoFillBackground(True)
        palette.setColor(self.backgroundRole(), QColor(208, 206, 206))
        self.setPalette(palette)

    def get_frame(self):
        return self.frame_pantalla
