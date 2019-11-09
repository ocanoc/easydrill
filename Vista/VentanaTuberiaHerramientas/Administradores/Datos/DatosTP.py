import csv

from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class DatosTP(QWidget):
    def __init__(self, parent=None):
        super(DatosTP, self).__init__(parent)
        self.model = QStandardItemModel()
        self.model.setHorizontalHeaderLabels(
            ['Grado', 'OD\n [pg]', "ID\n [pg]", "Peso\nnominal\n[lb/ft]", "Peso\najustado\n[Kg]", "Conexión"])
        self.table = QTableView()
        self.table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.table.setModel(self.model)
        self.table.setAlternatingRowColors(True)
        self.header = self.table.horizontalHeader()
        self.header.setSectionResizeMode(QHeaderView.Stretch)
        self.table.setHorizontalHeader(self.header)
        self.table.setAlternatingRowColors(True)
        self.table.setFixedSize(440, 385)
        self.table.setStyleSheet("""
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
                        background-color: rgb(0, 80, 85);
                        }""")
        self.layoutpantalla = QVBoxLayout()
        self.layoutpantalla.addWidget(self.table)

        self.data = []
        self.setLayout(self.layoutpantalla)
        self.fill_table()

    def fill_table(self):
        with open('CSV/Tuberias.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            rows = 0
            for row in csv_reader:
                if line_count == 0:
                    line_count += 1
                else:
                    self.data.append(row)
                    self.model.insertRow(self.model.rowCount())
                    self.model.setData(self.model.index(rows, 0), str(row[0]))
                    self.model.setData(self.model.index(rows, 1), str(row[1]))
                    self.model.setData(self.model.index(rows, 2), str(row[3]))
                    self.model.setData(self.model.index(rows, 3), str(row[5]))
                    self.model.setData(self.model.index(rows, 4), str(row[6]))
                    self.model.setData(self.model.index(rows, 5), str(row[4]))
                    rows += 1

    def get_data(self):
        if self.get_long():
            data = self.get_row()
            return data

    def get_row(self):
        indices = self.table.selectionModel().selectedRows()
        if indices:
            for index in sorted(indices):
                return self.data[index.row()]
        else:
            QMessageBox.critical(self, "Error", "Selecciona una fila.")
