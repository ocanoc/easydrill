import sys

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from Controlador.Direccional.ControladorDireccional import ControladorDireccional


class DatosTrayectoria(QWidget):
    app = QApplication(sys.argv)
    app.setStyle('Fusion')
    trayectoria_select = 0
    texto_encabezado = QLabel()
    texto_encabezado.setScaledContents(True)
    texto_encabezado.setFixedSize(250, 50)
    texto_encabezado.setPixmap(QPixmap("Imagenes/Trayectoria/TextoDatosTrayectoria.png"))

    campo_profundidad = QLineEdit()
    campo_KOP = QLineEdit()
    campo_angulo_maximo = QLineEdit()
    campo_dop = QLineEdit()
    campo_severidad_incremeto = QLineEdit()
    campo_severidad_decremento = QLineEdit()
    campo_angulo_final = QLineEdit()

    campo_profundidad.setToolTip("Profundidad del objetivo")
    campo_KOP.setToolTip("Profundidad kick off point.")
    campo_severidad_incremeto.setToolTip("Severidad de construccion de la curva.")
    campo_angulo_maximo.setToolTip("Ángulo de la tangente.")
    campo_dop.setToolTip("Pofundidad drop off point.")
    campo_severidad_decremento.setToolTip("Severidad de abatimiento de la curva.")
    campo_angulo_final.setToolTip("Ángulo fial del pozo.")

    imagen_tipo = QLabel()
    imagen_tipo.setPixmap(QPixmap("Imagenes/Trayectoria/ImagenVertical.png"))
    imagen_tipo.setScaledContents(True)
    imagen_tipo.setFixedSize(210, 417)

    layout_vertical = QFormLayout()
    layout_vertical.setFormAlignment(Qt.AlignCenter)
    layout_vertical.setVerticalSpacing(50)
    layout_vertical.addRow("Profundidad [md]", campo_profundidad)
    layout_vertical.addRow("KOP [md]", campo_KOP)
    layout_vertical.addRow("Severidad 1 [°/ 30 md]", campo_severidad_incremeto)
    layout_vertical.addRow("Ángulo Máximo [°]", campo_angulo_maximo)

    layout_vertical2 = QFormLayout()
    layout_vertical2.setFormAlignment(Qt.AlignCenter)
    layout_vertical2.setVerticalSpacing(50)
    layout_vertical2.addRow("DOP [md]", campo_dop)
    layout_vertical2.addRow("Severidad 2 [°/ 30 md]", campo_severidad_decremento)
    layout_vertical2.addRow("Ángulo final [°]", campo_angulo_final)
    layout_vertical2.addRow("", QLabel())

    layout_datos = QHBoxLayout()
    layout_datos.setAlignment(Qt.AlignLeft)
    layout_datos.addLayout(layout_vertical)
    layout_datos.addSpacing(20)
    layout_datos.addLayout(layout_vertical2)

    label_instrucciones = QLabel("Ingresa los siguientes datos:")

    layout_central = QVBoxLayout()
    layout_central.setAlignment(Qt.AlignTop)
    layout_central.addSpacing(60)
    layout_central.addWidget(label_instrucciones)
    layout_central.addSpacing(10)
    layout_central.addLayout(layout_datos)

    layout_contenido = QHBoxLayout()
    layout_contenido.addSpacing(7)
    layout_contenido.addWidget(imagen_tipo, 2, Qt.AlignLeft)
    layout_contenido.addStretch(1)
    layout_contenido.addLayout(layout_central, 2)
    layout_contenido.addStretch(1)

    layout_pantalla = QVBoxLayout()
    layout_pantalla.addSpacing(0)
    layout_pantalla.addWidget(texto_encabezado)
    layout_pantalla.addSpacing(9)
    layout_pantalla.addLayout(layout_contenido)
    layout_pantalla.addSpacing(10)

    def __init__(self):
        super(DatosTrayectoria, self).__init__()
        self.setLayout(self.layout_pantalla)
        self.setFont(QFont('Calibri (Cuerpo)', 12, QFont.Bold))
        self.desactiva_todo()

    def get_frame(self):
        return self.frame_pantalla

    def cambia_trayectoria(self, tipo):
        if tipo is 1:
            self.imagen_tipo.setPixmap(QPixmap("Imagenes/Trayectoria/ImagenVertical.png"))
            self.desactiva_todo()
            self.activa_vertical()
        elif tipo is 2:
            self.imagen_tipo.setPixmap(QPixmap("Imagenes/Trayectoria/ImagenTipoJ.png"))
            self.desactiva_todo()
            self.activa_j()
        elif tipo is 3:
            self.imagen_tipo.setPixmap(QPixmap("Imagenes/Trayectoria/ImagenTipoS.png"))
            self.desactiva_todo()
            self.activa_s()
        elif tipo is 4:
            self.imagen_tipo.setPixmap(QPixmap("Imagenes/Trayectoria/ImagenHorizontal.png"))
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
        self.activa_lineedit(self.campo_severidad_decremento)
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
        self.acondicionar(self.campo_severidad_decremento)
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
        elif self.trayectoria_select is 2 or self.trayectoria_select is 4:
            try:
                if float(self.campo_profundidad.text()) > 0 \
                        and float(self.campo_KOP.text()) > 0 \
                        and float(self.campo_severidad_incremeto.text()) > 0 \
                        and float(self.campo_angulo_maximo.text()) > 0:
                    return True
            except ValueError:
                return False
        elif self.trayectoria_select is 3:
            try:
                if float(self.campo_profundidad.text()) > 0 \
                        and float(self.campo_KOP.text()) > 0 \
                        and float(self.campo_severidad_incremeto.text()) > 0 \
                        and float(self.campo_angulo_maximo.text()) > 0 \
                        and float(self.campo_dop.text()) > 0 \
                        and float(self.campo_severidad_decremento.text()) > 0 \
                        and float(self.campo_angulo_final.text()) > 0:
                    return True
            except ValueError:
                return False
        return False

    def get_datos(self):
        trayectoria = None
        if self.trayectoria_select is 1:
            trayectoria = ControladorDireccional.tipov(float(self.campo_profundidad.text()))
        elif self.trayectoria_select is 2 or self.trayectoria_select is 4:
            trayectoria = ControladorDireccional.tipo_j(float(self.campo_KOP.text()),
                                                        float(self.campo_severidad_incremeto.text()),
                                                        float(self.campo_angulo_maximo.text()),
                                                        float(self.campo_profundidad.text()))
        elif self.trayectoria_select is 3:
            trayectoria = ControladorDireccional.tipos(self.campo_KOP.text(),
                                                       float(self.campo_severidad_incremeto.text()),
                                                       float(self.campo_angulo_maximo.text()),
                                                       float(self.campo_profundidad.text()),
                                                       float(self.campo_dop.text()),
                                                       float(self.campo_severidad_decremento.text()),
                                                       float(self.campo_angulo_maximo.text()))
        return trayectoria

    @staticmethod
    def dato(line):
        return float(line.text())
