import sys
from fractions import Fraction

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class DatosHidraulicos(QDialog):
    def __init__(self, parent=None):
        super(DatosHidraulicos, self).__init__(parent)
        self.installEventFilter(self)
        self.setWindowFlag(Qt.WindowStaysOnTopHint)
        self.setWindowModality(Qt.NonModal)
        self.setWindowIcon(QIcon("Imagenes/Iconos/Gota.png"))
        self.setWindowTitle("Datos Hidraulicos")

        self.table = QTableView()
        self.model_table = QStandardItemModel()
        self.columnas = ['Tipo', 'OD\n [pg]', 'ID\n [pg]', "Longitud\n[md]", "inicio \n[md],", "ΔP\n [kg/cm<sup>3</>]",
                         "ΔP\n acumulada [kg/cm<sup>3</>]"]
        self.campo_limp_agujero = QLineEdit()
        self.model_table.setHorizontalHeaderLabels(self.columnas)
        self.table.setModel(self.model_table)
        self.acondiciona(self.table)

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

        self.fl_agujero = QFormLayout()
        self.fl_agujero.addRow("I.L [H.P./pg<sup>2</sup>]:", self.campo_limp_agujero)
        self.fl_cap_acarreo = QFormLayout()
        self.fl_cap_acarreo.addRow("CCI [adim]:", self.campo_cap_accarreo)

        self.layout_limpieza = QHBoxLayout()
        self.layout_limpieza.addLayout(self.fl_cap_acarreo)
        self.layout_limpieza.addLayout(self.fl_agujero)

        self.fl_velocidades = QFormLayout()
        self.fl_velocidades.addRow("Vi [ft/seg]:", self.campo_vel_interior)
        self.fl_vel_anular = QFormLayout()
        self.fl_vel_anular.addRow("Va [ft/seg]:", self.campo_vel_anular_op)
        self.fl_v_toberas = QFormLayout()
        self.fl_v_toberas.addRow("Vt [ft/seg]:", self.campo_velocidad_toberas)

        self.layout_vel = QHBoxLayout()
        self.layout_vel.addLayout(self.fl_velocidades)
        self.layout_vel.addLayout(self.fl_v_toberas)
        self.layout_vel.addLayout(self.fl_vel_anular)

        self.fl_potencia = QFormLayout()
        self.fl_potencia.addRow("HP<sub>b</sub> [HP]:", self.campo_potencia_h)
        self.fl_impacto = QFormLayout()
        self.fl_impacto.addRow("F<sub>b</sub> [lb]:", self.campo_impacto_h)

        self.layout_hidraulico = QHBoxLayout()
        self.layout_hidraulico.addLayout(self.fl_impacto)
        self.layout_hidraulico.addLayout(self.fl_potencia)

        self.acondiciona(self.campo_cap_accarreo)
        self.acondiciona(self.campo_impacto_h)
        self.acondiciona(self.campo_limp_agujero)
        self.acondiciona(self.campo_vel_anular_op)
        self.acondiciona(self.campo_velocidad_toberas)
        self.acondiciona(self.campo_potencia_h)
        self.acondiciona(self.campo_vel_interior)
        self.acondiciona(self.fl_cap_acarreo)
        self.acondiciona(self.fl_agujero)
        self.acondiciona(self.fl_velocidades)
        self.acondiciona(self.fl_v_toberas)
        self.acondiciona(self.fl_vel_anular)
        self.acondiciona(self.fl_potencia)
        self.acondiciona(self.fl_impacto)

        self.tab_datos = QTabWidget()
        self.tab_datos.setFixedSize(310, 80)
        self.tab1 = QWidget()
        self.tab1.setLayout(self.layout_vel)
        self.tab2 = QWidget()
        self.tab2.setLayout(self.layout_limpieza)
        self.tab3 = QWidget()
        self.tab3.setLayout(self.layout_hidraulico)
        self.tab_datos.addTab(self.tab3, "Hidraulico")
        self.tab_datos.addTab(self.tab2, "Limpieza")
        self.tab_datos.addTab(self.tab1, "Velocidades")
        self.layout_central = QVBoxLayout()
        self.layout_central.addWidget(self.table)
        self.layout_central.addWidget(self.tab_datos)
        self.setLayout(self.layout_central)

    def eventFilter(self, object, event):
        if event.type() == QEvent.WindowActivate:
            print("widget window has gained focus")
            self.setWindowOpacity(1.0)
        elif event.type() == QEvent.WindowDeactivate:
            self.setWindowOpacity(0.5)
            print("widget window has lost focus")
        elif event.type() == QEvent.FocusIn:
            print("widget has gained keyboard focus")
        elif event.type() == QEvent.FocusOut:
            print("widget has lost keyboard focus")

        return False

    @staticmethod
    def acondiciona(obj):
        if isinstance(obj, QLineEdit):
            obj.setCursor(Qt.IBeamCursor)
            obj.setFixedSize(80, 20)
            obj.setText(str(0))
            obj.setMaxLength(9)
        if isinstance(obj, QFormLayout):
            obj.setRowWrapPolicy(QFormLayout.WrapAllRows)
            obj.setFieldGrowthPolicy(QFormLayout.ExpandingFieldsGrow)
        if isinstance(obj, QTableView):
            obj.setSelectionMode(QAbstractItemView.SingleSelection)
            obj.setSelectionBehavior(QAbstractItemView.SelectRows)
            obj.setEditTriggers(QAbstractItemView.NoEditTriggers)
            obj.setAlternatingRowColors(True)
            header = obj.horizontalHeader()
            header.setSectionResizeMode(QHeaderView.Stretch)
            obj.setHorizontalHeader(header)
            obj.setAlternatingRowColors(True)
            obj.setFixedSize(800, 500)
            obj.setStyleSheet("""
                                      QTableView {
                                       font-size: 13px;
                                       }
                                       QHeaderView::section {
                                       background-color: rgb(154, 154, 154);
                                       color: black;
                                       padding-left: 4px;
                                       font-size: 13px;
                                       border: 1px solid #6c6c6c;
                                       }
                                       QHeaderView::section:checked
                                       {
                                       font-size: 13px;
                                       color: white;
                                       background-color: rgb(0, 80, 85);
                                       }""")


if __name__ == "__main__":
    cadena = "5 1/2"
    separador = " "
    separado_por_espacios = cadena.split(separador)
    print("Separado por espacios es:", separado_por_espacios)
    x = "1/2"
    x = Fraction(x)
    x = float(x)
    print(x)
    print("hola despues de la weas")
    app = QApplication(sys.argv)
    agregador = DatosHidraulicos()

    agregador.exec()
