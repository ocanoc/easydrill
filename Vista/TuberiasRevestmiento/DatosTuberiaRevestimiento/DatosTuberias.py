from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class DatosTuberia(QWidget):
    def __init__(self, parent=None):
        super(DatosTuberia, self).__init__(parent)
        self.campo_longitud = QLineEdit()
        self.campo_id = QLineEdit()
        self.campo_od = QLineEdit()
        self.campo_bl = QLineEdit()

        self.tipo_tuberia = QComboBox()
        self.tipo_tuberia.insertItem(0, "TR")
        self.tipo_tuberia.insertItem(1, "Liner")
        self.tipo_tuberia.setCursor(Qt.PointingHandCursor)
        self.tipo_tuberia.currentIndexChanged.connect(self.selectionchange)

        self.layout_izquierda = QFormLayout()
        self.layout_izquierda.addRow("Tipo de tuberia", self.tipo_tuberia)
        self.layout_izquierda.addRow("Longitud [m]", self.campo_longitud)
        self.layout_izquierda.setVerticalSpacing(20)
        self.layout_izquierda.setFormAlignment(Qt.AlignTop)

        self.layout_derecha = QFormLayout()
        self.layout_derecha.addRow("ID [pg]", self.campo_id)
        self.layout_derecha.addRow("OD [pg]", self.campo_od)
        self.layout_derecha.setVerticalSpacing(20)
        self.layout_derecha.setFormAlignment(Qt.AlignTop)

        self.layout_campos = QHBoxLayout()
        self.layout_campos.addLayout(self.layout_izquierda)
        self.layout_campos.addLayout(self.layout_derecha)

        self.layout_pantalla = QVBoxLayout()
        self.layout_pantalla.addLayout(self.layout_campos)
        self.setLayout(self.layout_pantalla)
        palette = QPalette()
        self.setAutoFillBackground(True)
        palette.setColor(self.backgroundRole(), QColor(208, 206, 206))
        self.setPalette(palette)
        self.setFont(QFont('Calibri (Cuerpo)', 12, QFont.Bold))

    def selectionchange(self, i):
        if i is 0:
            self.layout_derecha.removeRow(2)
        elif i is 1:
            self.campo_bl = QLineEdit()
            self.layout_derecha.addRow("B.L [m]", self.campo_bl)
