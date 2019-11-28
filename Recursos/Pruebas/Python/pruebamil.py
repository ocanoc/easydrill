import pyqtgraph as pg
from PyQt5.QtCore import *
from pyqtgraph.Qt import QtGui, QtCore

# generate layout
app = QtGui.QApplication([])
win = pg.GraphicsWindow()
label = pg.LabelItem(justify='right')
win.addItem(label)
p1 = win.addPlot(row=1, col=0)
p1.setAutoVisible(y=True)
pen = pg.mkPen(color=(6, 78, 83), width=5, style=Qt.SolidLine)
win.setBackground("w")
p1.showGrid(x=True, y=True)

p1.plot([1, 2], [1, 2], name="Perdidas", pen=pen, symbol='o', symbolSize=10, symbolBrush='r')

# cross hair
vLine = pg.InfiniteLine(angle=90, movable=False)
hLine = pg.InfiniteLine(angle=0, movable=False)
p1.addItem(vLine, ignoreBounds=True)
p1.addItem(hLine, ignoreBounds=True)

vb = p1.vb


def mouseMoved(evt):
    pos = evt[0]  ## using signal proxy turns original arguments into a tuple
    if p1.sceneBoundingRect().contains(pos):
        mousePoint = vb.mapSceneToView(pos)
        label.setText("<span style='font-size: 12pt'>x=%0.1f,   <span style='color: red'>y1=%0.1f</span>," % (
        mousePoint.x(), (mousePoint.y())))
        vLine.setPos(mousePoint.x())
        hLine.setPos(mousePoint.y())


proxy = pg.SignalProxy(p1.scene().sigMouseMoved, rateLimit=60, slot=mouseMoved)

if __name__ == '__main__':
    import sys

    if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
        QtGui.QApplication.instance().exec_()
