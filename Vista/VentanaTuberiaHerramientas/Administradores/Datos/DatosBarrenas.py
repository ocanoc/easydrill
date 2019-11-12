import csv

from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from VentanaTuberiaHerramientas.Administradores.Agregador.Agregador import Agregar


class DatosBarrenas(QWidget):
    def __init__(self, parent=None):
        super(DatosBarrenas, self).__init__(parent)
        self.last_clicked = 0
        self.label_triconicas = QLabel("Barrenas Triconicas")

        self.model_triconicas = QStandardItemModel()
        self.model_triconicas.setHorizontalHeaderLabels(
            ['Código \n IADC', 'OD\n [pg]', "Conexión", "Tipo", "Longitud\n[pg]", "Boquillas", "Peso\n[Kg]"])
        self.table_triconicas = QTableView()
        self.table_triconicas.setModel(self.model_triconicas)
        self.acondiciona(self.table_triconicas)

        self.data_triconicas = []

        self.label_pdc = QLabel("Barrenas PDC")

        self.model_pdc = QStandardItemModel()
        self.model_pdc.setHorizontalHeaderLabels(
            ['Código \n IADC', 'OD\n [pg]', "Conexión", "Tipo", "Longitud\n[pg]", "Boquillas",
             "Puertos \nFijos", "Peso\n[Kg]"])
        self.table_pdc = QTableView()
        self.table_pdc.setModel(self.model_pdc)
        self.acondiciona(self.table_pdc)

        self.data_pdc = []

        self.layoutpantalla = QVBoxLayout()
        self.layoutpantalla.addWidget(self.label_triconicas)
        self.layoutpantalla.addWidget(self.table_triconicas)
        self.layoutpantalla.addSpacing(5)
        self.layoutpantalla.addWidget(self.label_pdc)
        self.layoutpantalla.addWidget(self.table_pdc)
        self.table_pdc.clicked.connect(lambda *args: self.set_last_clicked(self.table_pdc))
        self.table_pdc.horizontalHeader().clicked.connect(lambda *args: self.set_last_clicked(self.table_pdc))
        self.table_triconicas.clicked.connect(lambda *args: self.set_last_clicked(self.table_triconicas))
        self.setLayout(self.layoutpantalla)
        self.csv_pdc = None
        self.csv_triconicas = None
        self.fill_table()

    def fill_table(self):
        with open('CSV/BarrenasTriconicas.csv') as self.csv_triconicas:
            triconicas = csv.reader(self.csv_triconicas, delimiter=',')
            line_count = 0
            rows = 0
            for row in triconicas:
                self.data_triconicas.append(row)
                self.model_triconicas.insertRow(self.model_triconicas.rowCount())
                self.agrega_fila(self.model_triconicas, rows, row)
                rows += 1

        with open('CSV/BarrenasPDC.csv') as self.csv_pdc:
            pdc = csv.reader(self.csv_pdc, delimiter=',')
            line_count = 0
            rows = 0
            for row in pdc:
                self.data_pdc.append(row)
                self.model_pdc.insertRow(self.model_pdc.rowCount())
                self.agrega_fila(self.model_pdc, rows, row)
                rows += 1

    def write_triconicas(self):
        with open('CSV/BarrenasTriconicas.csv', 'w', newline="") as file:
            writer = csv.writer(file)
            for x in self.data_triconicas:
                writer.writerow(x)
            file.close()

    def write_pdc(self):
        with open('CSV/BarrenasPDC.csv', 'w', newline="") as file:
            writer = csv.writer(file)
            for x in self.data_pdc:
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

    @staticmethod
    def acondiciona(obj):
        obj.setSelectionMode(QAbstractItemView.SingleSelection)
        obj.setSelectionBehavior(QAbstractItemView.SelectRows)
        obj.setEditTriggers(QAbstractItemView.NoEditTriggers)
        obj.setAlternatingRowColors(True)
        header = obj.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.Stretch)
        obj.setHorizontalHeader(header)
        obj.setAlternatingRowColors(True)
        obj.setFixedSize(800, 170)
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

    def agregar(self):
        nuevo = Agregar(9)
        if nuevo.exec_():
            data = nuevo.get_datos()
            tipo = nuevo.get_tipo()
            if tipo is 0:
                self.data_triconicas.append(data)
                self.model_triconicas.insertRow(self.model_triconicas.rowCount())
                self.agrega_fila(self.model_triconicas, self.model_triconicas.rowCount() - 1, data)
                self.write_triconicas()
            else:
                self.data_pdc.append(data)
                self.model_pdc.insertRow(self.model_pdc.rowCount())
                self.agrega_fila(self.model_pdc, self.model_pdc.rowCount() - 1, data)
                self.write_pdc()
            QMessageBox.information(self, "Informacion", "Se agrego la barrena con exito.")

    def eliminar(self):
        row = self.get_fila()
        if row is not None:
            result = QMessageBox.question(self, "Confirmacion.", "Una vez elimiando el elemento no se puede deshacer."
                                                                 " \n¿Desea continuar?",
                                          QMessageBox.Yes | QMessageBox.No)
            if result == QMessageBox.Yes:
                if self.last_clicked is 1:
                    self.model_triconicas.removeRow(row.row())
                    self.data_triconicas.pop(row.row())
                    self.table_triconicas.clearSelection()
                    self.write_triconicas()
                elif self.last_clicked is 2:
                    self.model_pdc.removeRow(row.row())
                    self.data_pdc.pop(row.row())
                    self.table_pdc.clearSelection()
                    self.write_pdc()

    def modificar(self):
        row = self.get_fila()
        new_data = []
        if row is not None:
            if self.last_clicked is 1:
                new_data = self.data_triconicas[row.row()].copy()
                new_data.insert(0, 0)
            elif self.last_clicked is 2:
                new_data = self.data_pdc[row.row()].copy()
                new_data.insert(0, 0)
            insert = Agregar(9)
            insert.is_modificador(new_data)
            if insert.exec_():
                data = insert.get_datos()
                tipo = insert.get_tipo()
                if tipo is 0:
                    self.data_triconicas[row.row()] = data
                    self.agrega_fila(self.model_triconicas, row.row(), data)
                    self.write_triconicas()
                else:
                    self.data_pdc[row.row()] = data
                    self.model_pdc.removeRow(row.row())
                    self.agrega_fila(self.model_pdc, row.row(), data)
                    self.write_pdc()

    def get_fila(self):
        if self.last_clicked is 1 and self.table_triconicas.selectionModel().selectedRows():
            p = self.table_triconicas.selectionModel().selectedRows()
            for x in p:
                return x
        elif self.last_clicked is 2 and self.table_pdc.selectionModel().selectedRows():
            p = self.table_pdc.selectionModel().selectedRows()
            for x in p:
                return x
        else:
            QMessageBox.critical(self, "Error", "Selecciona una fila.")
            return None

    @staticmethod
    def agrega_fila(model, pos, data):
        for x in range(0, model.columnCount()):
            model.setData(model.index(pos, x), str(data[x]))

    def set_last_clicked(self, source):
        if source is self.table_triconicas:
            print("hola")
            self.last_clicked = 1
        if source is self.table_pdc:
            print("hola2")
            self.last_clicked = 2
