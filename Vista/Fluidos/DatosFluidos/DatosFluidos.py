from MenuFluidos import *
from Widgets.SwitchButton.SwitchButton import SwitchButton


class DatosFluidos:
    flag = True
    app = QApplication(sys.argv)
    app.setStyle('Fusion')
    texto_encabezado = QLabel()
    texto_encabezado.setScaledContents(True)
    texto_encabezado.setFixedSize(250, 50)
    texto_encabezado.setPixmap(QPixmap("Imagenes/TextoDatosFluido.png"))
    tipo_datos = SwitchButton()
    label_dc = QLabel("Datos de campo")
    label_dl = QLabel("Datos de laboratorio")
    campo_densidad = QLineEdit()
    campo_l600 = QLineEdit()
    campo_l300 = QLineEdit()
    campo_pc = QLineEdit()
    campo_vp = QLineEdit()
    campo_gel = QLineEdit()
    MenuFluidos = MenuFluidos()
    frame_reologia = MenuFluidos.get_frame()
    layout_izquierda = QFormLayout()
    layout_izquierda.addRow("""Densidad<div class="fraction">
<span class="fup">gr</span>
<span class="bar">/</span>
<span class="fdn">cm<sup>2</sup></span>
</div>""", campo_densidad)
    layout_izquierda.addRow("""θ<sub>0</sub> [ llbf / 100ft<sup>2</sup> ]""", campo_gel)

    layout_centro = QFormLayout()
    layout_centro.addRow("""L<sub>300</sub>
<div class="fraction">
<span class="fup">lbf</span>
<span class="bar">/</span>
<span class="fdn">100ft<sup>2</sup></span>
</div>""", campo_l300)
    layout_centro.addRow("""L<sub>600</sub>
<div class="fraction">
<span class="fup">lbf</span>
<span class="bar">/</span>
<span class="fdn">100ft<sup>2</sup></span>
</div>""", campo_l600)

    layout_derecha = QFormLayout()
    layout_derecha.addRow("Vp cp", campo_vp)
    layout_derecha.addRow("""Pc <div class="fraction">
<span class="fup">lbf</span>
<span class="bar">/</span>
<span class="fdn">100ft<sup>2</sup></span>
</div>""", campo_pc)
    layout_derecha.setVerticalSpacing(20)
    layout_derecha.itemAt(0, QFormLayout.LabelRole)
    layout_derecha.setRowWrapPolicy(QFormLayout.WrapLongRows)
    layout_izquierda.setVerticalSpacing(20)
    layout_izquierda.setFormAlignment(Qt.AlignCenter)
    layout_derecha.setFormAlignment(Qt.AlignTop)
    layout_centro.setFormAlignment(Qt.AlignTop)
    layout_centro.setVerticalSpacing(20)

    frame_centro = QFrame()
    frame_centro.setMaximumHeight(110)
    frame_centro.setMinimumHeight(110)
    frame_centro.setLayout(layout_centro)
    frame_centro.hide()
    frame_derecha = QFrame()
    frame_derecha.setLayout(layout_derecha)
    frame_derecha.setMaximumHeight(100)
    frame_derecha.setMinimumHeight(110)

    frame_centro.setLayout(layout_centro)
    layoutvertical1 = QHBoxLayout()
    layoutvertical1.addSpacing(50)
    layoutvertical1.addLayout(layout_izquierda)
    layoutvertical1.addSpacing(150)
    layoutvertical1.addWidget(frame_centro, 1, Qt.AlignTop)
    layoutvertical1.addWidget(frame_derecha)
    layoutvertical1.addStretch(10)

    layout_switch = QHBoxLayout()
    layout_switch.addWidget(label_dc)
    layout_switch.addWidget(tipo_datos)
    layout_switch.addWidget(label_dl)
    layout_switch.addSpacing(250)
    layout_switch.setAlignment(Qt.AlignRight)

    layout_pantalla = QVBoxLayout()
    layout_pantalla.addSpacing(11)
    layout_pantalla.addWidget(texto_encabezado)
    layout_pantalla.addSpacing(5)
    layout_pantalla.addLayout(layoutvertical1)
    layout_pantalla.addSpacing(10)
    layout_pantalla.addLayout(layout_switch)
    layout_pantalla.addWidget(frame_reologia)
    frame_pantalla = QFrame()
    frame_pantalla.setLayout(layout_pantalla)
    frame_pantalla.setFont(QFont('Calibri (Cuerpo)', 12, QFont.Bold))

    def __init__(self):
        self.desactiva_todo()

    def get_frame(self):
        return self.frame_pantalla

    def cambia_datos(self, flag):
        if self.flag:
            self.frame_centro.show()
            self.frame_derecha.hide()
            self.flag = flag
            print("Laboratorio")
        else:
            print("Campo")
            self.frame_centro.hide()
            self.frame_derecha.show()
            self.flag = flag

    def desactiva_todo(self):
        self.acondicionar(self.campo_densidad)
        self.acondicionar(self.campo_gel)
        self.acondicionar(self.campo_l300)
        self.acondicionar(self.campo_l600)
        self.acondicionar(self.campo_pc)
        self.acondicionar(self.campo_vp)
        self.acondicionar(self.campo_pc)

    @staticmethod
    def acondicionar(lineedit):
        lineedit.setPlaceholderText("0")
        lineedit.setFixedWidth(80)

    def checkdatos(self):
        pass
