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
    layout_pantalla.addSpacing(9)
    layout_pantalla.addWidget(texto_encabezado)
    layout_pantalla.addSpacing(38)
    layout_pantalla.addLayout(layout_contenido)
    layout_pantalla.addStretch(1)

    datos = []

    lleno = False

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
        try:
            if self.etapa.count() < 10:
                if self.etapa.widget(self.etapa.count() - 1).is_fill() and self.check_di():
                    self.rename()
                    self.datos.append(self.etapa.widget(self.etapa.count() - 1).get_datos())
                    self.etapa.addItem(DatosTuberia(self.etapa), "Etapa {}".format(self.etapa.count() + 1))
                    self.etapa.setCurrentIndex(self.etapa.count()-1)
                    self.lleno = True
            else:
                QMessageBox.critical(self, "Error", "Demasiadas etapas")
        except ValueError:
            return False

    def elimina(self):
        if self.etapa.count() > 1:
            self.etapa.removeItem(self.etapa.currentIndex())
            self.datos.pop()
        else:
            self.lleno = False
            self.datos.clear()
            self.etapa.widget(self.etapa.count() - 1).clean()
            self.etapa.setItemText(self.etapa.count() - 1, "Etapa 1")
            QMessageBox.information(self, "Limpio", "No hay mas elementos")

    def actualiza(self):
        count = self.etapa.count()  # number of items
        for x in range(count):
            self.etapa.setItemText(x, "Etapa {}".format(x + 1))
            print(self.etapa.widget(x))

    def rename(self):
        self.etapa.setItemText(self.etapa.count() - 1, self.etapa.widget(self.etapa.count() - 1).get_name())

    def check_di(self):
        if self.etapa.count() is 1:
            return True
        elif self.etapa.widget(self.etapa.count() - 1).get_od() < self.etapa.widget(self.etapa.count() - 2).get_id():
            return True
        else:
            QMessageBox.critical(self, "Error", "El diámetro es mayor o igual al de la tubería anterior.")
            return False

    def is_fill(self):
        if self.lleno:
            return True
        else:
            return False

    @staticmethod
    def acodiciona(btn):
        btnancho = 30
        btn.setIconSize(QSize(btnancho, btnancho))
        btn.setFixedSize(btnancho, btnancho)
        btn.setCursor(Qt.PointingHandCursor)
