import sys

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from TuberiasRevestmiento.DatosTuberiaRevestimiento.DatosTuberias import DatosTuberia


class TuberiasRevestimiento:
    app = QApplication(sys.argv)
    app.setStyle('Fusion')
    trayectoria_select = 0

    texto_encabezado = QLabel()
    texto_encabezado.setScaledContents(True)
    texto_encabezado.setFixedSize(250, 50)
    texto_encabezado.setPixmap(QPixmap("Imagenes/TextiDatiosMecanicos.png"))

    imagen_mecanico = QLabel()
    imagen_mecanico.setPixmap(QPixmap("Imagenes/ImagenEstadoMecanico.png"))
    imagen_mecanico.setScaledContents(True)
    imagen_mecanico.setFixedSize(196, 379)

    wea = DatosTuberia()
    etapa = QToolBox()
    etapa.insertItem(1, wea, "Hlolis")
    etapa.insertItem(2, DatosTuberia(), "Etapa 1")
    etapa.insertItem(3, DatosTuberia(), "Etapa 2")
    etapa.setFixedSize(550, 315)

    btnancho = 30
    mas = QPushButton()
    mas.setIcon(QIcon("Imagenes/mas.png"))
    mas.setIconSize(QSize(btnancho, btnancho))
    mas.setFixedSize(btnancho, btnancho)

    menos = QPushButton()
    menos.setIcon(QIcon("Imagenes/menos.png"))
    menos.setIconSize(QSize(btnancho, btnancho))
    menos.setFixedSize(btnancho, btnancho)

    layout_botones = QHBoxLayout()
    layout_botones.addStretch(10)
    layout_botones.addWidget(mas)
    layout_botones.addWidget(menos, 1, Qt.AlignRight)
    layout_botones.addSpacing(65)

    layout_etapa = QVBoxLayout()
    layout_etapa.addSpacing(15)
    layout_etapa.addWidget(etapa)
    layout_etapa.addLayout(layout_botones)

    layout_contenido = QHBoxLayout()
    layout_contenido.addSpacing(40)
    layout_contenido.addWidget(imagen_mecanico)
    layout_contenido.addSpacing(75)
    layout_contenido.addLayout(layout_etapa)

    layout_pantalla = QVBoxLayout()
    layout_pantalla.addWidget(texto_encabezado)
    layout_pantalla.addSpacing(20)
    layout_pantalla.addLayout(layout_contenido)

    frame_pantalla = QFrame()
    frame_pantalla.setLayout(layout_pantalla)
    frame_pantalla.setFont(QFont('Calibri (Cuerpo)', 12, QFont.Bold))

    def __init__(self):
        pass

    def get_frame(self):
        return self.frame_pantalla
