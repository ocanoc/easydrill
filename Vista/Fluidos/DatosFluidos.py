from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


def datos_fluido():
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
    layoutvertical1 = QHBoxLayout()
    layoutvertical1.addLayout(layout_derecha)
    layoutvertical1.addLayout(layout_izquierda)
    return layoutvertical1
