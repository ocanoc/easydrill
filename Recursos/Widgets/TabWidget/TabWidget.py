from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class HorizontalTabBar(QTabBar):
    def paintEvent(self, event):
        painter = QStylePainter(self)
        option = QStyleOptionTab()
        for index in range(self.count()):
            self.initStyleOption(option, index)
            painter.drawControl(QStyle.CE_TabBarTabShape, option)
            painter.drawText(self.tabRect(index),
                             Qt.AlignCenter | Qt.TextDontClip,
                             self.tabText(index))

    def tabSizeHint(self, index):
        size = QTabBar.tabSizeHint(self, index)
        if size.width() < size.height():
            size.transpose()
        return size


class TabWidget(QTabWidget):
    def __init__(self, parent=None):
        QTabWidget.__init__(self, parent)
        self.setTabBar(HorizontalTabBar())
