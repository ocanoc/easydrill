import sys

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from Vista.SartaPerforacion.Datos.DatosBarrena.Datos.Datos import Datos


class CreaBarrena(QDialog):
    app = QApplication(sys.argv)
    app.setStyle('Fusion')
    aceptado = False
    data = []
    area_toberas = 0

    def __init__(self, parent=None):
        super(CreaBarrena, self).__init__(parent)
        self.setFixedSize(600, 500)
        self.setFont(QFont('Calibri (Cuerpo)', 10, QFont.Bold))
        p = self.palette()
        p.setBrush(10, QBrush(QImage("Imagenes/Fondo/FondoSeleccionBarrena.png")))
        self.setPalette(p)
        self.btn_aceptar = QPushButton("Aceptar")
        self.btn_cancelar = QPushButton("Cancelar")

        self.label_instrucciones = QLabel("Seleccione una barrena.")

        self.btn_aceptar.clicked.connect(lambda *args: self.aceptar())
        self.btn_cancelar.clicked.connect(lambda *args: self.cancelar())

        self.campo_area_toberas = QLineEdit()
        self.acodiciona(self.campo_area_toberas)
        self.acodiciona(self.btn_aceptar)
        self.acodiciona(self.btn_cancelar)

        self.layout_toberas = QFormLayout()
        self.layout_toberas.addRow("Area de toberas [pg<sup>2</sup>]: ", self.campo_area_toberas)
        self.layout_btn = QHBoxLayout()
        self.layout_btn.addWidget(self.btn_aceptar)
        self.layout_btn.addWidget(self.btn_cancelar)
        self.Datos = None
        self.layout_ventana = QVBoxLayout()
        self.title = None
        self.tipo = 0

    def set_tipo(self, tipo):
        self.tipo = tipo
        if tipo is 1:
            self.title = "Barrenas PDC"
        if tipo is 2:
            self.title = "Barrenas Triconicas"
        self.Datos = Datos()
        self.Datos.fill_table(tipo)
        self.layout_ventana.addSpacing(10)
        self.layout_ventana.addWidget(self.label_instrucciones)
        self.layout_ventana.addWidget(self.Datos)
        self.layout_ventana.addLayout(self.layout_toberas)
        self.layout_ventana.addLayout(self.layout_btn)
        self.setWindowTitle(self.title)
        self.setLayout(self.layout_ventana)

        self.setWindowTitle(self.title)

    def aceptar(self):
        self.data = self.Datos.get_data()
        if self.data is not None:
            self.area_toberas = self.get_area_toberas()
            if self.area_toberas is not 0:
                self.aceptado = True
                self.accept()

    def cancelar(self):
        self.aceptado = False
        self.reject()

    def get_data(self):
        if self.aceptado is True:
            if self.tipo is 1:
                self.data.insert(0, "Barrena PDC")
            elif self.tipo is 2:
                self.data.insert(0, "Barrena Triconica")
            return self.data, self.area_toberas
        else:
            return None, 0

    def get_area_toberas(self):
        try:
            area = float(self.campo_area_toberas.text())
            if area > 0:
                return area
            else:
                QMessageBox.critical(self, "Error", "El área de flujo no puede ser negativo.")
                return 0
        except ValueError:
            QMessageBox.critical(self, "Error", "Ingrese el área de toberas.")
        return 0

    @staticmethod
    def acodiciona(btn):
        if isinstance(btn, QPushButton):
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
        if isinstance(btn, QLineEdit):
            btn.setFixedWidth(85)
            btn.setCursor(Qt.IBeamCursor)
            btn.setPlaceholderText("0")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle('Fusion')
    ex = CreaBarrena()
    ex.set_tipo(2)
    ex.exec_()
