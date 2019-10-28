import sys
import csv

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class DatosPDC(QWidget):

    app = QApplication(sys.argv)
    app.setStyle('Fusion')

    model = QStandardItemModel()
    model.setHorizontalHeaderLabels(
        ['Grado', 'OD\n [pg]', "ID\n [pg]", "Peso\nnominal\n[lb/ft]", "Peso\najustado\n[Kg]"])
    table = QTableView()
    table.setModel(model)
    table.setAlternatingRowColors(True)
    table.setFixedWidth(20)
    table.setFixedSize(600, 470)
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

    layoutpantalla = QVBoxLayout()
    layoutpantalla.addWidget(table)
    layoutpantalla.addStretch(1)

    def __init__(self, parent=None):
        super(DatosPDC, self).__init__(parent)
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
                    self.model.insertRow(self.model.rowCount())
                    self.model.setData(self.model.index(rows, 0), str(row[0]))
                    self.model.setData(self.model.index(rows, 1), str(row[1]))
                    self.model.setData(self.model.index(rows, 2), str(row[3]))
                    self.model.setData(self.model.index(rows, 3), str(row[5]))
                    self.model.setData(self.model.index(rows, 4), str(row[6]))
                    rows += 1
