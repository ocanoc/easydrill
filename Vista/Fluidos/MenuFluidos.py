import sys

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class MenuFluidos(QWidget):
    app = QApplication(sys.argv)
    stop = False
    clicked = 0
    app.setStyle('Fusion')

    texto_encabezado = QLabel()
    texto_encabezado.setScaledContents(True)
    texto_encabezado.setFixedSize(250, 50)
    texto_encabezado.setPixmap(QPixmap("Imagenes/Fluidos/TextoModeloReologico.png"))

    instruccioes = QLabel()
    instruccioes.setScaledContents(True)
    instruccioes.setFixedSize(820, 28)
    instruccioes.setPixmap(QPixmap("Imagenes/Fluidos/InstruccionesFluido.png"))

    grafica_bingham = QLabel()
    grafica_bingham.setPixmap(QPixmap("Imagenes/Fluidos/GraficaBingham.png"))

    grafica_potencias = QLabel()
    grafica_potencias.setPixmap(QPixmap("Imagenes/Fluidos/GraficaPotencias.png"))

    grafica_potencias_m = QLabel()
    grafica_potencias_m.setPixmap(QPixmap("Imagenes/Fluidos/GraficaPotenciasM.png"))

    dibujo_smith = QLabel()
    dibujo_smith.setPixmap(QPixmap("Imagenes/Fluidos/DibujoSmith.png"))

    layout_contenido = QHBoxLayout()
    layout_contenido.addWidget(grafica_bingham)
    layout_contenido.addWidget(grafica_potencias)
    layout_contenido.addWidget(grafica_potencias_m)
    layout_contenido.addWidget(dibujo_smith)

    layout_pantalla = QVBoxLayout()
    layout_pantalla.addWidget(texto_encabezado)
    layout_pantalla.addWidget(instruccioes)
    layout_pantalla.addLayout(layout_contenido)

    def __init__(self):
        super(MenuFluidos, self).__init__()
        self.setLayout(self.layout_pantalla)
        self.acondiciona(self.grafica_bingham)
        self.acondiciona(self.grafica_potencias_m)
        self.acondiciona(self.grafica_potencias)
        self.acondiciona(self.dibujo_smith)
        self.setFont(QFont('Calibri (Cuerpo)', 12, QFont.Bold))

    def intercambiar_imagen(self, source, flag):
        if source is self.grafica_bingham:
            if flag:
                source.setPixmap(QPixmap("Imagenes/Fluidos/BinghamSelect.png"))
            elif self.clicked is not 1:
                source.setPixmap(QPixmap("Imagenes/Fluidos/GraficaBingham.png"))
        elif source is self.grafica_potencias:
            if flag:
                source.setPixmap(QPixmap("Imagenes/Fluidos/PotenciasSelect.png"))
            elif self.clicked is not 2:
                source.setPixmap(QPixmap("Imagenes/Fluidos/GraficaPotencias.png"))
        elif source is self.grafica_potencias_m:
            if flag:
                source.setPixmap(QPixmap("Imagenes/Fluidos/PModificadoSelect.png"))
            elif self.clicked is not 3:
                source.setPixmap(QPixmap("Imagenes/Fluidos/GraficaPotenciasM.png"))
        elif source is self.dibujo_smith:
            if flag:
                source.setPixmap(QPixmap("Imagenes/Fluidos/SmithSelect.png"))
            elif self.clicked is not 4:
                source.setPixmap(QPixmap("Imagenes/Fluidos/DibujoSmith.png"))

    def isclicked(self, source):
        if source is self.grafica_bingham:
            source.setPixmap(QPixmap("Imagenes/Fluidos/BinghamSelect.png"))
            self.grafica_potencias.setPixmap(QPixmap("Imagenes/Fluidos/GraficaPotencias.png"))
            self.grafica_potencias_m.setPixmap(QPixmap("Imagenes/Fluidos/GraficaPotenciasM.png"))
            self.dibujo_smith.setPixmap(QPixmap("Imagenes/DibujoSmith.png"))
            self.clicked = 1
        if source is self.grafica_potencias:
            source.setPixmap(QPixmap("Imagenes/Fluidos/PotenciasSelect.png"))
            self.grafica_bingham.setPixmap(QPixmap("Imagenes/Fluidos/GraficaBingham.png"))
            self.grafica_potencias_m.setPixmap(QPixmap("Imagenes/Fluidos/GraficaPotenciasM.png"))
            self.dibujo_smith.setPixmap(QPixmap("Imagenes/Fluidos/DibujoSmith.png"))
            self.clicked = 2
        if source is self.grafica_potencias_m:
            source.setPixmap(QPixmap("Imagenes/Fluidos/PModificadoSelect.png"))
            self.grafica_bingham.setPixmap(QPixmap("Imagenes/Fluidos/GraficaBingham.png"))
            self.grafica_potencias.setPixmap(QPixmap("Imagenes/Fluidos/GraficaPotencias.png"))
            self.dibujo_smith.setPixmap(QPixmap("Imagenes/Fluidos/DibujoSmith.png"))
            self.clicked = 3
        if source is self.dibujo_smith:
            source.setPixmap(QPixmap("Imagenes/Fluidos/SmithSelect.png"))
            self.grafica_bingham.setPixmap(QPixmap("Imagenes/Fluidos/GraficaBingham.png"))
            self.grafica_potencias.setPixmap(QPixmap("Imagenes/Fluidos/GraficaPotencias.png"))
            self.grafica_potencias_m.setPixmap(QPixmap("Imagenes/Fluidos/GraficaPotenciasM.png"))
            self.clicked = 4

    def get_clicked(self):
        if self.clicked:
            return True
        return False

    @staticmethod
    def acondiciona(label):
        ancho = 150
        largo = 180
        label.setScaledContents(True)
        label.setFixedSize(ancho, largo)
        label.setCursor(Qt.PointingHandCursor)
