import sys

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


# noinspection PyArgumentList
class Trayectoria:
    stop = False
    clicked = 0
    app = QApplication(sys.argv)
    opcion_seleccionada = 0
    texto_encabezado = QLabel()
    texto_encabezado.setScaledContents(True)
    texto_encabezado.setFixedSize(250, 50)
    texto_encabezado.setPixmap(QPixmap("Imagenes/TextoTrayectoria.png"))
    imagen_tipo_j = QLabel()
    imagen_tipo_j.setPixmap(QPixmap("Imagenes/ImagenTipoJ.png"))
    imagen_tipo_s = QLabel()
    imagen_tipo_s.setPixmap(QPixmap("Imagenes/ImagenTipoS.png"))
    imagen_vertical = QLabel()
    imagen_vertical.setPixmap(QPixmap("Imagenes/ImagenVertical.png"))
    imagen_horizontal = QLabel()
    imagen_horizontal.setPixmap(QPixmap("Imagenes/ImagenHorizontal.png"))
    layout_imagenes_tipos = QHBoxLayout()
    layout_imagenes_tipos.addWidget(imagen_vertical)
    layout_imagenes_tipos.addWidget(imagen_tipo_j)
    layout_imagenes_tipos.addWidget(imagen_tipo_s)
    layout_imagenes_tipos.addWidget(imagen_horizontal)
    layout_pantalla = QVBoxLayout()
    layout_pantalla.addWidget(texto_encabezado)
    layout_pantalla.addLayout(layout_imagenes_tipos)
    frame_trayectoria = QFrame()
    frame_trayectoria.setLayout(layout_pantalla)

    def __init__(self):
        self.acondiciona(self.imagen_tipo_j)
        self.acondiciona(self.imagen_tipo_s)
        self.acondiciona(self.imagen_vertical)
        self.acondiciona(self.imagen_horizontal)

    def get_frame(self):
        return self.frame_trayectoria

    def get_imagen_vertical(self):
        return self.imagen_vertical

    def cambiar_imagen(self, source, flag):
        if source is self.imagen_vertical:
            if flag:
                source.setPixmap(QPixmap("Imagenes/ImagenVerticalselect.png"))
            elif self.clicked is not 1:
                source.setPixmap(QPixmap("Imagenes/ImagenVertical.png"))
        elif source is self.imagen_horizontal:
            if flag:
                source.setPixmap(QPixmap("Imagenes/ImagenHorizontal select.png"))
            elif self.clicked is not 4:
                source.setPixmap(QPixmap("Imagenes/ImagenHorizontal.png"))
        elif source is self.imagen_tipo_j:
            if flag:
                source.setPixmap(QPixmap("Imagenes/ImagenTipoJselect.png"))
            elif self.clicked is not 2:
                source.setPixmap(QPixmap("Imagenes/ImagenTipoJ.png"))
        elif source is self.imagen_tipo_s:
            if flag:
                source.setPixmap(QPixmap("Imagenes/ImagenTipoSselect.png"))
            elif self.clicked is not 3:
                source.setPixmap(QPixmap("Imagenes/ImagenTipoS.png"))

    def isclicked(self, source):
        if source is self.imagen_vertical:
            source.setPixmap(QPixmap("Imagenes/ImagenVerticalselect.png"))
            self.imagen_tipo_j.setPixmap(QPixmap("Imagenes/ImagenTipoJ.png"))
            self.imagen_tipo_s.setPixmap(QPixmap("Imagenes/ImagenTipoS.png"))
            self.imagen_horizontal.setPixmap(QPixmap("Imagenes/ImagenHorizontal.png"))
            self.clicked = 1
        if source is self.imagen_tipo_j:
            source.setPixmap(QPixmap("Imagenes/ImagenTipoJselect.png"))
            self.imagen_tipo_s.setPixmap(QPixmap("Imagenes/ImagenTipoS.png"))
            self.imagen_vertical.setPixmap(QPixmap("Imagenes/ImagenVertical.png"))
            self.imagen_horizontal.setPixmap(QPixmap("Imagenes/ImagenHorizontal.png"))
            self.clicked = 2
        if source is self.imagen_tipo_s:
            source.setPixmap(QPixmap("Imagenes/ImagenTipoSselect.png"))
            self.imagen_tipo_j.setPixmap(QPixmap("Imagenes/ImagenTipoJ.png"))
            self.imagen_vertical.setPixmap(QPixmap("Imagenes/ImagenVertical.png"))
            self.imagen_horizontal.setPixmap(QPixmap("Imagenes/ImagenHorizontal.png"))
            self.clicked = 3
        if source is self.imagen_horizontal:
            source.setPixmap(QPixmap("Imagenes/ImagenHorizontal select.png"))
            self.imagen_tipo_j.setPixmap(QPixmap("Imagenes/ImagenTipoJ.png"))
            self.imagen_tipo_s.setPixmap(QPixmap("Imagenes/ImagenTipoS.png"))
            self.imagen_vertical.setPixmap(QPixmap("Imagenes/ImagenVertical.png"))
            self.clicked = 4

    def get_clicked(self):
        return self.clicked

    @staticmethod
    def acondiciona(label):
        ancho = 210
        largo = 417
        label.setScaledContents(True)
        label.setFixedSize(ancho, largo)
        label.setCursor(Qt.PointingHandCursor)