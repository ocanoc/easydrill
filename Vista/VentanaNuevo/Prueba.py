import sys

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from Fluidos.DatosFluidos.DatosFluidos import DatosFluidos
from MenuSartaPerforacion import SartaPerforacion
from TuberiasRevestmiento.MenuTuberiasRevestimiento import TuberiasRevestimiento
from Vista.SartaPerforacion.Datos.DatosSarta.CreadorCoples.CreadorCoples import CreadorCoples
from Vista.TrayectoriaDireccional.DatosTrayectoria.DatosTrayectoria import DatosTrayectoria
from Vista.VentanaResultados.MenuResultados import MenuResultados


class Prueba(QDialog):
    aceptado = False
    data = []
    area_toberas = 0

    def __init__(self):
        super(Prueba, self).__init__()
        palette = QPalette()
        palette.setBrush(10, QBrush(QImage("Imagenes/Fondo/Fondo.png")))
        self.setPalette(palette)
        self.setFixedSize(1000, 604)
        self.setFont(QFont('Arial', 10, QFont.AnyStyle))
        btn = QPushButton("datos")
        self.acodiciona(btn)

        self.layot = QVBoxLayout()

        # self.layot.addWidget(MenuEdicion())
        creador = CreadorCoples()
        menu_resultados = MenuResultados()
        self.DatosTrayectoria = DatosTrayectoria()
        self.DatosTrayectoria.cambia_trayectoria(3)
        self.DatosFluidos = DatosFluidos()
        self.Tuberiras_revetimietno = TuberiasRevestimiento()
        self.Sarta_Perforacion = SartaPerforacion()
        self.layot.addWidget(creador)

        self.layot.addWidget(btn)
        self.layot.addSpacing(20)

        self.setLayout(self.layot)

        btn.clicked.connect(lambda: creador.get_data())

    def termianr(self):
        pass

    @staticmethod
    def acodiciona(btn):
        if isinstance(btn, QPushButton):
            btn.setCursor(Qt.PointingHandCursor)
            btn.setStyleSheet("""
                            QPushButton {
                            background-color: rgb(0, 80, 85);
                            border-style: outset;
                            border-width: 1px;
                            border-radius: 5px;
                            font:  11px;
                            min-width: 6em;
                            padding: 6px;
                            color: white
                            }
                            QPushButton:pressed {
                                background-color: rgb(154, 154, 154);
                                border-style: inset;
                            }""")
        if isinstance(btn, QLineEdit):
            btn.setFixedWidth(85)
            btn.setCursor(Qt.IBeamCursor)
            btn.setPlaceholderText("0")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Prueba()
    window.show()
    app.exec_()
