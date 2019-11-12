import csv
import sys

from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class Datos(QWidget):
    app = QApplication(sys.argv)
    app.setStyle('Fusion')

    def __init__(self, parent=None):
        super(Datos, self).__init__(parent)
        self.list = []
        self.model_table = QStandardItemModel()
        self.table = QTableView()
        self.data = []
        self.layoutpantalla = QVBoxLayout()
        self.layoutpantalla.addWidget(self.table)
        self.layoutpantalla.addStretch(1)
        self.setLayout(self.layoutpantalla)

    def fill_table(self, tipo):
        file = None
        if tipo is 1:
            self.list = ['Código \n IADC', 'OD\n [pg]', "Conexión", "Tipo", "Longitud\n[pg]", "Boquillas",
                         "Peso\n[Kg]"]
            file = 'CSV/BarrenasTriconicas.csv'
        if tipo is 2:
            self.list = ['Código \n IADC', 'OD\n [pg]', "Conexión", "Tipo", "Longitud\n[pg]", "Boquillas",
                         "Puertos \nFijos", "Peso\n[Kg]"]
            file = 'CSV/BarrenasPDC.csv'
        self.model_table.setHorizontalHeaderLabels(self.list)
        self.table.setModel(self.model_table)
        self.acondiciona(self.table)
        with open(file) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            rows = 0
            for row in csv_reader:
                self.data.append(row)
                self.model_table.insertRow(self.model_table.rowCount())
                self.agrega_fila(self.model_table, rows, row)
                rows += 1
            csv_file.close()

    def get_data(self):
        data = self.get_row()
        return data

    def get_row(self):
        indices = self.table.selectionModel().selectedRows()
        if indices:
            for index in sorted(indices):
                return self.data[index.row()]
        else:
            QMessageBox.critical(self, "Error", "Selecciona una fila.")

    def acondiciona(self, obj):
        obj.setSelectionMode(QAbstractItemView.SingleSelection)
        obj.setSelectionBehavior(QAbstractItemView.SelectRows)
        obj.setEditTriggers(QAbstractItemView.NoEditTriggers)
        obj.setAlternatingRowColors(True)
        header = obj.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.Stretch)
        obj.setHorizontalHeader(header)
        obj.setAlternatingRowColors(True)
        obj.setFixedSize(560, 375)
        obj.setStyleSheet("""
                                          QTableView {
                                           font-size: 13px;
                                           }
                                           QHeaderView::section {
                                           background-color: rgb(0, 80, 85);
                                           color: white;
                                           padding-left: 4px;
                                           font-size: 13px;
                                           border: 1px solid #6c6c6c;
                                           }
                                           QHeaderView::section:checked
                                           {
                                           font-size: 13px;
                                           color: white;
                                           background-color: rgb(154, 154, 154);
                                           }""")

    @staticmethod
    def agrega_fila(model, pos, data):
        for x in range(0, model.columnCount()):
            model.setData(model.index(pos, x), str(data[x]))
