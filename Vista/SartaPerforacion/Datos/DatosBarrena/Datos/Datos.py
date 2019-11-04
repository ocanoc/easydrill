import csv
import sys

from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class Datos(QWidget):
    app = QApplication(sys.argv)
    app.setStyle('Fusion')

    def __init__(self, parent=None):
        super(Datos, self).__init__(parent)
        self.model = QStandardItemModel()
        self.model.setHorizontalHeaderLabels(
            ["Codigo\nIADC", 'OD\n [pg]', "Conexion", "Peso\n[lb]"])
        self.table = QTableView()
        self.table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.table.setModel(self.model)
        self.table.setAlternatingRowColors(True)
        self.header = self.table.horizontalHeader()
        self.header.setSectionResizeMode(QHeaderView.Stretch)
        self.table.setHorizontalHeader(self.header)
        self.table.setFixedWidth(20)
        self.table.setFixedSize(385, 400)
        self.table.setStyleSheet("""
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
        self.data = []
        self.layoutpantalla = QVBoxLayout()
        self.layoutpantalla.addWidget(self.table)
        self.layoutpantalla.addStretch(1)
        self.setLayout(self.layoutpantalla)

    def fill_table(self, tipo):
        file = None
        if tipo is 1:
            file = 'CSV/Barrenas.csv'
        if tipo is 2:
            file = 'CSV/Barrenas.csv'
        with open(file) as csv_file:
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
