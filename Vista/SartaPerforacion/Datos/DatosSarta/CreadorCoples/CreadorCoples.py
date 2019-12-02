from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class CreadorCoples(QWidget):
    def __init__(self, parent=None):
        super(CreadorCoples, self).__init__(parent)
        self.btn1 = QPushButton("Seleccionar")
        self.btn2 = QPushButton("Seleccionar")
        self.btn1.clicked.connect(lambda: self.agrega(1))
        self.btn2.clicked.connect(lambda: self.agrega(1))
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
        self.layout.addWidget(self.g_conexion_top)
        self.layout.addWidget(self.g_conexion_bit)

        self.layout.addLayout(self.layout_campo)
        self.layout.addStretch(1)

        self.setLayout(self.layout)

    def agrega(self, tipo):
        if tipo is 1:
            print("tipo1")

    def get_data(self):
        data = self.table.get_data()
        if data is not None:
            print("entre")
            try:
                if float(self.campo_longitud.text()) > 0:
                    long = self.campo_longitud.text()
                    return data, long
                else:
                    QMessageBox.critical(self, "Error", "Ingresa una longitud valida.")
                    return None, None
            except ValueError:
                QMessageBox.critical(self, "Error", "Ingresa una longitud.")
                return None, None
        else:
            return None, None

    def get_tipo(self):
        return self.table.get_tipo()
