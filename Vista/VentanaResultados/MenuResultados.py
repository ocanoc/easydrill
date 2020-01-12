from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from Controlador.Hidraulica.ControladorBarrena import ControladorBarrena
from Controlador.Hidraulica.Metodos.LeydePotencias import LeyDePotencias
from Controlador.Hidraulica.Metodos.LeydePotenciasModificado import LeyDePotenciasModificado
from Controlador.Hidraulica.Metodos.PlasticoBingham import PlascticoBingham
from Controlador.Hidraulica.Metodos.SmithTool import SmithTool
from Controlador.Tuberia.ControladorTuberia import ControladorTuberia
from ControladorSeccionesAnulares import *
from Modelo.Objetos.Tuberia.Interior import *
from Recursos.Constantes.Convertidor import Convertidor
from VentanaResultados.Graficador.GrafcadorLineas import Graficador
from VentanaResultados.VentanasFlotantes.DatosHidraulicos import DatosHidraulicos


class MenuResultados(QWidget):

    def __init__(self, parent=None):
        super(MenuResultados, self).__init__(parent)
        self.trayectoria = None
        self.lista_tr = []
        self.barrena = None
        self.datos_equipo_sup = []
        self.fluido = None
        self.bomba = None

        self.lista_sarta = []
        self.listaseciones = []
        self.presion_bna = 0
        self.presion_hestatica = 0
        self.ica_prom = 0
        self.vanular_prom = 0
        self.equiposup = 0
        self.primera_grafica = False
        self.presion_anular = 0
        self.vel_interior = 0
        self.presion_sup = 0

        self.pos_gasto = 50
        self.pos_densi = 50
        self.pos_tfa = 50

        self.datos_hidraulicos = DatosHidraulicos()
        self.datos_hidraulicos.installEventFilter(self)
        self.datos_hidraulicos.hide()
        self.texto_encabezado = QLabel()
        self.texto_encabezado.setScaledContents(True)
        self.texto_encabezado.setFixedSize(250, 50)
        self.texto_encabezado.setPixmap(QPixmap("Imagenes/Titulos/TextoResultados.png"))

        self.btn_datos_h = QPushButton("Datos Hidraulicos")
        self.btn_datos_h.clicked.connect(lambda: self.datos_hidraulicos.show())

        self.campo_dp_total = QLineEdit()
        self.campo_dp_total.setReadOnly(True)
        self.campo_dp_total.setToolTip("Caída de presión total")

        self.fl_dp = QFormLayout()
        self.fl_dp.addRow("\u0394P total [kg/cm<sup>2</>]", self.campo_dp_total)

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

        self.check_dec = QCheckBox("DEC")
        self.check_dec.setChecked(False)
        self.check_dec.clicked.connect(lambda: self.btnstate(self.check_dec, self.check_dec.isChecked()))

        self.check_p = QCheckBox("Caidas de Presion")
        self.check_p.setChecked(True)
        self.check_p.clicked.connect(lambda: self.btnstate(self.check_p, self.check_p.isChecked()))

        self.layout_c_b = QVBoxLayout()
        self.layout_c_b.addWidget(self.check_p)
        self.layout_c_b.addWidget(self.check_dec)

        self.grafica_presiones = Graficador()
        self.grafica_dec = Graficador()
        self.grafica_ph = Graficador()
        self.layout_graficador = QHBoxLayout()
        self.layout_graficador.addWidget(self.grafica_presiones)

        self.acondiciona(self.slider_gasto)
        self.acondiciona(self.campo_dp_total)
        self.acondiciona(self.slider_densidad)
        self.acondiciona(self.slider_tfa)
        self.acondiciona(self.tfa_nueva)
        self.acondiciona(self.gasto_nuevo)
        self.acondiciona(self.densidad_nueva)
        self.acondiciona(self.fl_slider_tfa)
        self.acondiciona(self.fl_slider_gasto)
        self.acondiciona(self.fl_slider_densidad)
        self.acondiciona(self.btn_datos_h)

        self.g_sensi = QGroupBox("Análisis de sensibilidad.")
        self.g_sensi.setFont(QFont('Consolas', 11))
        self.g_sensi.setLayout(self.layout_sensi)

        self.g_tabla = QGroupBox()
        self.g_tabla.setTitle("Resultados de las caídas de presión por fricción.")

        self.g_datos = QGroupBox()
        self.g_datos.setTitle("Datos.")
        self.g_datos.setFont(QFont('Consolas', 11))

        self.g_grafica = QGroupBox()
        self.g_grafica.setFixedWidth(700)
        self.g_grafica.setTitle("Gráfica: Comportamiento caidas de Presión.")
        self.g_grafica.setFont(QFont('Consolas', 12))
        self.g_grafica.setLayout(self.layout_graficador)

        self.g_select_grafica = QGroupBox()
        self.g_select_grafica.setTitle("Graficas.")
        self.g_select_grafica.setLayout(self.layout_c_b)

        self.layout_izquierda = QVBoxLayout()
        self.layout_izquierda.addSpacing(57)
        self.layout_izquierda.addWidget(self.g_sensi)
        self.layout_izquierda.addWidget(self.g_select_grafica)
        self.layout_izquierda.addLayout(self.fl_dp)
        self.layout_izquierda.addWidget(self.btn_datos_h)
        self.layout_derecha = QVBoxLayout()
        self.layout_derecha.addWidget(self.texto_encabezado)
        self.layout_derecha.addWidget(self.g_grafica)

        self.layout_pantalla = QHBoxLayout()
        self.layout_pantalla.addLayout(self.layout_derecha)
        self.layout_pantalla.addLayout(self.layout_izquierda)

        self.setLayout(self.layout_pantalla)

    def btnstate(self, source, status):
        for i in reversed(range(self.layout_graficador.count())):
            self.layout_graficador.itemAt(i).widget().setParent(None)
        if source is self.check_dec:
            self.g_grafica.setTitle("Gráfica: Comportamiento DEC y P. Hidrostatica.")
            self.layout_graficador.addWidget(self.grafica_dec)
            self.layout_graficador.addWidget(self.grafica_ph)
            self.check_dec.setChecked(True)
            self.check_p.setChecked(False)
        else:
            self.g_grafica.setTitle("Gráfica: Comportamiento caídas de Presión.")
            self.layout_graficador.addWidget(self.grafica_presiones)
            self.check_dec.setChecked(False)
            self.check_p.setChecked(True)


    @staticmethod
    def acondiciona(obj):
        if isinstance(obj, QPushButton):
            obj.setCursor(Qt.PointingHandCursor)
            obj.setFixedHeight(18)
        if isinstance(obj, QLineEdit):
            obj.setCursor(Qt.IBeamCursor)
            obj.setFixedSize(80, 18)
            obj.setText(str(0))
            obj.setMaxLength(9)
        if isinstance(obj, QSlider):
            obj.setCursor(Qt.PointingHandCursor)
            obj.setFixedSize(210, 8)
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

    def operate_data(self, trayecotria, fluido, externas, datos_sup, bomba, internas, barrena):
        self.trayectoria = trayecotria
        self.lista_tr = externas
        self.barrena = barrena
        self.datos_equipo_sup = datos_sup
        self.fluido = fluido
        self.bomba = bomba
        self.listaseciones = []
        self.lista_sarta = []
        anterior = None
        for x in reversed(internas):
            tuberia = Interior(Convertidor.fracc_to_dec(x[1]), Convertidor.fracc_to_dec(x[2]),
                               x[3], self.trayectoria, anterior)
            self.lista_sarta.append(tuberia)
            tuberia.set_tipo(x[0])
            anterior = tuberia
        ControladorTuberia.profundidad_vertical(self.lista_sarta, self.trayectoria)
        self.tfa_nueva.setText(str(self.barrena.get_area_toberas()))
        self.gasto_nuevo.setText(str(self.bomba.get_gasto()))
        self.densidad_nueva.setText(str(self.fluido.get_dl()))
        self.listaseciones = ControladorSecciones.creasecciones(self.lista_tr, self.lista_sarta)
        ControladorTuberia.profundidad_vertical(self.listaseciones, self.trayectoria)
        self.primera_grafica = True
        self.plot_grafica()

    def plot_grafica(self):
        self.presion_sup = 0
        self.presion_anular = 0
        self.presion_bna = 0
        self.equiposup = 0
        self.ica_prom = 0
        self.vanular_prom = 0
        self.presion_hestatica = 0
        dec_grafica = []
        ph_grafica = []
        profundidad_dec = []
        presion = 0
        pv = 0
        if self.primera_grafica:
            self.presion_hestatica = self.trayectoria[
                                         len(self.trayectoria) - 1].get_fin_pv() * self.fluido.get_dl() / 10
            if self.fluido.get_tipo() is 1:
                self.equiposup = PlascticoBingham.interior(self.bomba.get_gasto(), self.datos_equipo_sup[0],
                                                           self.fluido.get_dl(), self.datos_equipo_sup[1],
                                                           self.fluido.get_p_cedencia(),
                                                           self.fluido.get_visco_plastica())
                PlascticoBingham.set_plastico_bingham(self.lista_sarta, self.listaseciones, self.fluido, self.bomba)
            if self.fluido.get_tipo() is 2:
                self.equiposup = LeyDePotencias.interior(self.fluido, self.fluido.set_lec_fan_300(),
                                                         self.fluido.set_lec_fan_600(), self.bomba.get_gasto(),
                                                         self.datos_equipo_sup[0], self.fluido.get_dl(),
                                                         self.datos_equipo_sup[1], self.fluido.get_p_cedencia(),
                                                         self.fluido.get_visco_plastica())
                LeyDePotencias.set_ley_potencias(self.lista_sarta, self.listaseciones, self.fluido, self.bomba)
            if self.fluido.get_tipo() is 3:
                self.equiposup = LeyDePotenciasModificado.interior(self.fluido, self.fluido.set_lec_fan_300(),
                                                                   self.fluido.set_lec_fan_600(),
                                                                   self.bomba.get_gasto(), self.datos_equipo_sup[0],
                                                                   self.fluido.get_dl(), self.datos_equipo_sup[1],
                                                                   self.fluido.get_p_cedencia(),
                                                                   self.fluido.get_visco_plastica(),
                                                                   self.fluido.get_gel())
                LeyDePotenciasModificado.set_ley_potencias_modificado(self.lista_sarta, self.listaseciones, self.fluido,
                                                                      self.bomba)
            if self.fluido.get_tipo() is 4:
                self.equiposup = SmithTool.interior(self.fluido.get_visco_plastica(), self.datos_equipo_sup[0],
                                                    self.bomba.get_gasto(), self.datos_equipo_sup[0],
                                                    self.fluido.get_dl())
                SmithTool.set_smith_tool(self.lista_sarta, self.listaseciones, self.fluido, self.bomba)

            profundidad_secciones = [-self.datos_equipo_sup[1]]
            presion_secciones = [self.equiposup]
            ControladorSecciones.set_parametros(self.listaseciones, self.bomba, self.fluido)

            for x in self.listaseciones:
                self.ica_prom += x.get_indice_acarreo()
                self.vanular_prom += x.get_vel_anular()
                self.presion_hestatica += x.get_dp()
                self.presion_anular += x.get_dp()
                # revisar dnde hacer esto
                pv += x.get_long()
                x.set_fin_pv(pv)

            ControladorSecciones.set_dec(self.listaseciones, self.fluido, self.presion_anular)
            ControladorBarrena.set_vel_toberas(self.barrena, self.bomba)
            ControladorBarrena.set_parametros_hidraulicos(self.barrena, self.bomba, self.presion_hestatica, self.fluido)
            self.barrena.set_caida_presion(self.bomba.get_gasto(), self.fluido.get_dl())
            ControladorTuberia.set_velocdad_interior(self.lista_sarta, self.bomba)

            for x in self.lista_sarta:
                self.vel_interior += x.get_vel_interior()
                profundidad_secciones.append(x.get_fin_pd())
                presion += x.get_dp()
                presion_secciones.append(presion)

            profundidad_secciones.append(
                profundidad_secciones[len(profundidad_secciones) - 1] + self.barrena.get_long())
            presion += self.barrena.get_caidad_presion()
            presion_secciones.append(presion)

            for x in reversed(self.listaseciones):
                profundidad_secciones.append(x.get_inicio_pd())
                presion += x.get_dp()
                presion_secciones.append(presion)

            profundidad_dec.append(0)
            ph_grafica.append(0)
            dec_grafica.append(self.fluido.get_dl())

            for x in self.listaseciones:
                print(x, "\n")
                profundidad_dec.append(x.get_fin_pd())
                ph_grafica.append(x.get_fin_pv() * self.fluido.get_dl())
                dec_grafica.append(x.get_dec())

            self.grafica_presiones.plot(profundidad_secciones, presion_secciones)
            self.grafica_dec.plot_dec(profundidad_dec, dec_grafica)
            self.grafica_ph.plot_ph(profundidad_dec, ph_grafica)
            self.campo_dp_total.setText(" %0.3f" % (presion))
            self.presion_sup = presion
            self.update_campos()

    def update_campos(self):
        self.update_tabla()
        self.update_tabla_anular()

        self.datos_hidraulicos.vel_toberas.setText(str(self.barrena.get_vel_toberas()))
        self.datos_hidraulicos.presion_sup.setText(str(self.presion_sup))
        self.datos_hidraulicos.potencia_reque.setText(str(self.presion_sup * self.bomba.get_gasto() / 120.7))
        self.datos_hidraulicos.potencia_hidraulica.setText(str(self.barrena.get_caidad_presion() *
                                                               self.bomba.get_gasto() / 120.7))
        self.datos_hidraulicos.fuerza_impacto.setText(str(math.sqrt((self.barrena.get_caidad_presion() * 14.22) *
                                                                    math.pow(self.bomba.get_gasto(), 2) *
                                                                    self.fluido.get_dl() / 361)))
        self.datos_hidraulicos.indice_limpieza.setText(str(float(self.datos_hidraulicos.fuerza_impacto.text()) * 1.27 /
                                                           (math.pow(self.barrena.get_diametro(), 2))))

    def update_desidad(self):
        if self.primera_grafica:
            self.fluido.set_dl(float(self.densidad_nueva.text()))

    def update_gasto(self):
        if self.primera_grafica:
            self.bomba.set_gasto(float(self.gasto_nuevo.text()))

    def update_tfa(self):
        if self.primera_grafica:
            self.barrena.set_tfa(float(self.tfa_nueva.text()))

    def update_tabla(self):
        columnas = ['Elemento', 'OD\n [pg]', 'ID\n [pg]', "Longitud\n[md]", "Inicio \n[md]", "ΔP\n [kg/cm\u00b2]",
                    "ΔP\n acumulada \n[kg/cm\u00b2]"]
        model = QStandardItemModel()
        model.setHorizontalHeaderLabels(columnas)
        count = 0
        dp_acu = self.equiposup
        model.insertRow(count)
        model.setData(model.index(count, 0), "Conexiones\nsuperficiales")
        model.setData(model.index(count, 1), self.datos_equipo_sup[0])
        model.setData(model.index(count, 2), self.datos_equipo_sup[0])
        model.setData(model.index(count, 3), self.datos_equipo_sup[1])
        model.setData(model.index(count, 4), -self.datos_equipo_sup[1])
        model.setData(model.index(count, 5), dp_acu)
        model.setData(model.index(count, 6), dp_acu)
        count = 1

        for x in self.lista_sarta:
            model.insertRow(count)
            dp_acu += x.get_dp()
            model.setData(model.index(count, 0), x.get_tipo())
            model.setData(model.index(count, 1), x.get_dext())
            model.setData(model.index(count, 2), x.get_dint())
            model.setData(model.index(count, 3), x.get_long())
            model.setData(model.index(count, 4), x.get_inicio_pd())
            model.setData(model.index(count, 5), x.get_dp())
            model.setData(model.index(count, 6), dp_acu)
            count += 1
        model.insertRow(count)
        dp_acu += self.barrena.get_caidad_presion()
        model.setData(model.index(count, 0), "Barrena \n" + self.barrena.get_tipo())
        model.setData(model.index(count, 1), self.barrena.get_diametro())
        model.setData(model.index(count, 2), self.barrena.get_diametro())
        model.setData(model.index(count, 3), self.barrena.get_long())
        model.setData(model.index(count, 4), "")
        model.setData(model.index(count, 5), self.barrena.get_caidad_presion())
        model.setData(model.index(count, 6), dp_acu)
        self.datos_hidraulicos.set_model(model)

    def update_tabla_anular(self):
        columnas = ['Diámetro\nmayor\n [pg]', 'Diámetro\nmenor\n [pg]', "Longitud\n[md]", "Inicio \n[md]",
                    "ΔP\n [kg/cm\u00b2]",
                    "ΔP\n acumulada \n[kg/cm\u00b2]", "Velocidad\nAnular\n[pie/min]", "CCI\n[adim]"]
        model = QStandardItemModel()
        model.setHorizontalHeaderLabels(columnas)
        dp_acu = 0
        count = 0
        for x in self.listaseciones:
            model.insertRow(count)
            dp_acu += x.get_dp()
            model.setData(model.index(count, 0), x.get_dmayor())
            model.setData(model.index(count, 1), x.get_dmenor())
            model.setData(model.index(count, 2), x.get_long())
            model.setData(model.index(count, 3), x.get_inicio_pd())
            model.setData(model.index(count, 4), x.get_dp())
            model.setData(model.index(count, 5), dp_acu)
            model.setData(model.index(count, 6), x.get_vel_anular())
            model.setData(model.index(count, 7), x.get_indice_acarreo())
            count += 1
        self.datos_hidraulicos.set_model_anulares(model)
