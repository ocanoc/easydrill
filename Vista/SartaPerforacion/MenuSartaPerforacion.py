from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from DatosSarta import DatosSarta
from Modelo.Objetos.Hidraulica.Bomba import Bomba
from Vista.SartaPerforacion.Datos.DatosBarrena.DatosBarrena import CreaBarrena
from Vista.SartaPerforacion.Datos.DatosBomba.CreaBomba import CreeaBomba
from Vista.SartaPerforacion.Datos.DatosTuberiasSuperficiales.DatosTuberiasSuperficiales import \
    DatosTuberiasSuperficiales


class SartaPerforacion(QWidget):
    model = QStandardItemModel()
    model.setHorizontalHeaderLabels(
        ['Elemento', 'OD\n [pg]', "ID\n [pg]", "Longitud\n[m]",
         "Peso\n[kg]", "Conexión\n Top", "Conexión \n Bit", "Longitud \n acumulada"])

    texto_tp = QLabel()
    texto_tp.setPixmap(QPixmap("Imagenes/TP/TextoTp.png"))

    label_instrucciones = QLabel("Ingresa los siguientes datos:")
    label_instrucciones_barrena = QLabel("Selecciona un tipo de barrena:")

    table = QTableView()
    table.setSelectionMode(QAbstractItemView.SingleSelection)
    table.setSelectionBehavior(QAbstractItemView.SelectRows)
    table.setEditTriggers(QAbstractItemView.NoEditTriggers)
    header = table.horizontalHeader()
    header.setSectionResizeMode(QHeaderView.Stretch)
    header.setDefaultSectionSize(100)
    table.setFixedSize(815, 210)
    table.setHorizontalHeader(header)
    table.setModel(model)
    table.setAlternatingRowColors(True)

    table.setStyleSheet("""
        QHeaderView::section {
        background-color: rgb(0, 80, 85);
        color: white;
        padding-left: 4px;
        border: 1px solid #6c6c6c;
        }

        QHeaderView::section:checked
        {
        background-color: rgb(154, 154, 154);
        }""")

    barrena_triconica = QLabel()
    barrena_triconica.setPixmap(QPixmap("Imagenes/Barrenas/Triconica.png"))

    barrena_pdc = QLabel()
    barrena_pdc.setPixmap(QPixmap("Imagenes/Barrenas/PDC.png"))

    mas = QPushButton()
    mas.setIcon(QIcon("Imagenes/Iconos/mas.png"))
    mas.setToolTip("Agrega Elemento")

    menos = QPushButton()
    menos.setIcon(QIcon("Imagenes/Iconos/menos.png"))
    menos.setToolTip("Elimina Elemento")

    label_long_disp = QLabel("0")

    layout_botones = QFormLayout()
    layout_botones.addRow("", QLabel(""))
    layout_botones.addRow("Agregar elemento", mas)
    layout_botones.addRow("Eliminar elemento", menos)
    layout_botones.setAlignment(Qt.AlignCenter)
    layout_botones.setSpacing(15)

    layout_inferior = QHBoxLayout()
    layout_inferior.addWidget(table, 1, Qt.AlignCenter)
    layout_inferior.addSpacing(10)
    layout_inferior.addLayout(layout_botones, 1)
    layout_inferior.addStretch(1)


    texto_conexiones = QLabel()
    texto_conexiones.setPixmap(QPixmap("Imagenes/TP/TextoSuperficial.png"))

    tipo = QComboBox()
    tipo.addItems(["Selecciona", "Tipo 1", "Tipo 2", "Tipo 3", "Tipo 4"])

    longitud_equivalente = QLabel("N/A")

    btn_bomba = QPushButton("Agregar")

    campo_gasto = QLineEdit()
    campo_p_bombeo = QLineEdit()

    btn_tabla = QPushButton()
    btn_tabla.setIcon(QIcon("Imagenes/Iconos/info.png"))
    btn_tabla.setToolTip("Mostrar tabla conexiones superficiales")

    layout_equiposup = QFormLayout()
    layout_equiposup.addRow("Tipo:", tipo)
    layout_equiposup.addRow("Longitud \nequivalente [m]:", longitud_equivalente)
    # layout_equiposup.addRow("Bomba", btn_bomba)

    layout_equiposup.setVerticalSpacing(15)
    layout_equiposup.setAlignment(Qt.AlignCenter)

    g_conexiones_sup = QGroupBox()
    g_conexiones_sup.setTitle("Conexiones Superficiales.")
    g_conexiones_sup.setLayout(layout_equiposup)

    layout_bomba = QFormLayout()
    layout_bomba.addRow("Gasto [gpm]:", campo_gasto)
    layout_bomba.addRow("Presión de  \n bombeo [psi]:", campo_p_bombeo)

    g_datos_bomba = QGroupBox()
    g_datos_bomba.setTitle("Bomba.")
    g_datos_bomba.setLayout(layout_bomba)

    layout_datos = QHBoxLayout()
    layout_datos.addWidget(g_conexiones_sup)
    layout_datos.addWidget(btn_tabla, 1, Qt.AlignCenter)
    layout_datos.addWidget(g_datos_bomba)

    layout_izquierda = QVBoxLayout()
    layout_izquierda.addWidget(texto_conexiones)
    layout_izquierda.addSpacing(10)
    layout_izquierda.addWidget(label_instrucciones)
    layout_izquierda.addLayout(layout_datos)
    layout_izquierda.addSpacing(20)
    layout_izquierda.addWidget(texto_tp)
    layout_izquierda.addStretch(1)

    texto_barrena = QLabel()
    texto_barrena.setPixmap(QPixmap("Imagenes/TP/TextoBarrena.png"))

    layout_barrenas = QHBoxLayout()
    layout_barrenas.addWidget(barrena_triconica)
    layout_barrenas.addSpacing(40)
    layout_barrenas.addWidget(barrena_pdc)

    layout_derecha = QVBoxLayout()
    layout_derecha.addWidget(texto_barrena)
    layout_derecha.addWidget(label_instrucciones_barrena)
    layout_derecha.addLayout(layout_barrenas)
    layout_derecha.addStretch(1)

    layout_superior = QHBoxLayout()
    layout_superior.addLayout(layout_izquierda)
    layout_superior.addSpacing(40)
    layout_superior.addLayout(layout_derecha)
    layout_superior.addStretch(10)

    layout_pantalla = QVBoxLayout()
    layout_pantalla.addLayout(layout_superior)
    layout_pantalla.addLayout(layout_inferior)
    layout_pantalla.addStretch(1)

    bomba = None
    is_bomba = False
    clicked = 0
    diametro_agujero = 0
    data_barrena = []
    area_toberas = 0
    barrena = False
    last_opc = 0
    last_long_equi = "N/A"
    diametro_barrenas = 0

    def __init__(self, parent=None):
        super(SartaPerforacion, self).__init__(parent)
        self.acodiciona(self.g_datos_bomba)
        self.acodiciona(self.g_conexiones_sup)
        self.acodiciona(self.mas)
        self.acodiciona(self.menos)
        self.acondiciona_imagen(self.barrena_triconica)
        self.acondiciona_imagen(self.barrena_pdc)
        self.acodiciona(self.tipo)
        self.acodiciona(self.campo_p_bombeo)
        self.acodiciona(self.layout_botones)
        # self.acondiciona(self.btn_bomba)
        self.btn_bomba.setFixedWidth(110)
        self.acodiciona(self.texto_barrena)
        self.acodiciona(self.texto_conexiones)
        self.acodiciona(self.texto_tp)
        self.acodiciona(self.btn_tabla)
        self.acodiciona(self.campo_gasto)
        self.tipo.activated.connect(self.cambio_tipo)
        # self.barrena.currentIndexChanged.connect(self.cambio_barrena)
        self.mas.clicked.connect(lambda *args: self.agrega())
        self.menos.clicked.connect(lambda *args: self.elimina())
        self.btn_tabla.clicked.connect(lambda *args: self.muestratabla())
        # self.btn_bomba.clicked.connect(lambda *args: self.crea_bomba())
        self.setLayout(self.layout_pantalla)
        self.setFont(QFont('Calibri (Cuerpo)', 11, QFont.Bold))

    def cambio_tipo(self, i):
        if i is 0:
            self.longitud_equivalente.setText("N/A")
            self.last_opc = self.tipo.currentIndex()
            self.last_long_equi = "N/A"

        elif i is 1:
            self.longitud_equivalente.setText("133.2")
            self.last_opc = self.tipo.currentIndex()
            self.last_long_equi = "133.2"

        else:
            self.get_opc(i)

    def get_opc(self, i):
        print(i)
        items = ("1", "1")
        if i is 2:
            items = ("2.764", "3.826")
        elif i is 3:
            items = ("3.826", "4.276")
        elif i is 4:
            items = ("3.826", "4.276")

        item, okPressed = QInputDialog.getItem(self, "Diametro", "OD [in]:", items, 0, False)
        if okPressed and item:
            if item == "2.764":
                self.longitud_equivalente.setText("49.1")
                self.last_opc = self.tipo.currentIndex()
            elif item == "3.826":
                if i is 2:
                    self.longitud_equivalente.setText("232")
                if i is 3:
                    self.longitud_equivalente.setText("146")
                if i is 4:
                    self.longitud_equivalente.setText("103.7")
            elif item == "4.276":
                if i is 3:
                    self.longitud_equivalente.setText("146")
                if i is 4:
                    self.longitud_equivalente.setText("103.7")
            self.last_long_equi = self.longitud_equivalente.text()
            self.last_opc = self.tipo.currentIndex()
        else:
            self.tipo.setCurrentIndex(self.last_opc)
            self.longitud_equivalente.setText(self.last_long_equi)

    def cambio_barrena(self, i):
        self.campo_area_toberas.setText(self.barrena.get_selection(i))

    def elimina(self):
        if self.table.selectionModel().selectedRows():
            indexes = [QPersistentModelIndex(index) for index in self.table.selectionModel().selectedRows()]
            for index in indexes:
                self.model.removeRow(index.row())
        else:
            QMessageBox.critical(self, "Error", "Selecciona una fila.")

    def agrega(self):
        self.barrena = True
        if self.barrena is True:
            data = DatosSarta()
            if data.exec_():
                datos = data.get_data()
                self.model.insertRow(self.model.rowCount())
                self.add_row(self.model.rowCount() - 1, datos)
        else:
            QMessageBox.warning(self, "Aviso.", "Es necesario agregar una Barrena.")

    def muestratabla(self):
        dialog = DatosTuberiasSuperficiales(self)
        dialog.exec()

    @staticmethod
    def acodiciona(btn):
        btnancho = 25
        if isinstance(btn, QPushButton):
            btn.setIconSize(QSize(btnancho, btnancho))
            btn.setFixedSize(btnancho, btnancho)
            btn.setCursor(Qt.PointingHandCursor)
        if isinstance(btn, QComboBox):
            btn.setFixedWidth(117)
            btn.setCursor(Qt.PointingHandCursor)
        if isinstance(btn, QLabel):
            btn.setScaledContents(True)
            btn.setFixedSize(250, 50)
        if isinstance(btn, QLineEdit):
            btn.setFixedWidth(85)
            btn.setCursor(Qt.IBeamCursor)
            btn.setPlaceholderText("0")
        if isinstance(btn, QGroupBox):
            btn.setStyleSheet("""
            QGroupBox  {
            border: 2px solid gray;
            border-color: #005055;
            margin-top: 27px;
            }""")
            btn.setFont(QFont('Calibri (Cuerpo)', 11, QFont.Bold))
        if isinstance(btn, QFormLayout):
            btn.setRowWrapPolicy(QFormLayout.WrapAllRows)
            btn.setFieldGrowthPolicy(QFormLayout.ExpandingFieldsGrow)
            btn.setFormAlignment(Qt.AlignCenter)
            btn.setAlignment(Qt.AlignCenter)
            btn.setLabelAlignment(Qt.AlignCenter)

    def crea_bomba(self):
        crea = CreeaBomba(self)
        crea.exec_()
        if crea.get_ya():
            self.bomba = crea.get_bomba()
            dato = self.bomba.get_gasto()
            print(dato)
            dato2 = int(dato * 10000) / 10000
            self.campo_gasto.setText(f"{dato2}")
            self.btn_bomba.setText("Cambiar")
            self.is_bomba = True
        else:
            self.is_bomba = False

    def intercambiar_imagen(self, source, flag):
        if source is self.barrena_triconica:
            if flag:
                source.setPixmap(QPixmap("Imagenes/Barrenas/TriconicaSelect.png"))
            elif self.clicked is not 1:
                source.setPixmap(QPixmap("Imagenes/Barrenas/Triconica.png"))
        elif source is self.barrena_pdc:
            if flag:
                source.setPixmap(QPixmap("Imagenes/Barrenas/PDCSelect.png"))
            elif self.clicked is not 2:
                source.setPixmap(QPixmap("Imagenes/Barrenas/PDC.png"))

    def isclicked(self, source):
        if source is self.barrena_triconica:
            source.setPixmap(QPixmap("Imagenes/Barrenas/TriconicaSelect.png"))
            self.barrena_pdc.setPixmap(QPixmap("Imagenes/Barrenas/PDC.png"))
            self.clicked = 1
        if source is self.barrena_pdc:
            source.setPixmap(QPixmap("Imagenes/Barrenas/PDCSelect.png"))
            self.barrena_triconica.setPixmap(QPixmap("Imagenes/Barrenas/Triconica.png"))
            self.clicked = 2

    @staticmethod
    def acondiciona_imagen(label):
        ancho = 116
        largo = 180
        label.setScaledContents(True)
        label.setFixedSize(ancho, largo)
        label.setCursor(Qt.PointingHandCursor)

    def set_diametro_agujero(self, diametro):
        self.diametro_agujero = diametro

    def add_barrena(self, source):
        tipo = 0
        if source is self.barrena_triconica:
            tipo = 2
        if source is self.barrena_pdc:
            tipo = 1
        try:
            ya = False
            if self.barrena is True:
                result = QMessageBox.question(self, "Confirmacion.", "Se sustituira la barrena agregada anteiormente."
                                                                     " \n¿Desea continuar?",
                                              QMessageBox.Yes | QMessageBox.No)
                if result == QMessageBox.No:
                    ya = True
            if ya is False:
                crea_barrena = None
                crea_barrena = CreaBarrena(self)
                crea_barrena.set_tipo(tipo)
                if crea_barrena.exec_():
                    self.data_barrena, self.area_toberas = crea_barrena.get_data()
                    if self.data_barrena is not None:
                        self.isclicked(source)
                        if self.barrena is False:
                            self.model.insertRow(self.model.rowCount())
                            self.table.clearSelection()
                        self.barrena = True
                        self.model.setData(self.model.index(0, 0), self.data_barrena[0])
                        self.model.setData(self.model.index(0, 1), self.data_barrena[2])
                        self.model.setData(self.model.index(0, 2), "-")
                        self.model.setData(self.model.index(0, 3), float(self.data_barrena[5]) * 0.0254)
                        self.model.setData(self.model.index(0, 6), "-")
                        self.model.setData(self.model.index(0, 5), self.data_barrena[3])
                        if tipo is 2:
                            self.model.setData(self.model.index(0, 4), self.data_barrena[7])
                            self.model.setData(self.model.index(0, 7), self.data_barrena[6])
                        if tipo is 1:
                            self.model.setData(self.model.index(0, 4), self.data_barrena[6])
                            self.model.setData(self.model.index(0, 7), self.data_barrena[5])
                    self.table.clearSelection()

        except ValueError:
            pass

    def add_row(self, pos, data):
        elemento = ""
        od = ""
        di = ""
        long = 0
        peso = 0
        ct = ""
        cb = ""
        long_acu = ""
        if data[0] == "TP":
            elemento = data[0] + " " + data[1]
            od = data[3]
            di = data[4]
            long = float(data[7])
            peso = long * float(data[6]) * 1.488
            ct = data[6]
            cb = data[6]
            long_acu = data[7]

        if data[0] == "TP HW":
            elemento = data[0]
            od = data[1]
            di = data[3]
            long = float(data[6])
            peso = long * float(data[5]) * 1.488
            ct = data[4]
            cb = data[4]
            long_acu = data[6]
        if data[0] == "Lastra Barrenas":
            elemento = data[0]
            od = data[1]
            di = data[3]
            long = float(data[6])
            peso = long * float(data[5]) * 1.488
            ct = data[4]
            cb = data[4]
            long_acu = data[6]
        if data[0] == "Conexión":
            elemento = data[0]
            od = data[3]
            di = data[4]
            long = float(data[7]) * 0.0254
            peso = long * float(data[8]) * 1.488
            ct = data[1]
            cb = data[1]
            long_acu = data[6]
        if data[0] == "Martillo":
            elemento = data[0] + "  " + data[1]
            od = data[4]
            di = data[5]
            long = float(data[6])
            peso = data[7]
            ct = data[2]
            cb = data[3]
            long_acu = "-"
        if data[0] == "Amortiguador":
            elemento = data[0]
            od = data[1]
            di = data[2]
            long = float(data[7])
            peso = float(data[8])
            ct = data[4]
            cb = data[5]
            long_acu = "-"
        if data[0] == "Estabilizador":
            elemento = data[0] + " tipo " + data[1]
            od = data[5]
            di = data[6]
            long = float(data[7])
            peso = "-"
            ct = data[3]
            cb = data[4]
            long_acu = data[7]
        if data[0] == "MDW" or data[0] == "LWD":
            elemento = data[0]
            od = data[1]
            di = data[2]
            long = float(data[7])
            peso = float(data[8])
            ct = data[3]
            cb = data[5]
            long_acu = data[7]
        if data[0] == "Motor de fondo":
            elemento = data[0]
            od = data[6]
            di = data[7]
            long = float(data[8])
            peso = "-"
            ct = data[4]
            cb = data[5]
            long_acu = "-"
        if data[0] == "Porta Barrena":
            elemento = data[0]
            od = data[5]
            di = data[5]
            long = float(data[6]) * 0.0254
            peso = float(data[7])
            ct = data[1]
            cb = data[3]
            long_acu = "-"

        self.model.setData(self.model.index(pos, 0), elemento)
        self.model.setData(self.model.index(pos, 1), od)
        self.model.setData(self.model.index(pos, 2), di)
        self.model.setData(self.model.index(pos, 3), long)
        self.model.setData(self.model.index(pos, 4), peso)
        self.model.setData(self.model.index(pos, 5), ct)
        self.model.setData(self.model.index(pos, 6), cb)
        self.model.setData(self.model.index(pos, 7), long_acu)

    def get_datos(self):
        datos_sup = self.get_data_sup()
        data = self.collect_data()
        bomba = self.get_bomba()
        barrena = None
        return datos_sup, bomba, data

    def is_fil(self):
        self.get_datos()

    def get_data_sup(self):
        if self.tipo.currentIndex() is 0:
            QMessageBox.critical(self, "Error", "Selecciona las conexione superficiales.")
            return None
        else:
            return float(self.longitud_equivalente.text())

    def get_bomba(self):
        bomba = None
        try:
            if float(self.campo_gasto.text()) > 0 and float(self.campo_p_bombeo.text()) > 0:
                bomba = Bomba(float(self.campo_gasto.text()), float(self.campo_p_bombeo.text()))
                return bomba
            else:
                QMessageBox.critical(self, "Error", "Ingresa datos positivos.")
                return None
        except ValueError:
            QMessageBox.critical(self, "Error", "Ingresa una gasto.")
            return None

    def collect_data(self):
        data = []
        for row in range(self.model.rowCount()):
            data.append([])
            for column in range(self.model.columnCount()):
                index = self.model.index(row, column)
                data[row].append(str(self.model.data(index)))
        return data
