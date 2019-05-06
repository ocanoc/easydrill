import sys

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class DatosFluidos:
    app = QApplication(sys.argv)
    app.setStyle('Fusion')
    imagen_tipo = QLabel()
    imagen_tipo.setPixmap(QPixmap("Imagenes/GraficaBingham.png"))
    imagen_tipo.setScaledContents(True)
    imagen_tipo.setFixedSize(260, 310)
    texto_encabezado = QLabel()
    texto_encabezado.setScaledContents(True)
    texto_encabezado.setFixedSize(250, 50)
    texto_encabezado.setPixmap(QPixmap("Imagenes/TextoDatosFluido.png"))
    campo_densidad = QLineEdit()
    campo_l600 = QLineEdit()
    campo_l300 = QLineEdit()
    campo_pc = QLineEdit()
    campo_vp = QLineEdit()
    campo_gel = QLineEdit()
    layout_izquierda = QFormLayout()
    layout_izquierda.addRow("""Densidad <div class="fraction">
<span class="fup">gr</span>
<span class="bar">/</span>
<span class="fdn">cm<sup>2</sup></span>
</div>""", campo_densidad)
    layout_izquierda.addRow("""L<sub>600</sub>
<div class="fraction">
<span class="fup">lbf</span>
<span class="bar">/</span>
<span class="fdn">100ft<sup>2</sup></span>
</div>""", campo_l600)
    layout_izquierda.addRow("""L<sub>300</sub>
<div class="fraction">
<span class="fup">lbf</span>
<span class="bar">/</span>
<span class="fdn">100ft<sup>2</sup></span>
</div>""", campo_l300)
    layout_derecha = QFormLayout()
    layout_derecha.addRow("""Pc <div class="fraction">
<span class="fup">lbf</span>
<span class="bar">/</span>
<span class="fdn">100ft<sup>2</sup></span>
</div>""", campo_pc)
    layout_derecha.addRow("Vp cp", campo_vp)
    layout_derecha.addRow("""θ<sub>0</sub> <div class="fraction">
<span class="fup">lbf</span>
<span class="bar">/</span>
<span class="fdn">100ft<sup>2</sup></span>
</div> """, campo_gel)
    layout_derecha.setVerticalSpacing(20)
    layout_izquierda.setVerticalSpacing(20)
    layout_izquierda.setFormAlignment(Qt.AlignCenter)
    layout_derecha.setFormAlignment(Qt.AlignCenter)
    layoutvertical1 = QHBoxLayout()
    layoutvertical1.addWidget(imagen_tipo, Qt.AlignAbsolute)
    layoutvertical1.addSpacing(100)
    layoutvertical1.addLayout(layout_derecha)
    layoutvertical1.addSpacing(150)
    layoutvertical1.addLayout(layout_izquierda)
    layoutvertical1.addStretch(10)
    layout_pantalla = QVBoxLayout()
    layout_pantalla.addSpacing(11)
    layout_pantalla.addWidget(texto_encabezado)
    layout_pantalla.addSpacing(20)
    layout_pantalla.addLayout(layoutvertical1)
    layout_pantalla.addSpacing(10)
    frame_pantalla = QFrame()
    frame_pantalla.setLayout(layout_pantalla)
    frame_pantalla.setFont(QFont('Calibri (Cuerpo)', 12, QFont.Bold))

    def __init__(self):
        self.desactiva_todo()
        pass

    def get_frame(self):
        return self.frame_pantalla

    def desactiva_todo(self):
        self.acondicionar(self.campo_densidad)
        self.acondicionar(self.campo_gel)
        self.acondicionar(self.campo_l300)
        self.acondicionar(self.campo_l600)
        self.acondicionar(self.campo_pc)
        self.acondicionar(self.campo_vp)
        self.acondicionar(self.campo_pc)

    def cambia_trayectoria(self, tipo):
        if tipo is 1:
            self.imagen_tipo.setPixmap(QPixmap("Imagenes/GraficaBingham.png"))
            self.desactiva_todo()
            self.activa_bingham()
        elif tipo is 2:
            self.imagen_tipo.setPixmap(QPixmap("Imagenes/GraficaPotencias.png"))
            self.desactiva_todo()
            self.activa_potecias()
        elif tipo is 3:
            self.imagen_tipo.setPixmap(QPixmap("Imagenes/GraficaPotenciasM.png"))
            self.desactiva_todo()
            self.activa_potecia_m()
        elif tipo is 4:
            self.imagen_tipo.setPixmap(QPixmap("Imagenes/DibujoSmith.png"))
            self.desactiva_todo()
            self.activa_smith()

    @staticmethod
    def acondicionar(lineedit):
        lineedit.setPlaceholderText("0")
        lineedit.setReadOnly(True)
        lineedit.setFixedWidth(80)
        lineedit.setCursor(Qt.ForbiddenCursor)

    @staticmethod
    def activa_lineedit(lineedit):
        lineedit.setReadOnly(False)
        lineedit.setCursor(Qt.IBeamCursor)

    def activa_potecia_m(self):
        pass

    def activa_bingham(self):
        pass

    def activa_potecias(self):
        pass

    def activa_smith(self):
        pass
