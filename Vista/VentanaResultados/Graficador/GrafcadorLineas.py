import pyqtgraph as pg
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class Graficador(QWidget):

    def __init__(self, parent=None):
        super(Graficador, self).__init__(parent)
        # generate layout
        pg.setConfigOptions(antialias=True)
        self.win = pg.GraphicsWindow()
        self.p1 = self.win.addPlot(row=1, col=0)
        self.p1.setAutoVisible(y=True)
        self.pen = pg.mkPen(color=(6, 78, 83), width=5, style=Qt.SolidLine)
        self.win.setBackground("#d0cece")
        self.p1.showGrid(x=True, y=True)
        self.vLine = pg.InfiniteLine(angle=90, movable=False)
        self.hLine = pg.InfiniteLine(angle=0, movable=False)
        curve = self.p1.plot()
        curve.getViewBox().invertY(True)
        self.p1.addLegend()
        self.p1.setLabel('top',
                         "<span style=\"color:rgb(0, 80, 85);font-size:12px\">Presión "
                         "[kg/cm<sup>2</sup>]</span>")
        self.p1.setLabel('left', "<span style=\"color:rgb(0, 80, 85);font-size:12px\">Profundidad "
                                 "(m)</span>")
        self.vb = self.p1.vb
        self.legend = True
        self.layoutcentral = QVBoxLayout()
        self.layoutcentral.addStretch(1)
        self.layoutcentral.addWidget(self.win)
        self.setLayout(self.layoutcentral)
        self.vb = self.p1.vb
        self.setCursor(Qt.CrossCursor)
        self.campo_profunidad = QLineEdit()
        self.campo_dato = QLineEdit()
        self.f_profundiad = QFormLayout()
        self.f_profundiad.addRow("Profundiad [md]:", self.campo_profunidad)
        self.f_campo = QFormLayout()
        self.f_campo.addRow("Presión [kg/cm<sup>2</sup>]</span>:", self.campo_dato)
        self.l_campos = QHBoxLayout()
        self.l_campos.addSpacing(80)
        self.l_campos.setAlignment(Qt.AlignCenter)
        self.l_campos.addLayout(self.f_profundiad)
        self.l_campos.addSpacing(25)
        self.l_campos.addLayout(self.f_campo)
        self.l_campos.addStretch(1)
        self.layoutcentral.addLayout(self.l_campos)
        self.acodiciona(self.campo_dato)
        self.acodiciona(self.campo_profunidad)

        def mouseMoved(evt):
            print("holi")
            pos = evt[0]  ## using signal proxy turns original arguments into a tuple
            if self.p1.sceneBoundingRect().contains(pos):
                mousePoint = self.vb.mapSceneToView(pos)
                self.campo_profunidad.setText(" %0.0f" % (mousePoint.y()))
                self.campo_dato.setText(" %0.3f" % (mousePoint.x()))

        self.proxy = pg.SignalProxy(self.p1.scene().sigMouseMoved, rateLimit=60, slot=mouseMoved)

    def plot(self, p, dp):
        self.p1.clear()
        if self.legend:
            self.p1.plot(dp, p, name="Perdidas", pen=self.pen, symbol='o', symbolSize=10, symbolBrush='r')
            self.legend = False
        else:
            self.p1.plot(dp, p, pen=self.pen, symbol='o', symbolSize=10, symbolBrush='r')

    def plot_dec(self, p, dec):
        self.p1.clear()
        self.p1.setLabel('top',
                         "<span style=\"color:rgb(0, 80, 85);font-size:18px\">DEC "
                         "[g/cm<sup>3</sup>]</span>")

        if self.legend:
            self.f_campo.itemAt(0).widget().setText("DEC [g/cm<sup>3</sup>]</span>")
            self.p1.plot(dec, p, name="DEC", pen=self.pen, symbol='o', symbolSize=10, symbolBrush='r')
            self.legend = False
        else:
            self.p1.plot(dec, p, pen=self.pen, symbol='o', symbolSize=10, symbolBrush='r')

    @staticmethod
    def acodiciona(obj):
        if isinstance(obj, QLineEdit):
            obj.setReadOnly(True)
            obj.setFixedWidth(85)
            obj.setCursor(Qt.IBeamCursor)
            obj.setPlaceholderText("0")
