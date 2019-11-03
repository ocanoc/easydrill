import sys

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from Vista.SartaPerforacion.Datos.DatosBarrena.BarrenasPDC.BarrenasPDC import BarrenasPDC
from Vista.SartaPerforacion.Datos.DatosBarrena.BarrenasTriconicas.BarrenasTriconicas import BarrenasTriconicas
from Vista.SartaPerforacion.Datos.DatosBomba.CreaBomba import CreeaBomba
from Vista.SartaPerforacion.Datos.DatosTuberiasSuperficiales.DatosTuberiasSuperficiales import \
    DatosTuberiasSuperficiales


class TuberiaPerforacion(QWidget):
    app = QApplication(sys.argv)
    app.setStyle('Fusion')

    model = QStandardItemModel()
    model.setHorizontalHeaderLabels(
        ['Tipo \nelemeto', 'ID\n [pg]', "OD\n [pg]", "Long.\n[m]",
         "Peso\nnominal\n[lb/ft]", "Conexion\n 1", "Conexion \n 2"])

    texto_tp = QLabel()
    texto_tp.setPixmap(QPixmap("Imagenes/TP/TextoTp.png"))

    label_instrucciones = QLabel("Ingresa los siguientes datos:")
    label_instrucciones_barrena = QLabel("Selecciona un tipo de barrena:")

    table = QTableView()
    header = table.horizontalHeader()
    header.setMinimumSectionSize(65)
    header.setMaximumSectionSize(90)
    header.setSectionResizeMode(QHeaderView.Stretch)
    table.setFixedSize(650, 205)
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
    mas.setToolTip("Agrega Etapa")

    menos = QPushButton()
    menos.setIcon(QIcon("Imagenes/Iconos/menos.png"))
    menos.setToolTip("Elimina Etapa")

    label_long_disp = QLabel("0")

    layout_botones = QFormLayout()
    layout_botones.addRow("", QLabel(""))
    layout_botones.addRow("Agregar elemento", mas)
    layout_botones.addRow("Eliminar elemento", menos)
    layout_botones.addRow("Longitud Disponible [md]: ", label_long_disp)
    layout_botones.setAlignment(Qt.AlignCenter)
    layout_botones.setSpacing(15)

    layout_sarta = QHBoxLayout()
    layout_sarta.addWidget(table, 1, Qt.AlignCenter)
    layout_sarta.addSpacing(10)
    layout_sarta.addLayout(layout_botones, 1)
    layout_sarta.addStretch(1)

    layout_inferior = QVBoxLayout()
    layout_inferior.addLayout(layout_sarta)

    texto_conexiones = QLabel()
    texto_conexiones.setPixmap(QPixmap("Imagenes/TP/TextoSuperficial.png"))

    tipo = QComboBox()
    tipo.addItems(["Tipo 1", "Tipo 2", "Tipo 3", "Tipo 4"])

    longitud_equivalente = QLabel("133.2")

    btn_bomba = QPushButton("Agregar")

    campo_gasto = QLineEdit()

    btn_tabla = QPushButton()
    btn_tabla.setIcon(QIcon("Imagenes/Iconos/info.png"))
    btn_tabla.setToolTip("Mostrar tabla conexiones superficiales")

    layout_equiposup = QFormLayout()
    layout_equiposup.addRow("Conexiones superficiales", tipo)
    layout_equiposup.addRow("Longitud equivalente Tp [m]:", longitud_equivalente)
    # layout_equiposup.addRow("Bomba", btn_bomba)
    layout_equiposup.addRow("Gasto [gpm]:", campo_gasto)
    layout_equiposup.setVerticalSpacing(15)
    layout_equiposup.setAlignment(Qt.AlignCenter)

    layout_izquierda = QVBoxLayout()
    layout_izquierda.addWidget(texto_conexiones)
    layout_izquierda.addSpacing(30)
    layout_izquierda.addWidget(label_instrucciones)
    layout_izquierda.addLayout(layout_equiposup)
    layout_izquierda.addSpacing(40)
    layout_izquierda.addWidget(texto_tp)
    layout_izquierda.addStretch(1)

    texto_barrena = QLabel()
    texto_barrena.setPixmap(QPixmap("Imagenes/TP/TextoBarrena.png"))

    area_toberas = 0

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
    layout_superior.addSpacing(3)
    layout_superior.addWidget(btn_tabla, 1, Qt.AlignCenter)
    layout_superior.addSpacing(75)
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
    barrena = False

    def __init__(self, parent=None):
        super(TuberiaPerforacion, self).__init__(parent)
        self.acodiciona(self.mas)
        self.acodiciona(self.menos)
        self.acondiciona_imagen(self.barrena_triconica)
        self.acondiciona_imagen(self.barrena_pdc)
        self.acodiciona(self.tipo)
        # self.acondiciona(self.btn_bomba)
        self.btn_bomba.setFixedWidth(110)
        self.acodiciona(self.texto_barrena)
        self.acodiciona(self.texto_conexiones)
        self.acodiciona(self.texto_tp)
        self.acodiciona(self.btn_tabla)
        self.acodiciona(self.campo_gasto)
        self.tipo.currentIndexChanged.connect(self.cambio_tipo)
        # self.barrena.currentIndexChanged.connect(self.cambio_barrena)
        self.mas.clicked.connect(lambda *args: self.agrega())
        self.menos.clicked.connect(lambda *args: self.elimina())
        self.btn_tabla.clicked.connect(lambda *args: self.muestratabla())
        # self.btn_bomba.clicked.connect(lambda *args: self.crea_bomba())
        self.setLayout(self.layout_pantalla)
        self.setFont(QFont('Calibri (Cuerpo)', 12, QFont.Bold))

    def cambio_tipo(self, i):
        if i is 0:
            self.longitud_equivalente.setText("133.2")
        else:
            self.get_opc()

    def cambio_barrena(self, i):
        self.campo_area_toberas.setText(self.barrena.get_selection(i))

    def elimina(self):
        model = self.model
        indices = self.table.selectionModel().selectedRows()
        if indices:
            for index in sorted(indices):
                model.removeRow(index.row())
        else:
            QMessageBox.critical(self, "Error", "Selecciona una fila.")

    def agrega(self):
        if self.barrena is True:
            self.model.insertRow(self.model.rowCount())
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
            btn.setFixedWidth(85)
            btn.setCursor(Qt.PointingHandCursor)
        if isinstance(btn, QLabel):
            btn.setScaledContents(True)
            btn.setFixedSize(250, 50)
        if isinstance(btn, QLineEdit):
            btn.setFixedWidth(85)
            btn.setCursor(Qt.IBeamCursor)
            btn.setPlaceholderText("0")

    def get_opc(self):
        print(self.tipo.currentIndex())
        items = ("3.826", "4.276")
        if self.tipo.currentIndex() is 1:
            items = ("2.764", "3.826")
            item, okPressed = QInputDialog.getItem(self, "Diametro de la tuberia", "OD [in]:", items, 0, False)
            if okPressed and item:
                if float(item) is 2.764:
                    self.longitud_equivalente.setText("49.1")
                else:
                    self.longitud_equivalente.setText("232")
        if self.tipo.currentIndex() is 2:
            item, okPressed = QInputDialog.getItem(self, "Diametro de la tuberia", "OD [in]:", items, 0, False)
            if okPressed and item:
                if float(item) is 3.826:
                    self.longitud_equivalente.setText("146")
                else:
                    self.longitud_equivalente.setText("248")
        if self.tipo.currentIndex() is 3:
            item, okPressed = QInputDialog.getItem(self, "Diametro de la tuberia", "OD [in]:", items, 0, False)
            if okPressed and item:
                if float(item) is 3.826:
                    self.longitud_equivalente.setText("103.7")
                else:
                    self.longitud_equivalente.setText("176.5")

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
        try:
            ya = False
            if self.barrena is True:
                result = QMessageBox.question(self, "Confirmacion.", "Se sustituira la barrena agregada anteiormente."
                                                                     " \n¿Deseas continuar?",
                                              QMessageBox.Yes | QMessageBox.No)
                if result == QMessageBox.No:
                    ya = True
            if ya is False:
                crea_barrena = None
                if source is self.barrena_triconica:
                    crea_barrena = BarrenasTriconicas(self)
                    crea_barrena.exec()
                if source is self.barrena_pdc:
                    crea_barrena = BarrenasPDC(self)
                    crea_barrena.exec()
                self.data_barrena = crea_barrena.get_data()
                if self.data_barrena is not None:
                    self.isclicked(source)
                    rows = 0
                    if self.barrena is False:
                        self.model.insertRow(self.model.rowCount())
                    self.barrena = True
                    for row in self.data_barrena:
                        self.model.setData(self.model.index(0, rows), str(row))
                        rows += 1
        except ValueError:
            pass
