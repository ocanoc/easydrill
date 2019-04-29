import sys
from win32api import GetSystemMetrics
from Fluidos.DatosFluidos import *


class MainWindow (QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        width = 800
        height = 600
        self.setWindowTitle("Easy Drill")
        self.setGeometry((GetSystemMetrics(0)-width)/2, (GetSystemMetrics(1)-height)/2,width,height)
        self.setWindowIcon(QIcon("Imagenes/EasyDrllLogo.png"))
        self.setMaximumHeight(700)
        self.setMinimumHeight(600)
        self.init_ui()

    def init_ui(self):
        horizontal = QHBoxLayout()
        vertical = QVBoxLayout()
        btn1 = QPushButton("Nuevo")
        btn2 = QPushButton("Cargar")
        btn3 = QPushButton()
        btn1.setFont(QFont("Calibri(Cuerpo)", 15))
        btn2.setFont(QFont("Calibri(Cuerpo)", 15))
        btn3.setFont(QFont("Calibri(Cuerpo)", 15))
        btn3.setIcon(QIcon("BtnTuberias.png"))
        btn3.setIconSize(QSize(280,1800))
        btn1.setFixedHeight(40)
        btn1.setFixedWidth(280)
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
        vertical.addStretch()
        logo = QLabel()
        logo.setPixmap(QPixmap("Imagenes/EasyDrllLogo.png").scaledToHeight(90))
        linea = QLabel()
        linea.setPixmap(QPixmap("Imagenes/Linea.png").scaledToHeight(250))
        horizontal.addWidget(logo)
        horizontal.addSpacing(8)
        horizontal.addWidget(linea)
        horizontal.addSpacing(8)
        horizontal.addLayout(vertical)
        central_widget.setLayout(horizontal)
        self.setCentralWidget(central_widget)


if __name__ == '__main__':
    print("Width =", GetSystemMetrics(0))
    print("Height =", GetSystemMetrics(1))
    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())


