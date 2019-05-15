import sys

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class TuberiaPerforacion(QWidget):
    app = QApplication(sys.argv)
    app.setStyle('Fusion')

    model = QStandardItemModel()
    model.setHorizontalHeaderLabels(
        ['Tipo \nelemeto', 'ID\n [pg]', "OD\n [pg]", "Long.\n[m]",
         "Peso\nnominal\n[lb/ft]", "Peso\najustado\n[Kg]", "Resistencia\nTension\n[lb/ft]"])
    model.insertRow(model.rowCount())

    texto_tp = QLabel()
    texto_tp.setPixmap(QPixmap("Imagenes/TP/TextoTp.png"))

    table = QTableView()
    table.setModel(model)
    header = table.horizontalHeader()
    header.setMinimumSectionSize(65)
    table.setFixedSize(719, 185)
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

    mas = QPushButton()
    mas.setIcon(QIcon("Imagenes/Iconos/mas.png"))
    mas.setToolTip("Agrega Etapa")

    menos = QPushButton()
    menos.setIcon(QIcon("Imagenes/Iconos/menos.png"))
    menos.setToolTip("Elimina Etapa")

    layout_botones = QHBoxLayout()
    layout_botones.addSpacing(720)
    layout_botones.addWidget(mas)
    layout_botones.addSpacing(25)
    layout_botones.addWidget(menos)
    layout_botones.addStretch(1)

    layout_inferior = QVBoxLayout()
    layout_inferior.addWidget(texto_tp)
    layout_inferior.addSpacing(5)
    layout_inferior.addWidget(table, 1, Qt.AlignCenter)
    layout_inferior.addLayout(layout_botones)

    texto_conexiones = QLabel()
    texto_conexiones.setPixmap(QPixmap("Imagenes/TP/TextoSuperficial.png"))

    tipo = QComboBox()
    tipo.addItems(["Tipo 1", "Tipo 2", "Tipo 3", "Tipo 4"])

    longitud_equivalente = QLabel()

    bomba = QComboBox()
    bomba.addItems(["Datos Base"])

    label_gasto = QLabel("Datos base")

    btn_tabla = QPushButton()
    btn_tabla.setIcon(QIcon("Imagenes/Iconos/info.png"))
    btn_tabla.setToolTip("Mostrar tabla conexiones superficiales")

    layout_equiposup = QFormLayout()
    layout_equiposup.addRow("Conexiones superficiales", tipo)
    layout_equiposup.addRow("Longitud equivalente Tp [m]", longitud_equivalente)
    layout_equiposup.addRow("Bomba", bomba)
    layout_equiposup.addRow("Gasto[gpm]", label_gasto)
    layout_equiposup.setVerticalSpacing(10)
    layout_equiposup.setAlignment(Qt.AlignCenter)

    layout_izquierda = QVBoxLayout()
    layout_izquierda.addSpacing(9)
    layout_izquierda.addWidget(texto_conexiones)
    layout_izquierda.addSpacing(10)
    layout_izquierda.addLayout(layout_equiposup)

    texto_barrena = QLabel()
    texto_barrena.setPixmap(QPixmap("Imagenes/TP/TextoBarrena.png"))
    barrena = QComboBox()
    barrena.addItems(["Datos", "base"])

    laabel_area_toberas = QLabel("Area")

    layout_barrena = QFormLayout()
    layout_barrena.addRow("Barrena", barrena)
    layout_barrena.addRow("Area toberas [pg<sup>2</sup>]", laabel_area_toberas)
    layout_barrena.setVerticalSpacing(10)

    layout_derecha = QVBoxLayout()
    layout_derecha.addSpacing(9)
    layout_derecha.addWidget(texto_barrena)
    layout_derecha.addSpacing(10)
    layout_derecha.addLayout(layout_barrena)

    layout_superior = QHBoxLayout()
    layout_superior.addLayout(layout_izquierda)
    layout_superior.addSpacing(10)
    layout_superior.addWidget(btn_tabla, 1, Qt.AlignBaseline)
    layout_superior.addSpacing(130)
    layout_superior.addLayout(layout_derecha)
    layout_superior.addStretch(10)

    layout_pantalla = QVBoxLayout()
    layout_pantalla.addLayout(layout_superior)
    layout_pantalla.addSpacing(10)
    layout_pantalla.addLayout(layout_inferior)

    def __init__(self, parent=None):
        super(TuberiaPerforacion, self).__init__(parent)
        self.acodiciona(self.mas)
        self.acodiciona(self.menos)
        self.acodiciona(self.barrena)
        self.acodiciona(self.tipo)
        self.acodiciona(self.bomba)
        self.acodiciona(self.texto_barrena)
        self.acodiciona(self.texto_conexiones)
        self.acodiciona(self.texto_tp)
        self.acodiciona(self.btn_tabla)
        self.mas.clicked.connect(lambda *args: self.agrega())
        self.menos.clicked.connect(lambda *args: self.elimina())
        self.btn_tabla.clicked.connect(lambda *args: self.muestratabla())
        self.setLayout(self.layout_pantalla)
        self.setFont(QFont('Calibri (Cuerpo)', 12, QFont.Bold))

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
        dialog = Dialog(self)
        dialog.show()

    @staticmethod
    def acodiciona(btn):
        btnancho = 30
        if isinstance(btn, QPushButton):
            btn.setIconSize(QSize(btnancho, btnancho))
            btn.setFixedSize(btnancho, btnancho)
            btn.setCursor(Qt.PointingHandCursor)
        if isinstance(btn, QComboBox):
            btn.setFixedWidth(110)
        if isinstance(btn, QLabel):
            btn.setScaledContents(True)
            btn.setFixedSize(250, 50)
        btn.setCursor(Qt.PointingHandCursor)


class Dialog(QDialog):
    def __init__(self, *args, **kwargs):
        super(Dialog, self).__init__(*args, **kwargs)
        self.setWindowTitle("Tabla conexiones superficiales")
        self.setFixedSize(800, 400)
        tabla = QLabel()
        tabla.setPixmap(QPixmap("Imagenes/TP/TablaConexiones.png"))
        tabla.setScaledContents(True)
        tabla.setFixedSize(700, 400)
        layout = QHBoxLayout()
        layout.addWidget(tabla)
        self.setLayout(layout)
