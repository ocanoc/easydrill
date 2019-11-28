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
from VentanaResultados.Graficador.GrafcadorLineas import Graficador


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
        self.ica_prom = 0
        self.vanular_prom = 0
        self.datos_equipo_sup = []
        self.equiposup = 0
        self.primera_grafica = False
        self.presion_anular = 0
        self.vel_interior = 0

        self.pos_gasto = 50
        self.pos_densi = 50
        self.pos_tfa = 50

        self.texto_encabezado = QLabel()
        self.texto_encabezado.setScaledContents(True)
        self.texto_encabezado.setFixedSize(250, 50)
        self.texto_encabezado.setPixmap(QPixmap("Imagenes/Titulos/TextoResultados.png"))

        self.campo_limp_agujero = QLineEdit()
        self.campo_limp_agujero.setToolTip("Limpieza de agujero")
        self.campo_cap_accarreo = QLineEdit()
        self.campo_cap_accarreo.setToolTip("Capacidad de acarreo")

        self.campo_vel_anular_op = QLineEdit()
        self.campo_vel_anular_op.setToolTip("Velocidad anular")
        self.campo_vel_interior = QLineEdit()
        self.campo_vel_interior.setToolTip("Velocidad interior")
        self.campo_velocidad_toberas = QLineEdit()
        self.campo_velocidad_toberas.setToolTip("Velociada en las tobeas")

        self.campo_impacto_h = QLineEdit()
        self.campo_impacto_h.setToolTip("Impacto Hidraulico")
        self.campo_potencia_h = QLineEdit()
        self.campo_potencia_h.setToolTip("Potencia Hidraulica")

        self.campo_dp_total = QLineEdit()
        self.campo_dp_total.setToolTip("Caída de presión total")

        self.gasto_nuevo = QLineEdit("0")
        self.gasto_nuevo.setToolTip("Gasto")
        self.gasto_nuevo.editingFinished.connect(self.gasto_editado)

        self.densidad_nueva = QLineEdit("0")
        self.densidad_nueva.setToolTip("Densidad del FLuido")
        self.densidad_nueva.editingFinished.connect(self.densidad_editado)

        self.tfa_nueva = QLineEdit("0")
        self.tfa_nueva.setToolTip("Area de toberas")
        self.tfa_nueva.editingFinished.connect(self.tfa_editado)

        self.slider_tfa = QSlider(Qt.Horizontal)
        self.slider_tfa.valueChanged[int].connect(self.change_tfa)

        self.slider_gasto = QSlider(Qt.Horizontal)
        self.slider_gasto.valueChanged[int].connect(self.change_gasto)

        self.slider_densidad = QSlider(Qt.Horizontal)
        self.slider_densidad.valueChanged[int].connect(self.change_densidad)

        self.fl_slider_tfa = QFormLayout()
        self.fl_slider_tfa.setFieldGrowthPolicy(QFormLayout.ExpandingFieldsGrow)
        self.fl_slider_tfa.addRow("TFA [pg<sup>2</sup>]", self.slider_tfa)

        self.fl_slider_tfa.addRow("TFA [pg<sup>2</sup>]:", self.tfa_nueva)

        self.fl_slider_gasto = QFormLayout()
        self.fl_slider_gasto.addRow("Gasto [gpm]", self.slider_gasto)
        self.fl_slider_gasto.addRow("Gasto [gpm]:", self.gasto_nuevo)

        self.fl_slider_densidad = QFormLayout()
        self.fl_slider_densidad.addRow("Densidad [gr/cm<sup>3</sup>]", self.slider_densidad)
        self.fl_slider_densidad.addRow("Densidad [gr/cm<sup>3</sup>]:", self.densidad_nueva)

        self.layout_sensi = QVBoxLayout()
        self.layout_sensi.addLayout(self.fl_slider_densidad)
        self.layout_sensi.addLayout(self.fl_slider_gasto)
        self.layout_sensi.addLayout(self.fl_slider_tfa)
        self.layout_sensi.addStretch(1)

        self.check_dec = QCheckBox("Grafica DEC")
        self.check_dec.setChecked(False)
        self.check_dec.stateChanged.connect(lambda: self.btnstate(self.check_dec.isChecked()))

        self.fl_limpieza = QFormLayout()
        self.fl_limpieza.addRow("I.L [H.P./pg<sup>2</sup>]:", self.campo_limp_agujero)
        self.fl_limpieza.addRow("CCI [adim]:", self.campo_cap_accarreo)

        self.fl_velocidades = QFormLayout()
        self.fl_velocidades.addRow("Vi [ft/seg]:", self.campo_vel_interior)
        self.fl_velocidades.addRow("Va [ft/seg]:", self.campo_vel_anular_op)
        self.fl_velocidades.addRow("Vt [ft/seg]:", self.campo_velocidad_toberas)

        self.fl_hidraulico = QFormLayout()
        self.fl_hidraulico.addRow("HP<sub>b</sub> [HP]:", self.campo_potencia_h)
        self.fl_hidraulico.addRow("F<sub>b</sub> [lb]:", self.campo_impacto_h)
        self.fl_hidraulico.addRow("Mostrar Grafica DEC:", self.check_dec)
        self.grafica_presiones = Graficador()
        self.grafica_dec = Graficador()
        self.layout_graficador = QHBoxLayout()
        self.layout_graficador.addWidget(self.grafica_presiones)

        self.tab_datos = QTabWidget()
        self.tab_datos.setFixedSize(200, 200)
        self.tab1 = QWidget()
        self.tab1.setLayout(self.fl_velocidades)
        self.tab2 = QWidget()
        self.tab2.setLayout(self.fl_limpieza)
        self.tab3 = QWidget()
        self.tab3.setLayout(self.fl_hidraulico)
        self.tab_datos.addTab(self.tab3, "Hidraulico")
        self.tab_datos.addTab(self.tab2, "Limpieza")
        self.tab_datos.addTab(self.tab1, "Velocidades")

        dpt = QFormLayout()
        dpt.addRow("DPt [Psi]:", self.campo_dp_total)
        dpt.setSpacing(10)

        self.acondiciona(self.campo_cap_accarreo)
        self.acondiciona(self.campo_impacto_h)
        self.acondiciona(self.campo_dp_total)
        self.acondiciona(self.campo_limp_agujero)
        self.acondiciona(self.campo_vel_anular_op)
        self.acondiciona(self.campo_velocidad_toberas)
        self.acondiciona(self.campo_potencia_h)
        self.acondiciona(self.slider_gasto)
        self.acondiciona(self.slider_densidad)
        self.acondiciona(self.slider_tfa)
        self.acondiciona(self.tfa_nueva)
        self.acondiciona(self.gasto_nuevo)
        self.acondiciona(self.densidad_nueva)
        self.acondiciona(self.fl_slider_tfa)
        self.acondiciona(self.fl_slider_gasto)
        self.acondiciona(self.fl_slider_densidad)
        self.acondiciona(self.campo_vel_interior)
        self.acondiciona(self.fl_hidraulico)
        self.acondiciona(self.fl_limpieza)
        self.acondiciona(self.fl_velocidades)

        self.g_sensi = QGroupBox("Análisis de sensibilidad.")
        self.g_sensi.setFont(QFont('Consolas', 11))
        self.g_sensi.setLayout(self.layout_sensi)

        self.g_tabla = QGroupBox()
        self.g_tabla.setTitle("Resultados de las caídas de presión por fricción.")

        self.g_datos = QGroupBox()
        self.g_datos.setTitle("Datos.")
        self.g_datos.setFont(QFont('Consolas', 11))
        self.layout_g_datos = QVBoxLayout()
        self.layout_g_datos.addWidget(self.tab_datos)
        self.g_datos.setLayout(self.layout_g_datos)

        self.g_grafica = QGroupBox()
        self.g_grafica.setFixedWidth(700)
        self.g_grafica.setTitle("Grafica: Comportamiento caidas de Presión.")
        self.g_grafica.setFont(QFont('Consolas', 12))
        self.g_grafica.setLayout(self.layout_graficador)

        self.layout_izquierda = QVBoxLayout()
        self.layout_izquierda.addSpacing(25)
        self.layout_izquierda.addWidget(self.g_sensi)
        self.layout_izquierda.addWidget(self.g_datos)

        self.layout_derecha = QVBoxLayout()
        self.layout_derecha.addWidget(self.texto_encabezado)
        self.layout_derecha.addWidget(self.g_grafica)

        self.layout_pantalla = QHBoxLayout()
        self.layout_pantalla.addLayout(self.layout_derecha)
        self.layout_pantalla.addLayout(self.layout_izquierda)

        self.setLayout(self.layout_pantalla)

    def btnstate(self, status):
        if status:
            for i in reversed(range(self.layout_graficador.count())):
                self.layout_graficador.itemAt(i).widget().setParent(None)
            self.layout_graficador.addWidget(self.grafica_dec)
        else:
            for i in reversed(range(self.layout_graficador.count())):
                self.layout_graficador.itemAt(i).widget().setParent(None)
            self.layout_graficador.addWidget(self.grafica_presiones)

    @staticmethod
    def acondiciona(obj):
        if isinstance(obj, QPushButton):
            btnancho = 75
            obj.setIconSize(QSize(btnancho, btnancho))
            obj.setFixedSize(btnancho, btnancho)
            obj.setCursor(Qt.PointingHandCursor)
        if isinstance(obj, QLineEdit):
            obj.setCursor(Qt.IBeamCursor)
            obj.setFixedSize(120, 20)
            obj.setText(str(0))
            obj.setMaxLength(9)
        if isinstance(obj, QSlider):
            obj.setFixedSize(200, 7)
            obj.setValue(50)
            obj.setStyleSheet("""
                    QSlider::groove:horizontal {
                border: 1px solid #999999;
                height: 15px; 
                background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #009ca6 , stop:1 #005055);
                margin: 2px 0;
            }

            QSlider::handle:horizontal {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #b4b4b4, stop:1 #8f8f8f);
                border: 1px solid #5c5c5c;
                width: 20px;
                margin: -2px 0; 
                border-radius: 3px;
            }""")
            obj.setTickPosition(QSlider.TicksBothSides)
            obj.setTickInterval(1)
        if isinstance(obj, QFormLayout):
            obj.setRowWrapPolicy(QFormLayout.WrapAllRows)
            obj.setFieldGrowthPolicy(QFormLayout.ExpandingFieldsGrow)
            obj.setFormAlignment(Qt.AlignHCenter)
            obj.setLabelAlignment(Qt.AlignRight)

    def tfa_editado(self):
        self.tfa_nueva.setEnabled(False)
        self.tfa_nueva.setEnabled(True)
        self.pos_tfa = 50
        self.slider_tfa.setValue(50)
        self.update_tfa()
        self.plot_grafica()

    def densidad_editado(self):
        self.densidad_nueva.setEnabled(False)
        self.densidad_nueva.setEnabled(True)
        self.pos_densi = 50
        self.slider_densidad.setValue(50)
        self.update_desidad()
        self.plot_grafica()

    def gasto_editado(self):
        self.gasto_nuevo.setEnabled(False)
        self.gasto_nuevo.setEnabled(True)
        self.pos_gasto = 50
        self.slider_gasto.setValue(50)
        self.update_gasto()
        self.plot_grafica()

    def change_gasto(self, value):
        base = float(self.gasto_nuevo.text())
        if value > self.pos_gasto:
            aumento = abs(self.pos_gasto - value) * 25
            base += aumento
        else:
            aumento = abs(self.pos_gasto - value) * -25
            base += aumento
        self.gasto_nuevo.setText(str(base))
        self.pos_gasto = value
        self.update_gasto()
        self.plot_grafica()

    def change_densidad(self, value):
        base = float(self.densidad_nueva.text())
        if value > self.pos_densi:
            aumento = abs(self.pos_densi - value) * 0.01
            base += aumento
        else:
            aumento = abs(self.pos_densi - value) * -0.01
            base += aumento
        self.densidad_nueva.setText(str(base))
        self.pos_densi = value

        self.update_desidad()
        self.plot_grafica()

    def change_tfa(self, value):
        base = float(self.tfa_nueva.text())
        if value > self.pos_tfa:
            aumento = abs(self.pos_tfa - value) * 0.01
            base += aumento
        else:
            aumento = abs(self.pos_tfa - value) * -0.01
            base += aumento
        self.tfa_nueva.setText(str(base))
        self.pos_tfa = value
        self.update_tfa()
        self.plot_grafica()

    def set_densidad_nueva(self, data):
        self.densidad_nueva.setText(data)

    def set_gasto_nueva(self, data):
        self.gasto_nuevo.setText(data)

    def set_tfa_nueva(self, data):
        self.tfa_nueva.setText(data)

    def set_indice_limpieza(self, data):
        self.campo_limp_agujero.setText(data)

    def set_dec(self, data):
        self.campo_impacto_h.setText(data)

    def set_velocidad_optima(self, data):
        self.campo_vel_anular_op.setText(data)

    def set_indice_acarreo(self, data):
        self.campo_cap_accarreo.setText(data)

    def set_volumen_total(self, data):
        self.campo_velocidad_toberas.setText(data)

    def set_data_graphic(self, x, y):
        self.grafica_presiones.plot(x, y)

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
        self.datos_equipo_sup = []
        self.equiposup = 0
        self.presion_anular = 0
        # Prueba

        self.fluido = Fluido(1.06, 12, 12)
        self.bomba = Bomba(700, 0)
        self.barrena = Barrena(0.6473, 6.125)
        self.tfa_nueva.setText(str(self.barrena.get_area_toberas()))
        self.gasto_nuevo.setText(str(self.bomba.get_gasto()))
        self.densidad_nueva.setText(str(self.fluido.get_dl()))
        self.trayectoria = ControladorDireccional.tipov(4000)
        self.lista_sarta.append(Interior(5, 4.214, 2000, self.trayectoria, None))
        self.lista_sarta.append(Interior(3.5, 2.764, 1985, self.trayectoria, self.lista_sarta[0]))
        self.lista_tr.append(Exterior(9.625, 9, 2250, self.trayectoria, None))
        self.lista_tr.append(Exterior(7, 6.456, 950, self.trayectoria, self.lista_tr[0]))
        self.lista_tr.append(Exterior(6.125, 6.125, 785, self.trayectoria, self.lista_tr[1]))
        self.listaseciones = ControladorSecciones.creasecciones(self.lista_tr, self.lista_sarta, self.trayectoria)
        ControladorTuberia.profundidad_vertical(self.lista_sarta, self.trayectoria)
        self.primera_grafica = True
        self.plot_grafica()

    def plot_grafica(self):
        self.ica_prom = 0
        self.vanular_prom = 0
        dec_grafica = []
        profundidad_dec = []
        presion = 0
        pv = 0
        if self.primera_grafica:
            self.presion_hestatica = self.trayectoria[
                                         len(self.trayectoria) - 1].get_fin_pv() * self.fluido.get_dl() / 10
            self.equiposup = PlascticoBingham.interior(self.bomba.get_gasto(), 2.764, self.fluido.get_dl(), 133.2,
                                                       self.fluido.get_visco_plastica(), self.fluido.get_p_cedencia())
            profundidad_secciones = [-133.2]
            presion_secciones = [self.equiposup]

            PlascticoBingham.set_plastico_bingham(self.lista_sarta, self.listaseciones, self.fluido, self.bomba)
            ControladorSecciones.set_parametros(self.listaseciones, self.bomba, self.fluido)

            for x in self.listaseciones:
                self.ica_prom += x.get_indice_acarreo()
                self.vanular_prom += x.get_vel_anular()
                self.presion_hestatica += x.get_dp()
                self.presion_anular += x.get_dp()
                # revisar dnde hacer esto
                pv += x.get_long()
                x.set_fin_pv(pv)

            ControladorSecciones.set_dec(self.listaseciones, self.fluido)
            ControladorBarrena.set_vel_toberas(self.barrena, self.bomba)
            ControladorBarrena.set_parametros_hidraulicos(self.barrena, self.bomba, self.presion_hestatica, self.fluido)
            self.barrena.set_caida_presion(self.bomba.get_gasto(), self.fluido.get_dl())
            ControladorTuberia.set_velocdad_interior(self.lista_sarta, self.bomba)

            for x in self.lista_sarta:
                self.vel_interior += x.get_vel_interior()
                profundidad_secciones.append(x.get_fin_pd())
                presion += x.get_dp()
                presion_secciones.append(presion)

            profundidad_secciones.append(4000)
            presion += self.barrena.get_caidad_presion()
            presion_secciones.append(presion)

            for x in reversed(self.listaseciones):
                profundidad_secciones.append(x.get_inicio_pd())
                presion += x.get_dp()
                presion_secciones.append(presion)

            profundidad_dec.append(0)
            dec_grafica.append(self.fluido.get_dl())

            for x in self.listaseciones:
                profundidad_dec.append(x.get_fin_pd())
                dec_grafica.append(x.get_dec())

            self.grafica_presiones.plot(profundidad_secciones, presion_secciones)
            self.grafica_dec.plot_dec(profundidad_dec, dec_grafica)
            self.update_campos()

    def update_campos(self):
        self.campo_impacto_h.setText(str(self.barrena.get_imapcto_h()))
        self.campo_potencia_h.setText(str(self.barrena.get_potencia_h()))
        self.campo_limp_agujero.setText(str(self.barrena.get_potencia_h() / self.barrena.get_diametro()))
        self.campo_cap_accarreo.setText(str(self.ica_prom / len(self.listaseciones)))
        self.campo_vel_anular_op.setText(str(self.vanular_prom / len(self.listaseciones)))
        self.campo_vel_interior.setText(str(self.vel_interior / len(self.lista_sarta)))
        self.campo_velocidad_toberas.setText(str(self.barrena.get_vel_toberas()))

    def update_desidad(self):
        if self.primera_grafica:
            self.fluido.set_dl(float(self.densidad_nueva.text()))

    def update_gasto(self):
        if self.primera_grafica:
            self.bomba.set_gasto(float(self.gasto_nuevo.text()))

    def update_tfa(self):
        if self.primera_grafica:
            self.barrena.set_tfa(float(self.tfa_nueva.text()))
