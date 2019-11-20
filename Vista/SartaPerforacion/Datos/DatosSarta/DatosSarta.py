import sys

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from Vista.SartaPerforacion.Datos.DatosSarta.VistaLongitud.VistaLongitud import VistaLongitud
from Vista.VentanaTuberiaHerramientas.Administradores.Datos.Datos import Datos
from Vista.VentanaTuberiaHerramientas.Administradores.VistaHerramientas.VistaHerramientas import VistaHerramientas


class DatosSarta(QDialog):

    def __init__(self, parent=None):
        super(DatosSarta, self).__init__(parent)
        self.title = 'Elementos de la sarta de perforacion.'
        self.setWindowIcon(QIcon("Imagenes/Iconos/Gota.png"))
        self.setFixedSize(830, 570)
        self.setFont(QFont('Calibri (Cuerpo)', 12, QFont.Bold))
        p = self.palette()
        p.setBrush(10, QBrush(QImage("Imagenes/Fondo/FondoAgregador.png")))
        self.setPalette(p)

        self.label_title = QLabel("Selecciona un elemento.")
        self.tab = QTabWidget()
        self.tab.setIconSize(QSize(115, 50))
        self.tab.setFixedSize(800, 480)
        self.tab.addTab(VistaLongitud(6), QIcon("Imagenes/TextosTuberias/TextoTP.png"), "")
        self.tab.addTab(VistaLongitud(3), QIcon("Imagenes/TextosTuberias/TextoHW.png"), "")
        self.tab.addTab(VistaLongitud(4), QIcon("Imagenes/TextosTuberias/TextoDC.png"), "")
        self.tab.addTab(QWidget(), QIcon("Imagenes/TextosTuberias/TextoConexiones.png"), "")
        self.tab.addTab(Datos(5), QIcon("Imagenes/TextosTuberias/TextoEstabilizadores.png"), "")
        self.tab.addTab(Datos(11), QIcon("Imagenes/TextosTuberias/TextoHerramientas.png"), "")
        self.tab.addTab(Datos(7), QIcon("Imagenes/TextosTuberias/TextoPorta.png"), "")
        self.tab.addTab(VistaHerramientas(), QIcon("Imagenes/TextosTuberias/TextoMartillos.png"), "")
        self.tab.addTab(Datos(10), QIcon("Imagenes/TextosTuberias/TextoMotor.png"), "")

        self.btn_aceptar = QPushButton("Aceptar")
        self.btn_cancelar = QPushButton("Cancelar")

        self.btn_aceptar.clicked.connect(lambda *args: self.aceptar(self.tab.currentWidget()))
        self.btn_cancelar.clicked.connect(lambda *args: self.cancelar())

        self.acodiciona(self.btn_aceptar)
        self.acodiciona(self.btn_cancelar)

        self.layout_btn = QHBoxLayout()
        self.layout_btn.addWidget(self.btn_aceptar)
        self.layout_btn.addWidget(self.btn_cancelar)

        self.setWindowTitle(self.title)

        self.layout_ventana = QVBoxLayout()
        self.layout_ventana.addSpacing(15)
        self.layout_ventana.addWidget(self.label_title, 1, Qt.AlignLeft)
        self.layout_ventana.addWidget(self.tab)
        self.layout_ventana.addLayout(self.layout_btn)
        self.setWindowTitle(self.title)
        self.setLayout(self.layout_ventana)

        self.aceptado = True
        self.data = []

    def get_selection(self, selection):
        self.tabs.isActiveWindow()

    @staticmethod
    def aceptar(source):
        print(source.get_data())

    def cancelar(self):
        self.close()
        self.aceptado = False

    def aceptado(self):
        return self.aceptado

    def get_data(self):
        return self.data

    @staticmethod
    def acodiciona(btn):
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


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = DatosSarta()
    ex.exec_()
    sys.exit(app.exec_())
