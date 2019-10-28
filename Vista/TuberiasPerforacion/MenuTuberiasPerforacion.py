import sys

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from Datos.DatosBarrena.DatosBarrena import DatosBarrena
from Vista.TuberiasPerforacion.Datos.DatosBomba.CreaBomba import CreeaBomba
from Vista.TuberiasPerforacion.Datos.DatosTuberiasSuperficiales.DatosTuberiasSuperficiales import DatosTuberiasSuperficiales


class TuberiaPerforacion(QWidget):
    app = QApplication(sys.argv)
    app.setStyle('Fusion')

    model = QStandardItemModel()
    model.setHorizontalHeaderLabels(
        ['Tipo \nelemeto', 'ID\n [pg]', "OD\n [pg]", "Long.\n[m]",
         "Peso\nnominal\n[lb/ft]", "Peso\najustado\n[Kg]", "Resistencia\nTension\n[lb/ft]"])

    texto_tp = QLabel()
    texto_tp.setPixmap(QPixmap("Imagenes/TP/TextoTp.png"))

    table = QTableView()
    table.setModel(model)
    header = table.horizontalHeader()
    header.setMinimumSectionSize(65)
    table.setFixedSize(719, 233)
    table.setHorizontalHeader(header)
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

    layout_botones = QVBoxLayout()
    layout_botones.addSpacing(10)
    layout_botones.addWidget(mas)
    layout_botones.addSpacing(50)
    layout_botones.addWidget(menos)
    layout_botones.addStretch(1)

    layout_sarta = QHBoxLayout()
    layout_sarta.addWidget(table, 1, Qt.AlignCenter)
    layout_sarta.addLayout(layout_botones)
    layout_sarta.addStretch(1)

    layout_inferior = QVBoxLayout()
    layout_inferior.addSpacing(15)
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
    #layout_equiposup.addRow("Bomba", btn_bomba)
    layout_equiposup.addRow("Gasto [gpm]", campo_gasto)
    layout_equiposup.setVerticalSpacing(10)
    layout_equiposup.setAlignment(Qt.AlignCenter)

    layout_izquierda = QVBoxLayout()
    layout_izquierda.addWidget(texto_conexiones)
    layout_izquierda.addSpacing(10)
    layout_izquierda.addLayout(layout_equiposup)
    layout_izquierda.addSpacing(25)
    layout_izquierda.addWidget(texto_tp)

    texto_barrena = QLabel()
    texto_barrena.setPixmap(QPixmap("Imagenes/TP/TextoBarrena.png"))
    barrena = DatosBarrena()

    campo_area_toberas = QLineEdit()

    layout_barrenas = QHBoxLayout()
    layout_barrenas.addWidget(barrena_triconica)
    layout_barrenas.addWidget(barrena_pdc)

    layout_barrena = QFormLayout()
    layout_barrena.addRow("Area toberas [pg<sup>2</sup>]: ", campo_area_toberas)
    layout_barrena.setVerticalSpacing(10)

    layout_derecha = QVBoxLayout()
    layout_derecha.addWidget(texto_barrena)
    layout_derecha.addLayout(layout_barrenas)
    layout_derecha.addLayout(layout_barrena)

    layout_superior = QHBoxLayout()
    layout_superior.addLayout(layout_izquierda)
    layout_superior.addSpacing(10)
    layout_superior.addWidget(btn_tabla, 1, Qt.AlignBaseline)
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

    def __init__(self, parent=None):
        super(TuberiaPerforacion, self).__init__(parent)
        self.acodiciona(self.mas)
        self.acodiciona(self.menos)
        self.acodiciona(self.barrena)
        self.acondiciona_imagen(self.barrena_triconica)
        self.acondiciona_imagen(self.barrena_pdc)
        self.barrena.setFixedWidth(180)
        self.acodiciona(self.tipo)
        #self.acodiciona(self.btn_bomba)
        self.btn_bomba.setFixedWidth(110)
        self.acodiciona(self.texto_barrena)
        self.acodiciona(self.texto_conexiones)
        self.acodiciona(self.texto_tp)
        self.acodiciona(self.btn_tabla)
        self.acodiciona(self.campo_gasto)
        self.tipo.currentIndexChanged.connect(self.cambio_tipo)
        self.barrena.currentIndexChanged.connect(self.cambio_barrena)
        self.mas.clicked.connect(lambda *args: self.agrega())
        self.menos.clicked.connect(lambda *args: self.elimina())
        self.btn_tabla.clicked.connect(lambda *args: self.muestratabla())
        #self.btn_bomba.clicked.connect(lambda *args: self.crea_bomba())
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
        self.model.insertRow(self.model.rowCount())

    def muestratabla(self):
        dialog = DatosTuberiasSuperficiales(self)
        dialog.exec()

    @staticmethod
    def acodiciona(btn):
        btnancho = 30
        if isinstance(btn, QPushButton):
            btn.setIconSize(QSize(btnancho, btnancho))
            btn.setFixedSize(btnancho, btnancho)
            btn.setCursor(Qt.PointingHandCursor)
        if isinstance(btn, QComboBox):
            btn.setFixedWidth(110)
            btn.setCursor(Qt.PointingHandCursor)
        if isinstance(btn, QLabel):
            btn.setScaledContents(True)
            btn.setFixedSize(250, 50)
        if isinstance(btn, QLineEdit):
            btn.setFixedWidth(110)
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
            dato2 = int(dato * 10000)/10000
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
        ancho = 104
        largo = 160
        label.setScaledContents(True)
        label.setFixedSize(ancho, largo)
        label.setCursor(Qt.PointingHandCursor)

    def set_diametro_agujero(self, diametro):
        self.diametro_agujero = diametro
