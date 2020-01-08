import sys
from fractions import Fraction

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class DatosHidraulicos(QDialog):
    def __init__(self, parent=None):
        super(DatosHidraulicos, self).__init__(parent)
        self.setWindowFlag(Qt.WindowStaysOnTopHint)
        self.setWindowModality(Qt.NonModal)
        self.setWindowIcon(QIcon("Imagenes/Iconos/Gota.png"))
        self.setWindowTitle("Datos Hidraulicos")

        self.table_interiores = QTableView()
        self.model_table_interiores = QStandardItemModel()
        self.columnas = ['Tipo', 'OD\n [pg]', 'ID\n [pg]', "Longitud\n[md]", "inicio \n[md],", "ΔP \n[kg/cc]",
                         "ΔP\n acumulada \n[kg/cc]"]

        self.model_table_interiores.setHorizontalHeaderLabels(self.columnas)
        self.table_interiores.setModel(self.model_table_interiores)
        self.acondiciona(self.table_interiores)

        self.table_anulares = QTableView()
        self.model_table_anulares = QStandardItemModel()
        self.columnas2 = ['Tipo', 'OD\n [pg]', 'ID\n [pg]', "Longitud\n[md]", "inicio \n[md],", "ΔP \n[kg/cc]",
                          "ΔP\n acumulada \n[kg/cc]"]
        self.model_table_anulares.setHorizontalHeaderLabels(self.columnas2)
        self.table_anulares.setModel(self.model_table_anulares)
        self.acondiciona(self.table_anulares)

        self.vel_toberas = QLineEdit()
        self.vel_toberas.setToolTip("Velocidad en las toberas")

        self.presion_sup = QLineEdit()
        self.presion_sup.setToolTip("Presión superficial")

        self.potencia_reque = QLineEdit()
        self.potencia_reque.setToolTip("Potencia requerida por la bomba")

        self.potencia_hidraulica = QLineEdit()
        self.potencia_hidraulica.setToolTip("Potencia hidrualica")

        self.fuerza_impacto = QLineEdit()
        self.fuerza_impacto.setToolTip("Fuerza de impacto")

        self.indice_limpieza = QLineEdit()
        self.indice_limpieza.setToolTip("Potencia Hidraulica")

        self.fl_v_toberas = QFormLayout()
        self.fl_v_toberas.addRow("Vt [ft/seg]:", self.vel_toberas)

        self.fl_presion_sup = QFormLayout()
        self.fl_presion_sup.addRow("CCI [adim]:", self.presion_sup)

        self.fl_potencia_reque = QFormLayout()
        self.fl_potencia_reque.addRow("HP<sub>s</sub>[HP]:", self.potencia_reque)

        self.fl_potencia = QFormLayout()
        self.fl_potencia.addRow("HP<sub>b</sub>[HP]:", self.potencia_hidraulica)

        self.fl_impacto = QFormLayout()
        self.fl_impacto.addRow("F<sub>b</sub> [lb]:", self.fuerza_impacto)

        self.fl_indice_limpieza = QFormLayout()
        self.fl_indice_limpieza.addRow("I.L [H.P./pg<sup>2</sup>]:", self.indice_limpieza)

        self.acondiciona(self.presion_sup)
        self.acondiciona(self.vel_toberas)
        self.acondiciona(self.potencia_reque)
        self.acondiciona(self.fuerza_impacto)
        self.acondiciona(self.indice_limpieza)
        self.acondiciona(self.potencia_hidraulica)
        self.acondiciona(self.fl_presion_sup)
        self.acondiciona(self.fl_indice_limpieza)
        self.acondiciona(self.fl_v_toberas)
        self.acondiciona(self.fl_potencia_reque)
        self.acondiciona(self.fl_potencia)
        self.acondiciona(self.fl_impacto)

        self.tab_tables = QTabWidget()
        self.tab_tables.addTab(self.table_interiores, "Interiores")
        self.tab_tables.addTab(self.table_anulares, "Anulares")

        self.layout_campos = QHBoxLayout()
        self.layout_campos.addLayout(self.fl_v_toberas)
        self.layout_campos.addLayout(self.fl_presion_sup)
        self.layout_campos.addLayout(self.fl_potencia_reque)
        self.layout_campos.addLayout(self.fl_potencia)
        self.layout_campos.addLayout(self.fl_impacto)
        self.layout_campos.addLayout(self.fl_indice_limpieza)

        self.layout_central = QVBoxLayout()
        self.layout_central.addWidget(self.tab_tables)
        self.layout_central.addLayout(self.layout_campos)

        self.setLayout(self.layout_central)


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
            obj.setFixedSize(800, 250)
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

    def set_model(self, model):
        self.table_interiores.setModel(model)
        self.acondiciona(self.table_interiores)

    def set_model_anulares(self, model):
        self.table_anulares.setModel(model)
        self.acondiciona(self.table_anulares)

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
