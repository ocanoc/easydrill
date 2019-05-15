import sys

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from TuberiasRevestmiento.DatosTuberiaRevestimiento.DatosTuberias import DatosTuberia


class TuberiasRevestimiento(QWidget):
    app = QApplication(sys.argv)
    app.setStyle('Fusion')

    texto_encabezado = QLabel()
    texto_encabezado.setScaledContents(True)
    texto_encabezado.setFixedSize(250, 50)
    texto_encabezado.setPixmap(QPixmap("Imagenes/Revestimieto/TextoDatosMecanicos.png"))

    imagen_mecanico = QLabel()
    imagen_mecanico.setPixmap(QPixmap("Imagenes/Revestimieto/ImagenEstadoMecanico.png"))
    imagen_mecanico.setScaledContents(True)
    imagen_mecanico.setFixedSize(196, 379)

    etapa = QToolBox()
    etapa.setFixedSize(550, 315)

    mas = QPushButton()
    mas.setIcon(QIcon("Imagenes/Iconos/mas.png"))
    mas.setToolTip("Agrega Etapa")

    menos = QPushButton()
    menos.setIcon(QIcon("Imagenes/Iconos/menos.png"))
    menos.setToolTip("Elimina Etapa")

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

    def __init__(self):
        super(TuberiasRevestimiento, self).__init__()
        self.etapa.addItem(DatosTuberia(self.etapa), "Etapa 1")
        self.mas.clicked.connect(lambda *args: self.agrega())
        self.menos.clicked.connect(lambda *args: self.elimina())
        self.acodiciona(self.mas)
        self.acodiciona(self.menos)
        self.setLayout(self.layout_pantalla)
        self.setFont(QFont('Calibri (Cuerpo)', 12, QFont.Bold))

    def agrega(self):
        self.etapa.addItem(DatosTuberia(self.etapa), "Etapa {}".format(self.etapa.count() + 1))

    def elimina(self):
        self.etapa.removeItem(self.etapa.currentIndex())
        self.actualiza()

    def actualiza(self):
        count = self.etapa.count()  # number of items
        for x in range(count):
            self.etapa.setItemText(x, "Etapa {}".format(x + 1))
            print(self.etapa.widget(x))

    @staticmethod
    def acodiciona(btn):
        btnancho = 30
        btn.setIconSize(QSize(btnancho, btnancho))
        btn.setFixedSize(btnancho, btnancho)
        btn.setCursor(Qt.PointingHandCursor)
