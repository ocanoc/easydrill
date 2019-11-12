import sys

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from VentanaTuberiaHerramientas.MenuEdicion import MenuEdicion


class Prueba(QDialog):
    aceptado = False
    data = []
    area_toberas = 0

    def __init__(self):
        super(Prueba, self).__init__()
        self.setFixedSize(1000, 604)
        self.setFont(QFont('Calibri (Cuerpo)', 10, QFont.Bold))
        p = self.palette()
        p.setColor(self.backgroundRole(), QColor(208, 206, 206))
        self.setPalette(p)
        self.layot = QHBoxLayout()
        self.layot.addWidget(MenuEdicion())
        self.setLayout(self.layot)

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
    print("hola despues de la weas")