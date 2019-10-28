import sys

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from win32api import GetSystemMetrics

from Vista.VentanaNuevo.VentanaNuevo import Nuevo


class MenuInicio(QMainWindow):
    stop = True
    Nuevo = Nuevo()
    Nuevo.hide()
    frame_menu = QFrame()
    layout_pantalla = QVBoxLayout()
    layout_pantalla.addWidget(Nuevo)
    layout_pantalla.addWidget(frame_menu)
    layout_pantalla.addSpacing(10)
    btn_nuevo = QPushButton()
    btn_cargar = QPushButton()
    btn_admin = QPushButton()

    def __init__(self):
        super(MenuInicio, self).__init__()
        width = 1000
        height = 600
        self.setWindowTitle("Easy Drill")
        self.setGeometry((GetSystemMetrics(0) - width) / 2, (GetSystemMetrics(1) - height) / 2, width, height)
        self.setWindowIcon(QIcon("Imagenes/Iconos/Gota.png"))
        self.setFont(QFont('Calibri (Cuerpo)', 12, QFont.Bold))
        self.cambiarfondo()
        self.init_ui()

    def init_ui(self):
        self.btn_nuevo.setIcon(QIcon("Imagenes/MenuPrincipal/nuevo.png"))
        self.btn_cargar.setIcon(QIcon("Imagenes/MenuPrincipal/carga.png"))
        self.btn_admin.setIcon(QIcon("Imagenes/MenuPrincipal/admin.png"))

        self.acodiciona(self.btn_nuevo)
        self.acodiciona(self.btn_cargar)
        self.acodiciona(self.btn_admin)

        logo = QLabel()
        logo.setPixmap(QPixmap("Imagenes/MenuPrincipal/EasyDrllLogo.png"))
        logo.setScaledContents(True)
        logo.setFixedSize(556, 99)

        linea = QLabel()
        linea.setPixmap(QPixmap("Imagenes/MenuPrincipal/Linea.png").scaledToHeight(250))

        vertical = QVBoxLayout()
        vertical.addStretch()
        vertical.addWidget(self.btn_nuevo)
        vertical.addSpacing(8)
        vertical.addWidget(self.btn_cargar)
        vertical.addSpacing(8)
        vertical.addWidget(self.btn_admin)
        vertical.addSpacing(8)
        vertical.addStretch()

        horizontal = QHBoxLayout()
        horizontal.addSpacing(10)
        horizontal.addWidget(logo, Qt.StretchTile, Qt.AlignHCenter)
        horizontal.addSpacing(15)
        horizontal.addWidget(linea)
        horizontal.addSpacing(20)
        horizontal.addLayout(vertical, Qt.AlignHCenter)
        horizontal.addSpacing(20)

        self.frame_menu.setLayout(horizontal)
        central_widget = QWidget()
        central_widget.setLayout(self.layout_pantalla)
        self.setCentralWidget(central_widget)
        self.Nuevo.btn_cancelar.clicked.connect(lambda *args: self.cancelar())
        self.btn_nuevo.clicked.connect(lambda *args: self.nuevo())
        self.Nuevo.btn_aceptar.clicked.connect(lambda *args: self.cambiarfondo())
        self.Nuevo.btn_regresar.clicked.connect(lambda *args: self.cambiarfondo())
        self.installEventFilter(self)

    def cancelar(self):
        self.Nuevo.hide()
        self.Nuevo.pos = 0
        self.cambiarfondo()
        self.frame_menu.show()

    def nuevo(self):
        self.Nuevo.show()
        self.frame_menu.hide()

    def eventFilter(self, source, event):
        if event.type() == QEvent.Enter:
            self.intercambiar_imagen(source, True)
            self.stop = True
            return True
        elif event.type() == QEvent.Leave:
            self.intercambiar_imagen(source, False)
            self.stop = False
        elif event.type() == QEvent.MouseButtonPress:
            self.cambiarfondo()
        return False

    def cambiarfondo(self):
        palette = QPalette()
        if self.Nuevo.pos is 1 or self.Nuevo.pos is 3:
            palette.setBrush(10, QBrush(QImage("Imagenes/Fondo/Fondo 2.png")))
            self.Nuevo.btn_aceptar.setText("Siguiente")
        elif self.Nuevo.pos is 4:
            self.Nuevo.btn_aceptar.setText("Finalizar")
            palette.setBrush(10, QBrush(QImage("Imagenes/Fondo/Fondo.png")))
        elif self.Nuevo.pos is 2:
            palette.setBrush(10, QBrush(QImage("Imagenes/Fondo/Fondo 4.png")))
        else:
            self.Nuevo.btn_aceptar.setText("Siguiente")
            palette.setBrush(10, QBrush(QImage("Imagenes/Fondo/Fondo.png")))
        self.setPalette(palette)

    def intercambiar_imagen(self, source, flag):
        if source is self.btn_nuevo:
            if flag:
                source.setIcon(QIcon("Imagenes/MenuPrincipal/nuevopress.png"))
            else:
                source.setIcon(QIcon("Imagenes/MenuPrincipal/nuevo.png"))
        if source is self.btn_cargar:
            if flag:
                source.setIcon(QIcon("Imagenes/MenuPrincipal/cargarpress.png"))
            else:
                source.setIcon(QIcon("Imagenes/MenuPrincipal/carga.png"))
        if source is self.btn_admin:
            if flag:
                source.setIcon(QIcon("Imagenes/MenuPrincipal/adminpress.png"))
            else:
                source.setIcon(QIcon("Imagenes/MenuPrincipal/admin.png"))

    def acodiciona(self, btn):
        ancho = 300
        largo = 60
        btn.setCursor(Qt.PointingHandCursor)
        btn.setFixedSize(ancho, largo)
        btn.setIconSize(QSize(ancho, largo))
        btn.setStyleSheet("border: 0px;")
        btn.installEventFilter(self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MenuInicio()
    w.setFixedSize(1000, 604)
    w.show()
    sys.exit(app.exec_())
