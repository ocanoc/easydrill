import pyqtgraph as pg
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class Graficador(QWidget):
    def __init__(self, parent=None):
        super(Graficador, self).__init__(parent)
        pg.setConfigOptions(antialias=True)
        self.graphWidget = pg.PlotWidget()
        self.pen = pg.mkPen(color=(6, 78, 83), width=5, style=Qt.SolidLine)
        self.pen2 = pg.mkPen(color=(4, 54, 13), width=5, style=Qt.SolidLine)
        self.layoutcentral = QVBoxLayout()
        self.graphWidget = pg.PlotWidget()
        self.graphWidget.showGrid(x=True, y=True)

        self.graphWidget.setLabel('left',
                                  "<span style=\"color:rgb(0, 80, 85);font-size:18px\">Presión "
                                  "[kg/cm<sup>2</sup>]</span>")
        self.graphWidget.setLabel('bottom', "<span style=\"color:rgb(0, 80, 85);font-size:18px\">Profundidad "
                                            "(m)</span>")
        self.graphWidget.setBackground("w")
        self.graphWidget.showGrid(x=True, y=True)
        curve = self.graphWidget.plot()
        curve.getViewBox().invertY(True)
        self.layoutcentral.addWidget(self.graphWidget)
        self.setLayout(self.layoutcentral)

    def plot(self, p, dp):
        self.graphWidget.clear()
        self.graphWidget.plot(p, dp, name="Perdidas", pen=self.pen, symbol='o', symbolSize=10, symbolBrush='r')

    def plot_dec(self, p, dec):
        self.graphWidget.clear()
        self.graphWidget.plot(dec, p, pen=self.pen, symbol='o', symbolSize=10, symbolBrush='r')
