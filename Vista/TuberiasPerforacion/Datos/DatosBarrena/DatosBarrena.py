from PyQt5.QtWidgets import *

import csv


class DatosBarrena(QComboBox):
    def __init__(self, parent=None):
        super(DatosBarrena, self).__init__(parent)
        self.lista_barrenas = []
        self.barrena = []
        self.crea_data()

    def crea_data(self):
        with open('CSV/Barrenas.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            for row in csv_reader:
                if line_count == 0:
                    line_count += 1
                else:
                    self.lista_barrenas.append(row)
                    self.addItem(f"{row[0]} , {row[1]} pg")
                    line_count += 1

    def get_selection(self, selection):
        self.barrena = self.lista_barrenas[selection]
        return self.barrena[3]
