import sys

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

from Modelo.Objetos.Hidraulica.Bomba import Bomba


class CreeaBomba(QDialog):
    def __init__(self, parent=None):
        super(CreeaBomba, self).__init__(parent)
        self.title = 'Bomba'
        self.Bomba = None
        self.setFixedSize(200, 120)
        self.ya = False

        self.campo_carrera = QLineEdit()
        self.campo_eficiencia = QLineEdit()
        self.campo_camisa = QLineEdit()

        self.layout = QFormLayout()
        self.layout.addRow("Carrera (pg)", self.campo_carrera)
        self.layout.addRow("Camisa (pg)", self.campo_camisa)
        self.layout.addRow("Eficiencia (pg)", self.campo_eficiencia)

        self.btn_aceptar = QPushButton("Aceptar")
        self.btn_cancelar = QPushButton("Cancelar")

        self.btn_aceptar.clicked.connect(lambda *args: self.aceptar())
        self.btn_cancelar.clicked.connect(lambda *args: self.cancelar())

        self.acodiciona(self.btn_aceptar)
        self.acodiciona(self.btn_cancelar)

        self.layout_btn = QHBoxLayout()
        self.layout_btn.addWidget(self.btn_aceptar)
        self.layout_btn.addWidget(self.btn_cancelar)

        self.layout_ventana = QVBoxLayout()
        self.layout_ventana.addLayout(self.layout)
        self.layout_ventana.addLayout(self.layout_btn)
        self.setWindowTitle(self.title)
        self.setLayout(self.layout_ventana)

    def aceptar(self):
        try:
            camisa = float(self.campo_camisa.text())
            carrera = float(self.campo_carrera.text())
            efi = float(self.campo_eficiencia.text())
            if camisa > 0 and carrera > 0 and efi > 0:
                self.Bomba = Bomba(camisa, carrera, efi)
                self.ya = True
                self.close()
            else:
                QMessageBox.critical(self, "Error", "Datos menores que cero")
        except ValueError:
            QMessageBox.critical(self, "Error", "Datos erroneos o incompletos")

    def cancelar(self):
        self.close()

    def get_bomba(self):
        if self.ya:
            return self.Bomba
        else:
            return None

    def get_ya(self):
        return self.ya

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
    ex = CreeaBomba()
    ex.exec_()
    ex.getData()
    sys.exit(app.exec_())
