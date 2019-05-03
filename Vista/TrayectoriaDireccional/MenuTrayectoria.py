from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys


class Trayectoria:
    ancho = 210
    largo = 417
    app = QApplication(sys.argv)

    imagen_tipo_j = QLabel()
    imagen_tipo_j.setPixmap(QPixmap("Imagenes/ImagenTipoJ.png"))
    imagen_tipo_j.setScaledContents(True)
    imagen_tipo_j.setFixedSize(ancho, largo)
    imagen_tipo_j.setCursor(Qt.PointingHandCursor)
    imagen_tipo_s = QLabel()
    imagen_tipo_s.setPixmap(QPixmap("Imagenes/ImagenTipoS.png"))
    imagen_tipo_s.setCursor(Qt.PointingHandCursor)
    imagen_tipo_s.setScaledContents(True)
    imagen_tipo_s.setFixedSize(ancho, largo)
    imagen_vertical = QLabel()
    imagen_vertical.setMouseTracking(True)
    imagen_vertical.setPixmap(QPixmap("Imagenes/ImagenVertical.png"))
    imagen_vertical.setCursor(Qt.PointingHandCursor)
    imagen_vertical.setScaledContents(True)
    imagen_vertical.setFixedSize(ancho, largo)
    imagen_horizontal = QLabel()
    imagen_horizontal.setPixmap(QPixmap("Imagenes/ImagenHorizontal.png"))
    imagen_horizontal.setCursor(Qt.PointingHandCursor)
    imagen_horizontal.setScaledContents(True)
    imagen_horizontal.setFixedSize(ancho, largo)
    frame_trayectoria = QFrame()
    layout_imagenes_tipos = QHBoxLayout()
    layout_imagenes_tipos.setEnabled(True)
    layout_imagenes_tipos.addWidget(imagen_vertical)
    layout_imagenes_tipos.addWidget(imagen_tipo_j)
    layout_imagenes_tipos.addWidget(imagen_tipo_s)
    layout_imagenes_tipos.addWidget(imagen_horizontal)
    frame_trayectoria.setLayout(layout_imagenes_tipos)

    def __init__(self):
        pass

    def get_frame(self):
        return self.frame_trayectoria

    def get_imagen_vertical(self):
        return self.imagen_vertical

    def cambiar_imagen(self, source, flag):
        if source is self.imagen_vertical:
            if flag:
                source.setPixmap(QPixmap("Imagenes/ImagenVerticalselect.png"))
            else:
                source.setPixmap(QPixmap("Imagenes/ImagenVertical.png"))
        elif source is self.imagen_horizontal:
            if flag:
                source.setPixmap(QPixmap("Imagenes/ImagenHorizontal select.png"))
            else:
                source.setPixmap(QPixmap("Imagenes/ImagenHorizontal.png"))
        elif source is self.imagen_tipo_j:
            if flag:
                source.setPixmap(QPixmap("Imagenes/ImagenTipoJselect.png"))
            else:
                source.setPixmap(QPixmap("Imagenes/ImagenTipoJ.png"))
        elif source is self.imagen_tipo_s:
            if flag:
                source.setPixmap(QPixmap("Imagenes/ImagenTipoSselect.png"))
            else:
                source.setPixmap(QPixmap("Imagenes/ImagenTipoS.png"))