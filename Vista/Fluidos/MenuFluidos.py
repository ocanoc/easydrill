import sys

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class MenuFluidos(QMainWindow):
    app = QApplication(sys.argv)
    stop = False
    clicked = 0
    app.setStyle('Fusion')
    texto_encabezado = QLabel()
    texto_encabezado.setScaledContents(True)
    texto_encabezado.setFixedSize(250, 50)
    texto_encabezado.setPixmap(QPixmap("Imagenes/TextoModeloReologico.png"))
    instruccioes = QLabel()
    instruccioes.setScaledContents(True)
    instruccioes.setFixedSize(820, 28)
    instruccioes.setPixmap(QPixmap("Imagenes/InstruccionesFluido.png"))
    grafica_bingham = QLabel()
    grafica_bingham.setPixmap(QPixmap("Imagenes/GraficaBingham.png"))
    grafica_potencias = QLabel()
    grafica_potencias.setPixmap(QPixmap("Imagenes/GraficaPotencias.png"))
    grafica_potencias_m = QLabel()
    grafica_potencias_m.setPixmap(QPixmap("Imagenes/GraficaPotenciasM.png"))
    dibujo_smith = QLabel()
    dibujo_smith.setPixmap(QPixmap("Imagenes/DibujoSmith.png"))
    layout_contenido = QHBoxLayout()
    layout_contenido.addWidget(grafica_bingham)
    layout_contenido.addWidget(grafica_potencias)
    layout_contenido.addWidget(grafica_potencias_m)
    layout_contenido.addWidget(dibujo_smith)

    layout_pantalla = QVBoxLayout()
    layout_pantalla.addWidget(texto_encabezado)
    layout_pantalla.addWidget(instruccioes)
    layout_pantalla.addStretch()
    layout_pantalla.addLayout(layout_contenido)
    frame_pantalla = QFrame()
    frame_pantalla.setLayout(layout_pantalla)
    frame_pantalla.setFont(QFont('Calibri (Cuerpo)', 12, QFont.Bold))

    def __init__(self):
        super(MenuFluidos, self).__init__()
        self.acondiciona(self.grafica_bingham)
        self.acondiciona(self.grafica_potencias_m)
        self.acondiciona(self.grafica_potencias)
        self.acondiciona(self.dibujo_smith)

    def get_frame(self):
        return self.frame_pantalla

    def intercambiar_imagen(self, source, flag):
        if source is self.grafica_bingham:
            if flag:
                source.setPixmap(QPixmap("Imagenes/BinghamSelect.png"))
            elif self.clicked is not 1:
                source.setPixmap(QPixmap("Imagenes/GraficaBingham.png"))
        elif source is self.grafica_potencias:
            if flag:
                source.setPixmap(QPixmap("Imagenes/PotenciasSelect.png"))
            elif self.clicked is not 2:
                source.setPixmap(QPixmap("Imagenes/GraficaPotencias.png"))
        elif source is self.grafica_potencias_m:
            if flag:
                source.setPixmap(QPixmap("Imagenes/PModificadoSelect.png"))
            elif self.clicked is not 3:
                source.setPixmap(QPixmap("Imagenes/GraficaPotenciasM.png"))
        elif source is self.dibujo_smith:
            if flag:
                source.setPixmap(QPixmap("Imagenes/SmithSelect.png"))
            elif self.clicked is not 4:
                source.setPixmap(QPixmap("Imagenes/DibujoSmith.png"))

    def isclicked(self, source):
        if source is self.grafica_bingham:
            source.setPixmap(QPixmap("Imagenes/BinghamSelect.png"))
            self.grafica_potencias.setPixmap(QPixmap("Imagenes/GraficaPotencias.png"))
            self.grafica_potencias_m.setPixmap(QPixmap("Imagenes/GraficaPotenciasM.png"))
            self.dibujo_smith.setPixmap(QPixmap("Imagenes/DibujoSmith.png"))
            self.clicked = 1
        if source is self.grafica_potencias:
            source.setPixmap(QPixmap("Imagenes/PotenciasSelect.png"))
            self.grafica_bingham.setPixmap(QPixmap("Imagenes/GraficaBingham.png"))
            self.grafica_potencias_m.setPixmap(QPixmap("Imagenes/GraficaPotenciasM.png"))
            self.dibujo_smith.setPixmap(QPixmap("Imagenes/DibujoSmith.png"))
            self.clicked = 2
        if source is self.grafica_potencias_m:
            source.setPixmap(QPixmap("Imagenes/PModificadoSelect.png"))
            self.grafica_bingham.setPixmap(QPixmap("Imagenes/GraficaBingham.png"))
            self.grafica_potencias.setPixmap(QPixmap("Imagenes/GraficaPotencias.png"))
            self.dibujo_smith.setPixmap(QPixmap("Imagenes/DibujoSmith.png"))
            self.clicked = 3
        if source is self.dibujo_smith:
            source.setPixmap(QPixmap("Imagenes/SmithSelect.png"))
            self.grafica_bingham.setPixmap(QPixmap("Imagenes/GraficaBingham.png"))
            self.grafica_potencias.setPixmap(QPixmap("Imagenes/GraficaPotencias.png"))
            self.grafica_potencias_m.setPixmap(QPixmap("Imagenes/GraficaPotenciasM.png"))
            self.clicked = 4

    def get_clicked(self):
        return self.clicked

    @staticmethod
    def acondiciona(label):
        ancho = 150
        largo = 180
        label.setScaledContents(True)
        label.setFixedSize(ancho, largo)
        label.setCursor(Qt.PointingHandCursor)
