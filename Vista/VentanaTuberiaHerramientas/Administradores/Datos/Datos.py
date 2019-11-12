import csv

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from VentanaTuberiaHerramientas.Administradores.Agregador.Agregador import Agregar


class Datos(QWidget):
    def __init__(self, tipo, parent=None):
        super(Datos, self).__init__(parent)
        self.table_widht = 780
        self.table_height = 320
        self.label_title = QLabel()
        self.datos = None
        self.tipo = tipo + 1
        self.model_table = QStandardItemModel()
        self.table = QTableView()
        self.list = []
        self.file = None
        self.csv_file = None
        self.data = []
        self.layout_pantalla = QVBoxLayout()
        self.create_table(tipo)
        self.layout_pantalla.addWidget(self.table, 1, Qt.AlignHCenter)
        self.setLayout(self.layout_pantalla)

    def acondiciona(self, obj):
        obj.setSelectionMode(QAbstractItemView.SingleSelection)
        obj.setSelectionBehavior(QAbstractItemView.SelectRows)
        obj.setEditTriggers(QAbstractItemView.NoEditTriggers)
        obj.setAlternatingRowColors(True)
        header = obj.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.Stretch)
        obj.setHorizontalHeader(header)
        obj.setAlternatingRowColors(True)
        obj.setFixedSize(self.table_widht, self.table_height)
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

    def create_table(self, tipo):
        print(tipo)
        if tipo is 0:
            self.list = ['Tipo', 'OD\n [pg]', 'ID\n [pg]', "Conexión\nTop", "Conexión \nBit", "Longitud\n[m]",
                         "Peso\n[Kg]"]
            self.file = 'CSV/Martillos.csv'
            self.datos = 8
        if tipo is 1:
            self.list = ['OD\n [pg]', 'ID\n [pg]', "Conexión\nTop", "Tipo", "Conexión\nBit", "Tipo", "Longitud\n[m]",
                         "Peso\n[Kg]"]
            self.file = 'CSV/Amortiguadores.csv'
            self.datos = 16
        if tipo is 2:
            self.list = ['Grado', 'OD\n [pg]', 'ID\n [pg]', "Conexión\nTop", "Conexión \nBit", "Longitud\n[m]",
                         "Peso\n Nominal\n[Kg]"]
            self.file = 'CSV/Martillos.csv'
            self.datos = 8
        if tipo is 10:
            self.list = ["Lóbulos", "Etapas", "Tipo", "Conexión\nTop", "Conexión\nBit", 'OD\n [pg]', 'ID\n [pg]',
                         "Longitud\n[m]"]
            self.file = 'CSV/Motores.csv'
            self.datos = tipo
            self.label_title.setText("Motores de fondo.")
            self.layout_pantalla.addWidget(self.label_title, 1, Qt.AlignLeft)
            self.table_height = 380

        if tipo is 7:
            self.list = ["Conexión\nTop", "Tipo", "Conexión\nBit", "Tipo", 'OD\n [pg]', "Longitud\n[in]", "Peso\n[Kg]"]
            self.file = 'CSV/PortaBarrenas.csv'
            self.datos = tipo
            self.label_title.setText("Portabarrenas.")
            self.layout_pantalla.addWidget(self.label_title, 1, Qt.AlignLeft)
            self.table_height = 380

        self.model_table.setHorizontalHeaderLabels(self.list)
        self.table.setModel(self.model_table)
        self.acondiciona(self.table)

        self.fill_table()

    def fill_table(self):
        with open(self.file) as self.csv_file:
            data = csv.reader(self.csv_file, delimiter=',')
            rows = 0
            for row in data:
                self.data.append(row)
                self.model_table.insertRow(self.model_table.rowCount())
                self.agrega_fila(self.model_table, rows, row)
                rows += 1
            self.csv_file.close()

    def write(self):
        with open(self.file, 'w', newline="") as file:
            writer = csv.writer(file)
            for x in self.data:
                writer.writerow(x)
            file.close()

    def get_data(self):
        if self.get_long():
            data = self.get_row()
            return data

    def get_row(self):
        indices = self.table_triconicas.selectionModel().selectedRows()
        if indices:
            for index in sorted(indices):
                return self.data[index.row()]
        else:
            QMessageBox.critical(self, "Error", "Selecciona una fila.")

    def agregar(self):
        nuevo = Agregar(self.datos)
        if nuevo.exec_():
            data = nuevo.get_datos()
            self.data.append(data)
            self.model_table.insertRow(self.model_table.rowCount())
            self.agrega_fila(self.model_table, self.model_table.rowCount() - 1, data)
            self.write()
            QMessageBox.information(self, "Informacion", "Se agrego la herramienta con exito.")

    def eliminar(self):
        row = self.get_fila()
        if row is not None:
            result = QMessageBox.question(self, "Confirmacion.", "Una vez elimiando el elemento no se puede deshacer."
                                                                 " \n¿Desea continuar?",
                                          QMessageBox.Yes | QMessageBox.No)
            if result == QMessageBox.Yes:
                self.model_table.removeRow(row.row())
                self.data.pop(row.row())
                self.table.clearSelection()
                self.write()

    def modifcar(self):
        row = self.get_fila()
        if row is not None:
            new_data = self.data[row.row()].copy()
            insert = Agregar(self.datos)
            insert.is_modificador(new_data)
            if insert.exec_():
                data = insert.get_datos()
                self.data[row.row()] = data
                self.agrega_fila(self.model_table, row.row(), data)
                self.table.clearSelection()
                self.write()

    def get_fila(self):
        if self.table.selectionModel().selectedRows():
            p = self.table.selectionModel().selectedRows()
            for x in p:
                return x
        else:
            QMessageBox.critical(self, "Error", "Selecciona una fila.")
            return None

    @staticmethod
    def agrega_fila(model, pos, data):
        for x in range(0, model.columnCount()):
            model.setData(model.index(pos, x), str(data[x]))
