import sys

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

from Vista.SartaPerforacion.Datos.DatosBarrena.BarrenasTriconicas.DatosTriconicas.DatosTriconicas import DatosTriconicas


class BarrenasTriconicas(QDialog):
    aceptado = False
    data = []

    def __init__(self, parent=None):
        super(BarrenasTriconicas, self).__init__(parent)
        self.title = 'Barrenas Triconicas'
        self.setFixedSize(420, 500)

        self.btn_aceptar = QPushButton("Aceptar")
        self.btn_cancelar = QPushButton("Cancelar")

        self.btn_aceptar.clicked.connect(lambda *args: self.aceptar())
        self.btn_cancelar.clicked.connect(lambda *args: self.cancelar())

        self.acodiciona(self.btn_aceptar)
        self.acodiciona(self.btn_cancelar)

        self.layout_btn = QHBoxLayout()
        self.layout_btn.addWidget(self.btn_aceptar)
        self.layout_btn.addWidget(self.btn_cancelar)

        self.setWindowTitle(self.title)

        self.Datos_Triconicas = DatosTriconicas()
        self.layout_ventana = QVBoxLayout()
        self.layout_ventana.addWidget(self.Datos_Triconicas)
        self.layout_ventana.addLayout(self.layout_btn)
        self.setWindowTitle(self.title)
        self.setLayout(self.layout_ventana)

    def aceptar(self):
        self.data = self.Datos_Triconicas.get_data()
        if self.data is not None:
            for x in self.data:
                print(x, "\n")
            self.aceptado = True
            self.close()

    def cancelar(self):
        self.close()
        self.aceptado = False

    def get_data(self):
        if self.aceptado is True:
            return self.data
        else:
            return None

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
    ex = BarrenasTriconicas()
    ex.exec_()
