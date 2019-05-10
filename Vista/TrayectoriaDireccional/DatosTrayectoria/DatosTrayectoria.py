import sys

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class DatosTrayectoria:
    app = QApplication(sys.argv)
    app.setStyle('Fusion')
    trayectoria_select = 0
    texto_encabezado = QLabel()
    texto_encabezado.setScaledContents(True)
    texto_encabezado.setFixedSize(250, 50)
    texto_encabezado.setPixmap(QPixmap("Imagenes/TextoDatosTrayectoria.png"))
    campo_profundidad = QLineEdit()
    campo_KOP = QLineEdit()
    campo_angulo_maximo = QLineEdit()
    campo_dop = QLineEdit()
    campo_severidad_incremeto = QLineEdit()
    campo_severdad_decremento = QLineEdit()
    campo_angulo_final = QLineEdit()
    imagen_tipo = QLabel()
    imagen_tipo.setPixmap(QPixmap("Imagenes/ImagenVertical.png"))
    imagen_tipo.setScaledContents(True)
    imagen_tipo.setFixedSize(210, 417)
    layout_vertical = QFormLayout()
    layout_vertical.setFormAlignment(Qt.AlignCenter)
    layout_vertical.setVerticalSpacing(50)
    layout_vertical.addRow("Profunidad [md]", campo_profundidad)
    layout_vertical.addRow("KOP [md]", campo_KOP)
    layout_vertical.addRow("BUR [°/ 30 md]", campo_severidad_incremeto)
    layout_vertical.addRow("Angulo Máximo [°]", campo_angulo_maximo)
    layout_vertical2 = QFormLayout()
    layout_vertical2.setFormAlignment(Qt.AlignCenter)
    layout_vertical2.setVerticalSpacing(50)
    layout_vertical2.addRow("DOP [md]", campo_dop)
    layout_vertical2.addRow("DOR [°/ 30 md]", campo_severdad_decremento)
    layout_vertical2.addRow("Angulo final [°]", campo_angulo_final)
    layout_vertical2.addRow("", QLabel())
    layout_contenido = QHBoxLayout()
    layout_contenido.addSpacing(21)
    layout_contenido.addWidget(imagen_tipo, 2, Qt.AlignLeft)
    layout_contenido.addSpacing(60)
    layout_contenido.addLayout(layout_vertical)
    layout_contenido.addSpacing(120)
    layout_contenido.addLayout(layout_vertical2)
    layout_contenido.addStretch(10)
    layout_pantalla = QVBoxLayout()
    layout_pantalla.addSpacing(11)
    layout_pantalla.addWidget(texto_encabezado)
    layout_pantalla.addSpacing(8)
    layout_pantalla.addLayout(layout_contenido)
    layout_pantalla.addSpacing(10)
    frame_pantalla = QFrame()
    frame_pantalla.setLayout(layout_pantalla)
    frame_pantalla.setFont(QFont('Calibri (Cuerpo)', 12, QFont.Bold))

    def __init__(self):
        self.desactiva_todo()

    def get_frame(self):
        return self.frame_pantalla

    def cambia_trayectoria(self, tipo):
        if tipo is 1:
            self.imagen_tipo.setPixmap(QPixmap("Imagenes/ImagenVertical.png"))
            self.desactiva_todo()
            self.activa_vertical()

        elif tipo is 2:
            self.imagen_tipo.setPixmap(QPixmap("Imagenes/ImagenTipoJ.png"))
            self.desactiva_todo()
            self.activa_j()
        elif tipo is 3:
            self.imagen_tipo.setPixmap(QPixmap("Imagenes/ImagenTipoS.png"))
            self.desactiva_todo()
            self.activa_s()
        elif tipo is 4:
            self.imagen_tipo.setPixmap(QPixmap("Imagenes/ImagenHorizontal.png"))
            self.desactiva_todo()
            self.activa_h()
        self.trayectoria_select = tipo

    @staticmethod
    def acondicionar(lineedit):
        lineedit.setPlaceholderText("0")
        lineedit.setReadOnly(True)
        lineedit.setFixedWidth(80)
        lineedit.setCursor(Qt.ForbiddenCursor)

    def activa_vertical(self):
        self.activa_lineedit(self.campo_profundidad)

    def activa_j(self):
        self.activa_vertical()
        self.activa_lineedit(self.campo_KOP)
        self.activa_lineedit(self.campo_severidad_incremeto)
        self.activa_lineedit(self.campo_angulo_maximo)

    def activa_s(self):
        self.activa_j()
        self.activa_lineedit(self.campo_dop)
        self.activa_lineedit(self.campo_severdad_decremento)
        self.activa_lineedit(self.campo_angulo_final)

    def activa_h(self):
        self.activa_j()

    @staticmethod
    def activa_lineedit(lineedit):
        lineedit.setReadOnly(False)
        lineedit.setCursor(Qt.IBeamCursor)

    def desactiva_todo(self):
        self.acondicionar(self.campo_profundidad)
        self.acondicionar(self.campo_angulo_final)
        self.acondicionar(self.campo_severdad_decremento)
        self.acondicionar(self.campo_severidad_incremeto)
        self.acondicionar(self.campo_dop)
        self.acondicionar(self.campo_KOP)
        self.acondicionar(self.campo_angulo_maximo)

    def check(self):
        if self.trayectoria_select is 1:
            try:
                if float(self.campo_profundidad.text()) > 0:
                    return True
            except ValueError:
                return False
        elif self.trayectoria_select is 2:
            try:
                if float(self.campo_profundidad.text()) > 0:
                    return True
            except ValueError:
                return False
        elif self.trayectoria_select is 3:
            print("Holi")
        elif self.trayectoria_select is 4:
            print("Holi")
        return False
