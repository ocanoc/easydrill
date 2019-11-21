import sys  # We need sys so that we can pass argv to QApplication

import pyqtgraph as pg
from PyQt5 import QtWidgets


class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.graphWidget = pg.PlotWidget()
        self.setCentralWidget(self.graphWidget)

        self.hour = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.temperature = [30, 32, 34, 32, 33, 31, 29, 32, 35, 45]

        # plot data: x, y values

    def plot(self, p, dp):
        self.graphWidget.plot(p, dp)

def main():
    app = QtWidgets.QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
