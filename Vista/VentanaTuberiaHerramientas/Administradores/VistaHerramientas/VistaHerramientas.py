from PyQt5.QtWidgets import *

from VentanaTuberiaHerramientas.Administradores.Datos.Datos import Datos


class VistaHerramientas(QWidget):
    def __init__(self, parent=None):
        super(VistaHerramientas, self).__init__(parent)
        self.label_instrucciones = QLabel("Selecciona el tipo de herramienta.")

        self.tipo_herramienta = QComboBox()
        self.tipo_herramienta.addItems((["Selecciona", "Martillos", "Amortiguadores"]))
        self.tipo_herramienta.currentIndexChanged.connect(self.cambio_tipo)

        self.amortiguadores = Datos(1)
        self.amortiguadores.hide()
        self.martillos = Datos(0)
        self.martillos.hide()
        self.empty = QWidget()

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.label_instrucciones)
        self.layout.addWidget(self.tipo_herramienta)
        self.layout.addWidget(self.empty)
        self.layout.addWidget(self.amortiguadores)
        self.layout.addWidget(self.martillos)
        self.layout.addStretch(1)

        self.setLayout(self.layout)

    def cambio_tipo(self):
        if self.tipo_herramienta.currentIndex() is 0:
            self.empty.show()
            self.martillos.hide()
            self.amortiguadores.hide()
        if self.tipo_herramienta.currentIndex() is 1:
            self.empty.hide()
            self.martillos.show()
            self.amortiguadores.hide()
        if self.tipo_herramienta.currentIndex() is 2:
            self.empty.hide()
            self.martillos.hide()
            self.amortiguadores.show()

    def agregar(self):
        if self.tipo_herramienta.currentIndex() is 0:
            QMessageBox.critical(self, "Error", "Selecciona un tipo de herramienta.")
        elif self.tipo_herramienta.currentIndex() is 1:
            self.martillos.agregar()
        elif self.tipo_herramienta.currentIndex() is 2:
            self.amortiguadores.agregar()

    def eliminar(self):
        if self.tipo_herramienta.currentIndex() is 0:
            QMessageBox.critical(self, "Error", "Selecciona un tipo de herramienta.")
        elif self.tipo_herramienta.currentIndex() is 1:
            self.martillos.eliminar()
        elif self.tipo_herramienta.currentIndex() is 2:
            self.amortiguadores.eliminar()

    def modificar(self):
        if self.tipo_herramienta.currentIndex() is 0:
            QMessageBox.critical(self, "Error", "Selecciona un tipo de herramienta.")
        elif self.tipo_herramienta.currentIndex() is 1:
            self.martillos.modificar()
        elif self.tipo_herramienta.currentIndex() is 2:
            self.amortiguadores.modificar()

    def get_data(self):
        if self.tipo_herramienta.currentIndex() is 0:
            QMessageBox.critical(self, "Error", "Selecciona un tipo de herramienta.")
        elif self.tipo_herramienta.currentIndex() is 1:
            return self.martillos.get_data()
        elif self.tipo_herramienta.currentIndex() is 2:
            return self.amortiguadores.get_data()

    def get_tipo(self):
        if self.tipo_herramienta.currentIndex() is 0:
            QMessageBox.critical(self, "Error", "Selecciona un tipo de herramienta.")
        elif self.tipo_herramienta.currentIndex() is 1:
            return self.martillos.get_tipo()
        elif self.tipo_herramienta.currentIndex() is 2:
            return self.amortiguadores.get_tipo()
