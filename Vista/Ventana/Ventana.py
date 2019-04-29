import sys
from win32api import GetSystemMetrics
from Vista.TrayectoriaDireccional.MenuTrayectoria import *
from Vista.Fluidos.DatosFluidos import *
from Vista.Fluidos.MenuFluidos import *


class MainWindow (QMainWindow):
    def __init__(self):
        pos = 0
        super(MainWindow, self).__init__()
        width = 800
        height = 600
        self.setWindowTitle("Easy Drill")
        self.setGeometry((GetSystemMetrics(0)-width)/2, (GetSystemMetrics(1)-height)/2, width, height)
        self.setWindowIcon(QIcon("Imagenes/EasyDrllLogo.png"))
        self.setMaximumHeight(800)
        self.setMinimumHeight(600)
        easy_drill_logo = QLabel()
        easy_drill_logo.setPixmap(QPixmap("Imagenes/EasyDrllLogo.png").scaledToHeight(30))
        texto_encabezado = QLabel()
        self.cambiar_encabezado(texto_encabezado, 2)
        btn_aceptar = QPushButton("Aceptar")
        btn_aceptar.setFixedHeight(30)
        btn_aceptar.setFixedWidth(100)
        btn_cancelar = QPushButton("Cancelar")
        btn_cancelar.setFixedHeight(30)
        btn_cancelar.setFixedWidth(100)
        btn_regresar = QPushButton("Regresar")
        btn_regresar.setFixedHeight(30)
        btn_regresar.setFixedWidth(100)
        layout_btn = QHBoxLayout()
        layout_btn.addWidget(btn_aceptar, Qt.StretchTile, Qt.AlignRight)
        layout_btn.addWidget(btn_cancelar)
        layout_btn.addWidget(btn_regresar)
        layout_pantalla = QVBoxLayout()
        layout_pantalla.addWidget(easy_drill_logo, Qt.StretchTile, Qt.AlignRight)
        layout_pantalla.addWidget(texto_encabezado)
        layout_central = self.cambiar_central(2)
        layout_pantalla.addLayout(layout_central)
        layout_pantalla.addSpacing(20)
        layout_pantalla.addLayout(layout_btn)
        layout_pantalla.addSpacing(20)
        central_widget = QWidget()
        central_widget.setLayout(layout_pantalla)
        self.setCentralWidget(central_widget)

    @staticmethod
    def cambiar_encabezado(label, numero):
        if numero is 0:
            label.setPixmap(QPixmap("Imagenes/TextoTrayectoria.png").scaledToHeight(50))
        if numero is 1:
            label.setPixmap(QPixmap("Imagenes/TextoModelo.png").scaledToHeight(60))
        if numero is 2:
            label.setPixmap(QPixmap("Imagenes/TextoHidraulica.png").scaledToHeight(50))

    @staticmethod
    def cambiar_central(numero):
        if numero is 0:
            return trayectoria()
        if numero is 1:
            return tipo_fluidos()
        if numero is 2:
            return datos_fluido()


if __name__ == '__main__':
    print("Width =", GetSystemMetrics(0))
    print("Height =", GetSystemMetrics(1))
    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())
