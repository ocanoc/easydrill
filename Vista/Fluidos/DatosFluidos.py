import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from win32api import GetSystemMetrics


def datos(self):
    TextoHidraulica = QLabel()
    TextoHidraulica.setPixmap(QPixmap("TextoHidraulica.png").scaledToHeight(60))
    EasyDrllLogo = QLabel()
    EasyDrllLogo.setPixmap(QPixmap("EasyDrllLogo.png").scaledToHeight(30))
    BtnAceptar = QPushButton("Aceptar")
    BtnAceptar.setFixedHeight(30)
    BtnAceptar.setFixedWidth(100)
    BtnCancelar = QPushButton("Cancelar")
    BtnCancelar.setFixedHeight(30)
    BtnCancelar.setFixedWidth(100)
    BtnRegresar = QPushButton("Regresar")
    BtnRegresar.setFixedHeight(30)
    BtnRegresar.setFixedWidth(100)
    CampoDensidad = QLineEdit()
    CampoL600 = QLineEdit()
    CampoL300 = QLineEdit()
    CampoPc = QLineEdit()
    CampoVp = QLineEdit()
    CampoGel = QLineEdit()
    layoutIzquierda = QFormLayout()
    layoutIzquierda.addRow("""Densidad <div class="fraction">
<span class="fup">gr</span>
<span class="bar">/</span>
<span class="fdn">cm<sup>2</sup></span>
</div>""", CampoDensidad)
    layoutIzquierda.addRow("""L<sub>600</sub>
<div class="fraction">
<span class="fup">lbf</span>
<span class="bar">/</span>
<span class="fdn">100ft<sup>2</sup></span>
</div>""", CampoL600)
    layoutIzquierda.addRow("""L<sub>300</sub>
<div class="fraction">
<span class="fup">lbf</span>
<span class="bar">/</span>
<span class="fdn">100ft<sup>2</sup></span>
</div>""", CampoL300)
    layoutDerecha = QFormLayout()
    layoutDerecha.addRow("""Pc <div class="fraction">
<span class="fup">lbf</span>
<span class="bar">/</span>
<span class="fdn">100ft<sup>2</sup></span>
</div>""", CampoPc)
    layoutDerecha.addRow("Vp cp", CampoVp)
    layoutDerecha.addRow("""θ<sub>0</sub> <div class="fraction">
<span class="fup">lbf</span>
<span class="bar">/</span>
<span class="fdn">100ft<sup>2</sup></span>
</div> """, CampoGel)
    layoutBtn = QHBoxLayout()
    layoutBtn.addWidget(BtnAceptar, Qt.StretchTile, Qt.AlignRight)
    layoutBtn.addWidget(BtnCancelar)
    layoutBtn.addWidget(BtnRegresar)
    layoutvertical1 = QHBoxLayout()
    layoutvertical1.addLayout(layoutDerecha)
    layoutvertical1.addLayout(layoutIzquierda)
    layoutPantalla = QVBoxLayout()
    layoutEncabezado = QHBoxLayout()
    layoutEncabezado.addWidget(TextoHidraulica)
    layoutEncabezado.addWidget(EasyDrllLogo, Qt.StretchTile, Qt.AlignRight)
    layoutPantalla.addLayout(layoutEncabezado, Qt.AlignLeft)
    layoutPantalla.addLayout(layoutvertical1)
    layoutPantalla.addSpacing(150)
    layoutPantalla.addLayout(layoutBtn)
    layoutPantalla.addSpacing(50)
    central_widget = QWidget()
    central_widget.setLayout(layoutPantalla)
    self.setCentralWidget(central_widget)

