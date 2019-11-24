import pyqtgraph as pg
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class Graficador(QWidget):
    def __init__(self, parent=None):
        super(Graficador, self).__init__(parent)
        self.graphWidget = pg.PlotWidget()
        self.gradient = QLinearGradient()
        self.gradient.setColorAt(0, QColor(0, 0, 0))
        self.gradient.setColorAt(1, QColor(255, 0, 0))
        self.pen = pg.mkPen(color=(6, 78, 83), width=5, style=Qt.SolidLine)
        hour = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        temperature = [30, 32, 34, 32, 33, 31, 29, 32, 35, 45]

        self.graphWidget.setBackground("w")
        layoutcentral = QVBoxLayout()
        layoutcentral.addWidget(self.graphWidget)
        self.setLayout(layoutcentral)
        # plot data: x, y values

        self.graphWidget.showGrid(x=True, y=True)

    def plot(self, p, dp):
        self.graphWidget.plot(p, dp, pen=self.pen, symbol='o', symbolSize=10, symbolBrush=('r'))
        curve = self.graphWidget.plot()
        curve.getViewBox().invertY(True)
