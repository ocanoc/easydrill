import sys

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from Vista.TuberiasPerforacion.VentaBombas import Bombas


class Window(QWidget):
    def __init__(self, parent=None):
        super(Window, self).__init__(parent)
        self.btn_aceptar = QPushButton("prueba")
        self.btn_aceptar.clicked.connect(self.aceptar)


        # vertical box layout
        vlayout = QVBoxLayout()
        vlayout.addWidget(self.btn_aceptar)

        vlayout.addSpacing(10)
        vlayout.addStretch()
        self.setLayout(vlayout)

    # button_clicked slot
    @pyqtSlot()
    def aceptar(self):
        print("holi")
        w = Bombas()
        values = w.getResults()


application = QApplication(sys.argv)

# window
window = Window()
window.setWindowTitle('Button Group')
window.resize(220, 120)
window.show()

sys.exit(application.exec_())
