from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys
from DatosPDC.DatosPDC import DatosPDC


class BarrenasPDC(QDialog):
    def __init__(self, parent=None):
        super(BarrenasPDC, self).__init__(parent)
        self.title = 'Sarta de perforacion'
        self.setFixedSize(480, 600)

        self.btn_aceptar = QPushButton("Aceptar")
        self.btn_cancelar = QPushButton("Cancelar")

        self.btn_aceptar.clicked.connect(lambda *args: self.aceptar(self.tabs.currentWidget()))
        self.btn_cancelar.clicked.connect(lambda *args: self.cancelar())

        self.acodiciona(self.btn_aceptar)
        self.acodiciona(self.btn_cancelar)

        self.layout_btn = QHBoxLayout()
        self.layout_btn.addWidget(self.btn_aceptar)
        self.layout_btn.addWidget(self.btn_cancelar)

        self.setWindowTitle(self.title)

        self.Datos_PDC = DatosPDC()
        self.layout_ventana = QVBoxLayout()
        self.layout_ventana.addWidget(self.Datos_PDC)
        self.layout_ventana.addLayout(self.layout_btn)
        self.setWindowTitle(self.title)
        self.setLayout(self.layout_ventana)

        self.aceptado = True
        self.data = []

    def get_selection(self, selection):
        self.tabs.isActiveWindow()

    @staticmethod
    def aceptar(source):
        print(source.get_data())

    def cancelar(self):
        self.close()
        self.aceptado = False

    def aceptado(self):
        return self.aceptado

    def get_data(self):
        return self.data

    @staticmethod
    def acodiciona(btn):
        btn.setCursor(Qt.PointingHandCursor)
        btn.setStyleSheet("""
                QPushButton {
                background-color: rgb(0, 80, 85);
                border-style: outset;
                border-width: 1px;
                border-radius: 5px;
                font:  11px;
                min-width: 6em;
                padding: 6px;
                color: white
                }
                QPushButton:pressed {
                    background-color: rgb(154, 154, 154);
                    border-style: inset;
                }""")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = BarrenasPDC()
    ex.exec_()
