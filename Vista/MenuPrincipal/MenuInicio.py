import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from win32api import GetSystemMetrics


class MainWindow (QMainWindow):
    """docstring for Main Window."""
    def __init__(self):
        super(MainWindow, self).__init__()
        width = 800
        height = 600
        self.setWindowTitle("Easy Drill")
        self.setGeometry((GetSystemMetrics(0)-width)/2, (GetSystemMetrics(1)-height)/2,width,height)
        self.setWindowIcon(QIcon('petro.png'))
        self.initUI()

    def initUI (self):
        Horizotal = QHBoxLayout()
        vertical = QVBoxLayout()
        btn1 = QPushButton("Nuevo")
        btn2 = QPushButton("Cargar")
        btn3 = QPushButton("Tuberias y Herramientas")
        central_widget = QWidget()
        vertical.addStretch()
        vertical.addWidget(btn1)
        vertical.addWidget(btn2)
        vertical.addWidget(btn3)
        vertical.addStretch()
        Logo = QLabel()
        Logo.setPixmap(QPixmap("G:\Tesis\Recursos\Imagenes\EasyDrillLogo.png").scaledToHeight(100))

        Horizotal.addWidget(Logo)
        Horizotal.addSpacing(50)
        Horizotal.addLayout(vertical)
        central_widget.setLayout(Horizotal)
        self.setCentralWidget(central_widget)

if __name__ == '__main__':
    print("Width =", GetSystemMetrics(0))
    print("Height =", GetSystemMetrics(1))
    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())


