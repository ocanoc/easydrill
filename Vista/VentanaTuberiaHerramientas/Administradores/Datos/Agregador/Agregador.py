import sys
from fractions import Fraction

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class Agregar(QDialog):
    def __init__(self, source=None, parent=None):
        super(Agregar, self).__init__(parent)
        self.source = source
        self.setFont(QFont('Calibri (Cuerpo)', 11, QFont.Bold))
        p = self.palette()
        p.setBrush(10, QBrush(QImage("Imagenes/Fondo/FondoDatosBNA.png")))
        self.setPalette(p)

        self.label_instrucciones = QLabel("Ingresa los siguientes datos:")

        self.btn_aceptar = QPushButton("Aceptar")
        self.btn_cancelar = QPushButton("Cancelar")

        self.acondiciona(self.btn_aceptar)
        self.acondiciona(self.btn_cancelar)

        self.btn_aceptar.clicked.connect(lambda *args: self.aceptar())
        self.btn_cancelar.clicked.connect(lambda *args: self.reject())

        self.layout_btn = QHBoxLayout()
        self.layout_btn.setAlignment(Qt.AlignLeft)
        self.layout_btn.addSpacing(50)
        self.layout_btn.addWidget(self.btn_aceptar)
        self.layout_btn.addSpacing(50)
        self.layout_btn.addWidget(self.btn_cancelar)

        self.layout_campos = QFormLayout()
        self.layout_campos.setSpacing(10)
        self.layout_campos_2 = QFormLayout()
        self.layout_campos_2.setSpacing(10)

        self.setFixedSize(550, 273)
        if source is 9:
            self.tipo_barrena = QComboBox()
            self.tipo_barrena.addItems(["Triconicas", "PDC"])

            self.tipo_conexion = QComboBox()
            self.tipo_conexion.addItems(["PIN", "BOX"])

            self.tipo_barrena.currentIndexChanged.connect(self.cambio_tipo)
            self.layout_campos.addRow("Tipo de Barena", self.tipo_barrena)
            self.layout_campos.addRow("Código IADC:", QLineEdit())
            self.layout_campos.addRow("OD [pg]:", QLineEdit())
            self.layout_campos.addRow("Conexión:", QLineEdit())
            self.layout_campos.addRow("Peso [kg]:", QLineEdit())

            self.layout_campos_2.addRow("Tipo Conexión :", self.tipo_conexion)
            self.layout_campos_2.addRow("Longitud [pg]:", QLineEdit())
            self.layout_campos_2.addRow("Boquillas:", QLineEdit())

        self.layout_forms = QHBoxLayout()
        self.layout_forms.addSpacing(30)
        self.layout_forms.addLayout(self.layout_campos)
        self.layout_forms.addSpacing(30)
        self.layout_forms.addLayout(self.layout_campos_2)
        self.layout_forms.addSpacing(30)
        self.layout_forms.addStretch(1)

        self.layout_pantalla = QVBoxLayout()
        self.layout_pantalla.addWidget(self.label_instrucciones)
        self.layout_pantalla.addSpacing(15)
        self.layout_pantalla.addLayout(self.layout_forms)
        self.layout_pantalla.addSpacing(15)
        self.layout_pantalla.addLayout(self.layout_btn)
        self.layout_pantalla.addStretch(1)

        self.setLayout(self.layout_pantalla)

        self.datos = []

    def cambio_tipo(self, index):
        if index is 0:
            try:
                print("Holis")
                self.layout_campos_2.removeRow(3)
            except ValueError:
                print("error")
        else:
            self.layout_campos_2.addRow("Puertos Fijos", QLineEdit())

    @staticmethod
    def acondiciona(obj):
        if isinstance(obj, QPushButton):
            obj.setFixedSize(50, 30)
            obj.setCursor(Qt.PointingHandCursor)
            obj.setStyleSheet("""
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

    def aceptar(self):
        try:
            self.datos = []
            self.collect_data()
        except ValueError:
            self.datos = []
            QMessageBox.critical(self, "Aviso.", "Datos incompletos.")
        if self.check_datos():
            self.accept()
        else:
            self.datos = []
            QMessageBox.critical(self, "Aviso.", "Datos negativos.")

    def check_datos(self):
        if self.datos is not []:
            for x in self.datos:
                if isinstance(x, float) or isinstance(x, int):
                    if x < 0:
                        return False
            return True

    def get_datos(self):
        return self.datos

    def get_tipo(self):
        return self.tipo_barrena.currentIndex()

    def collect_data(self):
        if self.source is 9:
            self.datos.append(self.layout_campos.itemAt(3).widget().text())
            self.datos.append((self.layout_campos.itemAt(5).widget().text()))
            self.datos.append(self.layout_campos.itemAt(7).widget().text())

            if self.tipo_conexion.currentIndex() is 0:
                self.datos.append("PIN")
            else:
                self.datos.append("BOX")
            self.datos.append(float(self.layout_campos_2.itemAt(3).widget().text()))
            self.datos.append(int(self.layout_campos_2.itemAt(5).widget().text()))
            if self.tipo_barrena.currentIndex() is 1:
                self.datos.append(int(self.layout_campos_2.itemAt(7).widget().text()))

            self.datos.append(float(self.layout_campos.itemAt(9).widget().text()))

    def is_modificador(self, data):
        if self.source is 9:
            self.tipo_barrena.setCurrentIndex(int(data[0]))
            self.tipo_barrena.setEnabled(False)
            self.layout_campos.itemAt(3).widget().setText(data[1])
            self.layout_campos.itemAt(5).widget().setText(str(data[2]))
            self.layout_campos.itemAt(7).widget().setText(data[3])

            if data[4] is "PIN":
                self.tipo_conexion.setCurrentIndex(0)
            else:
                self.tipo_conexion.setCurrentIndex(1)

            self.layout_campos_2.itemAt(3).widget().setText(str(data[5]))
            self.layout_campos_2.itemAt(5).widget().setText(str(data[6]))
            if self.tipo_barrena.currentIndex() is 1:
                self.layout_campos_2.addRow("Puertos Fijos", QLineEdit())
                self.layout_campos_2.itemAt(7).widget().setText(data[7])
                self.layout_campos.itemAt(9).widget().setText(str(data[8]))
            self.layout_campos.itemAt(9).widget().setText(str(data[7]))


if __name__ == "__main__":
    cadena = "5 1/2"
    separador = " "
    separado_por_espacios = cadena.split(separador)
    print("Separado por espacios es:", separado_por_espacios)
    x = "1/2"
    x = Fraction(x)
    x = float(x)
    print(x)
    print("hola despues de la weas")
    app = QApplication(sys.argv)
    agregador = Agregar(9)
    agregador.exec_()
