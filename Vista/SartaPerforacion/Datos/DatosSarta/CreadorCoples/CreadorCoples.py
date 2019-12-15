from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

from Recursos.Constantes.Convertidor import Convertidor
from SartaPerforacion.Datos.DatosSarta.CreadorCoples.DatosCoples.DatosCoples import DatosCoples


class CreadorCoples(QWidget):
    def __init__(self, parent=None):
        super(CreadorCoples, self).__init__(parent)
        self.llene_bit = False
        self.llene_top = False
        self.datos = []
        self.label = QLabel("Ingresa los datos de la combinación")
        self.btn1 = QPushButton("Seleccionar")
        self.btn2 = QPushButton("Seleccionar")
        self.btn1.clicked.connect(lambda: self.agrega(1))
        self.btn2.clicked.connect(lambda: self.agrega(2))
        self.g_conexion_top = QGroupBox()
        self.g_conexion_top.setTitle("Conexion Top")
        self.g_conexion_bit = QGroupBox()
        self.g_conexion_bit.setTitle("Conexion Bit")

        self.fl_conexion_top = QFormLayout()
        self.fl_conexion_top.addRow("Conexión", QLineEdit())
        self.fl_conexion_top.addRow("OD [pg]:", QLineEdit())
        self.fl_conexion_top.addRow("ID [pg]:", QLineEdit())
        self.fl_conexion_top.addRow("", self.btn1)

        self.fl_conexion_bit = QFormLayout()
        self.fl_conexion_bit.addRow("Conexión", QLineEdit())
        self.fl_conexion_bit.addRow("OD [pg]:", QLineEdit())
        self.fl_conexion_bit.addRow("ID [pg]:", QLineEdit())
        self.fl_conexion_bit.addRow("", self.btn2)

        self.campo_longitud = QLineEdit()
        self.campo_longitud.setFixedWidth(85)
        self.campo_longitud.setCursor(Qt.IBeamCursor)
        self.campo_longitud.setPlaceholderText("0")

        self.g_conexion_top.setLayout(self.fl_conexion_top)
        self.g_conexion_bit.setLayout(self.fl_conexion_bit)

        self.layout_campo = QFormLayout()
        self.layout_campo.addRow("Longitud [m]:", self.campo_longitud)

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.label)
        self.layout.addWidget(self.g_conexion_top)
        self.layout.addWidget(self.g_conexion_bit)

        self.layout.addLayout(self.layout_campo)
        self.layout.addStretch(1)

        self.setLayout(self.layout)

    def agrega(self, tipo):
        nuevo = DatosCoples()
        if nuevo.exec_():
            datos = nuevo.get_data()
            if tipo is 1:
                self.fl_conexion_top.itemAt(1).widget().setText(datos[0])
                self.fl_conexion_top.itemAt(3).widget().setText(datos[2])
                self.fl_conexion_top.itemAt(5).widget().setText(datos[3])
                self.llene_top = True
            if tipo is 2:
                self.fl_conexion_bit.itemAt(1).widget().setText(datos[0])
                self.fl_conexion_bit.itemAt(3).widget().setText(datos[2])
                self.fl_conexion_bit.itemAt(5).widget().setText(datos[3])
                self.llene_bit = True

    def get_data(self):
        try:
            if float(self.campo_longitud.text()) > 0:
                self.collect_data()
                return self.datos
            else:
                QMessageBox.critical(self, "Error", "Ingresa una longitud valida.")
                return None
        except ValueError:
            QMessageBox.critical(self, "Error", "Datos erroneos o incompletos.")
            return None

    def get_tipo(self):
        return 13

    def collect_data(self):
        if Convertidor.fracc_to_dec((self.fl_conexion_top.itemAt(3).widget().text())) >= \
                Convertidor.fracc_to_dec(self.fl_conexion_bit.itemAt(3).widget().text()):
            self.datos.append(self.fl_conexion_top.itemAt(3).widget().text())
        else:
            self.datos.append(self.fl_conexion_bit.itemAt(3).widget().text())

        if Convertidor.fracc_to_dec((self.fl_conexion_top.itemAt(5).widget().text())) <= \
                Convertidor.fracc_to_dec(self.fl_conexion_bit.itemAt(5).widget().text()):
            self.datos.append(self.fl_conexion_top.itemAt(5).widget().text())
        else:
            self.datos.append(self.fl_conexion_bit.itemAt(5).widget().text())
        self.datos.append(float(self.campo_longitud.text()))
        text = self.fl_conexion_bit.itemAt(1).widget().text() + " a \n" + self.fl_conexion_top.itemAt(1).widget().text()
        self.datos.append(self.fl_conexion_bit.itemAt(1).widget().text())
        self.datos.append(self.fl_conexion_top.itemAt(1).widget().text())
        self.datos.append(text)
