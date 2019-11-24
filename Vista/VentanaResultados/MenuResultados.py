from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from Controlador.Hidraulica.ControladorBarrena import ControladorBarrena
from Controlador.Hidraulica.Metodos.PlasticoBingham import PlascticoBingham
from Controlador.Tuberia.ControladorTuberia import ControladorTuberia
from ControladorDireccional import *
from ControladorSeccionesAnulares import *
from Modelo.Objetos.Tuberia.Exterior import *
from Modelo.Objetos.Tuberia.Interior import *
from Objetos.Hidraulica.Bomba import Bomba
from Objetos.Hidraulica.Fluido import Fluido
from Objetos.Tuberia.Barrena import Barrena
from VentanaResultados.Graficador.Graficador import Graficador


class MenuResultados(QWidget):

    def __init__(self, parent=None):
        super(MenuResultados, self).__init__(parent)
        self.datos_direccionales = []
        self.lista_sarta = []
        self.lista_tr = []
        self.barrena = []
        self.datosfluido = []
        self.equposup = []
        self.gasto = 0
        self.listaseciones = []
        self.trayectoria = []
        self.fluido = None
        self.bomba = None
        self.barrena = None
        self.presion_bna = 0
        self.presion_hestatica = 0

        self.texto_encabezado = QLabel()
        self.texto_encabezado.setScaledContents(True)
        self.texto_encabezado.setFixedSize(250, 50)
        self.texto_encabezado.setPixmap(QPixmap("Imagenes/Titulos/TextoResultados.png"))

        self.campo_limp_agujero = QLineEdit()
        self.campo_limp_agujero.setToolTip("Limpieza de agujero")
        self.campo_vel_anular_op = QLineEdit()
        self.campo_vel_anular_op.setToolTip("Velocidad Anular Óptima")
        self.campo_cap_accarreo = QLineEdit()
        self.campo_cap_accarreo.setToolTip("Capacidad de acarreo")
        self.campo_dec = QLineEdit()
        self.campo_dec.setToolTip("Densidad Equivalente de Circulación")
        self.campo_dp_total = QLineEdit()
        self.campo_dp_total.setToolTip("Caída de presión total")
        self.campo_vol_total = QLineEdit()
        self.campo_vol_total.setToolTip("Volumen Total")
        self.campo_densidad = QLineEdit()
        self.campo_densidad.setToolTip("Densidad del FLuido")
        self.campo_visco = QLineEdit()
        self.campo_visco.setToolTip("Viscocidad del Fluido")
        self.gasto_nuevo = QLineEdit()
        self.densidad_nueva = QLineEdit()
        self.tfa_nueva = QLineEdit()

        self.slider_tfa = QSlider(Qt.Horizontal)
        self.slider_tfa.valueChanged[int].connect(self.change_gasto)

        self.slider_gasto = QSlider(Qt.Horizontal)
        self.slider_gasto.valueChanged[int].connect(self.change_gasto)

        self.slider_densidad = QSlider(Qt.Horizontal)
        self.slider_densidad.valueChanged[int].connect(self.change_densidad)

        self.fl_slider_tfa = QFormLayout()
        self.fl_slider_tfa.setFieldGrowthPolicy(QFormLayout.ExpandingFieldsGrow)
        self.fl_slider_tfa.addRow("TFA [pg<sup>2</sup>]", self.slider_tfa)

        self.fl_slider_tfa.addRow("TFA nueva [pg<sup>2</sup>]:", self.tfa_nueva)

        self.fl_slider_gasto = QFormLayout()
        self.fl_slider_gasto.addRow("Gasto [gpm]", self.slider_gasto)
        self.fl_slider_gasto.addRow("Gasto nuevo [gpm]:", self.gasto_nuevo)

        self.fl_slider_densidad = QFormLayout()
        self.fl_slider_densidad.addRow("Densidad [gr/cm<sup>3</sup>]", self.slider_densidad)
        self.fl_slider_densidad.addRow("Densidad nueva [gr/cm<sup>3</sup>]:", self.densidad_nueva)

        self.layout_sensi = QVBoxLayout()
        self.layout_sensi.addLayout(self.fl_slider_densidad)

        self.layout_sensi.addLayout(self.fl_slider_gasto)

        self.layout_sensi.addLayout(self.fl_slider_tfa)
        self.layout_sensi.addStretch(1)

        self.fl_densi = QFormLayout()
        self.fl_densi.addRow("ρ[lb/gal]:", self.campo_densidad)
        self.fl_visco = QFormLayout()
        self.fl_visco.addRow("μ[cP]:", self.campo_visco)

        self.fl_il = QFormLayout()
        self.fl_il.addRow("I.L [H.P./pg<sup>2</sup>]:", self.campo_limp_agujero)

        self.fl_vo = QFormLayout()
        self.fl_vo.addRow("Vo [ft/seg]:", self.campo_vel_anular_op)

        self.fl_ca = QFormLayout()
        self.fl_ca.addRow("CCI:", self.campo_cap_accarreo)

        self.fl_dec = QFormLayout()
        self.fl_dec.addRow("DEC [gr/cm<sup>3</sup>]:", self.campo_dec)

        dpt = QFormLayout()
        dpt.addRow("DPt [Psi]:", self.campo_dp_total)
        dpt.setSpacing(10)

        self.fl_vt = QFormLayout()
        self.fl_vt.addRow("Vt [m<sup>3</sup>]:", self.campo_vol_total)

        self.layout_d_hidraulico_derecho = QVBoxLayout()
        self.layout_d_hidraulico_derecho.addLayout(self.fl_il)
        self.layout_d_hidraulico_derecho.addLayout(self.fl_vo)
        self.layout_d_hidraulico_derecho.addLayout(self.fl_ca)
        self.layout_d_hidraulico_izq = QVBoxLayout()
        self.layout_d_hidraulico_izq.addLayout(self.fl_dec)
        self.layout_d_hidraulico_izq.addLayout(self.fl_vt)

        self.layout_hidraulico = QHBoxLayout()
        self.layout_hidraulico.addLayout(self.layout_d_hidraulico_derecho)
        self.layout_hidraulico.addSpacing(15)
        self.layout_hidraulico.addLayout(self.layout_d_hidraulico_izq)

        self.acondiciona(self.campo_cap_accarreo)
        self.acondiciona(self.campo_dec)
        self.acondiciona(self.campo_dp_total)
        self.acondiciona(self.campo_limp_agujero)
        self.acondiciona(self.campo_vel_anular_op)
        self.acondiciona(self.campo_vol_total)
        self.acondiciona(self.campo_densidad)
        self.acondiciona(self.campo_visco)
        self.acondiciona(self.slider_gasto)
        self.acondiciona(self.slider_densidad)
        self.acondiciona(self.slider_tfa)
        self.acondiciona(self.tfa_nueva)
        self.acondiciona(self.gasto_nuevo)
        self.acondiciona(self.densidad_nueva)
        self.acondiciona(self.fl_slider_tfa)
        self.acondiciona(self.fl_slider_gasto)
        self.acondiciona(self.fl_slider_densidad)
        self.acondiciona(self.fl_il)
        self.acondiciona(self.fl_vo)
        self.acondiciona(self.fl_ca)
        self.acondiciona(self.fl_dec)
        self.acondiciona(self.fl_vt)

        self.g_sensi = QGroupBox("Análisis de sensibilidad.")
        self.g_sensi.setFont(QFont('Consolas', 11))
        self.g_sensi.setLayout(self.layout_sensi)
        self.grafica = Graficador()
        self.layout_graficador = QVBoxLayout()
        self.layout_graficador.addWidget(self.grafica)

        self.g_chart = QGroupBox()
        self.g_chart.setLayout(self.layout_graficador)
        self.g_chart.setTitle("Comportamiento de las caídas de presión por fricción.")
        self.g_tabla = QGroupBox()
        self.g_tabla.setTitle("Resultados de las caídas de presión por fricción.")

        self.g_d_hidraulico = QGroupBox()
        self.g_d_hidraulico.setTitle("Diseño Hidraulico.")
        self.g_d_hidraulico.setFont(QFont('Consolas', 11))
        self.g_d_hidraulico.setLayout(self.layout_hidraulico)

        self.tab_central = QTabWidget()
        self.tab_central.setFixedSize(680, 500)
        self.tab_central.setIconSize(QSize(30, 30))
        self.tab_central.addTab(self.g_chart, QIcon("Imagenes/Iconos/IconoChart.png"), "Grafica")
        self.tab_central.addTab(self.g_tabla, QIcon("Imagenes/Iconos/IconoTabla.png"), "Tabla")

        self.layout_izquierda = QVBoxLayout()
        self.layout_izquierda.addSpacing(25)
        self.layout_izquierda.addWidget(self.g_sensi)
        self.layout_izquierda.addWidget(self.g_d_hidraulico)

        self.layout_derecha = QVBoxLayout()
        self.layout_derecha.addWidget(self.texto_encabezado)
        self.layout_derecha.addWidget(self.tab_central)

        self.layout_pantalla = QHBoxLayout()
        self.layout_pantalla.addLayout(self.layout_derecha)
        self.layout_pantalla.addLayout(self.layout_izquierda)

        self.setLayout(self.layout_pantalla)

    @staticmethod
    def acondiciona(obj):
        if isinstance(obj, QPushButton):
            btnancho = 75
            obj.setIconSize(QSize(btnancho, btnancho))
            obj.setFixedSize(btnancho, btnancho)
            obj.setCursor(Qt.PointingHandCursor)
        if isinstance(obj, QLineEdit):
            obj.setCursor(Qt.IBeamCursor)
            obj.setFixedSize(70, 20)
            obj.setPlaceholderText("0")
        if isinstance(obj, QSlider):
            obj.setFixedSize(250, 7)
            obj.setValue(50)
            obj.setStyleSheet("""
                    QSlider::groove:horizontal {
                border: 1px solid #999999;
                height: 15px; /* the groove expands to the size of the slider by default. by giving it a height, it has a fixed size */
                background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #009ca6 , stop:1 #005055);
                margin: 2px 0;
            }

            QSlider::handle:horizontal {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #b4b4b4, stop:1 #8f8f8f);
                border: 1px solid #5c5c5c;
                width: 20px;
                margin: -2px 0; /* handle is placed by default on the contents rect of the groove. Expand outside the groove */
                border-radius: 3px;
            }""")
            obj.setTickPosition(QSlider.TicksBothSides)
            obj.setTickInterval(1)
        if isinstance(obj, QFormLayout):
            obj.setRowWrapPolicy(QFormLayout.WrapAllRows)
            obj.setFieldGrowthPolicy(QFormLayout.ExpandingFieldsGrow)
            obj.setFormAlignment(Qt.AlignHCenter)
            obj.setLabelAlignment(Qt.AlignRight)

    def change_gasto(self, value):
        print(value)

    def change_densidad(self, value):
        print(value)

    def change_tfa(self, value):
        print(value)

    def set_densidad_nueva(self, data):
        self.densidad_nueva.setText(data)

    def set_gasto_nueva(self, data):
        self.gasto_nuevo.setText(data)

    def set_tfa_nueva(self, data):
        self.tfa_nueva.setText(data)

    def set_indice_limpieza(self, data):
        self.campo_limp_agujero.setText(data)

    def set_dec(self, data):
        self.campo_dec.setText(data)

    def set_velocidad_optima(self, data):
        self.campo_vel_anular_op.setText(data)

    def set_indice_acarreo(self, data):
        self.campo_cap_accarreo.setText(data)

    def set_volumen_total(self, data):
        self.campo_vol_total.setText(data)

    def set_data_graphic(self, x, y):
        self.grafica.plot(x, y)

    def get_data(self):
        self.operate_data()

    def operate_data(self):
        self.datos_direccionales = []
        self.lista_sarta = []
        self.lista_tr = []
        self.barrena = []
        self.datosfluido = []
        self.equposup = []
        self.gasto = 0
        self.listaseciones = []
        self.trayectoria = []
        self.fluido = None
        self.bomba = None
        self.barrena = None
        self.presion_bna = 0
        self.presion_hestatica = 0
        self.ica_prom = 0
        self.vanular_prom = 0
        # Prueba

        self.trayectoria = ControladorDireccional.tipov(4000)

        self.lista_sarta.append(Interior(5, 4.214, 2000, self.trayectoria, None))
        self.lista_sarta.append(Interior(3.5, 2.764, 1985, self.trayectoria, self.lista_sarta[0]))

        self.lista_tr.append(Exterior(9.625, 9, 2250, self.trayectoria, None))
        self.lista_tr.append(Exterior(7, 6.456, 950, self.trayectoria, self.lista_tr[0]))
        self.lista_tr.append(Exterior(6.125, 6.125, 785, self.trayectoria, self.lista_tr[1]))

        self.listaseciones = ControladorSecciones.creasecciones(self.lista_tr, self.lista_sarta, self.trayectoria)
        ControladorTuberia.profundidad_vertical(self.lista_sarta, self.trayectoria)
        self.fluido = Fluido(1.06, 12, 12)
        self.bomba = Bomba(1, 1, 1)
        self.gasto = 700
        self.bomba.set_gasto(self.gasto)
        self.barrena = Barrena(0.6473)
        self.barrena.set_caida_presion(700, 1.06)
        self.presion_hestatica = self.trayectoria[len(self.trayectoria) - 1].get_fin_pv() * self.fluido.get_dl() / 10
        PlascticoBingham.set_plastico_bingham(self.lista_sarta, self.listaseciones, self.fluido, self.bomba)
        profundidad_secciones = [-133.2]
        dp_sup = PlascticoBingham.interior(700, 2.764, 1.06, 133.2, 12, 12)
        presion_secciones = [dp_sup]
        presion = 0
        ControladorSecciones.set_parametros(self.listaseciones, self.bomba, self.fluido)
        for x in self.listaseciones:
            self.ica_prom += x.get_indice_acarreo()
            self.vanular_prom += x.get_vel_anular()
            self.presion_hestatica += x.get_dp()
            print(x, "\n")
        ControladorBarrena.set_vel_toberas(self.barrena, self.bomba)
        ControladorBarrena.set_parametros_hidraulicos(self.barrena, self.bomba, self.presion_hestatica, self.fluido)
        self.campo_cap_accarreo.setText(str(self.ica_prom / len(self.listaseciones)))
        self.campo_vel_anular_op.setText(str(self.vanular_prom / len(self.listaseciones)))
        for x in self.lista_sarta:
            profundidad_secciones.append(x.get_fin_pd())
            presion += x.get_dp()
            presion_secciones.append(presion)
        profundidad_secciones.append(4000)
        presion += self.barrena.get_caidad_presion()
        print(self.barrena.get_caidad_presion())
        presion_secciones.append(presion)
        for x in reversed(self.listaseciones):
            profundidad_secciones.append(x.get_inicio_pd())
            presion += x.get_dp()
            presion_secciones.append(presion)

        self.grafica.plot(profundidad_secciones, presion_secciones)

        """ 
          for x in reversed(self.listaseciones):
            profundidad_secciones.append(x.get_fin_pd())
            presion += x.get_dp()
            presion_secciones.append(presion)
        for x in profundidad_secciones:
            print(x, "\n")
        for x in presion_secciones:
            print(x, "\n")"""
