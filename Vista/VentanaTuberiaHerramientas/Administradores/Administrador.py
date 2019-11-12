from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from VentanaTuberiaHerramientas.Administradores.Datos.Datos import Datos
from VentanaTuberiaHerramientas.Administradores.Datos.DatosBarrenas import DatosBarrenas
from VentanaTuberiaHerramientas.Administradores.Datos.DatosTP import DatosTP
from VentanaTuberiaHerramientas.Administradores.VistaHerramientas.VistaHerramientas import VistaHerramientas


class Administrador(QWidget):
    def __init__(self, tipo):
        super(Administrador, self).__init__()

        self.setStyleSheet("""
          font-family: Calibri, Candara, Segoe, 
          "Segoe UI", Optima, Arial, sans-serif; 
          font-size: 18px; font-style: normal; font-variant: normal; font-weight: 700; line-height: 26.4px;""")

        self.mas = QPushButton()
        self.mas.setIcon(QIcon("Imagenes/Iconos/mas.png"))
        self.mas.setToolTip("Agregar elemento")
        self.acodiciona(self.mas)

        self.menos = QPushButton()
        self.menos.setIcon(QIcon("Imagenes/Iconos/menos.png"))
        self.menos.setToolTip("Eliminar elemento")
        self.acodiciona(self.menos)

        self.modificar = QPushButton()
        self.modificar.setIcon(QIcon("Imagenes/Iconos/modificar.png"))
        self.modificar.setToolTip("Modificar elemento")
        self.acodiciona(self.modificar)

        self.layout_botones1 = QFormLayout()
        self.layout_botones1.addRow("Agregar elemento:", self.mas)
        self.layout_botones2 = QFormLayout()
        self.layout_botones2.addRow("Eliminar elemento:", self.menos)
        self.layout_botones3 = QFormLayout()
        self.layout_botones3.addRow("Modificar elemento:", self.modificar)

        self.tabla = self.set_table(tipo)

        self.layout_botones = QHBoxLayout()
        self.layout_botones.addSpacing(20)
        self.layout_botones.addLayout(self.layout_botones1)
        self.layout_botones.addSpacing(70)
        self.layout_botones.addLayout(self.layout_botones2)
        self.layout_botones.addSpacing(70)
        self.layout_botones.addLayout(self.layout_botones3)
        self.layout_botones.addStretch(1)

        self.layout_widget = QVBoxLayout()
        self.layout_widget.addWidget(self.tabla, 1, Qt.AlignTop)
        self.layout_widget.addLayout(self.layout_botones, 1)
        self.layout_widget.addStretch(1)
        self.setLayout(self.layout_widget)

        self.mas.clicked.connect(lambda *args: self.tabla.agregar())
        self.menos.clicked.connect(lambda *args: self.tabla.eliminar())
        self.modificar.clicked.connect(lambda *args: self.tabla.modificar())

    @staticmethod
    def acodiciona(btn):
        if isinstance(btn, QPushButton):
            btnancho = 30
            btn.setIconSize(QSize(btnancho, btnancho))
            btn.setFixedSize(btnancho, btnancho)
            btn.setCursor(Qt.PointingHandCursor)

    @staticmethod
    def set_table(tipo):
        if tipo is 1:
            return DatosTP()
        if tipo is 2:
            return QWidget()
        if tipo is 3:
            return QWidget()
        if tipo is 4:
            return QWidget()
        if tipo is 5:
            return QWidget()
        if tipo is 6:
            return QWidget()
        if tipo is 7:
            return Datos(7)
        if tipo is 8:
            return VistaHerramientas()
        if tipo is 9:
            return DatosBarrenas()
        if tipo is 10:
            return Datos(10)
