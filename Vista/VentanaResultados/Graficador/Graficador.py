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
        self.graphWidget.setLabel('top',
                                  "<span style=\"color:rgb(0, 80, 85);font-size:18px\">Presión "
                                  "[kg/cm<sup>2</sup>]</span>")
        self.graphWidget.setLabel('left', "<span style=\"color:rgb(0, 80, 85);font-size:18px\">Profundidad "
                                            "(m)</span>")
        self.graphWidget.setBackground("w")
        self.graphWidget.showGrid(x=True, y=True)
        curve = self.graphWidget.plot()
        curve.getViewBox().invertY(True)
        self.layoutcentral.addWidget(self.graphWidget)
        self.setLayout(self.layoutcentral)
        self.graphWidget.addLegend()
        self.legend = True

    def plot(self, p, dp):
        self.graphWidget.clear()
        if self.legend:
            self.graphWidget.plot(dp, p, name="Perdidas", pen=self.pen, symbol='o', symbolSize=10, symbolBrush='r')
            self.legend = False
        else:
            self.graphWidget.plot(dp, p, pen=self.pen, symbol='o', symbolSize=10, symbolBrush='r')

    def plot_dec(self, p, dec):
        self.graphWidget.setLabel('top',
                                  "<span style=\"color:rgb(0, 80, 85);font-size:18px\">DEC "
                                  "[g/cm<sup>3</sup>]</span>")
        self.graphWidget.clear()
        if self.legend:
            self.graphWidget.plot(dec, p, name="DEC", pen=self.pen, symbol='o', symbolSize=10, symbolBrush='r')
            self.legend = False
        else:
            self.graphWidget.plot(dec, p, pen=self.pen, symbol='o', symbolSize=10, symbolBrush='r')
