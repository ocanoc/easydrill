from Recursos.Widgets.SwitchButton.SwitchButton import *
from Vista.Ventana.Ventana import *


# noinspection PyArgumentList
class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        width = 1000
        height = 600
        fondo = QImage("Imagenes/Fondo.png")
        palette = QPalette()
        palette.setBrush(10, QBrush(fondo))
        self.setPalette(palette)
        self.setWindowTitle("Easy Drill")
        self.setGeometry((GetSystemMetrics(0) - width) / 2, (GetSystemMetrics(1) - height) / 2, width, height)
        self.setWindowIcon(QIcon("Imagenes/Gota.png"))
        self.init_ui()

    def init_ui(self):
        horizontal = QHBoxLayout()
        vertical = QVBoxLayout()
        swt = SwitchButton()
        print(swt.isEnabled())
        btn1 = QPushButton("Nuevo")
        btn2 = QPushButton("Cargar")
        btn3 = QPushButton("Tuberia y Herramientas")
        btn1.setFont(QFont("Calibri(Cuerpo)", 12))
        btn2.setFont(QFont("Calibri(Cuerpo)", 12))
        btn3.setFont(QFont("Calibri(Cuerpo)", 12))
        btn3.setIconSize(QSize(280, 1800))
        btn1.setFixedWidth(250)
        btn2.setFixedWidth(250)
        btn3.setFixedWidth(250)
        btn1.setFixedHeight(40)
        btn2.setFixedHeight(40)
        btn3.setFixedHeight(40)
        central_widget = QWidget()
        vertical.addStretch()
        vertical.addWidget(btn1)
        vertical.addSpacing(10)
        vertical.addWidget(btn2)
        vertical.addSpacing(10)
        vertical.addWidget(btn3)
        vertical.addSpacing(10)
        vertical.addWidget(swt)
        vertical.addStretch()
        logo = QLabel()
        logo.setPixmap(QPixmap("Imagenes/EasyDrllLogo.png"))
        linea = QLabel()
        linea.setPixmap(QPixmap("Imagenes/Linea.png").scaledToHeight(250))
        horizontal.addSpacing(10)
        horizontal.addWidget(logo, Qt.StretchTile, Qt.AlignHCenter)
        horizontal.addSpacing(10)
        horizontal.addWidget(linea)
        horizontal.addSpacing(20)
        horizontal.addLayout(vertical, Qt.AlignHCenter)
        horizontal.addSpacing(20)
        central_widget.setLayout(horizontal)
        self.setCentralWidget(central_widget)


if __name__ == '__main__':
    print("Width =", GetSystemMetrics(0))
    print("Height =", GetSystemMetrics(1))
    app = QApplication(sys.argv)
    w = MainWindow()
    w.setFixedSize(1000, 600)
    w.show()
    sys.exit(app.exec_())
