import csv
import sys

from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class DatosTriconicas(QWidget):
    app = QApplication(sys.argv)
    app.setStyle('Fusion')

    model = QStandardItemModel()
    model.setHorizontalHeaderLabels(
        ["Codigo\nIADC", 'OD\n [pg]', "Conexion", "Peso\n[lb]"])
    table = QTableView()
    table.setModel(model)
    table.setAlternatingRowColors(True)
    header = table.horizontalHeader()
    header.setSectionResizeMode(QHeaderView.Stretch)
    table.setHorizontalHeader(header)
    table.setFixedWidth(20)
    table.setFixedSize(400, 470)
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

    header = table.horizontalHeader()
    header.setMinimumSectionSize(20)
    header.setDefaultSectionSize(85)
    data = []

    def __init__(self, parent=None):
        super(DatosTriconicas, self).__init__(parent)

        self.layoutpantalla = QVBoxLayout()
        self.layoutpantalla.addWidget(self.table)
        self.layoutpantalla.addStretch(1)
        self.setLayout(self.layoutpantalla)
        self.fill_table()

    def fill_table(self):
        with open('CSV/Barrenas.csv') as csv_file:
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
