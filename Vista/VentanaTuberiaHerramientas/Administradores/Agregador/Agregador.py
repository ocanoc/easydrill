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
        self.setWindowIcon(QIcon("Imagenes/Iconos/Gota.png"))
        self.setWindowTitle("Easy Drill")
        self.label_instrucciones = QLabel("Ingresa los siguientes datos:")

        self.btn_aceptar = QPushButton("Aceptar")
        self.btn_cancelar = QPushButton("Cancelar")

        self.acondiciona(self.btn_aceptar)
        self.acondiciona(self.btn_cancelar)

        self.btn_aceptar.clicked.connect(lambda *args: self.aceptar())
        self.btn_cancelar.clicked.connect(lambda *args: self.reject())

        self.layout_btn = QHBoxLayout()
        self.layout_btn.setAlignment(Qt.AlignLeft)
        self.layout_btn.addSpacing(25)
        self.layout_btn.addWidget(self.btn_aceptar)
        self.layout_btn.addSpacing(50)
        self.layout_btn.addWidget(self.btn_cancelar)

        self.layout_campos = QFormLayout()
        self.layout_campos_2 = QFormLayout()

        self.setFixedSize(580, 300)
        self.create_ui(source)

        self.layout_forms = QHBoxLayout()
        self.layout_forms.addSpacing(25)
        self.layout_forms.addLayout(self.layout_campos)
        self.layout_forms.addSpacing(25)
        self.layout_forms.addLayout(self.layout_campos_2)
        self.layout_forms.addSpacing(25)
        self.layout_forms.addStretch(1)

        self.layout_pantalla = QVBoxLayout()
        self.layout_pantalla.addWidget(self.label_instrucciones)
        self.layout_pantalla.addSpacing(10)
        self.layout_pantalla.addLayout(self.layout_forms)
        self.layout_pantalla.addSpacing(15)
        self.layout_pantalla.addLayout(self.layout_btn, 1)
        self.layout_pantalla.setAlignment(self.layout_btn, Qt.AlignBottom)
        self.layout_pantalla.addStretch(1)

        self.setLayout(self.layout_pantalla)

        self.datos = []

    def create_ui(self, source):
        if source is 3:
            print("here")
            p = self.palette()
            p.setBrush(10, QBrush(QImage("Imagenes/Fondo/FondoDatosHW.png")))
            self.setPalette(p)
            self.setFixedSize(580, 200)
            self.layout_campos.setSpacing(10)
            self.layout_campos_2.setSpacing(10)
            self.tipo_geometria = QComboBox()
            self.tipo_geometria.addItems(["CONVENCIONAL", "ESPIRAL", "TRI-ESPIRAL"])

            self.layout_campos.addRow("OD [pg]:", QLineEdit())
            self.layout_campos.addRow("ID [pg]:", QLineEdit())
            self.layout_campos.addRow("Geometria", self.tipo_geometria)

            self.layout_campos_2.addRow("Conexión:", QLineEdit())
            self.layout_campos_2.addRow("Longitud [pg]:", QLineEdit())
            self.layout_campos_2.addRow("Peso [lb/ft]:", QLineEdit())

        if source is 4:
            p = self.palette()
            p.setBrush(10, QBrush(QImage("Imagenes/Fondo/FondoDatosDC.png")))
            self.setPalette(p)
            self.setFixedSize(580, 200)
            self.layout_campos.setSpacing(10)
            self.layout_campos_2.setSpacing(10)
            self.tipo_geometria = QComboBox()
            self.tipo_geometria.addItems(["LISO", "ESPIRAL", "NO-MAGNETICO"])

            self.layout_campos.addRow("OD [pg]:", QLineEdit())
            self.layout_campos.addRow("ID [pg]:", QLineEdit())
            self.layout_campos.addRow("Geometria", self.tipo_geometria)

            self.layout_campos_2.addRow("Conexión:", QLineEdit())
            self.layout_campos_2.addRow("Longitud [pg]:", QLineEdit())
            self.layout_campos_2.addRow("Peso [lb/ft]:", QLineEdit())

        if source is 9:
            p = self.palette()
            p.setBrush(10, QBrush(QImage("Imagenes/Fondo/FondoDatosBNA.png")))
            self.setPalette(p)

            self.layout_campos.setSpacing(17)
            self.layout_campos_2.setSpacing(17)

            self.tipo_barrena = QComboBox()
            self.tipo_barrena.addItems(["Triconicas", "PDC"])

            self.tipo_conexion = QComboBox()
            self.tipo_conexion.addItems(["PIN", "BOX"])

            self.tipo_barrena.currentIndexChanged.connect(self.cambio_tipo)
            self.layout_campos.addRow("Tipo de Barena", self.tipo_barrena)
            self.layout_campos.addRow("Código IADC:", QLineEdit())
            self.layout_campos.addRow("OD [pg]:", QLineEdit())
            self.layout_campos.addRow("Conexión:", QLineEdit())
            self.layout_campos.addRow("Tipo Conexión :", self.tipo_conexion)

            self.layout_campos_2.addRow("Longitud [pg]:", QLineEdit())
            self.layout_campos_2.addRow("Peso [kg]:", QLineEdit())
            self.layout_campos_2.addRow("Boquillas:", QLineEdit())

        if source is 7:
            p = self.palette()
            p.setBrush(10, QBrush(QImage("Imagenes/Fondo/FondoDatosPortaBarrena.png")))
            self.setPalette(p)
            self.setFixedSize(580, 275)
            self.layout_campos.setSpacing(23)
            self.layout_campos_2.setSpacing(23)
            self.tipo_conexion_top = QComboBox()
            self.tipo_conexion_top.addItems(["PIN", "BOX"])
            self.tipo_conexion_bit = QComboBox()
            self.tipo_conexion_bit.addItems(["PIN", "BOX"])

            self.layout_campos.addRow("Conexión Top:", QLineEdit())
            self.layout_campos.addRow("Tipo conexión Top:", self.tipo_conexion_top)
            self.layout_campos.addRow("Conexión Bit:", QLineEdit())
            self.layout_campos.addRow("Tipo conexión Bit:", self.tipo_conexion_bit)

            self.layout_campos_2.addRow("OD [pg]:", QLineEdit())
            self.layout_campos_2.addRow("Longitud [pg]:", QLineEdit())
            self.layout_campos_2.addRow("Peso [kg]:", QLineEdit())

        if source is 8:
            p = self.palette()
            p.setBrush(10, QBrush(QImage("Imagenes/Fondo/FondoDatosMartillo.png")))
            self.setFixedSize(580, 265)
            self.setPalette(p)
            self.layout_campos.setSpacing(23)
            self.layout_campos_2.setSpacing(23)
            self.tipo_martillo = QComboBox()
            self.tipo_martillo.addItems(["HIDRÁULICO", "MECÁNICO"])

            self.layout_campos.addRow("Tipo martillo:", self.tipo_martillo)
            self.layout_campos.addRow("OD [pg]:", QLineEdit())
            self.layout_campos.addRow("ID [pg]:", QLineEdit())
            self.layout_campos.addRow("Conexión Top:", QLineEdit())

            self.layout_campos_2.addRow("Conexión Bit:", QLineEdit())
            self.layout_campos_2.addRow("Longitud [pg]:", QLineEdit())
            self.layout_campos_2.addRow("Peso [kg]:", QLineEdit())

        if source is 10:
            p = self.palette()
            p.setBrush(10, QBrush(QImage("Imagenes/Fondo/FondoDatosMotor.png")))
            self.setPalette(p)
            self.setFixedSize(580, 265)
            self.layout_campos.setSpacing(20)
            self.layout_campos_2.setSpacing(20)
            self.tipo_conexion_top = QComboBox()
            self.tipo_conexion_top.addItems(["PIN", "BOX"])

            self.layout_campos.addRow("Lóbulos:", QLineEdit())
            self.layout_campos.addRow("Etapas:", QLineEdit())
            self.layout_campos.addRow("Tipo conexión:", self.tipo_conexion_top)
            self.layout_campos.addRow("Conexión Top:", QLineEdit())

            self.layout_campos_2.addRow("Conexión Bit:", QLineEdit())
            self.layout_campos_2.addRow("OD [pg]:", QLineEdit())
            self.layout_campos_2.addRow("ID [pg]:", QLineEdit())
            self.layout_campos_2.addRow("Longitud [pg]:", QLineEdit())

        if source is 16:
            p = self.palette()
            p.setBrush(10, QBrush(QImage("Imagenes/Fondo/FondoDatosMartillo.png")))
            self.setFixedSize(580, 265)
            self.setPalette(p)
            self.layout_campos.setSpacing(23)
            self.layout_campos_2.setSpacing(23)
            self.tipo_conexion_top = QComboBox()
            self.tipo_conexion_top.addItems(["PIN", "BOX"])
            self.tipo_conexion_bit = QComboBox()
            self.tipo_conexion_bit.addItems(["PIN", "BOX"])

            self.layout_campos.addRow("OD [pg]:", QLineEdit())
            self.layout_campos.addRow("ID [pg]:", QLineEdit())
            self.layout_campos.addRow("Conexión Top:", QLineEdit())
            self.layout_campos.addRow("Tipo conexión Top:", self.tipo_conexion_top)

            self.layout_campos_2.addRow("Conexión Bit:", QLineEdit())
            self.layout_campos_2.addRow("Tipo conexión Bit:", self.tipo_conexion_bit)
            self.layout_campos_2.addRow("Longitud [pg]:", QLineEdit())
            self.layout_campos_2.addRow("Peso [kg]:", QLineEdit())

    def cambio_tipo(self, index):
        if index is 0:
            try:
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

        if self.source is 3 or self.source is 4:
            self.datos.append(self.layout_campos.itemAt(1).widget().text())
            self.datos.append((self.layout_campos.itemAt(3).widget().text()))
            self.datos.append(self.layout_campos.itemAt(5).widget().currentText())

            self.datos.append(self.layout_campos_2.itemAt(1).widget().text())
            self.datos.append(self.layout_campos_2.itemAt(3).widget().text())
            self.datos.append(self.layout_campos_2.itemAt(5).widget().text())

        if self.source is 9:
            self.datos.append(self.layout_campos.itemAt(3).widget().text())
            self.datos.append(self.layout_campos.itemAt(5).widget().text())
            self.datos.append(self.layout_campos.itemAt(7).widget().text())
            self.datos.append(self.layout_campos.itemAt(9).widget().currentText())

            self.datos.append(self.layout_campos_2.itemAt(1).widget().text())
            self.datos.append(self.layout_campos_2.itemAt(3).widget().text())
            self.datos.append(self.layout_campos_2.itemAt(5).widget().text())
            if self.tipo_barrena.currentIndex() is 1:
                self.datos.append(int(self.layout_campos_2.itemAt(7).widget().text()))


        if self.source is 7:
            self.datos.append(self.layout_campos.itemAt(1).widget().text())
            self.datos.append(self.layout_campos.itemAt(3).widget().currentText())
            self.datos.append(self.layout_campos.itemAt(5).widget().text())
            self.datos.append(self.layout_campos.itemAt(7).widget().currentText())

            self.datos.append(self.layout_campos_2.itemAt(1).widget().text())
            self.datos.append(self.layout_campos_2.itemAt(3).widget().text())
            self.datos.append(self.layout_campos_2.itemAt(5).widget().text())

        if self.source is 8:
            self.datos.append(self.layout_campos.itemAt(1).widget().currentText())
            self.datos.append((self.layout_campos.itemAt(3).widget().text()))
            self.datos.append(self.layout_campos.itemAt(5).widget().text())
            self.datos.append(self.layout_campos.itemAt(7).widget().text())

            self.datos.append(self.layout_campos_2.itemAt(1).widget().text())
            self.datos.append(self.layout_campos_2.itemAt(3).widget().text())
            self.datos.append(self.layout_campos_2.itemAt(5).widget().text())

        if self.source is 10:
            self.datos.append(self.layout_campos.itemAt(1).widget().text())
            self.datos.append(self.layout_campos.itemAt(3).widget().text())
            self.datos.append(self.layout_campos.itemAt(5).widget().currentText())
            self.datos.append(self.layout_campos.itemAt(7).widget().text())

            self.datos.append(self.layout_campos_2.itemAt(1).widget().text())
            self.datos.append(self.layout_campos_2.itemAt(3).widget().text())
            self.datos.append(self.layout_campos_2.itemAt(5).widget().text())
            self.datos.append(self.layout_campos_2.itemAt(7).widget().text())

        if self.source is 16:
            self.datos.append(self.layout_campos.itemAt(1).widget().text())
            self.datos.append((self.layout_campos.itemAt(3).widget().text()))
            self.datos.append(self.layout_campos.itemAt(5).widget().text())
            self.datos.append(self.layout_campos.itemAt(7).widget().currentText())

            self.datos.append(self.layout_campos_2.itemAt(1).widget().text())
            self.datos.append(self.layout_campos_2.itemAt(3).widget().currentText())
            self.datos.append(self.layout_campos_2.itemAt(6).widget().text())
            self.datos.append(self.layout_campos_2.itemAt(7).widget().text())

    def is_modificador(self, data):
        if self.source is 3 or self.source is 4:
            self.layout_campos.itemAt(1).widget().setText(data[0])
            self.layout_campos.itemAt(3).widget().setText(str(data[1]))
            if data[2] == 'CONVENCIONAL':
                self.layout_campos.itemAt(5).widget().setCurrentIndex(0)
            elif data[2] == 'ESPIRAL':
                self.layout_campos.itemAt(5).widget().setCurrentIndex(1)
            else:
                self.layout_campos.itemAt(5).widget().setCurrentIndex(2)

            self.layout_campos_2.itemAt(1).widget().setText(data[3])
            self.layout_campos_2.itemAt(3).widget().setText(data[4])
            self.layout_campos_2.itemAt(5).widget().setText(data[5])

        if self.source is 9:
            self.tipo_barrena.setCurrentIndex(int(data[0]))
            self.tipo_barrena.setEnabled(False)
            self.layout_campos.itemAt(3).widget().setText(data[1])
            self.layout_campos.itemAt(5).widget().setText(str(data[2]))
            self.layout_campos.itemAt(7).widget().setText(data[3])
            if data[4] == "PIN":
                self.tipo_conexion.setCurrentIndex(0)
            else:
                self.tipo_conexion.setCurrentIndex(1)

            self.layout_campos_2.itemAt(1).widget().setText(str(data[5]))
            self.layout_campos_2.itemAt(3).widget().setText(str(data[6]))
            self.layout_campos_2.itemAt(5).widget().setText(data[7])
            if self.tipo_barrena.currentIndex() is 1:
                self.layout_campos_2.itemAt(7).widget().setText(str(data[8]))

        if self.source is 7:
            self.layout_campos.itemAt(1).widget().setText(data[0])

            if data[1] == 'PIN':
                self.layout_campos.itemAt(3).widget().setCurrentIndex(0)
            else:
                self.layout_campos.itemAt(3).widget().setCurrentIndex(1)

            self.layout_campos.itemAt(5).widget().setText(data[2])

            if data[3] == "PIN":
                self.layout_campos.itemAt(7).widget().setCurrentIndex(0)
            else:
                self.layout_campos.itemAt(7).widget().setCurrentIndex(1)

            self.layout_campos_2.itemAt(1).widget().setText(data[4])
            self.layout_campos_2.itemAt(3).widget().setText(data[5])
            self.layout_campos_2.itemAt(5).widget().setText(data[6])

        if self.source is 8:
            if data[0] == 'HIDRÁULICO':
                self.layout_campos.itemAt(1).widget().setCurrentIndex(0)
            else:
                self.layout_campos.itemAt(1).widget().setCurrentIndex(1)
            self.layout_campos.itemAt(3).widget().setText(data[1])
            self.layout_campos.itemAt(5).widget().setText(str(data[2]))
            self.layout_campos.itemAt(7).widget().setText(data[3])

            self.layout_campos_2.itemAt(1).widget().setText(data[4])
            self.layout_campos_2.itemAt(3).widget().setText(data[5])
            self.layout_campos_2.itemAt(5).widget().setText(data[6])

        if self.source is 10:
            self.layout_campos.itemAt(1).widget().setText(data[0])
            self.layout_campos.itemAt(3).widget().setText(data[1])

            if data[2] == 'PIN':
                self.layout_campos.itemAt(5).widget().setCurrentIndex(0)
            else:
                self.layout_campos.itemAt(5).widget().setCurrentIndex(1)
            self.layout_campos.itemAt(7).widget().setText(data[3])

            self.layout_campos_2.itemAt(1).widget().setText(data[4])
            self.layout_campos_2.itemAt(3).widget().setText(data[5])
            self.layout_campos_2.itemAt(5).widget().setText(data[6])
            self.layout_campos_2.itemAt(5).widget().setText(data[7])

        if self.source is 16:
            self.layout_campos.itemAt(1).widget().setText(data[0])
            self.layout_campos.itemAt(3).widget().setText(str(data[1]))
            self.layout_campos.itemAt(5).widget().setText(data[2])
            if data[3] == 'PIN':
                self.layout_campos.itemAt(7).widget().setCurrentIndex(0)
            else:
                self.layout_campos.itemAt(7).widget().setCurrentIndex(1)

            self.layout_campos_2.itemAt(1).widget().setText(data[4])
            if data[5] == "PIN":
                self.layout_campos_2.itemAt(3).widget().setCurrentIndex(0)
            else:
                self.layout_campos_2.itemAt(3).widget().setCurrentIndex(1)
            self.layout_campos_2.itemAt(5).widget().setText(data[6])
            self.layout_campos_2.itemAt(7).widget().setText(data[7])


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
    agregador = Agregar(8)
    agregador.exec_()
