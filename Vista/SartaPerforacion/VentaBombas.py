import csv
import sys

from PyQt5.QtWidgets import *


class Bomba(QDialog):
    def __init__(self, parent=None):
        super(Bomba, self).__init__(parent)
        self.title = 'Bomba'
        self.bombas = []
        self.grupo = QButtonGroup()
        self.layout = QGridLayout()
        self.setWindowTitle(self.title)
        self.crea_data()
        self.crea_malla()
        self.setLayout(self.layout)
        self.show()

    def crea_malla(self):
        self.layout.setColumnStretch(1, 4)
        self.layout.setColumnStretch(2, 4)
        x = 0
        y = 0
        for data in self.bombas:
            str = f"\tGasto (gpm):{data[0]}\n Vel. (E.P.M): {data[1]}\nCamisa (pg): {data[2]} \n Carrera (pg): {data[3]}" \
                  f"" \
                  f"\nEficiencia (%): {data[3]}"
            j = QRadioButton(str)
            self.grupo.addButton(j)
            self.layout.addWidget(j, x, y)
            y += 1
            if y is 2:
                y = 0
                x += 1

    def crea_data(self):
        with open('CSV/Bombas.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            for row in csv_reader:
                if line_count == 0:
                    print(f'Column names are {", ".join(row)}')
                    line_count += 1
                else:
                    self.bombas.append(row)
                    line_count += 1

    def getResults(self):
        if self.exec_() == QDialog.Accepted:

            print(self.grupo.selectedId())
        else:
            return None


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Bomba()
    sys.exit(app.exec_())
